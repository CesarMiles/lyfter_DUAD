from actions import option_one_adding_student_information, all_student_average, get_top_three_students
from data import student_list_csv_file, function_to_open_student_list_csv

# Function to display the menu. No input request.
def menu_display():
    print ('''Menu de opciones:
        1. Si desea ingresar informacion de estudiantes a la base de datos, ingrese 1. 
        2. Si desea ver la informacion actual de estudiantes de la base de datos, ingrese 2. 
        3. Si desea ver los mejores tres promedios de los estudiantes, ingrese 3. 
        4. Si desea ver la nota promedio total de la base de datos, ingrese 4. 
        5. Si desea exportar la base de datos a CSV, ingrese 5. 
        6. Si desea importar una base de datos existente, ingrese 6.
        7. Si desea salir, ingrese 7.   ''')

# Function to gather user input and start loop of options. 
def user_menu_interaction():
    print(f'Bienvenido al programa de Control de Estudiantes.')
    menu_running = True
    student_list = []
    while menu_running:
        menu_display()
        try:
            user_menu_selection = int(input('Ingrese una opcion del menu: '))
            if user_menu_selection not in range(1, 8):
                print('Por favor ingrese un numero entre 1 y 7')
                continue

            elif user_menu_selection == 1:
                student_list.append(option_one_adding_student_information())
                print('Estudiante agregado correctamente')

            elif user_menu_selection == 2:
                if student_list:
                    print(f'Lista de Estudiantes:') 
                    for student in student_list:
                        print(student)
                else:
                    print(f'No hay estudiantes en la base de datos.')
            
            elif user_menu_selection == 3:
                top_students = get_top_three_students(student_list)
                if top_students:
                    print(f'Top 3 de estudiantes:')
                    for i, student in enumerate(top_students, 1):
                        print(f'{i}. {student.full_name} - Promedio: {student.average_grade}')
                else:
                    print(f'No hay estudiantes en la base de datos.')
            
            elif user_menu_selection == 4:
                if student_list:
                    general_average = all_student_average(student_list)
                    print(f'El promedio general de la lista es {general_average}')
                else:
                    print(f'No hay estudiantes en la base de datos.')
            
            elif user_menu_selection == 5:
                try:
                    student_list_csv_file('Student List.csv', student_list)
                except IndexError:
                    print(f'No se puede crear el archivo CSV por que no hay data')
            
            elif user_menu_selection == 6:
                imported_student_list = function_to_open_student_list_csv('Student List.csv')
                if imported_student_list:
                    student_list = imported_student_list
                    print(f'Datos importados correctamente')
                else:
                    print(f'No se pudieron importar los datos')

            elif user_menu_selection == 7:
                print('Gracias por usar el sitema. Cerrando programa.')
                menu_running = False

        except ValueError:
            print('Ingrese un numero entero del 1 al 7 segun su seleccion del menu.')
            continue


