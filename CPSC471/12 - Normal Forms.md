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
 - Definition: Given a set of FDs F, for a set of attributes X, X+ is the set of attributes that are functionally determined  by X based on F
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
 - Opposite DirectionL See if we could reduce the set F to its minimal form so that the minimal set is still equivalent to the original set F
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