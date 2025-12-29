from flask.views import MethodView
from flask import request, jsonify
from db_manager import DB_Manager
from jwt_manager import JWTManagerRSA
from product_repo import ProductRepository
from utils import admin_check, format_product, product_modify_item, format_product_detail, cache_invalidation
from user_repo import UserRepository
from cache import cache_manager

conn = DB_Manager()
jwt_manager = JWTManagerRSA()
product_repo = ProductRepository(conn)
user_repo = UserRepository(conn)

# End point to create products, only admin can perform this action 
class CreateProduct(MethodView):
    def post(self):
        try: 
            token = request.headers.get('Authorization')
            if (token is not None):
                is_admin = admin_check(token, jwt_manager, user_repo)
                if not is_admin:
                    return {"error": "Admin privileges required"}, 401
                
                data = request.get_json()
                required_fields = ['product_name', 'product_price', 'entry_date', 'stock']
                if not all(field in data for field in required_fields):
                    return {"error": "Missing required fields"}, 422
                
                else:
                    result = product_repo.create(
                        product_name = data.get("product_name"), 
                        product_price= data.get("product_price"), 
                        entry_date= data.get("entry_date"), 
                        stock= data.get("stock"))
                    # Confirmation of cache to invalidate data once new item is added.
                    if cache_manager.get_json("products:all"):
                        cache_manager.delete_data("products:all")
                    return {"message": f"product {result[1]} has been added"}
            else:
                return {"message": f"Token is required to perform this action"}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# Endpoint to list products only admin can perform this action to check on stock 
class GetProducts(MethodView):
    def get(self):
        try:
            # Verification to confirm Admin to perform this action
            token = request.headers.get('Authorization')
            if (token is not None):
                is_admin = admin_check(token, jwt_manager, user_repo)
                if not is_admin:
                    return {"error": "Admin privileges required"}, 401

                # If query is added to locate product by id process triggers and return details. 
                filtered_product_id = request.args.get('product_id')
                if filtered_product_id:
                    cache_key = f"product:{filtered_product_id}" # First endpoint will verify if product is within the cachedb 
                    cached_product = cache_manager.get_json(cache_key)
                    # If within cache, it will retrieve the data
                    if cached_product:
                        return jsonify(cached_product)

                    filtered_product = product_repo.get_product_by_id(filtered_product_id)
                    if not filtered_product:
                        return {"error": "Product not found"}, 404

                    formatted_filtered_product = format_product_detail(filtered_product)

                    # Mechanism to add value to cache for future searches
                    cache_manager.store_json(cache_key, formatted_filtered_product, time_to_live=600)
                    return formatted_filtered_product
            
                # Checking if all products are stored in cache, if they are confirmed process will retrieve data and excit the method
                all_products_cache = cache_manager.get_json("products:all")
                if all_products_cache:
                    return jsonify(all_products_cache)
                else:
                    products = product_repo.get_products()
                    formatted_products = [format_product(product) for product in products]
                    cache_manager.store_json("products:all", formatted_products, time_to_live=600)
                    return formatted_products
            
            else: 
                return {"message": f"Token is required to perform this action"}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# Modify endpoint only available for admin roles 
class ModifyProduct(MethodView):
    def patch(self):
        try:
            token = request.headers.get('Authorization')
            if (token is not None):
                is_admin = admin_check(token, jwt_manager, user_repo)
                if not is_admin:
                    return {"error": "Admin privileges required"}, 401
                
                data = request.get_json()
                if data.get('product_id') == None:
                    return {"error": "Missing product_id to modify"}, 400
                product_id_to_modify = data['product_id']
                items_to_modify = product_modify_item(data)

                if not items_to_modify:
                    return {"error": "No fields to update"}, 400
                
                product_repo.modify(product_id_to_modify, **items_to_modify)
                # Function to invalidate cache from individual product and all products if necessary
                cache_invalidation(cache_manager, product_id_to_modify)

                return {"message" : f'Product {product_id_to_modify} updated succesfully'}, 200

            else: 
                return {"message": f"Token is required to perform this action"}, 400 
            
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# Delete end point only available for admin roles 
class DeleteProduct(MethodView):
    def delete(self):
        try:
            token = request.headers.get('Authorization')
            if (token is not None):
                is_admin = admin_check(token, jwt_manager, user_repo)
                if not is_admin:
                    return {"error": "Admin privileges required"}, 401
        
                data = request.get_json()
                if data.get('product_id') == None:
                    return {"error": "Missing product_id to delete"}, 400
            
                product_id_to_delete = data['product_id']
                product_repo.delete(product_id_to_delete)
                # Function to invalidate cache from individual product and all products if necessary# Function to invalidate cache from individual product and all products if necessary
                cache_invalidation(cache_manager, product_id_to_delete)
                return {"message": f"Product {product_id_to_delete} deleted succesfully"}, 200

            else: 
                return {"message": f"Token is required to perform this action"}, 400
    
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

def product_api_methods(app):
    create_product = CreateProduct.as_view('create_product_api')
    app.add_url_rule('/create_product', view_func=create_product, methods=['POST'])

    get_products = GetProducts.as_view('get_products_api')
    app.add_url_rule('/list_products', view_func=get_products, methods=['GET'])

    modify_product = ModifyProduct.as_view('modify_product_api')
    app.add_url_rule('/modify_product', view_func=modify_product, methods=['PATCH'])

    delete_product = DeleteProduct.as_view('delete_product_api')
    app.add_url_rule('/delete_product', view_func=delete_product, methods=['DELETE'])