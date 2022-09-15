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

### Entity Relationship Diagram
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

**Weak Entity Types**
 - An entity that doesn't have a key attribute and that is identification-dependent on another entity type
 - A weak entity must participate in an identifying relationship type with an owner or identifying entity type
 - Entities are identified by the combination of:
	 - A partial key of the weak entity type (key attribute, with dotted line under the label)
	 - The particular entity they are related to in the identifying relationship type
	 - Essentially a combination of the partial key with the full key of the related entity

**Attributes of Relationship Types**
 - A property of the relationship itself, it requires all contributing entities of the relationship to exist.
 - Most relationship attributes are used with M:N relationships
	 - In 1:N relationships, they can be transferred to the entity type on the N-side of the relationship

**N-Ary Relationships (N>2)**
 - In general, 3 binary relationships can represent different information than a single ternary relationship
 - If needed, the binary and n-ary relationships can all be included in the schema design
 - In some cases, a ternary relationship can be represented as a weak entity if the data model allows a weak entity type to have multiple identifying relationships

**ER Diagram Example**
![[ER_Diagram_from_Lecture.png]]

**Summary of ER Notations**
![[Summary_of_ER_Notations.png]]

**The (Min, Max) Notation for Relationship Constraints)**
 - Read the (min, max) numbers next to the entity type and looking *away from* the entity type.
 - Not super common, at the bottom of this document
 - In our standard notation, the bottom part of this would look like:
	 `EMPLOYEE --N-- WORKS FOR --1-- DEPARTMENT`
 - No longer need the single and double lines as that info is captured here
![[Min_Max_Notation.png]]
![[ERD_Using_Min_Max.png]]
