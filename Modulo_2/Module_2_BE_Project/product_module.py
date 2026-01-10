from flask.views import MethodView
from flask import request, jsonify
from product_repo import product_repo
from decorators import admin_required, token_required
from utils import format_product_detail, format_product, product_modify_item, product_cache_invalidation
from cache import cache_manager

# End point to create products, only admin can perform this action 
class CreateProduct(MethodView):
    @admin_required
    def post(self):
        try:     
            data = request.get_json()
            required_fields = ['product_name', 'product_price', 'stock']
            if not all(field in data for field in required_fields):
                return {"error": "Missing required fields"}, 422
            
            if float(data.get("product_price")) <= 0:
                return {"error": "Price must be positive"}, 400
            
            if int(data.get("stock")) < 0:
                return {"error": "Stock cannot be negative"}, 400
            
            result = product_repo.create_product(
                product_name = data.get("product_name"), 
                product_price= data.get("product_price"), 
                stock= data.get("stock"))
            
            if not result:
                return {"error": "Failed to create product"}, 500
            
            product_cache_invalidation(cache_manager, result[0])

            product_id, product_name = result[0], result[1]
            
            return {
                "message": "Product created successfully",
                "product_id": product_id,
                "product_name": product_name
            }, 201

        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# Endpoint to retrieve products, including specific search for individual product by id
class GetProducts(MethodView):
    @token_required
    def get(self):
        try:
            filtered_product_id = request.args.get('product_id')
            if filtered_product_id:
                try:
                    filtered_product_id = int(filtered_product_id)
                except ValueError:
                    return {"error": "Product ID must be a number"}, 400

                cache_key = f"product:{filtered_product_id}"
                cached_product = cache_manager.get_json(cache_key)
                if cached_product:
                    return jsonify(cached_product)
                
                filtered_product = product_repo.get_product_by_id(filtered_product_id)
                if not filtered_product:
                    return {"error": "Product not found"}, 404

                cache_manager.store_json(cache_key, filtered_product, time_to_live=600)
                return format_product_detail(filtered_product), 200
            
            all_products_cache = cache_manager.get_json("products:all")
            if all_products_cache:
                return jsonify(all_products_cache)
            
            products = product_repo.get_products()
            cache_manager.store_json("products:all", [format_product(product) for product in products], time_to_live=600)
            return [format_product(product) for product in products], 200
        
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

#Endpoint to modify product, only available for admin users
class ModifyProduct(MethodView):
    @admin_required
    def patch(self):
        try:
            data = request.get_json()
            if 'product_id' not in data:
                return {"error": "Missing product_id to modify"}, 400
            
            product_id = data['product_id']
            product = product_repo.get_product_by_id(product_id)
            if not product:
                return {"error": "Product not found"}, 404
            
            items_to_modify = product_modify_item(data)
            if not items_to_modify:
                return {"error": "No fields to update"}, 400
            
            if 'product_price' in items_to_modify and items_to_modify['product_price'] <= 0:
                return {"error": "Price must be positive"}, 400
            
            if 'stock' in items_to_modify and items_to_modify['stock'] < 0:
                return {"error": "Stock cannot be negative"}, 400
            
            updated = product_repo.modify_product(product_id, **items_to_modify)
            
            if not updated:
                return {"error": "Failed to update product"}, 500
            product_cache_invalidation(cache_manager, product_id)
            return {"message" : f'Product {product_id} updated succesfully'}, 200
            
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

#Endpoint only available for admin roles to delete products 
class DeleteProduct(MethodView):
    @admin_required
    def delete(self):
        try:
            data = request.get_json()
            if 'product_id' not in data:
                return {"error": "Missing product_id to delete"}, 400
            
            product_id = data['product_id']
            
            product = product_repo.get_product_by_id(product_id)
            if not product:
                return {"error": "Product not found"}, 404
            
            deleted = product_repo.delete_product(product_id)
            
            if not deleted:
                return {"error": "Failed to delete product"}, 500
            product_cache_invalidation(cache_manager, product_id)
            return {"message": f"Product {product_id} deleted successfully"}, 200
    
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

def product_api_methods(app):
    create_product = CreateProduct.as_view('create_product_api')
    app.add_url_rule('/create_product', view_func=create_product, methods=['POST'])

    get_product = GetProducts.as_view('get_product_api')
    app.add_url_rule('/products', view_func=get_product, methods=['GET'])

    modify_product = ModifyProduct.as_view('modify_product_api')
    app.add_url_rule('/modify_product', view_func=modify_product, methods=['PATCH'])

    delete_product = DeleteProduct.as_view('delete_product_api')
    app.add_url_rule('/delete_product', view_func=delete_product, methods=['DELETE'])