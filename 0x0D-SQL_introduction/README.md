## SQL - Introduction


A database is a structured collection of data organized for efficient storage, retrieval, and management. A relational database is a type of database that uses a structured format to store data in tables with predefined relationships between them.

SQL stands for Structured Query Language, which is a domain-specific language used for managing and manipulating relational databases.

MySQL is an open-source relational database management system that uses SQL to manage and interact with databases.

To create a database in MySQL, you use the `CREATE DATABASE` statement: `CREATE DATABASE database_name;`

DDL stands for Data Definition Language, used for creating and modifying database structures. DML stands for Data Manipulation Language, used for querying and modifying data within the database.

To create or alter a table, you use the `CREATE TABLE` or `ALTER TABLE` statements, respectively.

To select data from a table, you use the `SELECT` statement: `SELECT column1, column2 FROM table_name WHERE condition;`

To insert data, use the `INSERT INTO` statement. To update data, use the `UPDATE` statement. To delete data, use the `DELETE FROM` statement.

Subqueries are nested queries that can be used within larger queries to retrieve data based on conditions evaluated dynamically.

MySQL offers various functions for tasks like string manipulation, date calculations, and mathematical operations. For example, to get the length of a string, you can use: `SELECT LENGTH(column_name) FROM table_name;`

Remember that the syntax and specific statements might vary slightly based on the version of MySQL you're using.