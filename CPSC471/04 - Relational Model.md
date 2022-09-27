### Relational Model (RM)
 - Based on the concept of a **Relation**: Formal foundation provided by a theory of relations
 - Represents the database as a collection of relations
	 - Relation: Table of values
 - Every row in the table represents a collection of related data values
 - These rows in the table denote a real-world entity or relationship
	 - Filled rows are called Tuples
 - Derived attributes are ignored in the RM
 - A mathematical Relation R from set A to set B: R is a subset of A x B

### Schema
 - Description of a Relation, essentially the header field of the table
 - Denoted by R(A1, A2, A3, ..., An)
 - R is the name of the relation
 - The attributes are A1, A2, A3, ..., An
 - Each attribute has a domain, a set of valid values
	 - Domains have a data type and a logical definition

### Tuple
 - An ordered collection of values, enclosed in angled brackets
 - Each value is derived from an appropriate domain
 - A relation is a set of such tuples (rows)
-

### Informal to Formal:
 - Table -> Relation
 - Column Header -> Attribute
 - All possible Column values -> Domain
 - Row -> Tuple
 - Table Definition -> Schema of a relation
 - Populated Table -> State of the relation

### Characteristics of Relations
  - Tuples are not considered to be ordered in the relation, despite appearing in tabular form
  - Ordering of attributes in a relation schema R (and of values within each tuple) are ordered
  - However a more general, self-describing definition does not require this ordering. (including both the name and value for each attribute)
	  - `t = {<name, "John Smith">, <office-phone, 444-444-4444>, <age, 22>}`
  - Values in a tuple are considered atomic (indivisible)
	  - Each value in a tuple must be from the domain of the attribute for that column
	  - Or a special `null` value
  - We refer to *component values* of a tuple t by:
	  - `t[Ai]` or `t.Ai`

### Relational Database Schema
 - A set `S` of relation schemas that belong to the same database
 - `S` is the name of the whole *database schema*
 - `S = {R1, R2, ..., Rn}` and a set IC of integrity constraints

### Relational Database State
 - `DB` of `S` is a state of relation states
 - A relational database state is sometimes called a relational database snapshot or instance
	 - Instance will not be used as it also applies to single tuples
 - A database state that does not meet the constraints is an invalid state
 - Populated with data, whenever the database is changed a new state arises

### Constraints
 - Determine which values are permissible and which are not in the database
 - Three main types:
 - **Inherent or Implicit**: Based on the data model itself
 - **Schema-based or Explicit**: Expressed in the schema by using the facilities provided by the model (max cardinality ratio)
 - **Application-based or Semantic**: Beyond the expressive power of the model, must be specified and enforced by the application programs

### Relational Integrity Constraints
 - Constraints are conditions that must hold on all valid relation states
 - Three main types of explicit schema-based constraints that can be expressed in the RM
	 - Key constraints
	 - Entity integrity constraints
	 - Referential integrity constraints
 - Another schema-based constraint is the domain constraint
	 - Every value in a tuple must be from the domain of its attribute (possible including null)

### Key Constraints
 - **Superkey** or `R`:
	 - A set of attributes `SK` of `R` with the following condition:
		 - No two tuples in any valid relation state `r(R)` will have the same value for `SK`
		 - That is, for any distinct tuples `t1`, `t2`, in `r(R)`, `t1[SK] != t2[SK]`
		 - This condition must hold in any valid state `r(R)`
 - **Key** of `R`
	 - A "minimal" superkey
	 - A superkey such that the removal of any attribute from it results in a set of attributes that is not a superkey
 - A key is a superkey, but not vice versa
 - Any set of attributes that includes a key is a superkey
 - A minimal superkey is still a key
 - If a relation has several keys, we call them *candidate keys*
 - A *primary key (PK)* is an *arbitrarily chosen* candidate key
	 - The primary key attributes are underlined in the schema
 - The primary key value is used to uniquely identify each tuple in a relation (provides the tuple identity)
 - Also used to reference the tuple from another tuple
	 - General rule: choose as primary key the smallest of the candidate keys (in terms of size)
	 - Not always applicable, choice is sometimes subjective

### Entity Integrity
 - The primary key attributes PK of each relation schema R in S cannot have null values in any tuple of r(R)
	 - This is because primary key values are used to identify the individual tuples
	 - `t[PK] != null` for any tuple `t in r(R)`
	 - if PK has several attributes, null is not allowed in any of them

### Referential Integrity Constraints
 - A constraint involving two relations
 - Used to specify a relationship among tuples in two relations
	 - The **referencing relation** and the **referenced relation**
	 - The referencing arrows drawn between attributes for different relations
![[Referential_Integrity.png]]

### Update Operations on Relations
 - `INSERT` a tuple
 - `DELETE` a tuple
 - `MODIFY` a tuple
 - Integrity constraints should not be violated by the update operations
 - Several update operations may have to be grouped together
 - Updates may propagate to cause other updates automatically. This may be necessary to maintain integrity constraints
 - In case of integrity violation, several actions can be taken
	 - Cancel the operation: `REJECT` or `RESTRICT`
	 - Perform, but notify the user of the violation
	 - Trigger additional updates so the violation is corrected: `CASCADE`, `SET NULL`
	 - Execute a user-specified error-correction routine