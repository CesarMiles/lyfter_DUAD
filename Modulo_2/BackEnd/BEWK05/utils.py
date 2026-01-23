def user_creation_req_check(request):
    if 'username' not in request.json:
        raise ValueError('username missing from the body')
    if 'password' not in request.json:
        raise ValueError('password missing from the body')
    if 'email' not in request.json:
        raise ValueError('email missing from the body')
    if 'full_name' not in request.json:
        raise ValueError('full_name missing from the body')
    if 'date_of_birth' not in request.json:
        raise ValueError('date_of_birth missing from the body')
    if 'account_status' not in request.json:
        raise ValueError('account_status missing from the body')
    

def car_creation_req_check(request):
    if 'brand' not in request.json:
        raise ValueError('brand missing from the body')
    if 'model' not in request.json:
        raise ValueError('model missing from the body')
    if 'factory_year' not in request.json:
        raise ValueError('factory year missing from the body')
    if 'car_rental_status' not in request.json:
        raise ValueError('car rental status missing from the body')

def rent_creation_req_check(request):
    if 'car_id' not in request.json:
        raise ValueError('car id missing from the body')
    if 'user_id' not in request.json:
        raise ValueError('user id missing from the body')
    if 'rent_start' not in request.json:
        raise ValueError('rent start missing from the body')
    if 'rent_end' not in request.json:
        raise ValueError('rent end missing from the body')
    if 'payment_status' not in request.json:
        raise ValueError('payment status missing from the body')
    if 'rent_status' not in request.json:
        raise ValueError('rent status missing from the body')
    

def user_modification_check(request):
    if 'account_status' not in request.json:
        raise ValueError('account status missing from body')
    if 'user_id' not in request.json:
        raise ValueError('user id missing from body')

def car_modification_check(request):
    if 'car_rental_status' not in request.json:
        raise ValueError('car rental status missing from body')
    if 'car_id' not in request.json:
        raise ValueError('car id missing from body')

def rent_modification_check(request):
    if 'rental_id' not in request.json:
        raise ValueError('rental id missing from body')
    if 'rent_status' not in request.json:
        raise ValueError('rent status missing from body')

def car_return_check(request):
    if 'car_id' not in request.json:
        raise ValueError('car id missing from body')
    if 'rental_id' not in request.json:
        raise ValueError('rental id missing from body')
    
def past_due_flag_check(request):
    if 'user_id' not in request.json:
        raise ValueError('user id missing from body')