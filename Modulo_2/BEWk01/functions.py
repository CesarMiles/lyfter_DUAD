
# Function to validate states of tasks
def state_check(request):
    valid_states = ['to do', 'in progress', 'completed']
    if request.json['state'] not in valid_states:
        raise ValueError('state must be either: to do, in progress, completed')


# Function to validate Title, Description and State
def task_req_check(request):
    if 'title' not in request.json:
            raise ValueError('title missing from the body')
    if 'description' not in request.json:
            raise ValueError('description missing from the body')
    if 'state' not in request.json:
            raise ValueError('state missing from the body')
    

# Function to find task by id 
def find_task_by_id(task_id, tasks_list):
    for index, task in enumerate(tasks_list):
            if task['id'] == task_id:
                return index, task
    return None, None