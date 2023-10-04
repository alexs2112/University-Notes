### Basic Concepts
 - Definition: *Reflection* is the ability of a running program to:
	 - Examine itself and the run-time environment (*Introspection*)
	 - Change its behaviour, structure, or data depending on what it finds
 - To do introspection, a program must have a representation of itself available at runtime
	 - Called *metadata*
	 - In an OO language, metadata is organized using *metaobjects*
		 - In Java, these are typically instances of classes like `Class.Method`, and `Field`
 - The normal, non-reflective part of a program is called the *base program*
	 - Consists of *base-level objects*
 - Each base-level object is an instance of some class
	 - This class is represented at the *metalevel* as a *class object* (an example of a metaobject)
 - The fields and methods for a class are represented with `Field` and `Method` metaobjects
	 - Are contained within the class object
 - Once introspection is done, you can change a program's structure, data, or behaviour
	 - Three general techniques:
		 - Direct metaobject modification
			 - Eg: Add methods or fields to an existing class
			 - Not possible in Java (avoids complications)
		 - Operations using metadata
			 - Eg: Dynamic method invocation, dynamic class loading, reflective construction
		 - *Intercession*
			 - Where code intercedes to modify its behavior as the program runs
			 - Typically involves intercepting method calls
			 - In Java, limited to dynamic proxies
 - Only a few languages support reflection
	 - Typically when run in an interpreter
	 - Eg: Java, Smalltalk, Python, Objective-C, Prolog, etc
 - Reflection allows you to build flexible, elegant, and easily maintained programs
	 - Can create programs that easily adapt to changing requirements (more modular)
		 - Eg. A pluggable framework that accepts new components after it is built and deployed
	 - Allows you to apply program-wide changes easily, without tedious hand-modification of code
		 - Adding logging or serialization to all classes of an existing program
		 - The program changes its own behaviour at runtime
			 - Not the programmer at compile time
	 - Can create useful utilities not easily done by other means:
		 - Object inspector
		 - Memory leak profiler
		 - Call stack inspector
 - Issues with Reflection:
	 - Since behaviour can be changed dynamically, security could be compromised
		 - Not a problem with Java due to the JVM
			 - Has a strong security model
			 - Limited intercession
	 - Reflective techniques are indirect, thus making code more complex
		 - Use reflection only where it makes sense
	 - Reflective method calls are slower than normal calls
		 - 20x improvement from Java 1.3 to 1.4

### Basic Mechanisms in Java
 - The reflection classes are in two packages:
	 - `java.lang`
		 - `Object`
		 - `Class`
	 - `java.lang.reflect`
		 - `Method`
		 - `Field`
		 - `Constructor`
		 - etc
 - `java.lang.Object`
	 - Is the root superclass of every object in a program
	 - Each base-level object keeps a reference to its class object
		 - Accessed with the method `public final Class getClass()`
		 - Eg. `Object myObj = new ..; Class classObj = myObj.getClass();`
 - `java.lang.Class`
	 - Is the class of metalevel class *objects*
	 - Has many useful reflective methods to:
		 - Create new instances
		 - Find methods, constructors, and fields of a class
		 - Traverse the inheritance hierarchy
 - Finding class objects
	 - For an already instantiated base-level object, use `getClass()`
	 - If you know the class name  at compile time, use the class literal `.class`
		 - `Class classObject = Color.class;`
	 - If the class name is represented as a String (usually at runtime) use the method:
		 - `public static Class forName(String className);`
		 - If not already loaded, dynamically loads the class from bytecode in the .class file
		 - If the class is in a named package, use the fully qualified name
			 - To work, the classpath must be set properly
		 - `String name = "java.io.File"; Class classObj = Class.forName(name);`
 - Java uses class objects (instances of Class) to represent the types of all entities:
	 - Ordinary objects
	 - Primitives (int, float, char, etc)
		 - Although primitives are not objects, Java uses class objects to represent their type
		 - Use a class literal to specify the class object
		 - `int.class, double.class`
		 - `void.class` represents the void return type
		 - To check if primitive, use `isPrimitive()` on the class object (`if (classObject.isPrimitive()) ...`)
	 - Arrays
		 - Java arrays are objects whose classes are created at runtime by the JVM
		 - A new class for each element type and dimension
		 - Use a class literal to specify the class object
			 - `int[].class.Object[].class`
		 - To check if an array, use `isArray()`
		 - To find the base type of an array, use `public Class getComponentType()`
	 - Interfaces
		 - Each declared interface is represented with a class object
		 - Can be specified with a class literal (`Collection.class`)
		 - Can be queried for supported methods and constants
		 - To check if an interface, use `isInterface()`
 - Methods for a class or interface are represented with metaobjects of the type `java.lang.reflect.Method`
 - Methods can be found at runtime by querying the class object
	 - To find a **public** method (either declared or inherited), use 
	   `Method getMethod(String name, Class[] paramTypes);`
	 - Eg: `Method m = classObject.getMethod("setColor", new Class[] { Color.class });`
	 - If no parameters, use `null` or zero-length array for the 2nd argument
 - Use `getDeclaredMethod()` to find a method explicitly declared by the class (not inherited)
	 - Returns methods of all visibilities (public, protected, package, private)
 - To find *all* public methods of a class (either declared or inherited) use: `Method[] getMethods()`
	 - To get all declared methods of any visibility: `Method[] getDeclaredMethods()`
 - A method object can be queried with:
	 - `String getName()`
	 - `Class getDeclaringClass()`
	 - `Class[] getExceptionTypes()`
	 - `Class[] getParameterTypes()`
	 - `Class getReturnType()`
	 - `int getModifiers()`
		 - The returned int can be decoded with methods in Modifier class
 - To call a method dynamically, use: `Object invoke(Object obj, Object[] args)`
	```java
	Object myObj = new ...;
	Class classObject = myObj.getClass();
	Color c = new ...;
	Method m = classObject.getMethod("setColor", new Class[] {Color.class});
	m.invoke(myObj, new Object[] {c});
	```
	- If there are no arguments, use null or zero length array for the second parameter
	- If a static method, use null for the 1st parameter
- Primitives are passed as parameters by putting them into a "wrapper object"
	```java
	int i = 10;
	Method m = classObject.getMethod("get", new Class[] {int.class});
	m.invoke(myObj, new Object[] {new Integer(i)});
	```
 - If a method normally returns a primitive, `invoke()` will return the primitive in a wrapper object
	 - Since typed as Object, you must cast it to the correct type
	 - Then unwrap it using an xxx Value() method
	 - Note: Java 5.0 introduced automatic boxing and unboxing
	```java
	int code;
	Method m = classObject.getMethod("hashCode", null);
	code = ((Integer)m.invoke(myObj, null)).intValue();
	```
 - To find the superclass object of a class object, use `Class getSuperClass()`
	 - `Class superclassObject = classObject.getSuperClass();`
	 - Returns null if `classObject` represents a primitive type, void, an interface, or Object class
	 - Returns class object for Object if an array
 - Use `Class[] getInterfaces()` on a class object to find all interfaces that the class directly implements
	 - If used on a class object that represents an interface, then returns the direct superinterfaces
### Simple Example
```java
import java.lang.reflect.*;

public class Test {
	public static void main(String[] args) {
		Object object = null;
		Class classObject = null;

		try {
			// load the class dynamically using 1st command-line arg
			classObject = Class.forName(arg[0]);
			
			// Create an instance of the class
			object = classObject.newInstance();
		} catch (InstantiationException e) {
			System.out.println(e); return;
		} catch (IllegalAccessException e) {
			System.out.println(e); return;
		} catch (ClassNotFoundException e) {
			System.out.println(e); return;
		}

		try {
			// Find the no-arg method named by 2nd command-line arg
			Method m = classObject.getMethod(arg[1], null);

			// Invoke the method on the object
			m.invoke(object, null);
		} catch (NoSuchMethodException e) {
			System.out.println(e); return;
		} catch (IllegalAccessException e) {
			System.out.println(e); return;
		} catch (InvocationTargetException e) {
			System.out.println(e); return;
		}
	}
}
```
 - Can be used on any class
 - Example: 
```java
public class myClass {
	public void print() {
		System.out.println("Hello, world!");
	}
	public void display() {
		System.out.println("Goodbye, cruel world!");
	}
}
```
 - Can be invoked like so:
```
> java Test MyClass print
Hello, world!
> java Test MyClass display
Goodbye, cruel world!
```
