# HTML
# CSS
# PHP

# SQL 
## Basic SQL commands 
Entering mySQL via a terminal: `mysql -u root -p`
This will propmt you with a password, if entering with root 

Showing all Databases: `show databases;` 
Access Database: mysql -u 
Showing all tables 


### Databases 
Show all databases:  
`show databases;`

Create new database:  
`create database [database];`  

Select database:   
`use [database];`

Determine what database is in use:   
`select database();`

### Tables
Show all tables:   
`show tables;`

Show table structure:   
`describe [table];`

List all indexes on a table:  
`show index from [table];`

Create new table with columns: 
`CREATE TABLE [table] ([column] VARCHAR(120), [another-column] DATETIME);`

Adding a column:   
`ALTER TABLE [table] ADD COLUMN [column] VARCHAR(120);`

Adding a column with an unique, auto-incrementing ID:   
`ALTER TABLE [table] ADD COLUMN [column] int NOT NULL AUTO_INCREMENT PRIMARY KEY;`

Inserting a record:   
`INSERT INTO [table] ([column], [column]) VALUES ('[value]', '[value]');`

MySQL function for datetime input:   
`NOW()`

Selecting records:   
`SELECT * FROM [table];`

Explain records:   
`EXPLAIN SELECT * FROM [table];`

Selecting parts of records:   
`SELECT [column], [another-column] FROM [table];`

Counting records: 
`SELECT COUNT([column]) FROM [table];`






# Basic CRUD
CRUD - Create Read Update Delete
Basic example of database manipulation 

This is designed to run on a LAMP stack server.
If you need help setting one up, you can use `LAMP.md` 

## Creating a database table 
We first need a database table that we can edit, unlike noSQL tables, a SQL table first has to be generated before someone can input data into the table. 

We need an:
- id
- name
- address 
- age

We can execute the following code to create a table named `employees`:  
```sql
CREATE TABLE employees (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    salary INT(10) NOT NULL
);
```
To run this directly on the mySQL server: 
Enter mysql via a terminal using: `mysql -u root -p`  
Show Databases: `show databases;`
Select database: `use database;`










 tail /var/log/apache2/error.log -F 
