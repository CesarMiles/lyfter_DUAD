from sqlalchemy import insert, update, delete, select
from models import invoice_details_table

class InvoiceDetailRepository:
    # Constructor to use connection and table name 
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.table = invoice_details_table
    
    # Create method which uses key:value arguments for managing the inserts of data 
    def create(self, invoice_id, product_id, quantity):
        with self.db_manager.engine.connect() as conn:
            stmt = insert(self.table).values(invoice_id=invoice_id, product_id=product_id, quantity=quantity).returning(self.table.c.item_id, self.table.c.invoice_id)
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()
    
    # Modify method using specific user_id  and key:value arguments to modify as required.
    def modify(self, item_id_to_modify, **kwargs):
        if not kwargs:
            print(f'There are no values to modify.')
            return None
        with self.db_manager.engine.connect() as conn:
            stmt = update(self.table).where(self.table.c.item_id == item_id_to_modify).values(**kwargs)
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount
    
    # Delete method which only requires user id for deletion
    def delete(self, item_id_to_delete):
        with self.db_manager.engine.connect() as conn:
            stmt = delete(self.table).where(self.table.c.item_id == item_id_to_delete)
            conn.execute(stmt)
            conn.commit()
            print(f'Item {item_id_to_delete} has been deleted')
            return 