from sqlalchemy import insert, update, delete, select
from db_manager import products_table

class ProductRepository:
    def __init__(self, connection):
        self.conn = connection
        self.table = products_table

    def create(self, **kwargs):
        stmt = insert(self.table).values(**kwargs).returning(self.table.c.product_id, self.table.c.product_name)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    def modify(self, modify_product_id, **kwargs):
        if not kwargs:
            print(f'There are no values to modify')
            return None
        
        stmt = update(self.table).where(self.table.c.product_id == modify_product_id).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
    
    def delete(self, product_id_to_delete):
        stmt = delete(self.table).where(self.table.c.product_id == product_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'User {product_id_to_delete} has been deleted')
        return 