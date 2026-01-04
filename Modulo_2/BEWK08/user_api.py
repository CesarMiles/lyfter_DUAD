from flask.views import MethodView
from flask import request, jsonify
from jwt_manager import jwt_manager
from user_repo import user_repo
from utils import user_modify_items
from decorators import token_required, admin_required

# End point to register a new user, this utilizes values username, password and role, after registration token is provided
class RegisterUser(MethodView):
    def post(self):
        try:
            data = request.get_json()
            required_fields = ["username", "password", "role"]
            if not all(field in data for field in required_fields):
                return {"error": "Missing required fields"}, 422
            else:
                result = user_repo.create(username= data.get("username"), password= data.get("password"), role=data.get("role"))
                user_id = result

                token = jwt_manager.encode({"user_id":user_id})

                return jsonify(token=token), 201
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# End point to login this will retrieve token 
class Login(MethodView):
    def post(self):
        try:
            data = request.get_json()
            if data.get('username') == None or data.get('password') == None:
                return {"error": "Missing username or password fields"}, 422
            result = user_repo.get_user_login(data.get('username'), data.get('password'))
            if result == None:
                return {"error": "username or password not found"}, 403
            user_id = result[0]

            token = jwt_manager.encode({"user_id":user_id})

            return jsonify(token=token), 201 
        
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500


# End point to retrieve user details, this proivde only the user whose authenticated through token. 
class GetUserDetials(MethodView):
    @token_required
    def get(self):
        try:
            user = user_repo.get_user_details(request.user_id)
            return jsonify(user_id=request.user_id, username=user[1], role=user[3])

        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# End point only available for admins to modify users 
class ModifyUser(MethodView):
    @admin_required
    def patch(self):
        try:
            data = request.get_json()
            if data.get('user_id') == None:
                return {"error": "Missing user_id to modify"}, 400
            
            user_id_to_modify = data['user_id']
            items_to_modify = user_modify_items(data)

            if not items_to_modify:
                return {"error": "No fields to update"}, 400
                
            user_repo.modify(modify_user_id=user_id_to_modify,**items_to_modify)
            return {"message": f"User {user_id_to_modify} updated succesfully"}, 200
        
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# Endpoint only available for admins to delete users 
class DeleteUser(MethodView):
    @admin_required
    def delete(self):
        try:
            data = request.get_json()
            if data.get('user_id') == None:
                return {"error": "Missing user_id to delete"}, 400
            
            user_id_to_delete = data['user_id']
            user_repo.delete(user_id_to_delete)
            return {"message": f"User {user_id_to_delete} deleted succesfully"}, 200
            
    
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

def user_api_methods(app):
    register_user = RegisterUser.as_view('register_user_api')
    app.add_url_rule('/register', view_func=register_user, methods=['POST'])

    user_login = Login.as_view('login_api')
    app.add_url_rule('/login', view_func=user_login, methods=['POST'])

    get_user = GetUserDetials.as_view('get_user_details_api')
    app.add_url_rule('/me', view_func=get_user, methods=['GET'])

    modify_user = ModifyUser.as_view('modify_user_api')
    app.add_url_rule('/modify_user', view_func=modify_user, methods=['PATCH'])

    delete_user = DeleteUser.as_view('delete_user')
    app.add_url_rule('/delete_user', view_func=delete_user, methods=['DELETE'])
