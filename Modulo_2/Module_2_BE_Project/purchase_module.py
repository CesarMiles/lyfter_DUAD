from flask.views import MethodView
from flask import request
from invoice_repo import invoice_repo
from utils import purchase_req_checks
from product_repo import product_repo
from invoice_detail_repo import invoice_detail_repo
from decorators import token_required

class PurchaseProduct(MethodView):
    @token_required
    def post(self):
        try:
            data = request.get_json()
            
            # basic validation
            if 'products' not in data or not data['products']:
                return {"error": "products array required"}, 400
            
            processed_items = []
            total_amount = 0

            # Product validation without modificaation 
            for product_request in data['products']:
                product_id = product_request['product_id']
                quantity = product_request['quantity']

                if not product_id or not quantity:
                    return {"error": "Each porduct must have product_id and quantity" }, 400

                product_info = product_repo.get_product_by_id(product_id)
                if not product_info:
                    return {"error": f"Product {product_id} doesn't exist"}, 400
                
                remaining_stock = (product_info['stock'] - quantity)
                if remaining_stock < 0:
                    return {"error": f"Insufficient stock for product {product_info['product_name']}"}, 400
                
                subtotal = product_info['product_price'] * quantity
                processed_items.append({
                    'product_id': product_id,
                    'product_name': product_info['product_name'],
                    'quantity': quantity,
                    'subtotal': subtotal,
                    'remaining_stock': remaining_stock
                })
                total_amount += subtotal
        
            # If all checks pass, process invoice creation
            invoice_id = invoice_repo.create_invoice(
                user_id=request.user_id, 
                total_amount=total_amount,
                invoice_status='completed'
            )
            
            if not invoice_id:
                return {"error": "Failed to create invoice"}, 500
        
            # Create invoice detail 
            for item in processed_items:
                invoice_detail_repo.create_invoice_detail(
                    invoice_id=invoice_id, 
                    product_id=item['product_id'], 
                    quantity=item['quantity']
                )
                
                # UPdate stock
                updated = product_repo.modify_product(
                    item['product_id'], 
                    stock=item['remaining_stock']
                )
                
                if not updated:
                    print(f"Warning: Failed to update stock for product {item['product_id']}")
            
            return {
                "message": "Purchase completed successfully",
                "invoice_id": invoice_id,
                "total_amount": total_amount,
                "items": [{
                    "product_id": item['product_id'],
                    "product_name": item['product_name'],
                    "quantity": item['quantity'],
                    "subtotal": item['subtotal']
                } for item in processed_items]
            }, 201
            
        except Exception as e:
            return {"error": f'Purchase failed: {str(e)}'}, 500
        

def purchase_api_methods(app):
    purchase_product = PurchaseProduct.as_view('purchase_api')
    app.add_url_rule('/purchase_product', view_func=purchase_product, methods=['POST'])