from api import ListUsers, ListCars, ListRents
from flask import Flask


app = Flask(__name__)

list_users = ListUsers.as_view('user_list_api')
app.add_url_rule('/users', view_func=list_users, methods=['GET'])
list_cars = ListCars.as_view('cars_list_api')
app.add_url_rule('/cars', view_func=list_cars, methods=['GET'])
list_rents = ListRents.as_view('rents_list_api')
app.add_url_rule('/rents', view_func=list_rents, methods=['GET'])


app.run(host='localhost', debug=True)