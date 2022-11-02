### DDL vs DML
 - Data Definition Language
	 - Schema definitions and changes
 - Data Manipulation Language
	 - Deals with changing and querying the data

### Schema and Catalog Concepts in SQL
 - Cover the basic standard SQL syntax - Variations in existing RDBMS systems
 - **SQL Schema**
	 - Identified by a schema name
	 - Includes an authorization identifier and descriptors for each element
 - **Scheme elements** include
	 - Tables, constraints, views, domains, other constructs
 - Each statement in SQL ends with a semicolon
 - `CREATE SCHEMA` statement:
	 - `CREATE SCHEME COMPANY AUTHORIZATION 'Jsmith'`
 - **Catalog**
	 - Named collection of schemas in an SQL environment
	 - Also has the concept of a cluster of catalogs
 - Terminology:
	 - Table for relation
	 - Row for tuple
	 - Column for attribute

### The CREATE TABLE Command in SQL
 - Specifying a new relation:
	 - Provide name of table
	 - Specify attributes, types, initial constraints
 - Can optionally specify schema
	 - `CREATE TABLE COMPANY.EMPLOYEE ...` or `CREATE TABLE EMPLOYEE ...`
 - Base Tables (base relations)
	 - Relation and its tuples are actually created and stored as a file by the DBMS
 - Virtual Relations (views)
	 - Created through the `CREATE VIEW` statement. Do not correspond to any physical file

### Foreign Keys
 - Some may cause errors
	 - Specified either via:
		 - Circular references
		 - Refer to a table that has not yet been created
	 - DBAs have a way to stop referential integrity enforcement to get around this problem

### Basic Attribute Data Types
 - Numeric data types:
	 - Integer numbers: `INTEGER` or `INT` and `SMALLINT`
	 - Floating-point numbers: `FLOAT` or `REAL` and `DOUBLE PRECISION`
 - Character-string data types
	 - Fixed length: `CHARACTER(n)` or `CHAR(n)`
	 - Varying length: `CHARACTER VARYING (n)` or `VARCHAR(n)` or `CHAR VARYING(n)`
 - Bit-string data types
	 - Fixed length: `BIT(n)`
	 - Varying length: `BIT VARYING(n)`
 - Boolean data type
	 - Values of `TRUE`, `FALSE`, or `NULL`
 - DATE data type
	 - Ten positions
	 - Components are `YEAR`, `MONTH`, `DAY` in the form `YYYY-MM-DD`
	 - Multiple mapping functions available in RDBMSs to change date formats
 - Additional attribute data types: @todo

### Domains
 - Name used with the attribute specification
 - Makes it easier to change the data type for a domain that is used by numerous attributes
 - Improves schema readability
 - Example:
	 - `CREATE DOMAIN SSN_TYPE AS CHAR(9);`
	 - `CREATE TABLE EMP (SSN SSN_TYPE NOT NULL, ...);`

### Basic Constraints
 - RM has 3 basic constraint types that are supported in SQL
	 - Key constraint: a primary key value cannot be duplicated
	 - Entity Integrity constraint: A primary key value cannot be null
	 - Referential Integrity constraints: The foreign key must have a value that is already present as a primary key, or may be null
 - Examples: `NOT NULL`, `CHECK (condition)`, `PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY`

### Key Constraints
 - `PRIMARY KEY` clause
	 - Specifies one or more attributes that make up the primary key of a relation
 - `UNIQUE` clause
	 - Specifies `CANDIDATE` keys

### Referential Integrity Constraints
 - `FOREIGN KEY` clause
	 - Default operation: reject update on violation
	 - Attach referential triggered action clause
		 - Options include: `SET NULL`, `CASCADE`, and `SET DEFAULT`
		 - Action taken by the DBMS for `SET NULL` or `SET DEFAULT` is the same for both `ON DELETE` and `ON UPDATE`
		 - `CASCADE` option suitable for relationship relations

### Giving Names to Constraints
 - Using the keyword `CONSTRAINT`
	 - Name a constraint
	 - Useful for later altering

### Specifying Constraints on Tuples Using CHECK
 - Additional constraints on individual tuples within a relation are also possible using CHECK
 - `CHECK` clauses at the end of a `CREATE TABLE` statement:
	 - Apply to each tuple individually
	 - `CHECK (Dept_create_date <= Mgr_start_date);`

# Basic Retrieval
### Tables are Multisets
 - SQL allows duplicate tuples in tables
	 - Unlike RM
	 - Multiset or bag behavior
	 - Tuple-id may be used as a key (internal attribute)

### Basic SQL Query
 - Basic form of the `SELECT` statement:
	 - `SELECT <attribute list> FROM <table list> [WHERE <condition>];
 - Which is
	 - PROJECT _attribute_ (SELECT _condition_ (R1 x ... x Rn)) where <table_list> = R1, ..., Rn

### SELECT Statement
 - Projection attributes (SELECT clause)
	 - Attributes whose values are to be retrieved
 - Selection condition (WHERE clause)
	 - Boolean condition that must be true for any retrieved tuple. Selection conditions include join conditions when multiple relations are involved
 - Logical comparison operators:
	 - =, <, <=, >=, and <> (!=)
 - Examples:
	 - `SELECT Bdate, Address FROM EMPLOYEE;`
	 - `SELECT * FROM EMPLOYEE WHERE Salary > 30000;`
	 - `SELECT Bdate, Address FROM EMPLOYEE WHERE Salary > 30000;`

### Examples:
 - Retrieve the birth date and address of the employee(s) whose name is 'John B. Smith'
	`SELECT Bdate, Address FROM EMPLOYEE WHERE Fname='John' AND Minit='B' AND Lname='Smith';`
 - Retrieve the name and address of all employees who work for the "Research" department
	`SELECT Fname, Lname, Address FROM EMPLOYEE, DEPARTMENT WHERE Dname='Research' AND Dnumber=Dno`
 - For every project located in "Stafford", list the project number, the controlling department number, and the department manager's last name, address, and birth date
 ```
 SELECT Pnumber, Dnum, Lname, Address, Bdate
 FROM EMPLOYEE, DEPARTMENT, PROJECT
 WHERE Plocation="Stafford"
 AND Dnumber=Dnum
 AND MGR_SSN=SSN;
 ```

### Ambiguous Attribute Names?
 - Must qualify the attribute name with the relation name to prevent ambiguity
```
SELECT Dname, Location
FROM DEPARTMENT, DEPT_LOCATIONS
WHERE DEPARTMENT.Dnumber=DEPT_LOCATIONS.Dnumber;
```
 - Can always use qualification

### Aliasing Tables:
 - For each employee, retrieve the employee’s first and last name and the first and last name of their immediate supervisor
```
SELECT E.Fname, E.Lname, S.Fname, S.Lname
FROM EMPLOYEE AS E, EMPLOYEE AS S
WHERE E.Super_SSN = S.SSN;
```
 - Recommended practice to abbreviate names and to prefix same or similar attributes from multiple tables
 - Can also aliase attributes themselves
	 - `SELECT E.Fname AS Employee_First_Name,`
 - Or aliase both at once:
	 - `FROM EMPLOYEE AS E(Fn, Mi, Ln, SSN, ...)`
	 - Does not change the original schema

### DISTINCT
 - SQL does not automatically eliminate duplicate tuples in query results
 - For aggregate operations, duplicates must be accounted for
 - Use the keyword `DISTINCT` in the `SELECT` clause
	 - Only distinct tuples should remain in the result
 - Example: Retrieve the salary of every employee (A) and all distinct salary values (B)
	```
	A:
	SELECT ALL Salary FROM EMPLOYEE;
	or
	SELECT Salary FROM EMPLOYEE;

	B: SELECT DISTINCT Salary FROM EMPLOYEE;
	```

### Set Operations
 - `UNION, EXCEPT, INTERSECT`
 - Corresponding multiset operations: `UNION ALL, EXCEPT ALL, INTERSECT ALL`
 - Type compatibility is needed for these operations to be valid
 - Example:
	 - Make a list of all project numbers for projects that involve an employee whose last name is ‘Smith’, either as a worker or as a manager of the department that controls the project.
	 ```
	(SELECT DISTINCT Pnumber
	FROM EMPLOYEE, DEPARTMENT, PROJECT
	WHERE MGR_SSN=SSN AND Dnumber=Dnum
	AND Lname="Smith")	 
	
	UNION

	(SELECT DISTINCT Pnumber
	FROM PROJECT, WORKS_ON, EMPLOYEE
	WHERE Pnumber=PNO AND ESSN=SSN
	AND Lname="Smith")
	```

### LIKE & BETWEEN
 - `LIKE`
	 - Used for string pattern matching
	 - `%` replaces an arbitrary number of zero or more characters
	 - Underscore (`_`) replaces a single character
	 - Examples:
		 - `WHERE Address LIKE '%Houston,TX%';`
		 - `WHERE Ssn LIKE '_ _ 1_ _ 8901'`
 - `BETWEEN`
	 - Comparison operator
	 - Example:
		 - `WHERE(Salary BETWEEN 30000 AND 40000) AND Dno=5;`

### Arithmetic Operations
 - Standard arithmetic operators
	 - Addition, subtraction, multiplication, and division may be included as a part of `SELECT`
 - Example:
	 - Show the resulting salaries if every employee working on the ‘ProductX’ project is given a 10 percent raise.
	```
	SELECT E.Fname, E.Lname, 1.1*E.Salary, AS Increased_Salary
	FROM EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
	WHERE E.SSN=W.ESSN AND W.PNO=P.PNumber
	AND P.Pname="ProductX";	
	```

### Ordering of Query Results
 - Use `ORDER BY` clause
	 - `DESC, ASC`
	 - Typically placed at the end of the query
	 - `ORDER BY D.Dname DESC, E.Lname ASC, E.Fname ASC`

### INSERT
 - Used to add one or more tuples to a relation
 - Attribute values should be listed in the same order as the attributes were specified in the `CREATE TABLE` command
 - Constraints on data types are observed automatically
 - Any integrity constraints as a part of the DDL specification are enforced
 - Example:
```
INSERT INTO EMPLOYEE  
VALUES ('Richard','K','Marini','653298653','1984-12-12', '98 Oak Rise,  
Calgary, AB', 'O', 60000, '653298653', 4);
```

### Bulk Loading of Tables
 - Only works for data already in the DB
 - Creates more than one tuple in the database, needs to extract the data from the DB itself
```
CREATE TABLE WORKS_ON_INFO (  
	Employee_name VARCHAR(15) NOT NULL,  
	Project_name VARCHAR(15) NOT NULL,  
	Hours_per_week DECIMAL(3,1));

INSERT INTO WORKS_ON_INFO  
SELECT CONCAT(E.Fname, E.Lname), P.Pname, W.Hours  
FROM EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P  
WHERE E.SSN=W.ESSN AND W.PNO=P.Pnumber
```
 - Can also create a new table, T' can be created with the same attributes as T and using LIKE it can be loaded with entire data
	```
	CREATE TABLE EMPS LIKE EMPLOYEE;

	CREATE TABLE D5EMPS LIKE EMPLOYEE(
		SELECT *
		FROM EMPLOYEE AS E
		WHERE E.DNO=5
	);

	CREATE TABLE EMPNAMES LIKE EMPLOYEE(
		SELECT E.Lname, E.Fname, E.Salary
		FROM EMPLOYEE AS E
	);
	```

### DELETE
 - Removes tuples from a relation
	 - Optional WHERE clause to select what to be deleted (otherwise all of them, empty table)
	 - Referential integrity should be enforced
	 - Tuples deleted from only ONE tuple at a time (unless CASCADE is specified)
	 - The number of tuples deleted depends on the number of tuples in the relation that satisfy the WHERE-clause
 - Examples:
```
DELETE FROM EMPLOYEE;  

DELETE FROM EMPLOYEE  
WHERE DNO=5;  

DELETE FROM EMPLOYEE  
WHERE Sex=‘M’;  

DELETE FROM EMPLOYEE  
WHERE Salary>1000000
```

### UPDATE
 - Modify attributes of one or more selected tuples
 - WHERE clause selects the tuples to be modified
 - Additional SET clause specifies the attributes to be modified and their new values
 - Modifies tuples in the same relation
 - Referential integrity is enforced
 - Examples:
```
UPDATE PROJECT  
SET Plocation=‘Calgary’, Dnum=5  
WHERE Pnumber=10;

UPDATE EMPLOYEE  
SET Salary=Salary*1.1  
WHERE Sex<>’M’;  

UPDATE EMPLOYEE  
SET Salary=Salary*1.1;	
```
