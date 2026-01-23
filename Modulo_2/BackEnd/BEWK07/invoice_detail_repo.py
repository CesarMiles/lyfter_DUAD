from sqlalchemy import insert, update, delete, select
from models import invoice_details_table, invoice_table, products_table

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
    
    # Get that uses joins to generate a specific view of a invoice with the details of its purchase, its used when an users queries for only invoice_id 
    def get_invoice_with_details(self, invoice_id):
        with self.db_manager.engine.connect() as conn:
            stmt = select(
                invoice_table.c.invoice_id,
                invoice_table.c.total_amount,
                invoice_table.c.invoice_status,
                products_table.c.product_name,
                products_table.c.product_price,
                invoice_details_table.c.quantity,
                (products_table.c.product_price * invoice_details_table.c.quantity).label('subtotal')
            ).select_from(invoice_table.join(invoice_details_table,invoice_table.c.invoice_id == invoice_details_table.c.invoice_id)).join(products_table, invoice_details_table.c.product_id == products_table.c.product_id).where(invoice_table.c.invoice_id == invoice_id)
            result = conn.execute(stmt)
            return result.all()
