from sqlalchemy import insert, update, delete, select
from models import products_table
from db_manager import conn

class ProductRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.table = products_table
    
    #Method to create products on db
    def create_product(self, **kwargs):
        with self.db_manager.engine.connect() as conn:
            stmt = insert(self.table).values(**kwargs).returning(self.table.c.product_id, self.table.c.product_name)
            result = conn.execute(stmt)
            conn.commit()
            return result.first()
    
    def modify_product(self, product_id, **kwargs):
        if not kwargs:
            return False
        
        with self.db_manager.engine.connect() as conn:
            stmt = update(self.table).where(self.table.c.product_id == product_id).values(**kwargs)
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount > 0
    
    def delete_product(self, product_id):
        with self.db_manager.engine.connect() as conn:
            stmt = delete(self.table).where(self.table.c.product_id == product_id)
            result = conn.execute(stmt)  
            conn.commit()
            return result.rowcount > 0
    
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

product_repo = ProductRepository(conn)