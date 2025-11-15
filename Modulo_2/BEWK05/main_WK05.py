from database_logic import PgManager
from db_creation_file import DataAndQueries
from api import ListUsers
from flask import Flask

# Part 1 - Creating DB on a single script generating mock data. 

# Instancing the oboject to generate the connection
pg_manager = PgManager('postgres', 'postgres', 'pass123', 'localhost')

# Instancing the object to generate data and use it combined with PgManager
data_and_queries = DataAndQueries()

# Execution of query, this query logic its located on db_creation_file.py this is to create only the data base for the users
# pg_manager.execute_query(data_and_queries.user_dbcreation)

# Execution of query, this query is to add mock data to user table
# pg_manager.execute_many_queries(data_and_queries.user_insert_query, data_and_queries.users_data)

# Execution of query, this query logic its located on db_creation_file.py this is to create only the data base for the cars
# pg_manager.execute_query(data_and_queries.car_dbcreation)

# Execution of query, this query is to add mock data to user table
# pg_manager.execute_many_queries(data_and_queries.car_insert_query, data_and_queries.car_data)

# Execution of query this query is to add the cross table to be used to track rentals.
# pg_manager.execute_query(data_and_queries.rental_relation_dbcreation)



# Part 2 - Testing data base 
# Query to add new user to user's table
# pg_manager.execute_query(data_and_queries.user_insert_query, data_and_queries.new_user)

# Query to add new car to car's table
# pg_manager.execute_query(data_and_queries.car_insert_query, data_and_queries.new_car)

# Query to modify user 
# pg_manager.execute_query(data_and_queries.modify_user)

# Query to modify car
# pg_manager.execute_query(data_and_queries.modify_car, ('unavail', 51))

# Query to add new rental
# pg_manager.execute_query(data_and_queries.rental_insert_query, data_and_queries.new_rental)

# Query to modify rental 
# pg_manager.execute_query(data_and_queries.modify_rental, (1,))

# Query to select all cars rented
# print(pg_manager.execute_query(data_and_queries.user_query,))



app = Flask(__name__)

list_users = ListUsers.as_view('list_api')
app.add_url_rule('/users', view_func=list_users, methods=['GET'])


app.run(host='localhost', debug=True)