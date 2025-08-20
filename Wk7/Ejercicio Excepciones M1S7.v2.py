def sum(calc_balance, user_input):
        return calc_balance + user_input

def substraction(calc_balance, user_input):
        return calc_balance - user_input

def multiply(calc_balance, user_input):
        return calc_balance * user_input

def division(calc_balance, user_input):
        try:
                return calc_balance / user_input
        except ZeroDivisionError as error:
                calc_balance = 0
                return f'No se puede dividir por . {error}'

def calculator(calc_balance, user_input, operator):
        if operator == '+':
                return sum(calc_balance, user_input)
        elif operator == '-':
                return substraction(calc_balance, user_input)
        elif operator == '*':
                return multiply(calc_balance, user_input)
        elif operator == '/':
                return division(calc_balance, user_input)
        return calc_balance


def input_numbers():
        input_running = True
        while input_running:
                try:
                        return int(input('Ingrese un numero: '))
                except ValueError as error:
                        print(f'Por favor ingresa valores numericos enteros. {error}')



def application():
        calc_balance = 0
        app_running = True

        while app_running:
                arithmetic_operator =  input('Ingrese "-" para restar, "+" para sumar, "*" para multiplicar, "/" para dividir" o "AC" para borrar todo, si deseas salir de la calculadora digite "salir": ')

                if arithmetic_operator.lower() == 'salir':
                        app_running = False
                        continue
                
                elif arithmetic_operator.upper() == 'AC':
                                calc_balance = 0
                                print('Calculadora reiniciada')
                                continue
                
                elif arithmetic_operator not in {'+', '-', '*', '/', 'AC'}:
                        print(f'Ingresaste un valor diferente. Por favor vuelve a digitar un valor valido, "+", "-", "*", "/", "AC" o "salir": ')
                        continue
                
                user_input = input_numbers()
                result = calculator(calc_balance, user_input, arithmetic_operator)
                if isinstance(result, str):
                        print(result)
                else:
                        calc_balance = result
                        print(calc_balance)


application()