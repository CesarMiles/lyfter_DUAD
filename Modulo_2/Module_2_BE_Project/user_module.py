from flask.views import MethodView
from flask import request, jsonify
from jwt_manager import jwt_manager
from user_repo import user_repo
from utils import user_id_check


#Endpoint to register a new user. This will retrieve a token for usage if required.
class RegisterUser(MethodView):
    def post(self):
        try:
            data = request.get_json()
            required_fields = ["email", "password"]
            if not all(field in data for field in required_fields):
                return {"error" : "Missing required fields email or password"}, 422
            else:
                role = data.get("role", "user")
                result = user_repo.create_user(email=data.get("email"), password=data.get("password"), role=role)
                user_id = result

                token = jwt_manager.encode({"user_id":user_id})

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

            token = jwt_manager.encode({"user_id":result[0]})
            return jsonify(token=token), 201
        
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

#Endpoint to retrieve user details on /me URL 
class GetUserDetails(MethodView):
    def get(self):
        try:
            token = request.headers.get('Authorization')
            if token is not None:
                user_id = user_id_check(token, jwt_manager)
                user = user_repo.get_user_details(user_id)
                return jsonify(user_id=user[0], email=user[1], role=user[3])
            else:
                return {"message": f"Token is required to perform this action"}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500


def user_api_methods(app):
    register_user = RegisterUser.as_view('register_user_api')
    app.add_url_rule('/register', view_func=register_user, methods=['POST'])

    user_login = Login.as_view('login_api')
    app.add_url_rule('/login', view_func=user_login, methods=['POST'])

    get_user = GetUserDetails.as_view('get_user_details_api')
    app.add_url_rule('/me', view_func=get_user, methods=['GET'])