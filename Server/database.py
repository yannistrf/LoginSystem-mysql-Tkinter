import mysql.connector

"""
    This is an interface to interact with our login system's database.
"""
class Database:
    # Need the database server information
    def __init__(self, host, user, passwd, database):
        # try to connect to the database
        try:    
            self.database = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        # In case of failure terminate the program
        except:
            print("Couldn't connect to the database. Exiting...")
            exit(-1)
        
        self.cursor = self.database.cursor()
    
    def login(self, username, password):
        self.cursor.execute(f"SELECT COUNT(*) FROM user_info WHERE name='{username}' AND password='{password}'")
        result = self.cursor.fetchone()
        
        # Only one match should return, we have unique usernames
        if result[0] == 1:
            return True
        
        return False
    
    def register(self, username, password):
        try:
            self.cursor.execute(f"INSERT INTO user_info VALUES ('{username}', '{password}')")    
            self.database.commit()
            print("REGISTRATION SUCCESSFUL")
            return True
        except mysql.connector.errors.IntegrityError:
            print("USERNAME ALREADY IN USE")
            return False
        
    def delete(self, username, password):
        pass


