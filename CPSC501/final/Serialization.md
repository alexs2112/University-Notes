### XML
 - XML uses pairs of tags to create an *element*
	 - Start tag: `<tag-name>`
	 - End tag: `</tag-name>`
	 - *Content* goes between the tags
	 - *Child elements* can be nested inside an element
 - An *empty element tag* has the form `<tag-name />` (equivalent to `<tag-name></tag-name>`)
 - A start tag may also contain name-value pairs called attributes
	 - Form: `<tag-name attribute-name="attribute-value">`
	 - Can contain many pairs separated by spaces: `<zoo location="Paris" rank="12">`
 - A file or stream of well-formed XML is called a *document* that must contain one *root element*

### Reflective Serialization
 - A reflective serializer should serialize any type of object passed in as a parameter

**Basic design:**
 - Give the object a unique identifier number
	 - Could be done with `java.util.IdentityHashMap`
 - Get a list of all the object's fields
	 - Of all visibilities
		 - Use `getDeclaredFields()` and traverse the inheritance hierarchy
	 - Filter out static fields
 - Uniquely identify each field with its:
	 - Declaring class
	 - Field name
 - Get the value for each field
	 - If a primitive, simply store it so it can be easily retrieved later
	 - If a non-array object, recursively serialize the object
		 - Use the new object's unique id number as a reference
		 - Store the reference as the field value in the originating object
		 - Don't serialize an object more than once
			 - Occurs when you have several references to the same object
	 - If an array object, serialize it
		 - Then serialize each element of the array
			 - Use recursion if the element is an object

### Dynamic Loading
 - An ordinary class can be loaded at runtime using `public static Class forName(String className)`
 - Throws `ClassNotFoundException` if the corresponding `.class` file is not found on the classpath

**Arrays**:
 - Array classes do not have a `.class` file. No normal class name (are generated as needed by the JVM)
 - Array classes are named using codes:

|Encoding|Element Type|
|---|---|
|B|byte|
|C|char|
|D|double|
|F|float|
|I|int|
|J|long|
|L`<type>`|reference type|
|S|short|
|Z|boolean|
 - For each dimension of the array, use a `[`, then their element type code
	 - 1D int array: `[I`
	 - 2D float array: `[[F`
	 - 1D array of objects: `[Ljava.lang.String`
 - Array classes can be loaded using `forName()`
	 - Eg. array of String objects:
	   `Class classObject = Class forName("[Ljava.lang.String");`

### Reflective Deserialization
**Basic design:**
 - Get a list of objects, stored in the XML document
	 - Use `getRootElement()` from the `Document` class, and `getChildren()` from `Element` class
 - For each object, create an uninitialized instance
	 - Dynamically load its class using `forName()`
		 - The class name is an attribute of the *object* element
 - Create an instance of the class
	 - If a non-array object get the declared no-arg constructor, then use `newInstance()`
		 - May need to `setAccessible(true)`
	 - If an array object, use `Array.newInstance(...)`
		 - Use `getComponentType()` to find element type
		 - The length is an attribute of the *object* element
 - Associate the new instance with the object's unique identifier number using a table
	 - `java.util.HashMap` is ideal
		 - The id is the key
		 - The object reference is the value
	 - The id is an attribute of the *object* element
 - Assign values to all instance variables in each non-array object:
	 - Get a list of the child elements
		 - Use `getChildren()` from `Element` class
		 - Each child is a field of the object
	 - Iterate through each field in the list
		 - Find the name of its declaring class
			 - Is an attribute of the *field* element
		 - Load the class dynamically
		 - Find the field name
			 - Is an attribute of *field* element
		 - Use `getDeclaredField()` to find `Field` metaobject
		 - Initialize the value of the field using `set()`
			 - If a primitive type, use the stored value
				 - Use `getText()` and create appropriate wrapper object
			 - If a reference, use the unique identifier to find the corresponding instance in the table
			 - May need to `setAccessible(true)`
	 - Array objects are treated specially:
		 - Find the element type with `getComponentType()`
		 - Iterate through each element of the array
			 - Set the element's value using `Array.set()`
			 - As above, treat primitives differently than references
