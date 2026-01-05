from flask.views import MethodView
from flask import request, jsonify
from jwt_manager import jwt_manager
from user_repo import user_repo
from decorators import token_required
from utils import user_modify_items
from sqlalchemy.exc import IntegrityError


#Endpoint to register a new user. This will retrieve a token for usage if required.
class RegisterUser(MethodView):
    def post(self):
        try:
            data = request.get_json()
            required_fields = ["email", "password"]
            if not all(field in data for field in required_fields):
                return {"error" : "Missing required fields email or password"}, 422
            
            role = data.get("role", "user")

            try:
                result = user_repo.create_user(email=data.get("email"), password=data.get("password"), role=role)
            except IntegrityError:
                return {"error": "Email already registered"}, 409
            
            user_id = result

            token = jwt_manager.encode({"user_id":user_id, "role":role})

            return jsonify(token=token), 201
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500
        

#Endpoint to login, this method will use login and password to retrieve token
class Login(MethodView):
    def post(self):
        try:
            data = request.get_json()
            required_fields = ["email", "password"]
            if not all(field in data for field in required_fields):
                return {"error" : "Missing required fields email or password"}, 422
            
            result = user_repo.user_login(data.get('email'), data.get('password'))
            if result == None:
                return {"error": "email or password not found"}, 403
            print(result)
            token = jwt_manager.encode({"user_id":result[0], "role":result[3]})
            return jsonify(token=token), 201
        
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

#Endpoint to retrieve user details on /me URL 
class GetUserDetails(MethodView):
    @token_required
    def get(self):
        try:
            user = user_repo.get_user_details(request.user_id)
            return jsonify(user_id=request.user_id, email=user[1], role=user[3])

        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

class ModifyUser(MethodView):
    @token_required
    def patch(self):
        try:
            data = request.get_json()
            items_to_modify = user_modify_items(data)

            if not items_to_modify:
                return {"error": "No fields to update"}, 400
            
            if 'role' in items_to_modify:
                return {"error": "role cannot be modified"}, 400
            
            user_repo.modify_user(request.user_id, **items_to_modify)
            return {"message": f"User {request.user_id} updated succesfully"}, 200
        
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

class DeleteUser(MethodView):
    @token_required
    def delete(self):
        try:
            data = request.get_json()
            if data.get('user_id') != request.user_id:
                return {"error": "You can only delete your own user"}, 400
            
            user_repo.delete(request.user_id)
            return {"message": f"User {request.user_id} deleted succesfully"}, 200
            
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500


def user_api_methods(app):
    register_user = RegisterUser.as_view('register_user_api')
    app.add_url_rule('/register', view_func=register_user, methods=['POST'])

    user_login = Login.as_view('login_api')
    app.add_url_rule('/login', view_func=user_login, methods=['POST'])

    get_user = GetUserDetails.as_view('get_user_details_api')
    app.add_url_rule('/me', view_func=get_user, methods=['GET'])

    modify_user = ModifyUser.as_view('modify_user_api')
    app.add_url_rule('/modify_user', view_func=modify_user, methods=['PATCH'])

    delete_user = DeleteUser.as_view('delete_user')
    app.add_url_rule('/delete_user', view_func=delete_user, methods=['DELETE'])