import csv

# Function to capture intent of user to continue with the data entry 
def user_info_entry_confirmation():
    running = True
    while running:
        user_input = input('Confirme si desea ingresar informacion al archivo. Y/N: ').upper()
        if user_input == 'Y':
            running = False
            return True
        elif user_input == 'N':
            running = False
            return False
        else:
            print('Por favor ingrese un valor valido')
            continue

# Function to build the dictionary that will be used to create the list
def dictionary_construction():
    game_info = {}
    game_info['name'] = input('Ingrese el nombre del juego: ')
    game_info['genre'] = input('Ingrese el genero del juego: ')
    game_info['developer'] = input('Ingrese el nombre del desarrollador: ')
    game_info['clasification'] = input('Ingrese la clasificacion ESRB: ')
    return game_info    

# Function to create the list that will be used with the function to create the csv file
def game_list_creation():
    game_list = []
    while user_info_entry_confirmation():
        game_list.append(dictionary_construction())
    return game_list

# Function to create the CSV file, note: this save the csv file using \t as delimiter instead of regular ,
def game_list_csv_file(file_path, data, headers):
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(data)

# Main function to combine functions game_list_creation and game_list_csv_file
def main():
    games_data = game_list_creation()
    try: 
        game_list_csv_file('game_list_with_tab.csv', games_data, games_data[0].keys())
    except IndexError:
        print("No se genero archivo porque no hay datos")


main()