

def user_modify_items(data):
    kwargs = {}
    if 'username' in data:
        kwargs['username'] = data['username']
    if 'password' in data:
        kwargs['password'] = data['password']
    if 'role' in data:
        kwargs['role'] = data['role']
    return kwargs