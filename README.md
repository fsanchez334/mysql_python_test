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

## Roadmap items
The following items are potential tasks that I currently see as improvements to be made to this project

- Move helper functions into a seperate file 
- Develop an Objected Oriented approach group relevant functions associated with connecting to the MYSQL database, inserting and querying the table
- Incorporate logic to handle incomplete or improper data
- Develop logic to cross check the schema of the incoming data with the target schema of the table
- Develop a second script that reads from the MySQL table as it is being updated
- Develop logic to perform aggregations and generate gold views for data visualization software like Tableau or Power BI
