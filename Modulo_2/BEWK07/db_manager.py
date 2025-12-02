from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date

metadata_obj = MetaData(schema="deliverable_wk07")

user_table = Table(
    "users",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("username", String(30), nullable=False, unique=True),
    Column("password", String(30), nullable=False),
    Column("role", String(10), nullable=False)
)

products_table = Table(
    "products",
    metadata_obj,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", String(20), nullable=False),
    Column("product_price", Integer, nullable=False),
    Column("entry_date", Date, nullable=False),
    Column("stock", Integer, nullable=False)
)

invoice_table = Table(
    "invoice",
    metadata_obj,
    Column("invoice_id", Integer, primary_key=True),
    Column("user_id", ForeignKey("deliverable_wk07.users.user_id"), nullable=False),
    Column("total_amount", Integer, nullable=False),
    Column("invoice_status", String(20), nullable=False)
)

invoice_details_table = Table(
    "invoice_detail",
    metadata_obj,
    Column("item_id", Integer, primary_key=True),
    Column("invoice_id", ForeignKey("deliverable_wk07.invoice.invoice_id"), nullable=False),
    Column("product_id", ForeignKey("deliverable_wk07.products.product_id"), nullable=False),
    Column("quantity", Integer, nullable=False)
)

class DB_Manager:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:pass123@localhost:5432/postgres')
        metadata_obj.create_all(self.engine)