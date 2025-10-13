from flask import Flask, request, jsonify
from data_persistance import task_db_update, function_to_open_jsonfile
from functions import state_check

app = Flask(__name__)
tasks = function_to_open_jsonfile()


@app.route('/')
def home():
    return 'Task Manager'

@app.route('/tasks/add_task', methods=['POST'])
def add_task():
    try:
        if 'title' not in request.json:
            raise ValueError('title missing from the body')
        if 'description' not in request.json:
            raise ValueError('description missing from the body')
        if 'state' not in request.json:
            raise ValueError('state missing from the body')
        state_check(request)
        data = request.get_json()
        data['id'] = len(tasks) + 1
        tasks.append({
            'id' : data['id'],
            'title' : data['title'],
            'description' : data['description'],
            'state' : data['state']
        })
        task_db_update(tasks)
        return data
    except ValueError as e:
        return jsonify(message=str(e)), 400

@app.route('/tasks', methods=['GET'])
def tasks_view():
    filtered_tasks = tasks
    task_filter = request.args.get('state')
    if task_filter:
        filtered_tasks = list(
            filter(lambda task: task['state'] == task_filter, filtered_tasks)
        )
        return filtered_tasks
    if request.method == 'GET':
        return tasks
    

@app.route('/tasks/<task_id>', methods=['GET', 'PUT', 'DELETE'])
def single_task_view(task_id):
    int_task_id = int(task_id)
    if request.method == 'GET':
        return tasks[int_task_id] 

    if request.method == 'PUT':
        new_task = request.get_json()
        old_task = tasks[int_task_id]
        old_task.update(new_task)
        return old_task 

    if request.method == 'DELETE':
        del tasks[int_task_id]
        return 'Ok!'



if __name__ == "__main__":
    app.run(host="localhost", debug=True)