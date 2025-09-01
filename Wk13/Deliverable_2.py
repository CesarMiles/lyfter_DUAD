def int_only(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg,(int, float)):
                raise TypeError (f'The parameters {arg} must be a number')
        result = func(*args)
        return result


    return wrapper

@int_only
def sum_two_numbers(a, b):
    return a + b


sumarization = sum_two_numbers(3, 2)
print(sumarization)