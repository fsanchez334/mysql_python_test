import pandas as pd
import mysql.connector
import getpass
from datatabaseConnector import DatabaseConnector
from helperfunctions import *

if __name__ == "__main__":
    #Prompt the user
    print("Hello - we will connect you to the database")
    provided_user, provided_password, provided_host, provided_port, provided_database = get_database_details()
    #pythonexpense_project
    #From the provided information, create the database connection
    db_obj= DatabaseConnector(provided_user, provided_password, provided_host, provided_port, provided_database)
    connection_passed = db_obj.connect_to_database()
    cursor = None
    if connection_passed:
        print("Connected to the database")
        cursor = db_obj.get_cursor()
        #Show the user what tables they have at their disposal
        cursor.execute("SHOW TABLES;")
        print(cursor.fetchall())
        #Now we want the user to specify what table they want
        table_desired = input("Specify the table you want to access: ")        

        #From here, prompt the user to provide the path to the csv that will be used to ingest into the database
        path_to_ingest = input("Please provide the path to the csv file containing records you would like to insert into the table: ")
        additional_records = pd.read_csv(path_to_ingest)
        #I want to double check that the schema will match - else, alert the user
        validate_schema(cursor_db=cursor, table_name=table_desired, csv_df=additional_records)

        #Assuming the data is clean, we have to manipulate the data
        #In order to add data to the MySQL table, the data has to be in the form of a list made up of tuples
        #records_extracted = additional_records.to_records(index=False).tolist()
        #rint(records_extracted)
        #Now that we have this, we can go ahead and insert into the table
        #We need to know the column names
        #column_names = tuple([x[0] for x in cursor.description])
        #print(column_names)