from sqlalchemy import create_engine
from models import metadata_obj

class DB_Manager:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:pass123@localhost:5432/postgres')
        metadata_obj.create_all(self.engine)

conn = DB_Manager()
