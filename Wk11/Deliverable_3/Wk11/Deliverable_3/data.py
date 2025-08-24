import csv
from models import Student

# Function to convert object to dict
def student_to_dict(student):
    return student.to_dict()

# Fuinction to convert dict to object
def dict_to_student(student_dict):
    return Student(  
        full_name = student_dict['full name'],
        section = student_dict['Section'],
        spanish_grade = int(student_dict['Spanish grade']),
        english_grade = int(student_dict['English grade']),
        socials_grade = int(student_dict['Socials grade']),
        science_grade = int(student_dict['Science grade'])
    )

# Function to create the CSV file
def student_list_csv_file(file_name, student_list):
    if not student_list:
        print('No hay datos para exportar')
        return

    headers = student_list[0].to_dict().keys()

    with open(file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows([student.to_dict() for student in student_list])

# Function to open CSV file previously created
def function_to_open_student_list_csv(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:  
            reader = csv.DictReader(file)
            student_dicts = list(reader)
            if not student_dicts:
                print('El archivo CSV esta vacio')
                return None
            
            student_objects = []
            for student_dict in student_dicts:
                try:
                    student = dict_to_student(student_dict)
                    student_objects.append(student)
                except (ValueError, KeyError) as e:
                    print(f'Error convirtiendo fila: {e}')
                    continue
                
        return student_objects
    
    except FileNotFoundError as error:
        print(f'No hay lista previamente creada. Error: {error}')
        return None