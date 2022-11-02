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

∀∃
### Universal Quantifier in SQL
 - 