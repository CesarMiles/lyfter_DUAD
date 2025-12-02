from sqlalchemy import insert, update, delete, select

class CarRepository:
    def __init__(self, connection, table):
        self.conn = connection
        self.table = table


    def create(self, **kwargs):
        stmt = insert(self.table).values(**kwargs).returning(self.table.c.car_id, self.table.c.brand)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    def modify(self, modify_car_id, **kwargs):
        if not kwargs:
            print('There are no values to modify')
            return None
        
        stmt = update(self.table).where(self.table.c.car_id == modify_car_id).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
    
    def assign_car_to_user(self, car_to_be_assigned, user):
        stmt = update(self.table).where(self.table.c.car_id == car_to_be_assigned).values(user_id=user)
        
    def delete(self, car_id_to_delete):
        stmt = delete(self.table).where(self.table.c.car_id == car_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'Car {car_id_to_delete} has been deleted')
        return

    def get_cars(self):
        stmt = select(self.table)
        result = self.conn.execute(stmt)
        return result.all()