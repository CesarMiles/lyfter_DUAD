from flask.views import MethodView
from flask import Flask, request, jsonify, make_response 
from utils import state_check, task_req_check, find_task_by_id, refresh_tasks, token_authentication
from data_persistance import read_credentials_from_file

app = Flask(__name__)

class TaskAPI(MethodView):
    @token_authentication
    @refresh_tasks
    def get(self,tasks):
        filtered_tasks = tasks
        task_filter = request.args.get('state')
        if task_filter:
            filtered_tasks = list(
                filter(lambda task: task['state'] == task_filter, filtered_tasks)
            )
            return jsonify(filtered_tasks)
        return jsonify(tasks)
    
    @token_authentication
    @refresh_tasks
    def post(self, tasks):
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

class TaskDetailAPI(MethodView):
    @token_authentication
    @refresh_tasks
    def put(self, tasks, task_id):
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

    @token_authentication    
    @refresh_tasks
    def delete(self, tasks, task_id):
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

class Login(MethodView):
    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return jsonify({"error": "Username or Password incorrect"}), 400
        
        credentials = read_credentials_from_file()

        if auth.username in credentials:
            user_data = credentials[auth.username]
            if auth.password == user_data["password"]:
                    token = 123
                    return jsonify({
                        "message": "Login Succesful",
                        "token" : token
                    }), 200
                    
        return jsonify({"error": "Username or Password incorrect"}), 401

tasks_view = TaskAPI.as_view('tasks_api')
app.add_url_rule('/tasks', view_func=tasks_view, methods=['GET', 'POST'])

task_detail_view = TaskDetailAPI.as_view('task_detail_api')
app.add_url_rule('/tasks/<int:task_id>', view_func=task_detail_view, methods=['PUT', 'DELETE'])

login_view = Login.as_view('login_api')
app.add_url_rule('/login', view_func=login_view, methods=['POST'])

if __name__ == "__main__":
    app.run(host="localhost", debug=True)