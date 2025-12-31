
def user_id_check(token, jwt_manager):
    token = token.replace("Bearer ", "")
    decoded = jwt_manager.decode(token)
    user_id = decoded["user_id"]
    return user_id