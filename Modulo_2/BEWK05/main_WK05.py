from database_logic import PgManager


# Instancing the oboject to generate the connection
pg_manager = PgManager('postgres', 'postgres', 'pass123', 'localhost')

# 
pg_manager.execute_query(pg_manager.dbcreation)
print('Table created')

pg_manager.execute_many_queries(pg_manager.insert_query, pg_manager.users_data)
print('data inserted')