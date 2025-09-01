def first_decorator(func):
    def wrapper(*args):
        print(f'Impriminedo los parametros: {args}')
        result = func(*args)
        print(f'Retorno de la funcion: {result}')
        return result
    return wrapper

@first_decorator
def pokemon_type(a, b):
    return f'The pokemons are {a} {b}'

test_pokemon = pokemon_type('Charizard', 'Pikachu')


