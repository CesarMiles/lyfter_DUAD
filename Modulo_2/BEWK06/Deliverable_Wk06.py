from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, SmallInteger, insert, update, delete

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
    def create(self, **kwargs):
        return insert(users_table).values(**kwargs).returning(users_table.c.user_id, users_table.c.full_name)
    
    def modify(self, modify_user_id, **kwargs):
        if kwargs:
            return update(users_table).where(users_table.c.user_id == modify_user_id).values(**kwargs)
        else:
            return print(f'There are no values to modify.')
    
    def delete(self, user_id_to_delete):
        return delete(users_table).where(users_table.c.user_id == user_id_to_delete)
    
    def get_users(self):
        return 
    
class AddressRepository:
    def create(self, **kwargs):
        return insert(address_table).values(**kwargs).returning(address_table.c.address_id, address_table.c.user_id)
    
    def modify(self, modify_address_id, **kwargs):
        if kwargs:
            return update(address_table).where(address_table.c.address_id == modify_address_id).values(**kwargs)
        else:
            return print('There are no values to modify')
    
    def delete(self, address_id_to_delete):
        return delete(address_table).where(address_table.c.address_id == address_id_to_delete)

class CarRepository:
    def create(self, **kwargs):
        return insert(car_table).values(**kwargs).returning(car_table.c.car_id, car_table.c.brand)
    
    def modify(self, modify_car_id, **kwargs):
        if kwargs:
            return update(car_table).where(car_table.c.car_id == modify_car_id).values(**kwargs)
        else:
            return print(f'There are no values to modify')
    
    def delete(self, car_id_to_delete):
        return delete(car_table).where(car_table.c.car_id == car_id_to_delete)

user = UserRepository()
car = CarRepository()

with engine.connect() as conn:
    conn.execute(car.delete(1))
    conn.commit()