from flask.views import MethodView
from flask import Flask, request
from db_creation_file import DataAndQueries
from database_logic import PgManager

data_and_queries = DataAndQueries()
pgmanager = PgManager('postgres', 'postgres', 'pass123', 'localhost')

class ListUsers(MethodView):
    def get(self):
        try:
            user_name = request.args.get('user_name')
            results = pgmanager.execute_query(data_and_queries.user_query)
            formatted_results = [pgmanager.format_user(result) for result in results]
            if user_name:
                filtered_user = list(filter(lambda user: user['user_name'] == user_name, formatted_results ))
                return filtered_user
            else:
                return formatted_results
        
        except Exception as error:
            print('Error getting all users from database: ', error)
            return {"error": "Cannot retrieve users from database"}, 500 
    

class ListCars(MethodView):
    def get(self):
        try:
            car_model = request.args.get('model')
            results = pgmanager.execute_query(data_and_queries.car_query)
            formatted_results = [pgmanager.format_car(result) for result in results]
            if car_model:
                filtered_car = list(filter(lambda car: car['model'] == car_model, formatted_results))
                return filtered_car
            else: 
                return formatted_results
        
        except Exception as error:
            print('Error getting all cars from database: ', error)
            return {"error": "Cannot retrieve cars from database"}, 500
        
class ListRents(MethodView):
    def get(self):
        try:
            rent_status = request.args.get('rent_status')
            results = pgmanager.execute_query(data_and_queries.rent_query)
            formatted_results = [pgmanager.format_rents(result) for result in results]
            if rent_status:
                filtered_rents = list(filter(lambda rent: rent['rent_status'] == rent_status, formatted_results))
                return filtered_rents
            else: 
                return formatted_results
        
        except Exception as error:
            print('Error getting all rents from database: ', error)
            return {"error": "Cannot retrieve rents from database"}, 500


class CreateCarRentalAPI(MethodView):
    def post(self):
        pass

class MopdifyCarRentalAPI(MethodView):
    def put(self):
        pass

    def patch(self):
        pass




