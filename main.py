import pandas as pd
import mysql.connector
import getpass

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

db_connection = connectToDatabase()
db_cursor = db_connection.cursor()
db_cursor.execute("SHOW DATABASES")
databases_results = db_cursor.fetchall()
print(databases_results)
db_cursor.execute("SELECT * FROM pythonexpense_project.expenses")
sample_output = db_cursor.fetchall()
print(sample_output)
#Ingest the sample csv file that we have produced with ChatGpt:
#path_for_expenses = input("Please provide the path for the sample csv: ")
#df =  pd.read_csv(path_for_expenses)
#From here, we need to select the columns we care about - for now, we don't need the notes column. We can drop it
#df.drop('notes', axis=1, inplace=True)
#print(df)
