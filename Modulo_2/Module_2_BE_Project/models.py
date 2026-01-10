from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, func

metadata_obj = MetaData(schema="m2_be_project")

user_table = Table(
    "users",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("email", String(30), nullable=False, unique=True),
    Column("password", String(30), nullable=False),
    Column("role", String(10), nullable=False, server_default='user'),
    Column("create_date", Date, nullable=False, server_default=func.now())
)

products_table = Table(
    "products",
    metadata_obj,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", String(20), nullable=False),
    Column("product_price", Integer, nullable=False),
    Column("stock", Integer, nullable=False)
)

invoice_table = Table(
    "invoice",
    metadata_obj,
    Column("invoice_id", Integer, primary_key=True),
    Column("user_id", ForeignKey("m2_be_project.users.user_id"), nullable=False),
    Column("total_amount", Integer, nullable=False),
    Column("invoice_status", String(20), nullable=False, server_default='payed')
)

invoice_details_table = Table(
    "invoice_detail",
    metadata_obj,
    Column("item_id", Integer, primary_key=True),
    Column("invoice_id", ForeignKey("m2_be_project.invoice.invoice_id"), nullable=False),
    Column("product_id", ForeignKey("m2_be_project.products.product_id"), nullable=False),
    Column("quantity", Integer, nullable=False)
)