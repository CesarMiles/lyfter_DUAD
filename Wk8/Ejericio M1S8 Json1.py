import json

# Function to open json file and save data locally on python
def function_to_open_jsonfile():
    try:
        with open('Jsonfile.json', 'r', encoding='utf-8') as file:  
            pokemon_data = json.load(file)
            json_pokemon_file = json.dumps(pokemon_data, indent=4)
            print(f'Esta es la base de datos Pokemon. \n {json_pokemon_file}')
        return pokemon_data
    except FileNotFoundError as error:
        print(f'No se encuentra la base de datos. Error: {error}')
        return None

# Function to get user confirmation on updating the current database(db)
def user_modification_confirmation():
    running = True
    while running:
        user_input = input('Confirme si desea actualizar la base de datos. Y/N: ').upper()
        if user_input == 'Y':
            running = False
            return True
        elif user_input == 'N':
            running = False
            return False
        else:
            print('Por favor ingrese un valor valido')
            continue

# Function to create a dictionary to be added to the current data base as an append.
def create_new_pokemon():
    print ('Ingrese los datos del nuevo pokemon')
    return  {
        'name': {'english': input(f'Nombre: ')}, 
        'type': [input(f'tipo: ')], 
        'base': {
            'HP': get_valid_int('HP: '), 
            'Attack': get_valid_int('Attack: '), 
            'Defense': get_valid_int('Defense: '), 
            'Sp. Attack': get_valid_int('Sp. Attack: '), 
            'Sp. Defense': get_valid_int('sp. Defense: '), 
            'Speed': get_valid_int('Speed: ')
            }
            }

# Function to ensure that info from base is type 'int'
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Debe ser un numero entero!')

# Function to update the current Pokemon db
def updating_pokemon_db(pokemon_db):
    with open('jsonfile.json', 'w', encoding='utf-8') as file:
        json.dump(pokemon_db, file, indent=4)
    return print('Base de datos guardada!')

# Main fuction to launch application.
def main():
    pokemon_db = function_to_open_jsonfile()

    if pokemon_db:
        if user_modification_confirmation():
            new_pokemon = create_new_pokemon()
            pokemon_db.append(new_pokemon)
            updating_pokemon_db(pokemon_db)
        else:
            print('Operacion cancelada')
    else:
        print(f'Cerrando programa')

main()