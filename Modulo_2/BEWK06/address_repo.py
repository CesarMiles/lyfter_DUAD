from sqlalchemy import insert, update, delete, select

class AddressRepository:
    def __init__(self, connection, table):
        self.conn = connection
        self.table = table

    def create(self, **kwargs):
        stmt = insert(self.table).values(**kwargs).returning(self.table.c.address_id, self.table.c.user_id)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    def modify(self, modify_address_id, **kwargs):
        if not kwargs:
            print('There are no values to modify')
            return None
        stmt = update(self.table).where(self.table.c.address_id == modify_address_id).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
    
    def delete(self, address_id_to_delete):
        stmt = delete(self.table).where(self.table.c.address_id == address_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'Address {address_id_to_delete} has been deleted')
        return
    
    def get_address(self):
        stmt = select(self.table)
        result = self.conn.execute(stmt)
        return result.all()