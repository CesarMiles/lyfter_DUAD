from flask import Flask, request, jsonify
from utils import state_check, task_req_check, find_task_by_id, refresh_tasks

app = Flask(__name__)


@app.route('/')
def home():
    return 'Task Manager'

@app.route('/tasks', methods=['POST'])
@refresh_tasks
def add_task(tasks):
    try:
        task_req_check(request)
        state_check(request)
        data = request.get_json()
        new_id = max([task['id'] for task in tasks], default=0) + 1
        tasks.append({
            'id' : new_id,
            'title' : data['title'],
            'description' : data['description'],
            'state' : data['state']
        })
        return jsonify({"message": f"Task {new_id}. {data['title']}, has been added"}), 201
    except ValueError as e:
        return jsonify(message=str(e)), 400

@app.route('/tasks', methods=['GET'])
@refresh_tasks
def tasks_view(tasks):
    filtered_tasks = tasks
    task_filter = request.args.get('state')
    if task_filter:
        filtered_tasks = list(
            filter(lambda task: task['state'] == task_filter, filtered_tasks)
        )
        return jsonify(filtered_tasks)
    if request.method == 'GET':
        return jsonify(tasks)
    

@app.route('/tasks/<task_id>', methods=['PUT'])
@refresh_tasks
def single_task_edit(tasks, task_id):
    try:
        task_id_int = int(task_id)
        task_index, task_to_modify = find_task_by_id(task_id_int, tasks)

        if task_index is None:
            return jsonify({"error": f'Task with id {task_id} not found'}), 404

        if request.method == 'PUT':
            task_req_check(request)
            state_check(request)
            new_task = request.get_json()
            task_to_modify.update({
                'title': new_task['title'],
                'description': new_task['description'],
                'state': new_task['state']
            })
            return task_to_modify
    
    except ValueError:
        return jsonify({"error": "Task ID must be a number"}), 400

@app.route('/tasks/<task_id>', methods=['DELETE'])
@refresh_tasks
def single_task_delete(tasks, task_id):
    try:
        task_id_int = int(task_id)
        task_index, task_to_modify = find_task_by_id(task_id_int, tasks)

        if task_index is None:
            return jsonify({"error": f'Task with id {task_id} not found'}), 404

        if request.method == 'DELETE':
            del tasks[task_index]
            return jsonify({"message": f"Task {task_id} has been deleted"}), 204
    
    except ValueError:
        return jsonify({"error": "Task ID must be a number"}), 400


if __name__ == "__main__":
    app.run(host="localhost", debug=True)