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