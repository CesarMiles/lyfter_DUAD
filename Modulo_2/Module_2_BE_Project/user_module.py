from flask.views import MethodView
from flask import request, jsonify
from jwt_manager import jwt_manager
from user_repo import user_repo


#Endpoint to register a new user. This will retrieve a token for usage if required.
class RegisterUser(MethodView):
    def post(self):
        try:
            data = request.get_json()
            required_fields = ["email", "password"]
            if not all(field in data for field in required_fields):
                return {"error" : "Missing required fields username or password"}, 422
            else:
                role = data.get("role", "user")
                result = user_repo.create_user(email=data.get("email"), password=data.get("password"), role=role)
                user_id = result

                token = jwt_manager.encode({"user_id":user_id})

                return jsonify(token=token), 201
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500
        

def user_api_methods(app):
    register_user = RegisterUser.as_view('register_user_api')
    app.add_url_rule('/register', view_func=register_user, methods=['POST'])