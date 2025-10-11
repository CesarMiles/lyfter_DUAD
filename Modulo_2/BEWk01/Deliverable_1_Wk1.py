from flask import Flask, request
from data_persistance import task_db_update, function_to_open_jsonfile

app = Flask(__name__)
tasks = function_to_open_jsonfile()


@app.route('/')
def home():
    return 'Task Manager'

@app.route('/tasks/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    data['id'] = len(tasks)
    tasks.append(data)
    if data:
        task_db_update(tasks)
    return data

@app.route('/tasks', methods=['GET'])
def all_tasks_view():
    if request.method == 'GET':
        return tasks

@app.route('/tasks/<task_id>', methods=['GET', 'PUT', 'DELETE'])
def single_task_view(task_id):
    global tasks
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