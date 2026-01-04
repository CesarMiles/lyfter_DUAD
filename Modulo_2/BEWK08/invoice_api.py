from flask.views import MethodView
from flask import request
from invoice_repo import invoice_repo
from utils import purchase_req_checks
from product_repo import product_repo
from utils import format_invoices, format_invoice_details
from invoice_detail_repo import invoice_detail_repo
from cache import cache_manager
from decorators import token_required


# Purchase endpoint this contains the logic to make a purchase, this endpoint will check for stock if available will proceed with purchase and reduce the stock from the db. Format to make the purchase is 
# {
#     "products": [
#         {
#             "product_id": 4,
#             "quantity": 1
#         },
#         {
#             "product_id": 3, 
#             "quantity": 3
#         }
#     ]
# }

class Purchase_Product(MethodView):
    @token_required
    def post(self):
        try:
            purchase_req_checks(request)
            data = request.get_json()
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
            
            invoice_id = invoice_repo.create(user_id=request.user_id, total_amount=total_amount)

            for product in processed_items:
                invoice_detail_repo.create(invoice_id, product['product_id'], product['quantity'])
                product_repo.modify(product['product_id'], stock=product['remaining_stock'])
                cache_manager.delete_data(f"product:{product['product_id']}")

            if cache_manager.get_json("products:all"):
                cache_manager.delete_data("products:all")
            return {"message" : f'Purchase complete Invoice Id {invoice_id}, Items: {[product_name['product_name'] for product_name in processed_items]}'}, 200

        except Exception as e:
            return {"error": f'Database error: {e}'}, 500
    

# End point avialable for users and admins to retrive invoices this will provide the details of the invoice based on user id, it also allows for invoice_id specific search to retrieve details of the purchase details. This function only provides user info of their own invoice
class GetInvoicedetails(MethodView):
    @token_required
    def get(self):
        try:
            invoices = invoice_repo.get(request.user_id)
            if len(invoices) == 0 :
                return {"message": f"You currently have no invoices"}, 200

            filtered_invoice_id = request.args.get('invoice_id')

            if filtered_invoice_id:
                invoice_verification = invoice_repo.belongs_to_user(filtered_invoice_id, request.user_id)
                if not invoice_verification:
                    return {"error": "Invoice not found on your record"}
                
                filtered_invoice = invoice_detail_repo.get_invoice_with_details(filtered_invoice_id)
                
                formatted_filtered_invoices = format_invoice_details(filtered_invoice)
                
                return formatted_filtered_invoices
            
            formatted_invoices = [format_invoices(invoice) for invoice in invoices]

            return formatted_invoices
            
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

def invoice_api_methods(app):
    purchase_product = Purchase_Product.as_view('purchase_api')
    app.add_url_rule('/purchase_product', view_func=purchase_product, methods=['POST'])

    get_invoices = GetInvoicedetails.as_view('get_invoice_api')
    app.add_url_rule('/my_invoices', view_func=get_invoices, methods=['GET'])