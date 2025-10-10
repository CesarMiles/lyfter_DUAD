public_variable = 'Variable Global'

def internal_variable():
    secret_variable = 'x'
    print(f'Esta es la variable secreta {secret_variable}')


def pen_testing():
    try:
        print(f'La variable secreta es {secret_variable}')
    except NameError:
        global public_variable 
        public_variable = 'variable publica'
        print(f'No se puede accesar a la variable secreta, solo a la {public_variable}')


internal_variable()
pen_testing()
print(public_variable)