import getpass 
def get_database_details():
    provided_user = getpass.getpass("Please provide the user to connect to the database: ")
    provided_password= getpass.getpass("Please provide the user's password: ")
    provided_host = getpass.getpass("Please provide the host hosting the MYSQL server: ")
    provided_port = getpass.getpass("Please provide the port to connect to: ")
    provided_database = getpass.getpass("Please provide the database you want to connect to: ")
    return provided_user, provided_password, provided_host, provided_port, provided_database

def validate_schema(cursor_db, table_name, csv_df):
    cursor_db.execute("SHOW COLUMNS FROM {}".format(table_name))
    csv_column_names = csv_df.columns.tolist()
    output = cursor_db.fetchall()
    print(output)
    print(csv_column_names)