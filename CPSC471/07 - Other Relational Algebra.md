### Query Tree Notation
 - An internal structure to represent a query
 - Standard technique for estimating the work involved in executing a query, the generation of intermediate results, and the optimization of execution
 - Nodes stand for operations like selection, projection, join, renaming, division, ...
 - Leaf nodes represent base relations
 - A tree gives a good visual feel of the complexity of the query and the operations involved
 - Algebraic Query Optimization consists of rewriting the query or modifying the query tree into an equivalent tree
 - Example at the bottom of this page

### Aggregate Function Operation (Ƒ)
 - Use of the Aggregate Functional operation
 - Ƒ _MAX Salary_ (EMPLOYEE)
	 - Maximum Salary in relation EMPLOYEE
 - Ƒ _MIN Salary_ (EMPLOYEE)
 - Ƒ _AVG Salary_ (EMPLOYEE)
 - Ƒ _COUNT SSN_ (EMPLOYEE)
	 - Counts the number of rows
 - Ƒ _COUNT SSN, AVG Salary_ (EMPLOYEE)
	 - Creates a table of pairs

### Using Grouping with Aggregation
 - Grouping calculations by attributes
	 - Grouping attribute placed to the left of Ƒ
	 - Aggregate functions to the right of Ƒ
 - _DNO_ Ƒ _COUNT SSN, AVG Salary_ (EMPLOYEE)
	 - Counts Employees and computers average salary per department

### Additional Relational Operations: OUTER JOIN
 - In NATURAL JOIn and EQUIJOIN, tuples without a matching (or related) tuple are eliminated from the join result
	 - Tuples with null in the join attributes are also eliminated
	 - This amounts to loss of information
 - Example:
	 - List all employees, then match them with their dependants
	 - Need to still list employees who do not have dependents

### Outer Joins
 - LEFT OUTER JOIN (⟕)
	 - R ⟕ _Cond_ S
	 - Similar to a theta join, but all tuples from R are listed
	 - The tuples of R that do not satisfy Cond, are padded with null values for the attributes in S
	 - Essentially list all of R, if they don't satisfy cond then populate them with null
 - RIGHT OUTER JOIN (⟖)
	 - R ⟖ _Cond_ S
	 - Similar to a theta join, but all tuples from S are listed
	 - The tuples of S that do not satisfy Cond, are padded with null values for the attributes in R
	 - Essentially list all of S, if they don't satisfy cond then populate them with null
 - Full OUTER JOIN (⟗)
	 - R ⟗ _Cond_ S
	 - Both LEFT and RIGHT outer joins
 - Examples at the bottom of this page

### Images
**Outer Join Example**
![[Outer_join_example.png]]