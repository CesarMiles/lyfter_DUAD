def open_and_read_file(file_name):
    new_list = []
    try:
        with open(file_name) as file:
            for line in file.readlines():
                new_list.append(line.strip() + '\n')
        return new_list
    except FileNotFoundError as error:
        print(f'El archivo {file_name} no existe. {error}')
        exit()


def create_sorted_list(file_name):
    songs_list = open_and_read_file(file_name)
    songs_list.sort()
    return songs_list


def write_new_sorted_list(file_name, new_file_name):
    with open(new_file_name, 'w', encoding='utf-8') as file:
        file.writelines(create_sorted_list(file_name))


def main_function(file_name, new_file_name):
    create_sorted_list(file_name)
    write_new_sorted_list (file_name, new_file_name)


main_function('Songs.txt', 'New Song List.txt')