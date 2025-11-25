from sqlalchemy import Table, Column, Integer, String, ForeignKey, SmallInteger, MetaData

metadata_obj = MetaData(schema="deliverable_wk06")

users_table = Table(
    "users",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("full_name", String(30), nullable=False),
    Column("email_address", String(40), nullable=False),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("address_id", Integer, primary_key=True),
    Column("country", String(20), nullable=False),
    Column("province", String(20), nullable=False),
    Column("city", String(20), nullable=False),
    Column("user_id", ForeignKey("deliverable_wk06.users.user_id"), nullable=False),
)

car_table = Table(
    "car",
    metadata_obj,
    Column("car_id", Integer, primary_key=True),
    Column("model", String(30), nullable=False),
    Column("brand", String(30), nullable=False),
    Column("factory_year", SmallInteger, nullable=False),
    Column("user_id", ForeignKey("deliverable_wk06.users.user_id"), nullable=True),
)


