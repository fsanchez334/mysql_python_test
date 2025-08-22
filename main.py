import pandas as pd
import mysql.connector
import getpass
from datatabaseConnector import DatabaseConnector

if __name__ == "__main__":
    #Prompt the user
    print("Hello - we will connect you to the database")
    provided_user = getpass.getpass("Please provide the user to connect to the database: ")
    provided_password= getpass.getpass("Please provide the user's password: ")
    provided_host = getpass.getpass("Please provide the host hosting the MYSQL server: ")
    provided_port = getpass.getpass("Please provide the port to connect to: ")
    provided_database = getpass.getpass("Please provide the database you want to connect to: ")
    #pythonexpense_project
    #From the provided information, create the database connection
    db_obj= DatabaseConnector(provided_user, provided_password, provided_host, provided_port, provided_database)
    connection_passed = db_obj.connect_to_database()
    cursor = None
    if connection_passed:
        print("Connected to the database")
        cursor = db_obj.get_cursor()
    else:
        print("Connection failed -  please check configuration")

    #From here, prompt the user to provide the path to the csv that will be used to ingest into the database
    path_to_ingest = input("Please provide the path to the csv file containing records you would like to insert into the table")
    additional_records = pd.read_csv(path_to_ingest)

    #Assuming the data is clean, we have to manipulate the data
    #In order to add data to the MySQL table, the data has to be in the form of a list made up of tuples
    records_extracted = additional_records.to_records(index=False).tolist()
    print(records_extracted)
    #Now that we have this, we can go ahead and insert into the table
    #We need to know the column names
    #column_names = tuple([x[0] for x in cursor.description])
    #print(column_names)