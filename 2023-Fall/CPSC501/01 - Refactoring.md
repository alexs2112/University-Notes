### Basic Concepts
 - **Definition**: Disciplined process of changing the internal structure of software to make it easier to understand and maintain, without changing external observable behaviour
 - **Goal**: Improve the design of the code after it is written and working
 - `JUnit` is used in this course to test iterative refactoring steps with unit tests
 - Well-designed software systems decay as they are modified over time, refactoring reverses this decay
	 - Bad design can be radically improved with a series of *small* changes
	 - Refactoring done during maintenance: When fixing bugs or adding new features
 - Works well with iterative development techniques
	 1. Choose part of the system
	 2. Analysis of requirements
	 3. Design
	 4. Coding
	 5. Testing
	 - Refactoring is a form of redesign that can be superimposed on the iterative lifecycle
		 - Can refactor during design, coding, and testing (not analysis)
		 - Refactoring is a cyclical process

### Simple Examples
**Rename Method** refactoring (p. 273)
```java
public class Employee {
	private String lastName;
	...
	public void func1(String value) {
		lastName = value;
	}
}
...
// Client code
Employee employee = new Employee();
employee.func1("Smith");
```
 - Rename the method to better describe what it does
```java
public class Employee {
	private String lastName;
	...
	public void setLastName(String value) {
		lastName = value;
	}
}
...
// Client code
Employee employee = new Employee();
employee.setLastName("Smith");
```
 - Note: This would be done in smaller steps (can be broken down to 8 steps for some reason)
	 - Compiled and tested after each change

**Pull Up Method** refactoring (p. 322)
```java
public class Employee {
	protected String lastName;
	...
}
public class Clerk extends Employee {
	public String getLastName() {
		return lastName;
	}
}
public class Cashier extends Employee {
	public String getLastName() {
		return lastName;
	}
}
```
 - Move duplicate subclass methods into the superclass:
```java
public class Employee {
	private String lastName;
	...
	public String getLastName() {
		return lastName;
	}
}
public class Clerk extends Employee { ... }
public class Cashier extends Employee { ... }
```
 - Eliminates redundant code that is hard to maintain