def first_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Printing function parameters: {args} and {kwargs}')
        result = func(*args, **kwargs)
        print(f'Printing function outcome: {result}')
        return result
    return wrapper

@first_decorator
def pokemon_type(*args, **kwargs):
    return f'The pokemons are {args} and their type {kwargs}'

test_pokemon = pokemon_type('Charizard', 'Pikachu', Charizard='Fire', Pikachu='Electric')


