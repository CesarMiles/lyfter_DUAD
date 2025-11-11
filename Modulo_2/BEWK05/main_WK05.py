from database_logic import PgManager


# Instancing the oboject to generate the connection
pg_manager = PgManager('postgres', 'postgres', 'pass123', 'localhost')

# # Execution of query, this query logic its located on db_creation_file.py this is to create only the data base 
# pg_manager.execute_query(pg_manager.user_dbcreation)

# # Execution 
# pg_manager.execute_many_queries(pg_manager.user_insert_query, pg_manager.users_data)

# pg_manager.execute_query(pg_manager.car_dbcreation)

# pg_manager.execute_many_queries(pg_manager.car_insert_query, pg_manager.car_data)


pg_manager.execute_query(pg_manager.rental_relation_dbcreation)
