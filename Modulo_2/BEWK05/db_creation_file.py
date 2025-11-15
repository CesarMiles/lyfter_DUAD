
class DataAndQueries:
    def __init__(self):

        self.user_dbcreation = """create table lyfter_car_rental.customer_car_rental_data (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        password VARCHAR(50),
        email VARCHAR(50),
        full_name VARCHAR(50),
        date_of_birth DATE,
        account_status VARCHAR(9)
    );"""
    
        self.car_dbcreation = """create table lyfter_car_rental.car_data (
	car_id SERIAL PRIMARY KEY,
	brand VARCHAR(50),
	model VARCHAR(50),
	factory_year INT,
	car_rental_status VARCHAR(9)
    );"""
        
        self.rental_relation_dbcreation = """create table lyfter_car_rental.rental_information (
        rental_id SERIAL PRIMARY KEY,
        car_id INT NOT NULL references lyfter_car_rental.car_data(car_id),
        user_id INT NOT NULL references lyfter_car_rental.customer_car_rental_data(user_id),
        rent_request_date DATE not NULL default CURRENT_DATE,
        rent_start DATE,
        rent_end DATE,
        payment_status VARCHAR(10),
        rent_status VARCHAR(15)
        );"""

        self.user_insert_query = """
        INSERT INTO lyfter_car_rental.customer_car_rental_data 
        (username, password, email, full_name, date_of_birth, account_status) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        self.modify_user = """
        UPDATE lyfter_car_rental.customer_car_rental_data
        SET account_status = 'inactive'
        WHERE user_id = 52
        """

        self.car_insert_query = """
        INSERT INTO lyfter_car_rental.car_data 
        (car_id, brand, model, factory_year, car_rental_status)
        VALUES (%s, %s, %s, %s, %s)
        """

        self.modify_car = """
        UPDATE lyfter_car_rental.car_data
        SET car_rental_status = %s
        WHERE car_id = %s
        """

        self.rental_insert_query = """
        INSERT INTO lyfter_car_rental.rental_information 
        (car_id, user_id, rent_start, rent_end, payment_status, rent_status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        self.modify_rental = """
        UPDATE lyfter_car_rental.rental_information
        SET rent_status = 'completed'
        WHERE rental_id = %s
        """
        self.car_query = """
        SELECT * FROM lyfter_car_rental.car_data 
        WHERE car_rental_status = %s
        """

        self.user_query = """
                SELECT * FROM lyfter_car_rental.customer_car_rental_data 
        """

        self.new_user = ('john_user', 'jhon_pass', 'jhon@email.com', 'Jhon Doe', '1997-05-14', 'active')

        self.new_car = (51, 'byd', 'seagul', 2025, 'available')

        self.new_rental = (51, 51, '2025-11-14', '2025-11-30', 'completed', 'pending')



