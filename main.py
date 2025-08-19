import pandas as pd
import mysql.connector
import getpass

user = input("Please provide user to the database: ")
password = getpass.getpass("Please provide the password to connect to the database: ")
conn = mysql.connector.connect(
    host="localhost",   # or "localhost", depending on your setup
    port=3306,          # default MySQL port
    user="{}".format(user),
    password="{}".format(password)
)

connection_status = conn.is_connected()
print(connection_status)