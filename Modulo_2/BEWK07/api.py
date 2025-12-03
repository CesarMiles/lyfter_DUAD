from flask.views import MethodView
from flask import request, Response, jsonify
from db_manager import DB_Manager
from jwt_manager import JWTManager
from user_repo import UserRepository

conn = DB_Manager()
jwt_manager = JWTManager("superclave", 'HS256')

class RegisterUserAPI(MethodView):
    def post(self):
        try:
            data = request.get_json()
            required_fields = ["username", "password", "role"]
            if not all(field in data for field in required_fields):
                return {"error": "Missing required fields"}, 400
            else:
                user_repo = UserRepository(conn)
                result = user_repo.create(username= data.get("username"), password= data.get("password"), role=data.get("role"))
                user_id = result

                token = jwt_manager.encode({"id":user_id})

                return jsonify(token=token), 201
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500