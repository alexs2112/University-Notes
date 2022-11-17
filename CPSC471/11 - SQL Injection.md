### Overview
 - Simple to prevent SQL Injection attacks
 - One of the top level security threats
 - Fool the database by injecting code to change the existing SQL code

### Example Code:
```
query =
"SELECT * FROM USERS WHERE Username = '"
+ user +
"'
AND Password = '"
+ password +
'"
```
 - Let password be `X' OR 'X' = 'X';--`
```
SELECT *
FROM USERS
WHERE Username = 'username'
AND Password = 'X' OR 'X' = 'X';--
'"
```
 - `;--` End with comment, not necessary as SQL immediately stops after ;
 - Let password be `X'; SELECT * FROM Tables;--`
 - Tells us every single table, can proceed to `SELECT *` from any other table

### Preventing Attacks
1. Validate input
2. Do not build a query using string concatenation
	- Use a parametrized query instead (language specific)
 - Example in Java
```
PreparedStatement query = connection.prepareStatement(
"SELECT * FROM users WHERE User=? AND Password=?");
sql.setString(1, user);
sql.setString(2, pwd);
ResultSet rs = query.executeQuery();
```
 - SQL Statement is compiled ahead of time, it is just data, not a string that can be altered
 - user and pwd are inserted at runtime, never compiled as SQL