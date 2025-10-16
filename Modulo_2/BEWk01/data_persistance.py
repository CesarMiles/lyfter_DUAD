import json

# Function to save json file based on tasks
def task_db_update(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)
    return print('Database updated')

# Function to open json file 
def read_tasks_from_file():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:  
            tasks_data = json.load(file)
            print(f'Data base loaded')
        return tasks_data
    except FileNotFoundError as error:
        return []
    except json.decoder.JSONDecodeError as error:
        return []