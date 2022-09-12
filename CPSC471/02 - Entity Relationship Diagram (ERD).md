### Methodologies for Conceptual Design
 - Entity Relationship (ER) Diagrams
 - Enhanced Entity Relationship (EER) Diagrams
 - Design Tools in industry
 - UML (Unified Modeling Language) Class Diagrams

### Entity Relationship Diagram
 - Basic ER model is composed of entity types, attributes for those entities, and specifies relationships that can exist between entities.
 - Meant to represent entities in a database

### Steps:
 1. Identify the Entities
 2. Identify the Relationships
 3. Identify Attributes, Participations, and Cardinalities

### ER Notations
**Entity**
 - Thing that exists either physically or logically, represented in the database
 - Look for singular nouns.
 - Represented by a rectangle
	 - Weak entities are represented by a double rectangle

**Entity Set/Entity Collection**
 - Each entity type will have a collection of entities stored in the database
 - Each set is the current **state** of the entities of that type that are stored in the database

**Attributes**
 - Properties of entities
 - Each attribute has a data type associated with it (int, string, date, etc). Sometimes called a *Value Set*
 - Represented by ellipses (ovals)
 - Every ellipse represents one attribute and is directly connected to its entity
 - Underlined attributes are attributes that must be unique for that entity (Key Attribute)

**Types of Attributes**
 - Key Attribute (underlined text, require a unique value, an entity can have multiple keys)
 - Composite Attribute (other attributes assigned to it, can be broken down)
 - Multivalued Attribute (double ellipse, denoted in text as `{Colors}` or `{PreviousDegrees}`)
 - Derived Attribute (dotted ellipse)
 - These can stack, some Attributes can have multiple types
	 - Example of composite multivalued attribute: `{PreviousDegrees (College, Year, Degree, Field)}`

**Relationships**
 - Represented by diamond shaped boxes, between entities
 - All the entities participating in a relationship are connected to it by a line
 - Can be thought of as verbs, linking two or more nouns (entities)
	 - EMPLOYEE John Smith **works on** the ProductX Project
 - Relationships of the same type are grouped or typed into a *Relationship Type*
	 - The WORKS_ON relationship type in which EMPLOYEEs and PROJECTs participate
 - The degree of a relationship type is the number of participating entity types
 - Relationship Set: Current set of relationship instances represented in the database. The current *state* of a relationship type.

**Constraints on Relationships**
 - Ratio constraints on Relationship Types
 - Cardinality Ratio (specifies **maximum** participation)
	 - One to One (1:1)
	 - One to Many (1:N) or Many to One(N:1)
	 - Many to Many (M:N)
 - Existence Dependency Constraint (specifies **minimum** participation, aka *participation constraint*)
	 - Zero (optional participation, non existence-dependent)
	 - One or more (mandatory participation, existence-dependent)
 - If the constraints on a relationship are different, and the relationship is connected to the same entity, you can label the lines.
	 - This is called a **Recursive Relationship Type**
		 - Relationship type between the same participating entity type in *distinct roles*
		 - AKA *self-referencing relationship type*

**Participation Constraints**
 - Total Participation - Each entity is involved in the relationship. Represented by double lines.
	 - Example: Every *Employee* needs to *Work For* a *Department*
 - Partial Participation - Not all entities are involved. Represented by single lines.
	 - Example: Not every *Employee* needs to *Manage* a *Department*, but every *Department* needs to have an *Employee* to *Manage* it

**Summary of ER Notations**
![[Summary_of_ER_Notations.png]]

