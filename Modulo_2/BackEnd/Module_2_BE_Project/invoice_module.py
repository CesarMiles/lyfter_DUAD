from flask.views import MethodView
from flask import request, jsonify
from invoice_repo import invoice_repo
from invoice_detail_repo import invoice_detail_repo
from decorators import token_required, admin_required
from cache import cache_manager
from utils import invoice_cache_invalidation, format_invoice

class GetInvoices(MethodView):
    @token_required
    def get(self):
        try:
            if hasattr(request, 'user_payload') and request.user_payload.get("role") == "admin":
                all_invoice_cache = cache_manager.get_json("invoice:all")
                if all_invoice_cache:
                    return jsonify(all_invoice_cache), 200
                
                invoices = invoice_repo.get_all()
                cache_manager.store_json("invoice:all", format_invoice(invoices), time_to_live=600)
                return jsonify(format_invoice(invoices)), 200
                
            else:
                invoices = invoice_repo.get(request.user_id)
                if not invoices:
                    return {"message" : "You currently have 0 invoices"}

                cache_manager.store_json(f"invoice:{request.user_id}", format_invoice(invoices), time_to_live=600)

            return jsonify(format_invoice(invoices)), 200
        
        except Exception as e:
            return {"error": str(e)}, 500

class GetInvoiceDetails(MethodView):
    @token_required
    def get(self, invoice_id):
        try:
            if not invoice_repo.belongs_to_user(invoice_id, request.user_id):
                if not (hasattr(request, 'user_role') and request.user_role == 'admin'):
                    return {"error": "Not authorized to view this invoice"}, 403
            
            details = invoice_detail_repo.get_invoice_with_details(invoice_id)
            print(details)
            return jsonify([{
                "product_name": det[3],
                "product_price": float(det[4]),
                "quantity": det[5],
                "subtotal": float(det[6])
            } for det in details]), 200
            
        except Exception as e:
            return {"error": str(e)}, 500

class AdminUpdateInvoice(MethodView):
    @admin_required
    def patch(self, invoice_id):
        try:
            data = request.get_json()
            if 'invoice_status' in data:
                updated = invoice_repo.modify_invoice(invoice_id, invoice_status=data['invoice_status'])
                if updated:
                    invoice_cache_invalidation(cache_manager, request.user_id)
                    return {"message": f"Invoice {invoice_id} updated to {data['invoice_status']}"}, 200
                return {"error": "Invoice not found"}, 404
            return {"error": "Only invoice_status can be updated"}, 400
        except Exception as e:
            return {"error": str(e)}, 500

def invoice_api_methods(app):
    get_invoices = GetInvoices.as_view('get_invoices_api')
    app.add_url_rule('/invoices', view_func=get_invoices, methods=['GET'])
    
    get_invoice_details = GetInvoiceDetails.as_view('get_invoice_details_api')
    app.add_url_rule('/invoices/<int:invoice_id>', view_func=get_invoice_details, methods=['GET'])
    
    admin_update = AdminUpdateInvoice.as_view('admin_update_invoice_api')
    app.add_url_rule('/admin/invoices/<int:invoice_id>', view_func=admin_update, methods=['PATCH'])