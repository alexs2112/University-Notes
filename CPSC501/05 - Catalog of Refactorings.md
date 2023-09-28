 **Format:**
 - Name
 - Summary
 - Motivation
 - Mechanics
 - Examples

### Chapters of Refactorings
**Composing Methods**:
 - Are refactorings that reorganize the methods of a class
	 - And deal with troublesome local variables
 - *Extract methood* most commonly used
**Moving Features Between Objects**:
 - Reassigns responsibilities to other classes
 - *Move Method*, *Move Field*, and *Extract Class* are commonly used
**Organizing Data**:
 - Make working with data easier
 - Some refactorings promote better encapsulation (*Encapsulate Field*)
 - Others eliminate type codes
**Simplifying Conditional Expressions**:
 - Used to make logic within a method clearer
	 - *Decompose Conditional*
 - *Replace Conditional with Polymorphism* changes the class
**Making Method Calls Simpler**:
 - Use *Rename Method* to make intentions clearer
 - Some refactorings shorten parameter lists
	 - *Preserve Whole Object*
 - Often simplify a class's interface
	 - *Hide Method* and *Remove Setting Method*
**Dealing with Generalization**:
 - Some refactorings move responsibilities up/down the class hierarchy
	 - *Pull Up Field*, *Push Down Method*
 - Others change the hierarchy by creating/destroying classes
	 - *Extract Subclass*, *Collapse Hierarchy*
**Big Refactorings**:
 - Are much lengthier and time consuming than the previous refactorings
	 - Involves many small refactorings
 - *Tease Apart Inheritance*
 - *Convert Procedural Design to Objects*
 - *Separate Domain from Presentation*
 - *Extract Hierarchy*

### Examples
**Form Template Method**
 - Used when there is similar (but not identical) code in sibling classes
 - Their methods do similar (but different) steps in the same order
 - Goal is *Template Method* design pattern
	 - Identical code put into common superclass
```java
public class RetailClient extends Client {
	...
	public double amountOwing(int daysWorked) {
		double base = daysWorked * dailyRate();
		double discount = base * discountRate();
		return base - discount;
	}
}

public class CorporateClient extends Client {
	...
	public double amountOwing(int daysWorked) {
		double base = retainer + (daysWorked/30.0) * monthlyRate();
		double discount = 500.0 + base * 0.02;
		return base - discount;
	}
}
```
 - Mechanics:
	 - Extract methods that are either identical or completely different
```java
public class RetailClient extends Client {
	...
	public double baseAmount(int daysWorked) {
		return daysWorked * dailyRate();
	}
	public double discountAmount(double base) {
		return base * discountRate();
	}
	public double amountOwing(int daysWorked) {
		double base = baseAmount(daysWorked);
		return base - discountAmount(base);
	}
}

public class CorporateClient extends Client {
	...
	public double baseAmount(int daysWorked) {
		return retainer + (daysWorked/30.0) * monthlyRate();
	}
	public double discountAmount(double base) {
		return 500.0 + base * 0.02;
	}
	public double amountOwing(int daysWorked) {
		double base = baseAmount(daysWorked);
		return base - discountAmount(base);
	}
}
```
 - Pull up the common method into the superclass, and declare differing methods as abstract
```java
public class Client {
	...
	public double amountOwing(int daysWorked) {
		double base = baseAmount(daysWorked);
		return base - discountAmount(base);
	}
	public abstract double baseAmount(int daysWorked);
	public abstract double discountAmount(double base);
}
```
 - Remove pulled up methods from subclasses
 - Now it is easy to add new kinds of Clients
	 - Create a new concrete subclass, overriding the abstract methods

**Replace Type Code with Subclasses**:
 - Allows you to remove switch statements, if followed by *Replace Conditional with Polymorphism*
 - Original code:
```java
public class Account {
	private int type;
	static final int SAVINGS = 0;
	static final int CHEQUING = 1;

	public Account(int typeCode) {
		type = typeCode;
	}
	...
}
```
 - Mechanics:
	 - Self-encapsulate the type code
		 - If used by the constructor, replace constructor with factory method
```java
public class Account {
	...
	public int getType() {
		return type;
	}
	public static Account create(int typeCode) {
		return new Account(typeCode);
	}
	...
}
```
 - For each type code, create a subclass
	 - Override the `getType()` method
	 - Change the factory method
```java
public class Savings extends Account {
	public int getType() { return Account.SAVINGS; }
}
public class Chequing extends Account {
	public int getType() { return Account.CHEQUING; }
}
public class Account {
	...
	public static Account create(int typeCode) {
		switch(typeCode) {
			case SAVINGS:
				return new Savings();
			case CHEQUING:
				return new Chequing();
			default:
				throw new IllegalArgumentException("Bad type code");
		}
	}
}
```
 - Remove the type code field
	 - Declare accessors as abstract
```java
public class Account {
	...
	public abstract int getType();
	...
}
```
 - Use *Push Down Method* and *Push Down Field* for features specific to a subclass
 - If you have switch statements in methods other than the factory method, use *Replace Conditional with Polymorphism*
