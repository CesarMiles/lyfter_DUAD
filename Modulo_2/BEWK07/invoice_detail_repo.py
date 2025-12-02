from sqlalchemy import insert, update, delete, select
from db_manager import invoice_details_table

class InvoiceDetailRepository:
    # Constructor to use connection and table name 
    def __init__(self, connection):
        self.conn = connection
        self.table = invoice_details_table
    
    # Create method which uses key:value arguments for managing the inserts of data 
    def create(self, **kwargs):
        stmt = insert(self.table).values(**kwargs).returning(self.table.c.item_id, self.table.c.invoice_id)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    # Modify method using specific user_id  and key:value arguments to modify as required.
    def modify(self, item_id_to_modify, **kwargs):
        if not kwargs:
            print(f'There are no values to modify.')
            return None
        
        stmt = update(self.table).where(self.table.c.item_id == item_id_to_modify).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
    
    # Delete method which only requires user id for deletion
    def delete(self, item_id_to_delete):
        stmt = delete(self.table).where(self.table.c.item_id == item_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'Item {item_id_to_delete} has been deleted')
        return 