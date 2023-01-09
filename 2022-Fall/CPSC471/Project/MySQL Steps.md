### Project Setup
 - Using the `MySQL 8.0 Command Line Client`
 - `show databases;` to confirm that you can see the DBs and that it is working

### Making a New User
 - https://dev.mysql.com/doc/refman/8.0/en/creating-accounts.html
```
CREATE USER 'testuser'@'localhost'
	IDENTIFIED BY '1qaz@WSX';
GRANT ALL 
	ON *.* 
	TO 'testuser'@'localhost' 
	WITH GRANT OPTION;
```
 - To list users: `SELECT user FROM user;`

### Test Database
```
SHOW DATABASES;
CREATE DATABASE test;
USE test;
SHOW TABLES;
CREATE TABLE ...
```