from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, SmallInteger, insert, update, delete, select

DB_URI = 'postgresql://postgres:pass123@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)
# pgmanager = PgManager('postgres', 'postgres', 'pass123', 'localhost')
# def __init__(self, db_name, user, password, host, port=5432):

metadata_obj = MetaData(schema="deliverable_wk06")


users_table = Table(
    "users",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("full_name", String(30), nullable=False),
    Column("email_address", String(40), nullable=False),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("address_id", Integer, primary_key=True),
    Column("country", String(20), nullable=False),
    Column("province", String(20), nullable=False),
    Column("city", String(20), nullable=False),
    Column("user_id", ForeignKey("deliverable_wk06.users.user_id"), nullable=False),
)

car_table = Table(
    "car",
    metadata_obj,
    Column("car_id", Integer, primary_key=True),
    Column("model", String(30), nullable=False),
    Column("brand", String(30), nullable=False),
    Column("factory_year", SmallInteger, nullable=False),
    Column("user_id", ForeignKey("deliverable_wk06.users.user_id"), nullable=True),
)

try:
    connection = engine.connect()
    print('Connection Succesful')

    metadata_obj.create_all(engine)

    connection.close()
except Exception as e:
    print('Connection failed:', e)

class UserRepository:
    def __init__(self, connection):
        self.conn = connection
    
    def create(self, **kwargs):
        stmt = insert(users_table).values(**kwargs).returning(users_table.c.user_id, users_table.c.full_name)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    def modify(self, modify_user_id, **kwargs):
        if not kwargs:
            print(f'There are no values to modify.')
            return None
        
        stmt = update(users_table).where(users_table.c.user_id == modify_user_id).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
    
    def delete(self, user_id_to_delete):
        stmt = delete(users_table).where(users_table.c.user_id == user_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'User {user_id_to_delete} has been deleted')
        return 
    
    def get_users(self):
        stmt = select(users_table)
        result = self.conn.execute(stmt)
        return result.all()
    
class AddressRepository:
    def __init__(self, connection):
        self.conn = connection

    def create(self, **kwargs):
        stmt = insert(address_table).values(**kwargs).returning(address_table.c.address_id, address_table.c.user_id)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    def modify(self, modify_address_id, **kwargs):
        if not kwargs:
            print('There are no values to modify')
            return None
        stmt = update(address_table).where(address_table.c.address_id == modify_address_id).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
    
    def delete(self, address_id_to_delete):
        stmt = delete(address_table).where(address_table.c.address_id == address_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'Address {address_id_to_delete} has been deleted')
        return
    
    def get_address(self):
        stmt = select(address_table)
        result = self.conn.execute(stmt)
        return result.all()

class CarRepository:
    def __init__(self, connection):
        self.conn = connection


    def create(self, **kwargs):
        stmt = insert(car_table).values(**kwargs).returning(car_table.c.car_id, car_table.c.brand)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    def modify(self, modify_car_id, **kwargs):
        if not kwargs:
            print('There are no values to modify')
            return None
        
        stmt = update(car_table).where(car_table.c.car_id == modify_car_id).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
        
    def delete(self, car_id_to_delete):
        stmt = delete(car_table).where(car_table.c.car_id == car_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'Car {car_id_to_delete} has been deleted')
        return

    def get_cars(self):
        stmt = select(car_table)
        result = self.conn.execute(stmt)
        return result.all()


# with engine.connect() as conn:
#     address_repo = AddressRepository(conn)

#     new_address = address_repo.create(country="Costa Rica", province="Alajuela", city="Grecia", user_id=9)
#     print(f'New address ID: {new_address}')

#     all_address = address_repo.get_address()
#     for address in all_address:
#         print(f"ID: {address.address_id}, User Id: {address.user_id}")

#     rows_updated = address_repo.modify(new_address, city="Grecia City")
#     print(f"Filas actualizadas: {rows_updated}")


with engine.connect() as conn:
    car_repo = CarRepository(conn)

    new_car = car_repo.create(model="Seagul", brand="BYD", factory_year=2020)
    print(f'New Car ID: {new_car}')

    all_cars = car_repo.get_cars()
    for car in all_cars:
        print(f"ID: {car.car_id}, User Id: {car.user_id}")

    rows_updated = car_repo.modify(new_car, user_id=9)
    print(f"Filas actualizadas: {rows_updated}")