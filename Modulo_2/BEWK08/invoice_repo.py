from sqlalchemy import insert, update, delete, select
from models import invoice_table
from db_manager import conn

class InvoiceRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.table = invoice_table

    def create(self, **kwargs):
        with self.db_manager.engine.connect() as conn:
            stmt = insert(self.table).values(**kwargs).returning(self.table.c.invoice_id, self.table.c.user_id)
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()
    
    def modify(self, modify_invoice_id, **kwargs):
        if not kwargs:
            print(f'There are no values to modify')
            return None
        
        with self.db_manager.engine.connect() as conn:
            stmt = update(self.table).where(self.table.c.invoice_id == modify_invoice_id).values(**kwargs)
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount
    
    def delete(self, invoice_id_to_delete):
        with self.db_manager.engine.connect() as conn:
            stmt = delete(self.table).where(self.table.c.invoice_id == invoice_id_to_delete)
            conn.execute(stmt)
            conn.commit()
            print(f'Invoice id {invoice_id_to_delete} has been deleted')
            return 
    
    def get(self, user_id):
        with self.db_manager.engine.connect() as conn:
            stmt = select(self.table).where(self.table.c.user_id == user_id)
            result = conn.execute(stmt)
            return result.all()
    
    def belongs_to_user(self, invoice_id, user_id):
        with self.db_manager.engine.connect() as conn:
            stmt = select(self.table.c.invoice_id).where(
                (self.table.c.invoice_id == invoice_id) &
                (self.table.c.user_id == user_id)
            )
            result = conn.execute(stmt)
            return result.first() is not None

invoice_repo = InvoiceRepository(conn)