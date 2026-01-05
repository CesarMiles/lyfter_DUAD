from flask import request
from functools import wraps
from jwt_manager import jwt_manager
from user_repo import user_repo


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth or not auth.startswith('Bearer '):
            return {"error": "Bearer token required"}, 401
        
        token = auth[7:] 
        payload = jwt_manager.decode(token)
        
        if not payload or "user_id" not in payload:
            return {"error": "Invalid token"}, 401
        
        # Adjuntar al request
        request.user_id = payload["user_id"]
        request.user_payload = payload  
        
        return f(*args, **kwargs)
    return decorator


def admin_required(f):
    @wraps(f)
    @token_required  
    def decorator(*args, **kwargs):
        if hasattr(request, 'user_payload') and request.user_payload.get("role") == "admin":
            return f(*args, **kwargs)
        
        user = user_repo.get_user_details(request.user_id)
        
        if not user or user[3] != "admin":  
            return {"error": "Admin privileges required"}, 403
        
        return f(*args, **kwargs)
    return decorator