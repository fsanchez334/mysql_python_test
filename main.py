import pandas as pd
import mysql.connector
import getpass
from datatabaseConnector import DatabaseConnector

def connectToDatabase():
    user = input("Please provide user to the database: ")
    password = getpass.getpass("Please provide the password to connect to the database: ")
    conn = mysql.connector.connect(
        host="localhost",   # or "localhost", depending on your setup
        port=3306,          # default MySQL port
        user="{}".format(user),
        password="{}".format(password)
    )
    connection_status = conn.is_connected()
    if connection_status:
        print("Successfully connected to the database")
        return conn
    else:
        print("Something went wrong - try again")
        return -1
    
if __name__ == "main":
    #Prompor

db_connection = connectToDatabase()
db_cursor = db_connection.cursor()
db_cursor.execute("SHOW DATABASES")
databases_results = db_cursor.fetchall()
print(databases_results)
db_cursor.execute("SELECT * FROM pythonexpense_project.expenses")
sample_output = db_cursor.fetchall()
print(sample_output)

#Now, let's consider the case where we are given new records - records that we have to then insert
path_to_ingest = input("Please provide csv file, containing records we need to insert into our table")
additional_records = pd.read_csv(path_to_ingest)
#Here, we know that we need to drop the notes column - improvement: compare the schemas dynamically
additional_records.drop('notes', axis=1, inplace=True)
print(additional_records)
#In order to add data to the MySQL table, the data has to be in the form of a list made up of tuples
records_extracted = additional_records.to_records(index=False).tolist()
#Now that we have this, we can go ahead and insert into the table
#We need to know the column names
column_names = tuple([x[0] for x in db_cursor.description])
cols = ", ".join(f"`{c}`" for c in column_names)  # backtick each name
insert_query = f"INSERT INTO pythonexpense_project.expenses ({cols}) VALUES (%s,%s,%s,%s,%s,%s,%s)"
db_cursor.executemany(insert_query, records_extracted)
db_connection.commit()
print(db_cursor.rowcount, "were inserted.")