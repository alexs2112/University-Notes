### Extended Entity Relationship Diagram
 - EERD is a high level data model that incorporates extensions to the original ER model
 - In addition to ERD concepts, EERD includes
	 - Superclasses and Subclasses
	 - Specializations and Generalizations
	 - Categories and Unions
 - Specialization: A subclass is a special case of a superclass (top down)
 - Generalization: A superclass is a general class of a subclass (bottom up)
 - Is a matter of perspective
 - Subclasses inherit all attributes of a superclass

### Constraints on Specialization and Generalization
**Membership Constraints**
 - Predicate-Defined: based on some predicate to determine if an entity is part of a subclass
	 - Example: Job_type = "Engineer"
 - Attribute-Defined: Predicate defined when all subclasses have their membership condition on the same attribute
 - User-Defined: No condition is specified
**Disjoint Constraints**
 - Disjoint:
	- Entities of subclasses of the same superclass are mutually exclusive
	- Indicated by a circled `d` in the EERD
 - Overlapping
	 - Entities can overlap (allowed, not required)
	 - Indicated by a circled `o` in the EERD
**Completeness Constraint**
 - Total: Specifies that every entity in the superclass must be a member of some subclass in the specialization/generalization
	 - Shown in EERD by a double line
 - Partial: Allows an entity not to belong in any subclasses
	 - Shown in EERD by a single line

### Category and Union
 - Category represents a single super class or sub class relationship with more than one superclass
 - It can be a total or partial participation

### Aggregation
 - A process that represents a relationship between a whole object and its component parts
 - Abstracts a relationship between multiple relationships

### Steps to Draw EERD
1. Identify the Entities
2. Identify the Relationships among the entities
	- Superclass-Subclass
	- Category or Union (disjoint or overlap)
	- Aggregation
	- Binary or n-ary relationships
	- Attributes of relationships
3. Cardinalities, Participations, and Attributes

