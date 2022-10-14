### Basics of RA
 - A basic set of operations for the relational model, enables a user to specify *queries*
 - Procedural query language, takes instances of relations as input and yields instances of new relations as output. Uses operators to perform queries
	 - This property of creating new relations makes the algebra "closed", the result is always a relation
 - **Types**
	 - **Unary Relational Operations**
		 - SELECT (σ)
		 - PROJECT (π)
		 - RENAME (ρ)
	 - **Operations from Set Theory**
		 - UNION (∪)
		 - INTERSECTION (∩)
		 - DIFFERENCE (-)
		 - CARTESIAN PRODUCT (x)
	 - **Binary Relational Operations**
		 - JOIN (several versions exist)
		 - DIVISION
 - Additional relational operations:
	 - OUTER JOINS, OUTER UNION
	 - AGGREGATE FUNCTIONS
		 - SUM, COUNT, AVG, MIN, MAX

*Note: The _italicized_ is subscript*
### SELECT (σ)
 - Selects a *subset* of the tuples from a relation based on a *selection condition*.
 - σ _condition_ (R)
 - Examples:
	 - Select the EMPLOYEE tuples whos department number is 4:
		 - σ _DNO=4_ (EMPLOYEE)
	 - Select the employees whose salary is greater than $30000:
		 - σ _salary>30000_ (EMPLOYEE)
	 - σ _(DNO=4 and Salary>25000) or (DNO=5 and Salary > 30000)_ (EMPLOYEE)
 - Properties:
	 - The SELECT operation on R produces a relation S with the same schema as R
	 - SELECT is commutative
	 - A cascade of SELECT operations may be replaced by a single selection with a conjunction of all the conditions
		 - σ _cond1_ (σ _cond2_ ) (R) = σ _cond1 AND cond2_ (R)

### Project (π)
 - Projects a relation to a subset of attributes
 - π _attribute list_ (R)
 - Results in a relation with only the columns of the requested attributes
 - Properties:
	 - Removes any duplicate tuples in the result (possible when a key attribute is not requested)
	 - Number of tuples in the result of projection is always less than or equal to the number of tuples in R
	 - If the list of attributes includes a *key* of R, then the number of tuples in the result is *equal* to the number of tuples in R
	 - PROJECT is not commutative

### RENAME (ρ)
 - ρ _S_ (R)
	 - Renames R to S
 - ρ _(B1, B2, ..., BN)_ (R)
	 - Renames R's attributes to (B1, B2, ..., BN)
 -  ρ _S(B1, B2, ..., BN)_ (R)
	 - Both of the above

### RA Expressions
 - Applying several relational algebra operations in a row
	 - A single relational algebra expression by nesting the operations, or
	 - Apply one operation at a time and create *intermediate result relations*
 - In the latter case, we must give names to the relations that hold the intermediate results
 - Example:
	 - Nested operations:
		 - π _Fname, Lname, Salary_ (σ _DNO=5_ (EMPLOYEE))
	 - Sequence of operations:
		 - DEP5_EMPS <- σ _DNO=5_ (EMPLOYEE)
		 - RESULT <- π _Fname, Lname, Salary_ (DEP5_EMPS)

### Set Operations:
 - R ∪ S = all tuples in R or in S
	 - Duplicates are eliminated
 - R ∩ S = all tuples n R and in S
	 - Common elements
 - R - S = all tuples in R that are not in S
 - Both R and S must be *type compatible*
	 - Same  number of attributes
	 - R.ti and S.ti are type compatible

### Properties of UNION, INTERSECT, and DIFFERENCE
 - Both union and intersection are commutative
	 - R ∩ S = S ∩ R
 - Both union and intersection can be treated as n-ary operations applicable to any number of relations as both are associative operations
	 - R ∪ (S ∪ T) = (R ∪ S) ∪ T
 - The minus operation is not commutative

### CARTESIAN PRODUCT
 - Multiply each tuple in R1 with each tuple in R2
 - Example at the bottom of this page
 - Properties:
	 - R(A1, A2, ..., An) x S(B1, B2, ..., Bm) results in:
	 - Q(A1, A2, ..., An, B1, B2, ..., Bm)
		 - Relation state has one tuple for each combination of tuples, one from R and one from S
	 - The two operands do NOT have to be type compatible
	 - If |R| = r and |S| = s, then |Q| = r x s

### Binary Relational Operations: JOIN (⨝)
 - Combines a CARTESIAN PRODUCT and a SELECT
 - R ⨝ _condition_ S
 - Is the same as: σ _condition_ (R x S)
 - **Example:** Retrieve the name of the manager of each department
	 - Combine each DEPARTMENT tuple with the EMPLOYEE tuple whose SSN value matches the MGR_SSN value in the department tuple
	 - DEPT_MGR <- DEPARTMENT ⨝ _MGR_SSN=SSN_ EMPLOYEE
	 - MGR_SSN = SSN is the join condition
		 - Combines each department record with the employee who manages the department
 - Properties:
	 - R(A1, A2, ..., An) ⨝ _cond_ S(B1, B2, ..., Bm) results in
	 - Q(A1, A2, ..., An, B1, B2, ..., Bm)
		 - Relation state has one tuple for each combination of tuples: r from R and s from S that satisfy Cond
	 - The general case of a join is called a **Theta join**
	 - R ⨝ _theta_ S, where theta is any general boolean expression
	 - In practice, most join conditions equate two or more attributes

### Binary Relational Operations: EQUIJOIN
 - The most common use of join involves join conditions with *equality comparisons (=)* only

![[Operations_of_RA.png]]

**Cartesian Product:**
![[Cartesian_Product.png]]