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

# Function triggered by the user input. To collect student information.
def option_one_adding_student_information():
    print('Ingrese los datos del estudiante')
    return {
        'full name' : input('Nombre Completo: '),
        'Section' : input('Seccion: '),
        'Spanish grade' : get_valid_int('Nota español: '),
        'English grade' : get_valid_int('Nota de ingles: '),
        'Socials grade' : get_valid_int('Nota de sociales: '),
        'Science grade' : get_valid_int('Nota de ciencias: ')
    }


# Function to generage average of grades. 
def student_average_grade(student_info):
    student_average_grade = (student_info['Spanish grade'] +
                             student_info['English grade'] +
                             student_info['Socials grade'] +
                             student_info['Science grade']) / 4
    return student_average_grade

# Function to add average score to individual student info.
def student_information_with_grade_average(student_info):
    student_full_info = student_info
    student_full_info['Average grade'] = student_average_grade(student_info)
    return student_full_info








