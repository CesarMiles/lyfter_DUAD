from datetime import date

# Class user to define the uer name and the date of birth 
class User:
    def __init__(self, name, birth_year, birth_month, birth_day):
        self.name = name
        self.date_of_birth = date(birth_year, birth_month, birth_day)
    
    #Property to calculate age of user
    @property
    def age(self):
        today = date.today()
        return (today.year - self.date_of_birth.year)
    

#Decorator to use user as parameter to calculate if user is underage
def check_under_age(func):
    def wrapper(user, *args):
        if user.age < 18:
            raise ValueError(f'Usuario {user.name} es menor de edad.')
        return func(user, *args)
    return wrapper

#Function to test decorator
@check_under_age
def enter_bar(user, bar_name):
    print(f'{user.name} entered {bar_name}')


#Testing enviorment
user1 = User('Cesar', 2010, 5, 14)
enter_bar(user1, 'Bar feliz')
