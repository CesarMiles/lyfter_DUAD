from flask.views import MethodView
from flask import Flask, request
from db_creation_file import DataAndQueries
from database_logic import PgManager

data_and_queries = DataAndQueries()
pgmanager = PgManager('postgres', 'postgres', 'pass123', 'localhost')

class ListUsers(MethodView):
    def users_get(self):
        try:
            results = pgmanager.execute_query(data_and_queries.user_query)
            formatted_results = [pgmanager.format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print('Error getting all users from database: ', error)
            return False
    




class CreateCarRentalAPI(MethodView):
    def post(self):
        pass

class MopdifyCarRentalAPI(MethodView):
    def put(self):
        pass

    def patch(self):
        pass




