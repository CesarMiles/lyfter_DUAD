from sqlalchemy import insert, update, delete, select


# Repository for each class to manage the db. Each class replicate the same structure. 
class UserRepository:
    # Constructor to use connection and table name 
    def __init__(self, connection, table):
        self.conn = connection
        self.table = table
    
    # Create method which uses key:value arguments for managing the inserts of data 
    def create(self, **kwargs):
        stmt = insert(self.table).values(**kwargs).returning(self.table.c.user_id, self.table.c.full_name)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.scalar()
    
    # Modify method using specific user_id  and key:value arguments to modify as required.
    def modify(self, modify_user_id, **kwargs):
        if not kwargs:
            print(f'There are no values to modify.')
            return None
        
        stmt = update(self.table).where(self.table.c.user_id == modify_user_id).values(**kwargs)
        result = self.conn.execute(stmt)
        self.conn.commit()
        return result.rowcount
    
    # Delete method which only requires user id for deletion
    def delete(self, user_id_to_delete):
        stmt = delete(self.table).where(self.table.c.user_id == user_id_to_delete)
        self.conn.execute(stmt)
        self.conn.commit()
        print(f'User {user_id_to_delete} has been deleted')
        return 
    
    # Get method to retrieve all users from the table
    def get_users(self):
        stmt = select(self.table)
        result = self.conn.execute(stmt)
        return result.all()
    
