### Overview
 - A proxy is a "person authorized to act on behalf of another"
 - In OOP, a *proxy* is an object that substitutes for another object called the *target*
	 - To work, the proxy must implement the target's entire interface
		 - Support all the target's methods
 - The proxy may:
	 - Implement its own version of *all* the methods
		 - Act as a *substitute* for the target
	 - Or delegate some or all calls it receives to the target
		 - Acts as an *intermediary* between the caller and the target
 - If an intermediary, a proxy may add functionality before and after forwarding the method to the target
	 - Allows you to add behaviour to objects
**Intercession**:
 - Method invocation *intercession* is the ability to intercept method calls reflectively
	 - Not supported by Java
	 - Is approximated using *dynamic proxies*

### Dynamic Proxies
 - Proxies are useful when you need to add similar behaviour to many different classes
	 - Eg. Adding tracing code to all method calls
 - Without proxies, you could create non-tracing and tracing classes
	 - Or subclasses of a common superclass
	 - You arrange to instantiate the needed class at runtime
	 - Drawbacks:
		 - Tedious: must be done for all methods of all classes
		 - Error prone: may overlook a method
		 - Fragile: if a method is added or changes, then the traced class must also be added/changed
 - Dynamic proxies allows the added behaviour to be implemented in a single class
 - `java.lang.reflect.Proxy`
	 - Can create a *proxy class* (a class object) that implements a set of *proxied interfaces* with:
		 - `static Class getProxyClass(ClassLoader loader, Class[] interfaces)`
		 - The name of the class is `$Proxy` followed by a number
	 - Proxy classes have a constructor that takes an `InvocationHandler` parameter
	 - You create a *proxy instance* with the constructor and `newInstance()`
	```java
	Proxy cl = Proxy.getProxyClass(MyInterface.getClassLoader(), 
									new Class[] { MyInterface.class });
	Constructor c = cl.getConstructor(new Class[] { InvocationHandler.class });
	Object proxy = c.newInstance(new Object[] { new MyIH(target) });
	```
	 - Or with a single call
    ```java
	Object proxy = Proxy.newProxyInstance(
		MyInterface.getClassLoader(),
		new Class[] { MyInterface.class },
		new MyIH(target)
	);
    ```
	 - Use `isProxyClass()` to see if a class object represents a proxy class
	   `if (Proxy.isProxyClass(obj.getClass()) { ... }`
**Invocation Handler**:
 - The proxy instance delegates handling of methods to its *invocation handler*
	 - Is an object that implements the `InvocationHandler` interface
		 - Must implement the `invoke()` method
		 - Must also keep a reference to the target object
```java
public class MyIH implements InvocationHandler {
	private Object target;

	public MyIH(Object obj) {
		target = obj;
	}

	public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
		// Merely forwards the message to the target
		return method.invoke(target, args);
	}
}
```
 - Could add pre- or post-processing to the invoke method
```java
	public Object invoke(...) {
		Object result = null;

		// Preprocessing here
		result = method.invoke(target, args);
		// Postprocessing here

		return result;
	}
```

### Example - Tracing Proxy:
 - Target interface
```java
public interface MyInterface {
	public void print();
	public void display();
}
```
 - Target class
```java
public class MyClass implements MyInterface {
	public void print() {
		System.out.println("Hello, world!");
	}
	public void display() {
		System.out.println("Goodbye, cruel world!");
	}
}
```
 - Invocation handler
```java
public class TracingIH implements InvocationHandler {
	public static Object createProxy(Object obj) {
		return Proxy.newProxyInstance(
			obj.getClass().getClassLoader(),
			obj.getClass().getInterfaces(),
			new TracingIH(obj)
		);
	}

	private Object target;
	private TracingIH(Object obj) {
		target = obj;
	}

	public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
		Object result = null;
		
		try {
			System.out.println(method.getName() + "() begins");
			result = method.invoke(target, args);
		} catch(InvocationTargetException e) {
			System.out.println(method.getName() + " throws " + e.getCause());
			throw e.getCause();
		}
		System.out.println(method.getName() + "() returns\n");
		
		return result;
	}
}
```
 - Client code
```java
public class Test {
	public static void main(String[] args) {
		MyInterface obj = new MyClass();
		if (args.length > 0 && args[0].equals("trace")) {
			obj = (MyInterface)TracingIH.createProxy(obj);
		}
		
		// If trace is not set, works on the original object
		obj.print();
		obj.display();
	}
}
```
 - Sample run: `java Test trace`
```
print() begins
Hello, world!
print() returns

display() begins
Goodbye, cruel world!
display() returns
```
