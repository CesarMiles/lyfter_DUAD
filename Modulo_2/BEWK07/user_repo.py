from sqlalchemy import insert, update, delete, select
from models import user_table

class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.table = user_table
    
    # Create method which uses key:value arguments for managing the inserts of data 
    def create(self, **kwargs):
        with self.db_manager.engine.connect() as conn:
            stmt = insert(self.table).values(**kwargs).returning(self.table.c.user_id, self.table.c.role)
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar() 
    
    # Modify method using specific user_id  and key:value arguments to modify as required.
    def modify(self, modify_user_id, **kwargs):
        if not kwargs:
            print(f'There are no values to modify.')
            return None
        
        with self.db_manager.engine.connect() as conn:
            stmt = update(self.table).where(self.table.c.user_id == modify_user_id).values(**kwargs)
            result = conn.execute(stmt)
            conn.commit()
            return result.rowcount    

    # Delete method which only requires user id for deletion
    def delete(self, user_id_to_delete):
        with self.db_manager.engine.connect() as conn:
            stmt = delete(self.table).where(self.table.c.user_id == user_id_to_delete)
            conn.execute(stmt)
            conn.commit()
            print(f'User {user_id_to_delete} has been deleted')
            return 
    
    # Get method to retrieve all users from the table
    def get_user_details(self, user_id):
        with self.db_manager.engine.connect() as conn:
            stmt = select(self.table).where(user_table.c.user_id == user_id)
            result = conn.execute(stmt)
            users = result.all()
            if (len(users)==0):
                return None
            else:
                return users[0]
    
    # Get method for login
    def get_user_login(self, username, password):
        with self.db_manager.engine.connect() as conn:
            stmt = select(self.table).where(user_table.c.username == username).where(user_table.c.password == password)
            result = conn.execute(stmt)
            user = result.all()
            if (len(user)==0):
                return None
            return user[0]