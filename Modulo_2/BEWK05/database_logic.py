import psycopg2

# Class to generate PG Manager with this class we manage the connection, the queries to be executed and we inherit the data to be used to generate the table and insert the data 
#Remove inheritance since it doesn't share the same capabilities 
class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
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
            "user_id": user_record[0],
            "username": user_record[1],
            "password": user_record[2],
            "email": user_record[3],
            "full_name": user_record[4],
            "date_of_birth": user_record[5],
            "account_status": user_record[6]
        }
    
    def execute_query(self, query, args=None):
        if args:
            self.cursor.execute(query, args)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        print('Query executed')
        if self.cursor.description:
            results = self.cursor.fetchall()
            return results
        
    def execute_many_queries(self, query, data):
        self.cursor.executemany(query, data)
        self.connection.commit()
        print('Queries executed')
        if self.cursor.description:
            results = self.cursor.fetchall()
            return results
        

