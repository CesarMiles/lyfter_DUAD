from models import Student
# Function to ensure that info from grades is type 'int'
def get_valid_int(prompt, min_value = 0, max_value = 100):
    while True:
        try:
            score = int(input(prompt))
            if min_value <= score <= max_value:
                return score
            else:
                print(f'La nota debe ser un numero entre {min_value} y {max_value}')
        except ValueError:
            print('Debe ser un numero entero!')

# Function triggered by the user input. To collect student information and generate object.
def option_one_adding_student_information():
    print('Ingrese los datos del estudiante')
    full_name = input('Nombre Completo: ')
    section = input('Seccion: ')
    spanish_grade = get_valid_int('Nota español: ')
    english_grade = get_valid_int('nota de ingles: ')
    socials_grade = get_valid_int('Nota de sociales: ')
    science_grade = get_valid_int('Nota de ciencias: ')

    return Student(full_name, section, spanish_grade, english_grade, socials_grade, science_grade)

# Function to generate general average among students 
def all_student_average(student_list):
    if not student_list:
        return 0.0
    all_student_average = []
    for student in student_list:
        all_student_average.append(student.average_grade)
    
    total_average = sum(all_student_average) / len(all_student_average)
    return round(total_average, 2)

# Function to get student average for sorting
def get_student_average(student):
    return student.average_grade

# Function to get top three students
def get_top_three_students(student_list):
    if not student_list:
        return []
    
    sorted_students = sorted(student_list, key = get_student_average, reverse = True)
    return sorted_students[:3]