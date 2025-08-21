import csv

# Function to create the CSV file
def student_list_csv_file(file_name, student_list, headers):
        with open(file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(student_list)

# Function to open CSV file previously created
def function_to_open_student_list_csv(file_name):
    try:
        with open('Student list.csv', 'r', encoding='utf-8') as file:  
            reader = csv.DictReader(file)
            student_list = list(reader)
            for student in student_list:
                student['Spanish grade'] = int(student['Spanish grade'])
                student['English grade'] = int(student['English grade'])
                student['Socials grade'] = int(student['Socials grade'])
                student['Science grade'] = int(student['Science grade'])
                student['Average grade'] = float(student['Average grade'])
        return student_list
    
    except FileNotFoundError as error:
        print(f'No hay lista previamente creada. Error: {error}')
        return None