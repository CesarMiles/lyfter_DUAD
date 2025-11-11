import psycopg2
from db_creation_file import DBGenerator

# Class to generate PG Manager with this class we manage the connection, the queries to be executed and we inherit the data to be used to generate the table and insert the data 
class PgManager(DBGenerator):
    def __init__(self, db_name, user, password, host, port=5432):
        super().__init__()
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection()
        if self.connection:
            print('Connected to database!')
            self.cursor = self.connection.cursor()

    # Method to generate the connection, this uses the data that its provided at the time of instancing the object 
    def create_connection(self):
        try:
            connection = psycopg2.connect(
                dbname = self.db_name,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,
            )
            return connection
        except Exception as error:
            print('Error connecting to the data base', error)
            return None
        
    # This method its to clode the connection to the data base to prevent 
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")

    def format_user(self, user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "password": user_record[3],
        }
    
    def execute_query(self, query, *args):
        self.cursor.execute(query, args)
        self.connection.commit()
        if self.cursor.description:
            results = self.cursor.fetchall()
            return results
        
    def execute_many_queries(self, query, data):
        self.cursor.executemany(query, data)
        self.connection.commit()
        if self.cursor.description:
            results = self.cursor.fetchall()
            return results

