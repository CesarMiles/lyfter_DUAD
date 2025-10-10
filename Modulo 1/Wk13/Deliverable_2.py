def int_only(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg,(int, float)):
                raise TypeError (f'The parameters {arg} must be a number')
        
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f'The parameter {key}={value} must be a number')
            
        result = func(*args, **kwargs)
        return result


    return wrapper

@int_only
def calculate_total_price(price, quantity, discount=0):
    return price * quantity * (1 - discount)


print(calculate_total_price(100, 2, discount=0.1))

try:
    print(calculate_total_price(100, 2, discount='10%'))
except TypeError as e:
    print(f'Error found: {e}')