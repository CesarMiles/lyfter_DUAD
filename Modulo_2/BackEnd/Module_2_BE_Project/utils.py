
def user_modify_items(data):
    kwargs = {}
    if 'email' in data:
        kwargs['email'] = data['email']
    if 'password' in data:
        kwargs['password'] = data['password']
    if 'role' in data:
        kwargs['role'] = data['role']
    return kwargs

def format_product_detail(product):
    if isinstance(product, dict):
        return {
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "product_price": product["product_price"],
            "stock": product["stock"]
        }
    # If its a tuple list
    elif isinstance(product, (tuple, list)):
        return {
            "product_id": product[0],
            "product_name": product[1],
            "product_price": product[2],
            "stock": product[3]
        }
    
def format_product(product_row):
    return {
        "product_id": product_row[0],
        "product_name": product_row[1],
        "product_price": product_row[2],
        "stock": product_row[3]
    }

def format_invoice(invoices):
    return [{
                "invoice_id": inv[0],
                "user_id": inv[1],
                "total_amount": inv[2],
                "status": inv[3]
            } for inv in invoices]

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

def user_cache_invalidation(cache_manager, user_id):
    if cache_manager.get_data(f"users:{user_id}"):
        cache_manager.delete_data(f"users:{user_id}")
    return 

def product_cache_invalidation(cache_manager, product_id):
    if cache_manager.get_data(f"product:{product_id}"):
        cache_manager.delete_data(f"product:{product_id}")
    if cache_manager.get_data("products:all"):
        cache_manager.delete_data("products:all")
    return 

def invoice_cache_invalidation(cache_manager, user_id):
    if cache_manager.get_data(f"invoice:{user_id}"):
        cache_manager.delete_data(f"invoice:{user_id}")
    if cache_manager.get_data("invoice:all"):
        cache_manager.delete_data("invoice:all")
    return 