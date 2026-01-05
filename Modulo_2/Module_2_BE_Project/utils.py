
def user_modify_items(data):
    kwargs = {}
    if 'email' in data:
        kwargs['email'] = data['email']
    if 'password' in data:
        kwargs['password'] = data['password']
    if 'role' in data:
        kwargs['role'] = data['role']
    return kwargs