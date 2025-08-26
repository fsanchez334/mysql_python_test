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
    print(csv_df.dtypes)
    #First validate that the names are the same 
    extracted_names_db = set([tuplet[0] for tuplet in output])
    csv_column_names_set = set(csv_column_names)
    if extracted_names_db == csv_column_names_set:
        print("The schema between the the csv file and the target database is consistent - insofar as column names are concerned")
    else:
        print("There are some inconsistencies in the columns between the two")
        expected_in_mysql_table = extracted_names_db - csv_column_names_set
        csv_not_in_table = csv_column_names_set - expected_in_mysql_table
        print("In table not in csv: {}".format(expected_in_mysql_table))
        print("In CSV not in table: {}".format(csv_not_in_table))

    