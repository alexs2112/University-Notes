### Conversion of ERD to RM
 1. Mapping of regular entity types
 2. Mapping of weak entity types
 3. Mapping of binary 1:1 relationships
 4. Mapping of binary 1:N relationships
 5. Mapping of binary N:N relationships
 6. Mapping of multivalued attributes
 7. Mapping of composite attributes
 8. Mapping of n-ary relationships

**1. Mapping of Regular Entity Types:**
 - Create a relation for the entity
 - Add the simple attributes in the relation
 - Choose one of the key attributes as Primary Key
 - If the chosen key is composite, the set of simple attributes that form it will be the primary key

**2. Mapping of Weak Entity Types:**
 - Create a relation for the entity
 - Add the simple attributes in the relation
 - Include the primary key of owner entity as a foreign key
	 - The primary key of a weak entity is the combination of the primary key of the owner and the partial key of the weak entity

**3. Mapping of Binary 1:1 Relationship**
 - Create a relation for the relationship if needed
 - Add the simple attributes in the relation if any
 - Three approaches:
 1. **Foreign Key Approach:** Choose one of the relations and include a foreign key in that relation (better to choose an entity with total participation)
 2. **Merged Relation:** merge two entity types and the relationship into a single relation (Appropriate when both participations are total)
 3. **Cross-reference:** Set up a third relation for the purpose of cross-referencing

**4. Mapping of Binary 1:N Relationship**
 - As above
 - Include primary key of 1-side as a foreign key of N-side

**5. Mapping of Binary N:N Relationship**
 - As above
 - Include the primary keys of both the participating entities in the relation. Their combination will form the primary key of the relation.

**6. Mapping of Multivalued Attributes**
 - Create a relation for the attribute
 - Add the primary key of the main entity as primary key of the relation
 - Add the name of the multivalued attribue
 - The primary key of the relation will be the combination of primary key coming from the main entity and the name of the multivalued attribute

**7. Mapping of Composite Attributes**
 - Create a relation for the attribute if needed
 - Add the primary key of the main entity as primary key of the relation
 - Add the attributes that makes it composite
 - The primary key of the relation will be the combination of primary key coming from the main entity and the attributes of the composite attribute

**8. Mapping of n-ary Relationships**
 - Create a relation for the relationship
 - Add the simple attributes in the relation if any
 - Include the primary keys of all the participating entities in the relation. Their combination will form the primary key of the relation
