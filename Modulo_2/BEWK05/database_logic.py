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
        
    # This method its to close the connection to the data base to prevent leaving it open after the usage 
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")

    # Function to format the data retrieved from the GET methods specfically for users 
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
    
    # Function to format the data retrieved from the GET methods specfically for cars 
    def format_car(self, car_record):
        return {
            "car_id": car_record[0],
            "brand": car_record[1],
            "model": car_record[2],
            "factory_year": car_record[3],
            "car_rental_status": car_record[4]
        }
    
    # Function to format the data retrieved from the GET methods specfically for rents 
    def format_rents(self, rent_record):
        return {
            "rental_id": rent_record[0],
            "car_id": rent_record[1],
            "user_id": rent_record[2],
            "rent_request_date": rent_record[3],
            "rent_start": rent_record[4],
            "rent_end" : rent_record[5],
            "payment_status" : rent_record[6],
            "rent_status" : rent_record[7]
        }
    
    # Function to execute the query using an attribute of query and arguments 
    def execute_query(self, query, args=None):
        if args:
            self.cursor.execute(query, args) # Using cursor from psycopg to execute the query with arguments 
        else:
            self.cursor.execute(query) # Using cursor from psycopg to execute the query without arguments such as gets 
        self.connection.commit() # using commit method from psycopg to save any change on the db
        print('Query executed') # Printing to confirm query has been executed 
        if self.cursor.description: # Using desription method to confirm if there was a SELECT operation to then use fetchall
            results = self.cursor.fetchall()
            return results

