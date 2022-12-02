### Functional Dependencies
 - Used to specify formal measures of the "goodness" of relational designs
 - A set of attributes X functionally determines a set of attributes Y if the value of X determines a unique value for Y
	 - Y functionally depends on X
 - Examples:
	 - Social Security Number determines Employee Name
		 - SSN -> {LNAME, FNAME}
	 - Project Number determines Project Name and Location
		 - PNUMBER -> {PNAME, PLOCATION}
	 - Employee SSN and Project Number determines the hours per week that the employee works on the project
		 - {SSN, PNUMBER} -> HOURS
 - Formal Definition
	 - Let X and Y be sets of attributes of a relation schema R
	 - X -> R if for any two tuples t1 and t2 in any relation instance r(R), t1[X] = t2[X] => t1[Y] = t2[Y]
	 - X -> Y in R specifies a constraint on all relation instances r(R)

### FD on Keys
 - If K is a key of R, then K functionally determines any combination of all attributes in R
	 - Since we never have two distinct tuples with t1[K] = t2[K]

### Defining FDs From Instances
 - To define the FDs, we need to understand the meaning of the attributes involved and the relationship between them
 - A FD is a property of the attributes in the schema R
 - Only looking at some r(R) of a relation, all we can conclude is that some FD may exist
 - What we can definitely conclude is that certain FDs do not exist when there are tuples that show a violation of those dependencies

### Inference Rules for FDs
 - A DB designer specifies a set F of FDs
 - Other FDs can be deduced from F
	 - We want the basic set of FDs to be as small as possible
 - Definition: An x -> y is inferred from or implied by a set of dependencies F specified on R if x -> y holds in every legal relation state r of R; that is, whenever r satisfies all the dependencies in F, x->y also holds in r

### FD Closure
 - Let F be a set of FDs for a given relation schema
 - The closure of F, denoted F* (+ instead of * ), is the set of all FDs in F in addition to all FDs that can be inferred from F
 - F* is calculated using a set of inference rules/axioms

### Armstrong Inference Rules
 - IR1. Reflexive: If Y ⊆ X, then X -> Y
 - IR2. Augmentation: If X -> Y then XZ -> YZ
	 - XZ stands for X union Z
 - IR3. Transitive: If X -> Y and Y -> Z then X -> Z
 - IR1, IR2, IR3 form a sound and complete set of inference rules
	 - These rules hold and all other rules that hold can be deduced from these
 - IR4. Decomposition: If X -> YZ, then X -> Y and X -> Z
 - IR5. Union: If X -> Y and X -> Z then X -> YZ
 - IR6. Psuedo-Transitive: If X -> Y and WY -> Z then WX -> Z
 - All can be deduced from IR1, IR2, IR3 (completeness)

### Attribute Closure
 - To compute F*, we first need to find all attributes X that appear on the left hand-side of each FD in F, then find all the attributes that functionally depend on X, X*
 - Definition: Given a set of FDs F, for a set of attributes X, X+ is the set of attributes that are functionally determined by X based on F
	- X* is called the closure of X under F
 - X* can be calculated by  repeatedly applying IR1 - IR3 using F

### Algorithm to Determine Closure
 - Algorithm: Determining X*
 - Input: A set F of FDs on a relation schema R, and a set of attributes X, X ⊆ R
```
X* <- X
repeat
	for each Y -> Z in F do
		if Y ⊆ X* then X* <- X* union Z
```

### Equivalence of Sets of FDs
 - Definition: Given two sets of FDs on a relation schema R
	 - F covers G if G* ⊆ F*
	 - Every FD in G can be inferred from F
 - To determine if F coers G
	 1. For each X -> Y in G, calculate X* under F
	 2. Check if Y ⊆ X*
	 - F covers G if 2. is correct for each X -> Y in G
 - Example:
 - `F = {A -> C, AC -> D, E -> AD, E -> H}` and `G = {A -> CD, E -> AH}`
 - A* (under F for A -> CD) = {A, C, D}
 - E* (under F for E -> AH) = {E, A, D, H}
 - F covers G
	 - Can show that F = G by showing that G also covers F

### Minimal Covers of FDs
 - Opposite Direction: See if we could reduce the set F to its minimal form so that the minimal set is still equivalent to the original set F
 - An attribute in a functional dependency is considered extraneous attribute if we can remove it without changing the closure of the set of dependencies
 - Definition: Given F, a set of FDs, and a FD X -> A in F, attribute Y is extraneous in X if Y subset X, and F logically implies (`F - {X -> A} union { (X - {Y}) -> A}`)
	 - Removing X -> A but keeping (X - {Y}) -> A does not change the closure of F

### Minimal Sets of FDs
 - Must satisfy the following conditions
 1. Every dependency in F has a single attribute for its RHS (canonical form)
	 - Use IR4 (Decomposition)
 2. We cannot remove any dependency from F and have a set of dependencies that is equivalent to F
	 - No FDs that can be inferred from the rest in F
 3. We cannot replace any dependency X -> A in F with a dependency Y -> A, where Y subset X and still have a set of dependencies that is equivalent to F
	 - No extraneous attributes in LHS

### Minimal Cover
 - Definition: A minimal cover of a set of FDs F is a minimal set of dependencies that is equivalent to F
 - We can always find at least one minimal cover for any set of dependencies
 - Algorithm:
	 - Input: A set of functional dependencies E
```
1. F <- E
2. Convert F to canonical form
3. Remove extraneous attributes from F
4. Remove reduntant FDs from F
```
 - Examples to this are in pdf slide 35 on d2l

### Minimal Sets of FDs Facts
 - Every set of FDs has an equivalent minimal set
 - There can be several equivalent minimal sets
 - There is no simple algorithm for computing a minimal set of FDs that is equivalent to a set F of FDs
	 - The process of Algorithm MinSet is used until no further reduction is possible
 - To synthesize a set of relations, we will assume that we start with a set of dependencies that is a minimal set

### Calculating a Key for a Relation
 - Superkey of R:
	 - A set of attributes SK of R with the following condition
		 - No two tuples in any valid relation state r(R) will have the same value for SK  
		 - That is, for any distinct tuples t1 and t2 in r(R), t1[SK] ≠ t2[SK]  
		 - This condition must hold in any valid state r(R)
 - Key of R:  
	 - A "minimal" superkey  
	 - That is, a key is a superkey K such that removal of any attribute from K results in a set of attributes that is not a superkey
 - Algorithm:
```
Input: R and F = FDs on the attributes of R  
	K <- R
	for each attribute A in K do  
		compute (K – A)+ under F
		if (K – A)+ = R then
			K <- K – {A}
```
 - Example given (slide 43)

### Candidate Keys
 - If a relation schema has more than one key, each is called a candidate key.
 - One of the candidate keys is arbitrarily designated to be the primary key, and the others are called secondary keys.

### Prime and Nonprime Attributes
 - A prime attribute is a member of some candidate key
 - A nonprime attribute is not a prime attribute - that is, it is not a member of every candidate key

### Normalization of Relations
 - **Normalization:**
	 - The process of decomposing unsatisfactory “bad” relations by breaking up their attributes into smaller relations making a “good” design
 - **Normal Form**:
	 - Condition using keys and FDs of a relation to certify whether a relation schema is in a particular normal form

### Normal Forms Based on Keys
 - 1st normal form (1NF)
	 - All attributes depend on the key
 - 2nd normal form (2NF)
	 - All attributes depend on the whole key
 - 3rd normal form (3NF)
	 - All attributes depend on nothing but the key
 - BCNF
	 - All key attributes must define every other attribute
	 - For every non-trivial FD for R, X -> A, X is a superkey for R

# First Normal Form
 - Disallows
	 - Composite attributes
	 - Multivalued attributes
	 - Nested relations: attributes whose values for an individual tuple are non-atomic
 - Tend to end up with redundancy
 - Considered to be part of the definition of a relation
 - Most RDBMSs allow only those relations to be defined that are in 1NF

# Second Normal Form
### Full FD
 - Full functional dependency: a FD Y -> Z where removal of any attribute from Y means the FD does not hold any more
 - Examples:
	 - {SSN, PNUMBER} -> HOURS is a full FD
		 - Neither SSN -> HOURS nor PNUMBER -> HOURS holds
	 - {SSN, PNUMBER} -> ENAME is not a full FD
		 - Since SSN -> ENAME also holds

### Partial FD
 - Partial functional dependency: a FD Y -> Z where removal of some attribute from Y and the FD still holds.
 - Example:  
	 - {SSN, Lname} -> Fname is a partial FD 
	 - Since SSN -> Fname holds

### General Definition for 2NF
 - A relation schema R is in second normal form (2NF) if *every* non-prime attribute A in R is *fully functionally dependent* on *every* key of R.
	 - It is sufficient to find one violation to prove it is not 2NFS

### Decomposition (Normalization to 2NF)
 - Given a relation schema R and a set of FDs F on the attributes of R
 - When R is not in 2NF, it can be decomposed into subset relation schemas `D = {R1, R2, ..., Rm}`
	 - The smaller relation schemas Ri will be in 2NF
	 - F is preserved in the Decomposition
 - For each FD X -> Y that violates 2NF in R
	 - Create a new sub relation schema S with attributes X U Y and X is the primary key for S
	 - Remove attributes Y from R

# Third Normal Form
### Transitive FD
 - A FD X -> Y in a relation schema R is transitive if  
	 - There exists a set of attributes Z in R that is neither a candidate key nor a subset of any key of R, and
	 - both X -> Z and Z -> Y hold.
	 - Basically there is a nonprime that defines a nonprime

### General Definition for 3NF
 - A relation schema R is in 3NF if every non-prime attribute of R:
	 - Is fully functionally dependent on every key of R (2NF), and
	 - Is non-transitively dependent on every key of R
 - Alternative general definition (functionally equivalent):
	 - Whenever a FD X -> A holds in R, then either:
		 - X is a superkey of R, or
		 - A is a prime attribute of R
	- So X is not a superkey and A is nonprime
	- This can occur due to two types of problematic functional dependencies:
		- A nonprime attribute determines another nonprime attribute (transitive dependency violates 3NF)
		- A proper subset of a key of R functionally determines a nonprime attribute (partial dependency, violates 3NF and 2NF)

### Decomposition (Normalization to 3NF)
 - Given a relation schema R and a set of FDs F on the attributes of R
 - When R is not in 3NF, it can be decomposed into subset relation schemas `D = {R1, R2, ..., Rm}`
	 - The smaller relation schemas Ri will be in 3NF
	 - F is preserved in the decomposition
 - For each FD X -> Y that violates 3NF in R
	- Create a new sub relation schema S with attributes X U Y and X is the primary key for S
	 - Remove attributes Y from R

# Boyce-Codd Normal Form (BCNF)
 - A relation schema R is in BCNF if whenever an FD X -> A holds in R, then X is a superkey of R
 - Each normal form is strictly stronger than the previous one
	 - Every 2NF relation is in 1NF
	 - Every 3NF relation is in 2NF
	 - Every BC
 - In practice, most relations in 3NF are also in BCNF

### Decomposition (Normalization to BCNF)
 - Given a relation schema R and a set of FDs F on the attributes of R
 - When R is not in BCNF, it can be decomposed into subset relation schemas `D = {R1, R2, ..., Rm}`
	 - The smaller relation schemas Ri will be in BCNF
	 - F is preserved in the decomposition
 - For each FD X -> Y That violates BCNF in R
	 - Create a new sub-relation schema S with attributes  X union Y and X is the primary key for S
	 - Remove attributes Y from R

# Lossless Join (Additive Join)
 - Note: The word loss refers to loss of information, not to loss of tuples
 - A better term is "addition of spurious information"

### Projection of FDs
 - Definition: Given a set of FDs F on relation schema R, with Ri (subset eq) R, the projection of F on Ri, denoted PI_Ri(F), is the set of dependencies X -> Y in F+ such that attributes in X union Y are all contained in Ri

### Testing for Lossless Join Property
 - Input: A universal relation R, a decomposition D of R,  and a set F of FDs
1. Create an initial matrix S with one row i for each relation Ri in D, one column j for each attribute Aj in R
2. Set S(i,j) <- bij for all matrix entries [each bij is a distinct symbol associated with indices (i,j)]
3. For each for i representing relation schema Ri do
	 - for each column j representing attribute Aj do
		 - If (relation Ri include attribute Aj) then set S(i,j) <- aj [each aj is a distinct symbol associated with index j]
4. Repeat:
	 - For each FD X -> Y in F do
		 - for all rows in S which have the same symbols in the columns corresponding to attributes in X do
			 - make the symbols in each column that corresponds to an attribute in Y be the same in all these rows as follows:
			 - if any of the rows has an "a" symbol for the column, then set the other rows to that same "a" symbol in the column
			 - if no "a" symbol exists for the attribute in any of the rows, then choose one of the "b" symbols that appear in one of the rows for the attribute and set the other rows to that same "b" symbol in the column
 - Until a complete loop execution results in no changes to S
 - If a row is made up entirely of "a" symbols then the decomposition has the lossless join property, otherwise it does not.

### Checking Non-Additivity of Binary Relational Decompositions
 - Binary Decomposition: Decomposition of a relation R into two relations
 - NJB (Non-additive join test for binary decompositions): A decomposition D = {R1, R2} of R has the lossless join property with respect to a set of FDs F on R if and only if either of the following FDs is in F+:
	 - (R1 intersection R2) -> (R1 - R2)
	 - (R1 intersection R2) -> (R2 - R1)

### Successive Non-additive Join Decomposition
 -  If a decomposition D = {R1, ..., Rm} of R has the lossless join property
 - And if a decomposition D1 = {Q1, ..., Qk} of Ri has the lossless join peroperty
 - Then the decomposition
	 - D' = {R1, ..., Ri-1, Q1, ..., Qk, Ri+1, ..., Rm}
 - also has the lossless join property

### Bottom-up Design
 - Procedure:
	 - A universal relation schema R = {a1, a2, ..., an} includes all the attributes of the database
	 - Given a universal relation schema R and a set of FDs F
	 1. Find a minimal cover for F
	 2. Decompose R until all relation schemas are in 3NF or BCNF

### Decomposition Goals
 - A universal relation schema R = {a1, a2, ..., an} with a set of FDs F can be decomposed into a set of smaller relation schemas D = {R1, R2, ..., Rm}
 - Decomposition goals:
1. Attribute preservation
	-  Each ai will appear in at least one relation schema Ri in D
2. Each individual relation Ri in D must be in BCNF or 3NF
3. FD F is preserved as much as possible
4. Lossless (non-additive) join

### Decomposition into 3NF
 - Input: A universal relation R and a set of FDs F on the attributes of R
1. Find a minimal cover G for F
2. For each X, where X -> Y is in G, create a relation schema S with attributes X union {a1, a2, ..., ak}, where X -> a1, ..., X -> ak are the only FDs with X on the LHS in G (X is the key of S)
3. If none of the relation schemas in D contains a key of R, then create one or more relation schema in D that contains attributes that form a key of R
4. Eliminate redundant relations, if any

### Decomposition into BCNF
 - Input: A universal relation R and a set of FDs F on the attributes of R
1. D <- {R}
2. While there is a relation schema Q in D that is not in BCNF do
	 - Find FD X -> Y that violates BCNF in Q
	 - Decompose Q into (Q - Y) and (X union Y)
 - Assumption: No null values are allowed for the join attributes.