from sqlalchemy import create_engine
from repository import UserRepository, AddressRepository, CarRepository
from db_creation import users_table, address_table, car_table, metadata_obj

# Connecting with DB 
DB_URI = 'postgresql://postgres:pass123@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

# Code to try connection with  and validate or create tables. 
try:
    connection = engine.connect()
    print('Connection Succesful')

    metadata_obj.create_all(engine)

    connection.close()
except Exception as e:
    print('Connection failed:', e)

# Testing for user repository class for create, get all users, modify users.
with engine.connect() as conn:
    user_repo = UserRepository(conn, users_table)

    new_user = user_repo.create(full_name="Alba V", email_address="Alba@email.com")
    print(f'New user ID: {new_user}')

    all_users = user_repo.get_users()
    for user in all_users:
        print(f'ID: {user.user_id}, User name: {user.full_name}')

    rows_update = user_repo.modify(new_user, full_name="Alba Vargas")
    print(f'Rows updated: {rows_update}')

# Testing for address repository class for create, get all addresses, modify addresses.
with engine.connect() as conn:
    address_repo = AddressRepository(conn, address_table)

    new_address = address_repo.create(country="Costa Rica", province="Alajuela", city="Grecia", user_id=11)
    print(f'New address ID: {new_address}')

    all_address = address_repo.get_address()
    for address in all_address:
        print(f"ID: {address.address_id}, User Id: {address.user_id}")

    rows_updated = address_repo.modify(new_address, city="Grecia City")
    print(f"Rows updated: {rows_updated}")

# Testing for car repository class for create, get all cars, modify cars.
with engine.connect() as conn:
    car_repo = CarRepository(conn, car_table)

    new_car = car_repo.create(model="GLC", brand="Mercedez", factory_year=2025)
    print(f'New Car ID: {new_car}')

    all_cars = car_repo.get_cars()
    for car in all_cars:
        print(f"ID: {car.car_id}, User Id: {car.user_id}")

    rows_updated = car_repo.modify(new_car, user_id=11)
    print(f"Rows updated: {rows_updated}")