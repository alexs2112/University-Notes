 ### NULL
 - Meanings
	 - Unknown value
	 - Unavailable/Withheld value
	 - Not applicable attribute
 - Each individual NULL value is considered to be different from every other NULL value
 - NULL = NULL is avoided, typically evaluated to false
 - Can check if attributes are null with `IS NULL` or `IS NOT NULL`
 - Example: Retrieve the names of all employees who do not have supervisors.
```
SELECT Fname, Lname  
FROM EMPLOYEE  
WHERE Super_SSN IS NULL
```

### Three-Valued Logic
 - SQL uses a three-valued logic
 - TRUE, FALSE, UNKNOWN

### Nested Queries
 - Complete select-from-where blocks within WHERE clause of another query
 - Outer query and nested subqueries
 - Comparison operator IN:
	 - Compares value v with a set (or multiset) of values v
	 - Evaluates to TRUE if v is one of the elements in v
 - Example: Give all employees in the 'Research' department a 10% raise in salary.
```
UPDATE EMPLOYEE  
SET Salary = Salary * 1.1  
WHERE DNO IN (SELECT Dnumber  
	FROM DEPARMENT  
	WHERE Dname = 'Research');
```
 - Note: Since only one value is returned by the nested query here, can use = instead of IN
 - You can also use tuples of values in comparisons (surround them by brackets)
 - You can also use In with a fixed set, such as `WHERE Pno IN (1, 3, 7);`

### ANY (or SOME)
```
SELECT Lname, Fname  
FROM EMPLOYEE  
WHERE Salary > ANY  
	(SELECT Salary  
	FROM EMPLOYEE  
	WHERE DNO = 5);
```
 - Comparison passes if Salary > at least one value in the result of the nested query
 - Operators that can be combined with ANY: =, >, >=, <, <=, <>

### Correlated Nested Queries
 - Example: Retrieve the name of each employee who has a dependent with the same first name and is the same sex as the employee.
```
SELECT E.Lname, E.Fname  
FROM EMPLOYEE AS E  
WHERE E.SSN IN  
	(SELECT D.ESSN  
	FROM DEPENDENT AS D  
	WHERE E.Fname = D.Dependent_name   <- E refers to EMP in the outer query
	AND E.Sex = D.Sex );
```
 - Evaluated once for each tuple in the outer query
	 - For each E in EMPLOYEE, perform this condition and return the first one that satisfies it
 - Queries that are nested using the = or IN comparison operator can be collapsed into join query
```
SELECT E.Lname, E.Fname  
FROM EMPLOYEE AS E, DEPENDENT AS D  
WHERE E.SSN = D.ESSN  
	AND E.Fname = D.Dependent_name  
	AND E.Sex = D.Sex;
```

### UNIQUE
 - `UNIQUE(Q)`:
	 - Returns True if there are no duplicate tuples in the result of nested query Q
	 - Boolean function that returns TRUE or FALSE

### EXISTS
 - `EXISTS`
	 - Check whether the result of a correlated nested query is empty or not
	 - Boolean function that returns TRUE or FALSE
 - `EXISTS` and `NOT EXISTS`
	 - Used in conjunction with a correlated nested query
 - Example:
```
SELECT E.Lname, E.Fname  
FROM EMPLOYEE AS E  
WHERE EXISTS  
	(SELECT *  
	FROM DEPENDENT AS D  
	WHERE E.SSN = D.ESSN)
AND EXISTS  
	(SELECT *  
	FROM DEPARTMENT AS D  
	WHERE E.SSN = D.MGR_SSN);
```

### Universal Quantifier in SQL
 - No direct implementation for ∀x P(x)
 - Recall that this can be expressed as:
	 - `not ∃x not P(x)`
 - Recall that most of the time the query has the form:
	 - `∀x (Q(x) -> R(x))`
 - Recall that (Q -> R) is equivalent to (not Q or R)
	 - `∀x (Q(x) -> R(x))`
	 - `not ∃x (Q(x) and not R(x))`

### (INNER) JOIN
```
SELECT Lname, Fname, Address  
FROM EMPLOYEE, DEPARTMENT  
WHERE DNO = Dnumber  
AND Dname = ‘Research’
```
```
SELECT Lname, Fname, Address  
FROM EMPLOYEE JOIN DEPARTMENT ON DNO = Dnumber  
WHERE Dname = ‘Research’
```
```
SELECT Lname, Fname, Address  
FROM EMPLOYEE INNER JOIN DEPARTMENT  
	ON DNO = Dnumber  
WHERE Dname = ‘Research’
```

### Natural Join
 - Rename attributes of one relation so it can be joined with another using NATURAL JOIN
```
SELECT Lname, Fname, Address  
FROM (EMPLOYEE NATURAL JOIN  
	 (DEPARTMENT AS DEPT(Dname, DNO, MSSN, Msdate)))  
WHERE Dname = ‘Research’
```
 - Implicit join condition of `EMPLOYEE.Dno = DEPT.DNo`

### OUTER Joins
 - LEFT OUTER JOIN
	 - Every tuple in left table must appear in result
	 - If no matching tuple, padded with NULL
```
SELECT E.Lname AS Employee_name,  
	   S.Lname AS Supervisor_name  
FROM (EMPLOYEE AS E, LEFT OUTER JOIN  
	EMPLOYEE AS S  
	ON E.Super_SSN = S.SSN);

SELECT E.Lname AS Employee_name,  
	   S.Lname AS Supervisor_name  
FROM EMPLOYEE AS E, EMPLOYEE AS S  
WHERE E.Super_SSN += S.SSN
(+= for left, =+ for right, ++ for full)
```
 - RIGHT OUTER JOIN
	 - Every tuple in right table must appear in result
	 - If no matching tuple, padded with NULL
 - FULL OUTER JOIN
	 - Combines result of LEFT and RIGHT OUTER JOINs

### Multiway JOIN in the FROM Clause
 - Can nest JOIN specifications for a multiway join
```
SELECT Pnumber, Dnum, Lname, Address, Bdate  
FROM ((PROJECT JOIN DEPARTMENT ON Dnum = Dnumber)  
		JOIN EMPLOYEE ON MGR_SSN = SSN)  
WHERE Plocation=’Stafford’;

SELECT Pnumber, Dnum, Lname, Address, Bdate  
FROM EMPLOYEE, DEPARTMENT, PROJECT  
WHERE Plocation=‘Stafford’  
AND Dnumber=Dnum  
AND MGR_SSN=SSN;
```

### Aggregate Functions
 - Use to summarize information from multiple tuples into a single-type summary
 - Built in aggregate functions:
	 - `COUNT, SUM, MAX, MIN, AVG`
 - Grouping: Create subgroups of tuples before summarizing
 - To select entire groups, `HAVING` clause is used
 - Aggregate functions can be used in the `SELECT` clause or in a `HAVING` clause

### Renaming Results of Aggregation
 - Following query returns a single row of computed values:
```
SELECT SUM(Salary), MIN(Salary), MAX(Salary), AVG(Salary)  
FROM EMPLOYEE;

SELECT SUM(Salary) AS Total_Salary,  
MIN(Salary) AS Lowest_Salary,  
MAX(Salary) AS Highest_Salary,  
AVG(Salary) AS Average_Salary  
FROM EMPLOYEE;
```
 - NULL values are discarded when aggregate functions are applied to a particular column
 - Example: Find the sum of the salaries of all employees of the ‘Research’ department, as well as the maximum salary, the minimum salary, and the average salary in this department.
```
SELECT SUM(Salary), MIN(Salary), MAX(Salary), AVG(Salary)  
FROM (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber)  
WHERE Dname=’Research’;
```
 - Example: Retrieve the number of employees:
```
SELECT COUNT(*)  
FROM EMPLOYEE;
```
 - Example: Retrieve the number of employees in the 'Research' department:
```
SELECT COUNT(*)  
FROM EMPLOYEE, DEPARTMENT  
WHERE Dno = Dnumber  
AND Dname=’Research’;
```

### Aggregate Functions on Booleans
 - SOME and ALL may be applied as functions on Boolean Values
 - SOME returns true if at least one element in the collection is TRUE (similar to OR)
 - ALL returns true if all of the elements in the collection are TRUE (similar to AND)

### GROUP BY
 - Partition relation into subsets of tuples
	 - Based on grouping attributes
	 - Apply function to each such group independently
 - GROUP BY clause
	 - Specifies grouping attributes
 - `COUNT (*)` counts the number of rows in the group
 - Example: Find the number of employees and average salary per department
```
SELECT DNO, COUNT(*), AVG(Salary)  
FROM EMPLOYEE  
GROUP BY DNO;
```
 - The group by attributes must appear in the SELECT clause
 - Example: For each project, find the number of employees working on it.
```
SELECT Pnumber, Pname, COUNT(*)  
FROM PROJECT, WORKS_ON  
WHERE PNO = Pnumber  
GROUP BY Pnumber, Pname;
```
 - If the grouping attribute has NULL as a possible value, a separate group is created for the null value
 - Grouping is applied to the result of the join.

### HAVING
 - HAVING clause: provides a condition to select or reject an entire group
 - Example: For each project **on which more than two employees work**, retrieve the project number, the project name, and the number of employees who work on the project.
```
SELECT Pnumber, Pname, COUNT(*)  
FROM PROJECT, WORKS_ON  
WHERE PNO = Pnumber  
GROUP BY Pnumber, Pname  
HAVING COUNT(*) > 2;
```
 - WHERE is applied first, then HAVING

### WITH
 - The WITH clause allows a user to define a table that will only be used in a particular query
	 - Not available in all SQL implementations
 - Used for convenience to create a temporary "View" and use that immediately in a query
 - Allows a more straightforward way of looking a step by step query
```
WITH BIGDEPTS(DNO) AS  
    (SELECT DNO  
    FROM EMPLOYEE  
    GROUP BY DNO  
    HAVING COUNT(*) > 5)  
SELECT DNO, COUNT(*)  
FROM EMPLOYEE  
WHERE Salary > 40000  
AND DNO IN BIGDEPTS  
GROUP BY DNO;
```

### CASE
 - Used when a value can be different based on certain conditions
 - Can be used in any part of an SQL query where a value is expected
 - Applicable when querying, inserting, or updating tuples
```
UPDATE EMPLOYEE  
SET Salary =  
CASE WHEN DNO = 1 THEN Salary + 2000  
CASE WHEN DNO = 4 THEN Salary + 1000  
CASE WHEN DNO = 5 THEN Salary + 1500  
ELSE Salary+ 0
```

### ASSERTION and TRIGGER
 - Syntax can differ between implementations
 - Semantic constraints are beyond the scope of the EER and relational model
 - `CREATE ASSERTION`
	 - Specify additional types of constraints outside scope of built-in relational model constraints
	 - Cannot be violated
```
CREATE ASSERTION SALARY_CONSTRAINT
CHECK (NOT EXISTS
	(SELECT *
	FROM EMPLOYEE E, EMPLOYEE M, DEPARTMENT D
	WHERE E.Salary > M.Salary
	AND E.DNO = D.DNumber
	AND M.SSN = D.MGR_SSN));
```
 - `CREATE TRIGGER`
	 - Specify automatic actions that database system will perform when certain actions and events occur
	 - Monitors the DB for violations and triggers an action based on an event
	 - Three parts: Event, Condition, Action
```
CREATE TRIGGER SALARY_VIOLATION  
BEFORE INSERT OR UPDATE OF Salary, Super_SSN ON EMPLOYEE  
FOR EACH ROW  
WHEN (NEW.Salary > (SELECT Salary  
					FROM EMPLOYEE  
					WHERE SSN = NEW.Super_SSN))  
INFORM_SUPERVISOR(NEW.Super_SSN, NEW.SSN)
```

### VIEWS (Virtual Tables) in SQL
 - Single table derived from other tables called the Defining Tables
 - Considered to be a virtual table
```
CREATE VIEW WORKS_ON_DETAILS  
AS SELECT Fname, Lname, Pname, Hours  
FROM PROJECT, WORKS_ON, EMPLOYEE  
WHERE Pnumber=PNO  
AND ESSN=SSN;  

SELECT * FROM WORKS_ON_DETAILS;
```
 - Retains the attribute names from the SELECT
```
CREATE VIEW DEPT_INFO (Dept_name, No_of_employees, Total_salary)  
AS SELECT Dname, COUNT(*), SUM(Salary),  
FROM DEPARTMENT, EMPLOYEE  
WHERE Dnumber=DNO  
GROUP BY Dname;
```
 - Renames the attribute names from the SELECT

### Using and Deleting Views
 - Once a View is defined, SQL queries can use the View relation in the FROM clause
 - View is always up-to-date
	 - Responsibility of the DBMS and not the user
 - DROP VIEW command
	 - Dispose of the view

### View Update
 - Update on a view defined on a single table without any aggregate functions
	 - Can be mapped to an update on underlying base table, as long as the primary key is preserved in the view
 - Update not permitted on aggregate view:
```
UPDATE DEPT_INFO  
SET Total_salary = 100000000  
WHERE Dname= ‘Research’;
```
 - Cannot be processed because Total_salary is a computed value in the view definition

### View Update and Inline Views
 - View involving joins
	 - Often not possible for DBMS to determine which of the updates is intended
 - Clause WITH CHECK OPTION
	 - Must be added at the end of the view definition if a view is to be updated to make sure the tuplesbeing updated stay in the view
 - In-Line view
	 - Defined in the FROM clause of an SQL query

Views as Authorization Mechanism
 - SQL has Query authorization statements (GRANT and REVOKE)
 - Views can be used to hide certain attributes or tuples from unauthorized users
 - For a user who is only allowed to see employee information for those who work for department 5, they may only access the view:
```
CREATE VIEW DEPT5EMP  
AS SELECT *  
FROM EMPLOYEE  
WHERE DNO = 5;
```

### Schema Change Statements in SQL
 - Schema evolution commands
	 - DBA may want to change the schema while the database is operational
	 - Does not require recompilation of the database schema

### DROP
 - Used to drop named schema elements, such as tables, domains, or constraints
 - Drop behaviour options:
	 - CASCADE and RESTRICT
 - Example:
	 - `DROP SCHEMA COMPANY CASCADE;`
	 - This removes the schema and all its elements including tables, views, constraints, etc
 - `RESTRICT`: Only delete if element is empty
	 - `DROP TABLE EMPLOYEE RESTRICT;`
		 - Only drop if table has no constraints or routines
	 - `DROP TABLE EMPLOYEE CASCADE;`
		 - Drop table with associated constraints or routines

### ALTER
 - Alter table actions include:
	 - Adding or dropping a column (attribute)
	 - Changing a column definition
	 - Adding or dropping table constraints
```
ALTER TABLE COMPANY.EMPOYEE  
ADD COLUMN Job VARCHAR(12);

ALTER TABLE COMPANY.EMPOYEE  
DROP COLUMN Address CASCADE;

ALTER TABLE COMPANY.EMPOYEE  
MODIFY Sex VARCHAR(12);
```
 - Adding and Dropping constraints:
	 - Change constraints specified on a table
```
ALTER TABLE COMPANY.EMPOYEE  
DROP CONSTRAINT EMPSUPERFK CASCADE;
```
 - Changing default values:
```
ALTER TABLE COMPANY.DEPARTMENT  
ALTER COLUMN MGR_SSN DROP DEFAULT;

ALTER TABLE COMPANY.DEPARTMENT
ALTER COLUMN MGR_SSN SET DEFAULT ’999999999’;
```

### Example of conversion from TRC to SQL:
![[TRC_to_mysql.png]]