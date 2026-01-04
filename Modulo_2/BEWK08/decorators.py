from flask import request
from functools import wraps
from jwt_manager import JWTManagerRSA
from db_manager import DB_Manager
from user_repo import UserRepository

conn = DB_Manager()
jwt_manager = JWTManagerRSA()
user_repo = UserRepository(conn)

def user_id_check(token, jwt_manager):
    token = token.replace("Bearer ", "")
    decoded = jwt_manager.decode(token)
    user_id = decoded["user_id"]
    return user_id

def admin_check(token,jwt_manager, user_repo):
    token = token.replace("Bearer ", "")
    decoded = jwt_manager.decode(token)
    requester_id = decoded["user_id"]
    requester = user_repo.get_user_details(requester_id)
    if not requester[3] == "admin":
        return False
    return True


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            token = request.headers.get('Authorization')
            if not token:
                return {"message": f"Token is required to perform this action"}, 400
            
            user_id = user_id_check(token, jwt_manager)

            request.user_id = user_id

            return f(*args, **kwargs)
        
        except Exception as e:
            return {"error": f"Authentication error: {e}"}, 401

    return decorator

def admin_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            token = request.headers.get('Authorization')
            if not token:
                return {"message": f"Token is required to perform this action"}, 400
            
            user_id = user_id_check(token, jwt_manager)
            request.user_id = user_id
            
            is_admin = admin_check(token, jwt_manager, user_repo)
            if not is_admin:
                return {"error": "Admin privileges required"}, 401
            
            return f(*args, **kwargs)
            
        except Exception as e:
            return {"error": f"Authentication error: {e}"}, 401
    
    return decorator