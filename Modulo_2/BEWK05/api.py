from flask.views import MethodView
from flask import request
from data_and_queries import DataAndQueries
from database_logic import PgManager
from utils import user_creation_req_check, car_creation_req_check, rent_creation_req_check, user_modification_check, car_modification_check, car_return_check, rent_modification_check, past_due_flag_check

data_and_queries = DataAndQueries() # Instance to retrieve attributes to be used for queries. 
pgmanager = PgManager('postgres', 'postgres', 'pass123', 'localhost') # Intance to generate a connection to the DB

# First end point to retrieve users, this include a filter method in case search is required with each value of the columns on the DB
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
            } # If user enter filters they will be stored on this variable

            results = pgmanager.execute_query(data_and_queries.user_query) # Storin the results in general to be later filtered if necessary. 
            formatted_results = [pgmanager.format_user(result) for result in results] # Formatting results to be more readable and easily filtered as a dictionary

            has_active_filters = any(filters.values()) # Value to store TRUE if there are any query parameters from the URL 

            if has_active_filters: # Conditional to confirm if queries are stored on filters to start adjusting reults
                filtered_users = formatted_results
                for key, value in filters.items(): #Transforming dictionary list to tuple list to iterate 
                    if value:
                        if key == 'user_id':
                            value = int(value)
                        filtered_users = list(filter(lambda user: user[key] == value, filtered_users)) # using filter to retrieve only TRUE matchs from lambda function
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

# End point to generate users on DB 
class CreateUserAPI(MethodView):
    def post(self):
        try:
            user_creation_req_check(request) # This is a function which is located on utils.py to confirm that all reqs to create the user are in the body. 
            user_data = request.get_json() # With request.get_json() we transform the body of the request to json to be used to execute the query.
            # With pgmanager.execute_query which is described on database_logic.py we execute the query which is stored on data_and_queries.py 
            pgmanager.execute_query(data_and_queries.user_insert_query, (user_data['username'], user_data['password'], user_data['email'], user_data['full_name'], user_data['date_of_birth'], user_data['account_status']))
            return {"message": "User entered in database"}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete query error: {e}'}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# End point to generate car on DB, it uses the same logic as the user. 
class CreateCarAPI(MethodView):
    def post(self):
        try:
            car_creation_req_check(request)
            car_data = request.get_json()
            pgmanager.execute_query(data_and_queries.car_insert_query,(car_data['brand'], car_data['model'], car_data['factory_year'],car_data['car_rental_status']))
            return {"message": "Car entered in database"}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete query error: {e}'}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# End point to generate rent on DB, it uses the same logic as the user. 
class CreateRentAPI(MethodView):
    def post(self):
        try:
            rent_creation_req_check(request)
            rent_data = request.get_json()
            pgmanager.execute_query(data_and_queries.rental_insert_query, (rent_data['car_id'], rent_data['user_id'], rent_data['rent_start'], rent_data['rent_end'], rent_data['payment_status'], rent_data['rent_status']))
            pgmanager.execute_query(data_and_queries.modify_car, ('rented', rent_data['car_id'],)) # Query to modify car on car table to show as rented.
            return {"message": "Rent entered in database"}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete query error: {e}'}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# End point to modify a user on DB
class MopdifyUserAPI(MethodView):
    def patch(self):
        try:
            user_modification_check(request) # this function its defined on utils.py and it is to confirm values to be modify the user. 
            modification_data = request.get_json() # Here we store the data from the body 
            pgmanager.execute_query(data_and_queries.modify_user, (modification_data['account_status'], modification_data['user_id'])) # This is the method to execute the query only using the values that we require
            return {"message": "User has been modified"}, 200
        except ValueError as e:  
            return {"error" : f'Cannot complete modification: {e}'}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500
        
# End point to modify car on DB, this uses the same logic as the user 
class MopdifyCarAPI(MethodView):
    def patch(self):
        try:
            car_modification_check(request)
            modification_data = request.get_json()
            pgmanager.execute_query(data_and_queries.modify_car, (modification_data['car_rental_status'], modification_data['car_id']))
            return {"message": "Car has been modified"}, 200
        except ValueError as e:  
            return {"error" : f'Cannot complete modification: {e}'}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# End point to completea rental, this endpoint combines two queries to update two tables 
class CompletingRentalAPI(MethodView):
    def patch(self):
        try:
            car_return_check(request) # This function located on utils.py confirm the information required to complete the rent 
            car_return_info = request.get_json() # Here it is stored the information to complete the update 
            pgmanager.execute_query(data_and_queries.complete_rental, (car_return_info['rental_id'],)) # Query to update to complete the rental on the rental info table
            pgmanager.execute_query(data_and_queries.modify_car, ('available', car_return_info['car_id'],)) # Query to update the car on the car table 
            return {"message" : f'Rental has been completed, car id {car_return_info['car_id']} has been set to available'}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete rental: {e}'}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# End point to modify rent on DB, this uses the same logic as the user 
class ModifyRentAPI(MethodView):
    def patch(self):
        try:
            rent_modification_check(request)
            modification_data = request.get_json()
            pgmanager.execute_query(data_and_queries.modify_rent, (modification_data['rent_status'], modification_data['rental_id']))
            return {"message" : f'Rent id {modification_data['rental_id']} has been modified'}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete rental modification: {e}'}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500

# End point to flag user on their status for past due 
class UserPastDueFlag(MethodView):
    def patch(self):
        try:
            past_due_flag_check(request)
            user_id = request.get_json()
            pgmanager.execute_query(data_and_queries.modify_user, ('past due', user_id['user_id']))
            return {"message" : f'User id {user_id['user_id']} has been flagged as past due'}, 200
        except ValueError as e:
            return {"error" : f'Cannot complete user modification: {e}'}, 400
        except Exception as e:
            return {"error": f'Database error: {e}'}, 500   

def get_methods(app):
    list_users = ListUsers.as_view('user_list_api')
    app.add_url_rule('/users', view_func=list_users, methods=['GET'])
    list_cars = ListCars.as_view('cars_list_api')
    app.add_url_rule('/cars', view_func=list_cars, methods=['GET'])
    list_rents = ListRents.as_view('rents_list_api')
    app.add_url_rule('/rents', view_func=list_rents, methods=['GET'])

def post_methods(app):
    create_user = CreateUserAPI.as_view('user_creation_api')
    app.add_url_rule('/create_user', view_func=create_user, methods=['POST'])
    create_car = CreateCarAPI.as_view('car_creation_api')
    app.add_url_rule('/create_car', view_func=create_car, methods=['POST'])
    create_rent = CreateRentAPI.as_view('rent_creation_api')
    app.add_url_rule('/create_rent', view_func=create_rent, methods=['POST'])

def patch_methods(app):
    modify_user = MopdifyUserAPI.as_view('modify_user_api')
    app.add_url_rule('/modify_user', view_func=modify_user, methods=['PATCH'])
    modify_car = MopdifyCarAPI.as_view('modify_car_API')
    app.add_url_rule('/modify_car', view_func=modify_car, methods=['PATCH'])
    rental_completion = CompletingRentalAPI.as_view('completing_rental_api')
    app.add_url_rule('/complete_rental', view_func=rental_completion, methods=['PATCH'])
    rental_modification = ModifyRentAPI.as_view('modify_rental_api')
    app.add_url_rule('/modify_rental', view_func=rental_modification, methods=['PATCH'])
    user_past_due_flag = UserPastDueFlag.as_view('past_due_flag_api')
    app.add_url_rule('/past_due_flag', view_func=user_past_due_flag, methods=['PATCH'])
