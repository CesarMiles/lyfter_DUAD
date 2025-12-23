from sqlalchemy import insert, update, delete, select
from models import products_table

# Create, list, modify, delete methods to be used on end points 
class ProductRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.table = products_table

    def create(self, **kwargs):
        with self.db_manager.engine.connect() as conn:
            stmt = insert(self.table).values(**kwargs).returning(self.table.c.product_id, self.table.c.product_name)
            result = conn.execute(stmt)
            conn.commit()
            return result.first()
        
    def get_products(self):
        with self.db_manager.engine.connect() as conn:
            stmt = select(self.table)
            result = conn.execute(stmt)
            return result.all()
        
    def get_product_by_id(self, product_id):
        with self.db_manager.engine.connect() as conn:
            stmt = select(self.table).where(self.table.c.product_id == product_id)
            result = conn.execute(stmt)
            row = result.mappings().first()
        return dict(row) if row else None
        
    
    def modify(self, modify_product_id, **kwargs):
        if not kwargs:
            print(f'There are no values to modify')
            return None
        with self.db_manager.engine.connect() as conn:
            stmt = update(self.table).where(self.table.c.product_id == modify_product_id).values(**kwargs)
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount
    
    def delete(self, product_id_to_delete):
        with self.db_manager.engine.connect() as conn:
            stmt = delete(self.table).where(self.table.c.product_id == product_id_to_delete)
            conn.execute(stmt)
            conn.commit()
            print(f'User {product_id_to_delete} has been deleted')
            return 