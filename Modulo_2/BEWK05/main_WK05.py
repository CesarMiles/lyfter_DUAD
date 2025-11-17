from api import ListUsers, ListCars, ListRents, CreateUserAPI, CreateCarAPI, CreateRentAPI
from flask import Flask


app = Flask(__name__)

list_users = ListUsers.as_view('user_list_api')
app.add_url_rule('/users', view_func=list_users, methods=['GET'])
list_cars = ListCars.as_view('cars_list_api')
app.add_url_rule('/cars', view_func=list_cars, methods=['GET'])
list_rents = ListRents.as_view('rents_list_api')
app.add_url_rule('/rents', view_func=list_rents, methods=['GET'])

create_user = CreateUserAPI.as_view('user_creation_api')
app.add_url_rule('/create_user', view_func=create_user, methods=['POST'])
create_car = CreateCarAPI.as_view('car_creation_api')
app.add_url_rule('/create_car', view_func=create_car, methods=['POST'])
create_rent = CreateRentAPI.as_view('rent_creation_api')
app.add_url_rule('/create_rent', view_func=create_rent, methods=['POST'])


app.run(host='localhost', debug=True)