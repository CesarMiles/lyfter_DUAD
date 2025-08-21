from actions import option_one_adding_student_information, student_average_grade, student_information_with_grade_average

# Function to display the menu. No input request.
def menu_display():
    print ('''Bienvenido al programa de Control de Estudiantes, por favor lea el menu. 
        1. Si desea ingresar informacion de estudiantes a la base de datos, ingrese 1. 
        2. Si desea ver la informacion actual de estudiantes de la base de datos, ingrese 2. 
        3. Si desea ver los mejores tres promedios de los estudiantes, ingrese 3. 
        4. Si desea ver la nota promedio total de la base de datos, ingrese 4. 
        5. Si desea exportar la base de datos a CSV, ingrese 5. 
        6. Si desea importar una base de datos existente, ingrese 6.
        7. Si desea salir, ingrese 7.   ''')

# Function to generate value to be added to the list that will be used as db
def menu_action_option_one():
    student_info = option_one_adding_student_information()
    student_with_avg = student_information_with_grade_average(student_info)
    return student_with_avg

# Function to gather user input and start loop of options. 
def user_menu_interaction():
    menu_running = True
    student_list = []
    while menu_running:
        try:
            user_menu_selection = int(input('Ingrese una opcion del menu: '))
            if user_menu_selection == 1:
                student_list.append(menu_action_option_one())
                print('Estudiante agregado correctamente')

            elif user_menu_selection == 2:
                print(f'Lista de Estudiantes: {student_list}') 

            elif user_menu_selection == 7:
                print('Gracias por usar el sitema. Cerrando programa.')
                menu_running = False

        except ValueError:
            print('Ingrese un numero entero del 1 al 7 segun su seleccion del menu.')
            continue


