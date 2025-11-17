from flask.views import MethodView
from flask import Flask, request
from db_creation_file import DataAndQueries
from database_logic import PgManager
from utils import user_creation_req_check, car_creation_req_check, rent_creation_req_check

data_and_queries = DataAndQueries()
pgmanager = PgManager('postgres', 'postgres', 'pass123', 'localhost')

class ListUsers(MethodView):
    def get(self):
        try:
            filters = {
                'user_id' : request.args.get('user_id'),
                'username' : request.args.get('username'),
                'password' : request.args.get('password'),
                'email' : request.args.get('email'),
                'full_name' : request.args.get('full_name'),
                'date_of_birth' : request.args.get('date_of_birth'),
                'account_status' : request.args.get('account_status')
            }

            results = pgmanager.execute_query(data_and_queries.user_query)
            formatted_results = [pgmanager.format_user(result) for result in results]

            has_active_filters = any(filters.values())

            if has_active_filters:
                filtered_users = formatted_results
                for key, value in filters.items():
                    if value:
                        if key == 'user_id':
                            value = int(value)
                        filtered_users = list(filter(lambda user: user[key] == value, filtered_users))
                return filtered_users
            
            else:
                return formatted_results
        
        except Exception as error:
            print('Error getting all users from database: ', error)
            return {"error": "Cannot retrieve users from database"}, 500 
    

class ListCars(MethodView):
    def get(self):
        try:
            filters = { # Filters to be used if the query adds them to adjust the GET results
                'car_id' : request.args.get('car_id'),
                'brand' : request.args.get('brand'),
                'model' : request.args.get('model'),
                'factory_year' : request.args.get('factory_year'),
                'car_rental_status' : request.args.get('car_rental_status')
            }

            results = pgmanager.execute_query(data_and_queries.car_query) # Storing results to add them to the format method to transfor tuple to dictionary
            formatted_results = [pgmanager.format_car(result) for result in results] # With format method located on database_logic.py transfor tuple to dictionary for readability

            has_active_filters = any(filters.values()) # Value to store TRUE if there are any query parameters from the URL 
            if has_active_filters: # Conditional to confirm if queries are stored on filters to start adjusting reults
                filtered_cars = formatted_results
                for key, value in filters.items(): #Transforming dictionary list to tuple list to iterate 
                    if value:
                        if key == 'factory_year': 
                            value = int(value)
                        if key == 'car_id':
                            value = int(value)
                        filtered_cars = list(filter(lambda car: str(car[key]).lower() == str(value).lower(), filtered_cars))# using filter to retrieve only TRUE matchs from lambda function
                return filtered_cars
            
            else:
                return formatted_results

        except Exception as error:
            print('Error getting all cars from database: ', error)
            return {"error": "Cannot retrieve cars from database"}, 500
        
class ListRents(MethodView):
    def get(self):
        try:
            filters = {
                'rental_id' : request.args.get('rental_id'),
                'car_id' : request.args.get('car_id'),
                'user_id' : request.args.get('user_id'),
                'rent_request_date' : request.args.get('rent_request_date'),
                'rent_start' : request.args.get('rent_start'),
                'rent_end' : request.args.get('rent_end'),
                'payment_status' : request.args.get('payment_status'),
                'rent_status' : request.args.get('rent_status'),
            }

            results = pgmanager.execute_query(data_and_queries.rent_query)
            formatted_results = [pgmanager.format_rents(result) for result in results]

            has_active_filters = any(filters.values())

            if has_active_filters:
                filtered_rents = formatted_results
                for key, value  in filters.items():
                    if value:
                        if key == 'rent_id':
                            value = int(value)
                        if key == 'car_id':
                            value = int(value)
                        if key == 'user_id':
                            value = int(value)
                        filtered_rents = list(filter(lambda rent: rent[key] == value, filtered_rents))
                return filtered_rents
            
            else: 
                return formatted_results
        
        except Exception as error:
            print('Error getting all rents from database: ', error)
            return {"error": "Cannot retrieve rents from database"}, 500


class CreateUserAPI(MethodView):
    def post(self):
        try:
            user_creation_req_check(request)
            user_data = request.get_json()
            pgmanager.execute_query(data_and_queries.user_insert_query, (user_data['username'], user_data['password'], user_data['email'], user_data['full_name'], user_data['date_of_birth'], user_data['account_status']))
            return {"message": "User entered in database"}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete query error: {e}'}, 400
        
class CreateCarAPI(MethodView):
    def post(self):
        try:
            car_creation_req_check(request)
            car_data = request.get_json()
            pgmanager.execute_query(data_and_queries.car_insert_query,(car_data['car_id'], car_data['brand'], car_data['model'], car_data['factory_year'],car_data['car_rental_status']))
            return {"message": "Car entered in database"}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete query error: {e}'}, 400

class CreateRentAPI(MethodView):
    def post(self):
        try:
            rent_creation_req_check(request)
            rent_data = request.get_json()
            pgmanager.execute_query(data_and_queries.rental_insert_query, (rent_data['car_id'], rent_data['user_id'], rent_data['rent_start'], rent_data['rent_end'], rent_data['payment_status'], rent_data['rent_status']))
            return {"message": "Rent entered in database"}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete query error: {e}'}, 400

class MopdifyCarRentalAPI(MethodView):
    def put(self):
        pass

    def patch(self):
        pass




