# Expense Analyzer - Developing an ETL Pipeline using Python and MySQL

## Purpose 

The purpose of this project is to cover the following points 

- Develop a proof of concept project that uses the Python language to ingest data concerning a person's expenses 
- Clean the data and write the data to a local MYSQL server
- Develop a secondary script that reads from the appropriate MYSQL schema to develop aggregations

## Milestones

- Python logic to connect to the local MySQL database
- Imported library to cover a user's password input
- With the help of ChatGPT, imported the first 50 sample data points to store in the MySQL server
    - This was accomplished by importing the data manually in MySQL to automatically create the schema
- Created a specific user for the purposes of this ETL, restricting its access to the relevant schema
    - This is to prevent the usage of root 
    - The user was manually created in MySQL, given the appropriate and neccesary roles in a manner consistent with the concept of Least Privilege
- With the help of ChatGPT,created a sample set of 20 data points to insert into the MYSQL table
    - However, this data was inserted via the Python script
    