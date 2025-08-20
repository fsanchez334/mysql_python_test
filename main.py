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

#Ingest the sample csv file that we have produced with ChatGpt:
path_for_expenses = input("Please provide the path for the sample csv: ")
df =  pd.read_csv(path_for_expenses)
print(df)