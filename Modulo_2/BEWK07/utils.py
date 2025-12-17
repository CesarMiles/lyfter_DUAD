

def user_modify_items(data):
    kwargs = {}
    if 'username' in data:
        kwargs['username'] = data['username']
    if 'password' in data:
        kwargs['password'] = data['password']
    if 'role' in data:
        kwargs['role'] = data['role']
    return kwargs


def admin_check(token,jwt_manager, user_repo):
    token = token.replace("Bearer ", "")
    decoded = jwt_manager.decode(token)
    requester_id = decoded["user_id"]
    requester = user_repo.get_user_details(requester_id)
    if not requester[3] == "admin":
        return False
    return True


def format_product(product_row):
    return {
        "product_id": product_row[0],
        "product_name": product_row[1],
        "product_price": product_row[2],
        "entry_date": product_row[3],
        "stock": product_row[4]
    }

def product_modify_item(data):
    kwargs = {}
    if 'product_name' in data:
        kwargs['product_name'] = data['product_name']
    if 'product_price' in data:
        kwargs['product_price'] = data['product_price']
    if 'entry_date' in data:
        kwargs['entry_date'] = data['entry_date']
    if 'stock' in data:
        kwargs['stock'] = data['stock']
    return kwargs

def purchase_req_checks(request):
    if 'products' not in request.json:
        raise ValueError('Products missing from the body')
    for products in request.json['products']:
        if 'product_id' not in products:
            raise ValueError('Products id missing from the body')
        if 'quantity' not in products:
            raise ValueError('Quantity id missing from the body')
        

def format_invoices(invoice_row):
    return {
        "invoice_id": invoice_row[0],
        "user_id": invoice_row[1],
        "total_amount": invoice_row[2],
        "invoice_status": invoice_row[3]
    }