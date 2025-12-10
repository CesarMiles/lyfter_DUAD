from flask.views import MethodView
from flask import request, jsonify, Response
from db_manager import DB_Manager
from jwt_manager import JWTManager
from invoice_repo import InvoiceRepository
from invoice_detail_repo import InvoiceDetailRepository
from utils import purchase_req_checks
from product_repo import ProductRepository

conn = DB_Manager()
jwt_manager = JWTManager("superclave", 'HS256')
invoice_repo = InvoiceRepository(conn)
invoice_detail_repo = InvoiceDetailRepository(conn)
product_repo = ProductRepository(conn)


class Purchase_Product(MethodView):
    def post(self):
        try:
            token = request.headers.get('Authorization')
            purchase_req_checks(request)
            data = request.get_json()
            if (token is not None):
                token = token.replace("Bearer ", "")
                decoded = jwt_manager.decode(token)
                user_id = decoded["user_id"]

                processed_items = []
                total_amount = 0

                for product_request in data['products']:
                    product_id = product_request['product_id']
                    quantity = product_request['quantity']
                    
                    # Store individual product info on a list 
                    product_info = product_repo.get_product_by_id(product_id)
                    
                    if not product_info:
                        return {"error": f"Product {product_id} doesn't exist"}, 400
                    
                    # Calculate remaining stock 
                    remaining_stock = (product_info['stock'] - quantity)
                    if remaining_stock < 0:
                        return {"error": f"insufficient stock for {product_id}"}, 400
                    
                    # Calculate total amount per product
                    unit_price = product_info['product_price']
                    subtotal = unit_price * quantity
                    
                    processed_items.append({
                        'product_id': product_id,
                        'product_name': product_info['product_name'],
                        'quantity': quantity,   
                        'unit_price': unit_price,
                        'subtotal': subtotal,
                        'remaining_stock': remaining_stock
                    })
                    
                    total_amount += subtotal
                
                invoice_id = invoice_repo.create(user_id=user_id, total_amount=total_amount)

                for product in processed_items:
                    invoice_detail_repo.create(invoice_id, product['product_id'], product['quantity'])
                    product_repo.modify(product['product_id'], stock=product['remaining_stock'])

                return {"message" : f'Purchase complete Invoice Id {invoice_id}, Items: {[product_name['product_name'] for product_name in processed_items]}'}, 200
            
            else:
                return {"message": f"Token is required to perform this action"}, 400

        except Exception as e:
            return {"error": f'Database error: {e}'}, 500
    



def invoice_api_methods(app):
    purchase_product = Purchase_Product.as_view('purchase_api')
    app.add_url_rule('/purchase_product', view_func=purchase_product, methods=['POST'])