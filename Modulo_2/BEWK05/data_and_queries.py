
class DataAndQueries:
    def __init__(self):

        self.user_insert_query = """
        INSERT INTO lyfter_car_rental.customer_car_rental_data 
        (username, password, email, full_name, date_of_birth, account_status) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        self.car_insert_query = """
        INSERT INTO lyfter_car_rental.car_data 
        (brand, model, factory_year, car_rental_status)
        VALUES (%s, %s, %s, %s)
        """

        self.rental_insert_query = """
        INSERT INTO lyfter_car_rental.rental_information 
        (car_id, user_id, rent_start, rent_end, payment_status, rent_status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        self.modify_user = """
        UPDATE lyfter_car_rental.customer_car_rental_data
        SET account_status = %s
        WHERE user_id = %s
        """

        self.modify_car = """
        UPDATE lyfter_car_rental.car_data
        SET car_rental_status = %s
        WHERE car_id = %s
        """

        self.modify_rent = """
        UPDATE lyfter_car_rental.rental_information
        SET rent_status = %s
        WHERE rental_id = %s
        """

        self.complete_rental = """
        UPDATE lyfter_car_rental.rental_information 
        SET rent_status = 'completed' 
        WHERE rental_id = %s
        """


        self.car_query = """
        SELECT * FROM lyfter_car_rental.car_data 
        """

        self.user_query = """
        SELECT * FROM lyfter_car_rental.customer_car_rental_data 
        """

        self.rent_query = """
        SELECT * FROM lyfter_car_rental.rental_information
        """



