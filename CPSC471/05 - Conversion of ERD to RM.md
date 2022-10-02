### Goals During Mapping
 - Preserve all information, including all attributes
 - Maintain the constraints to the extent possible
	 - Relational Model cannot preserve all constraints (max cardinality ratio such as 1:10)
 - Minimize unnecessary data redundancy
 - Minimize null values

### Conversion Algorithm of ERD to RM
 1. Mapping of regular entity types
 2. Mapping of weak entity types
 3. Mapping of binary 1:1 relationships
 4. Mapping of binary 1:N relationships
 5. Mapping of binary N:N relationships
 6. Mapping of multivalued attributes
 7. Mapping of composite attributes
 8. Mapping of n-ary relationships
 9. Mapping Specialization and Generalization*
 10. Mapping of Union Types (Categories)*
 * * for EERD only

**1. Mapping of Regular Entity Types:**
 - Create a relation for the entity
	 - Entity `E` becomes `Rel(E)`
 - Add the simple attributes in the relation
	 - Break composite attributes to simple counterparts
 - Choose one of the key attributes as Primary Key
 - If the chosen key is composite, the set of simple attributes that form it will be the primary key

**2. Mapping of Weak Entity Types:**
 - Create a relation for the entity
 - Add the simple attributes in the relation
 - Include the primary key of all owner entities as a foreign key
	 - The primary key of a weak entity is the combination of the primary key of the owner and the partial key of the weak entity

**3. Mapping of Binary 1:1 Relationship**
 - Three approaches:
 1. **Foreign Key Approach:** Choose one of the relations with total participation and include a foreign key of the other relation. This relationship **will not** form a relation
	 - Also need to include the simple attributes of the relation to the relation you chose
 2. **Merged Relation:** merge two entity types and the relationship into a single relation (Appropriate when both participations are total)
 3. **Cross-reference:** Set up a third relation for the purpose of cross-referencing. Add the primary key of both entities, the primary key of this relation is the pair of primary keys

**4. Mapping of Binary 1:N Relationship**
 - Include primary key of the 1-side as a foreign key of the N-side

**5. Mapping of Binary M:N Relationship**
 - Create a new relation (`Rel(R)`), this is a relationship relation
 - Include the primary keys of both the participating entities in the relation. Their combination will form the primary key of the relation.

**6. Mapping of Multivalued Attributes**
 - Create a relation for the attribute
 - Add the primary key of the main entity as primary key of the relation
 - Add the value of the multivalued attribute
 - The primary key of the relation will be the combination of primary key coming from the main entity and the value of the multivalued attribute

**7. Mapping of Composite Attributes**
 - Not necessary if you break it up into simple attributes in step 1
 - Create a relation for the attribute if needed
 - Add the primary key of the main entity as primary key of the relation
 - Add the attributes that makes it composite
 - The primary key of the relation will be the combination of primary key coming from the main entity and the attributes of the composite attribute

**8. Mapping of n-ary Relationships**
 - Create a relation for the relationship
 - Add the simple attributes in the relation if any
 - Include the primary keys of all the participating entities in the relation. Their combination will form the primary key of the relation

**9. Mapping Specializations and Generalizations**
 - Option 1. Multiple relations - Superclass and subclasses
 - Option 2. Multiple relations - Subclasses only
 - Option 3. Single relation with one type attribute
 - Option 4. Single relation with multiple type attributes
 - **Handling multiple inheritance**:
	 - A shared subclass indicating multiple inheritence
	 - These classes must have all the same key attributes (otherwise it would be modeled as a category)

**10. Mapping of Union Types (Categories)**
 - Add primary key of superclass into the subclass/category
 - Add attributes of subclasses considering them as Entity
 - For mapping a category whose defining superclasses have different keys, it is customary to specify a new key attribute, called a *surrogate key*, when creating a relation to correspond to the category
