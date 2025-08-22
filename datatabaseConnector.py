import mysql.connector

class DatabaseConnector:
    
    def __init__(self, user: str, password: str, host: str, port: int, database: str):
        self.user = user
        self._password =  password
        self.host = host
        self.port = port
        self.database = database
        self.conn = None

    def connect_to_database(self):
        self.conn = mysql.connector.connect(
            host = self.host, 
            port = self.port,        
            user = self.user, 
            password= self._password,
            database = self.database
        )
        if self.conn.is_connected():
            self._password = None
            return True
        else:
            return False
        
    def get_cursor(self):
        return self.conn.cursor()
    
    def disconnect_from_database(self):
        self.conn.close()
        return True

    def commit_changes(self):
        self.conn.commit()
    
    def get_accessible_schemas(self, cursor):
        cursor.execute("SHOW DATABASES")
        container = cursor.fetchall()
        applicable_databases = [database[0] for database in container if database[0] not in {'information_schema', 'performance_schema'}]
        return applicable_databases