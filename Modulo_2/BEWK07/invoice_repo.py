from sqlalchemy import insert, update, delete, select
from db_manager import invoice_table

class InvoiceRepository:
    def __init__(self, connection):
        self.coon = connection
        self.table = invoice_table

    def create(self, **kwargs):
        stmt = insert(self.table).values(*kwargs).returning(self.table.c.invoice_id, self.table.c.user_id)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    def modify(self, modify_invoice_id, **kwargs):
        if not kwargs:
            print(f'There are no values to modify')
            return None
        
        stmt = update(self.table).where(self.table.c.invoice_id == modify_invoice_id).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
    
    def delete(self, invoice_id_to_delete):
        stmt = delete(self.table).where(self.table.c.invoice_id == invoice_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'Invoice id {invoice_id_to_delete} has been deleted')
        return 
    