### Reflective Serialization
 - *Serialization* is the process of converting an object into a stream of bytes
	 - Format can be binary or human-readable (text)
	 - The byte stream may be:
		 - Stored to a file or database
			 - Enables *object persistence*
		 - Transmitted to another program
			 - For *remote method invocation* (RMI)
		 - Transmitted across a network
			 - For *distributed objects*
 - *Deserialization* converts the byte stream into a recreation of the original object (its clone)
 - When you serialize an object you are saving its *state*
	 - ie. the current value of all its instance variables
 - To build a general-purpose serialization system, you need access to an objects metadata
	 - Requires reflection
 - Java has a Serializable marker interface
	 - If implemented by a class, its instances can be serialized automatically to a binary stream
 - A custom, general purpose serializer that serializes to a text stream has several advantages
	 - The stream is easily read or modified with a text editor
	 - Can send objects to a non-Java platform
	 - Can be applied to third-party classes that don't implement Serializable

### XML
 - XML (eXtensible Markup Language) is an ideal format for the text stream
	 - Is self-describing
	 - Encodes structured, hierarchical data
	 - Is well-supported with facilities that do parsing, presentation, etc
		 - eg. DOM (Documented Object Model), JDOM, SAX
 - XML uses pairs of tags to create an *element*
	 - Start tag: `<tag-name>`
	 - End tag: `</tag-name>`
	 - *Content* goes between the tags
	 - *Child elements* can be nested inside an element
	 - Eg.
	```xml
	<zoo>
		<animal>Panda</animal>
		<animal>Giraffe</animal>
	</zoo>
	```
 - An *empty element tag* has the form `<tag-name />`
	 - Equivalent to `<tag-name></tag-name>`
 - A start tag may also contain name-value pairs called attributes
	 - Form:
	   `<tag-name attribute-name="attribute-value">`
	 - Can contain many pairs separated by spaces
	 - Eg. `<zoo location="Paris" rank="12">`
 - A file or stream of well-formed XML is called a *document*
 - Each document must contain one *root element*
	 - Contains all other content

### Reflective Serialization
 - Using reflection to do serialization offers several advantages:
	 - Does not require invasive changes to hundreds of classes
	 - Works with all in-house, third-party, and JDK classes
		 - And any classes created in the future
	 - Debugging and maintenance is centralized to the serialization code
 - The reflective serializer should serialize any type of object passed in as a parameter
 - Basic design:
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

