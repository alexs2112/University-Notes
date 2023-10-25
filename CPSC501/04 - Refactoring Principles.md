### Refactoring
 - **Definition**: Disciplined process of changing the internal structure of software to make it easier to understand and maintain, without changing external observable behaviour
**Why Refactor?**:
 - Improves the design of software
	 - Reverses the decay of cumulative ad hoc changes
 - Makes software more readable
	 - A clear design is easier to understand and maintain
	 - Use refactoring to learn about unfamiliar code
 - Helps you find and eliminate bugs
 - Helps you program faster
	 - A poor design prevents rapid development
**When Refactor?**:
 - Continuously, as you develop or modify code
 - Whenever you duplicate code
 - When adding functionality to code
	 - Change the design to make adding features easy
 - As you find and fix bugs
	 - Its easier to spot bugs when the design is clear
 - As you do a code review
**Problems with Refactoring**:
 - Many refactorings change a class's public interface
	 - Methods may be renamed or removed
	 - Not a problem is you can edit all calling code
	 - If the interface is published, you need a transition period where the old interface is kept until clients adopt the new interface
		 - Mark an old method as deprecated and have it call the new method
 - You may not be able to refactor your way out of a design mistake
	 - May be necessary to do more upfront design
 - If software is tightly coupled to a database, changing the object model may cause change to the database schema
	 - Forces you to migrate data, which is difficult and expenses
	 - Isolate changes by putting a layer between the database and object model
**Don't Refactor When**:
- Its easier to rewrite from scratch
- You are close to a release deadline
**Refactoring and Design**
 - Refactoring is not a replacement for upfront design
 - Lets you create a simple, upfront design that does not build in unneeded flexibility
	 - You can always refactor later if necessary
**Refactoring and performance**
 - Refactoring usually makes software run more slowly
 - Also more amenable to performance tuning
	 - If well factored, *hot spots* will be isolated to a few short methods (found using a profiler late in development)
 - Tune the hot spots only, tuning other code is a waste

### When to Refactor
 - No hard and fast rules
	 - Best to use informed intuition, try to detect "bad smells in code"
**Duplicated code**: (*Extract Method*)
 - If the same code is in two or more places in the same class
 - The same code in two sibling classes (*Pull Up Method*)
 - Similar code in sibling classes (*Form Template Method*, put common code in superclass)
 - Same code in unrelated classes (*Extract Class* in one class, then use new class in other classes)
**Long method**:
 - Decompose into small methods (sometimes just one line long)
 - *Extract Method* on blocks of code that can be separated out
	 - May need to *Replace Temp with Query* to enable the extraction
**Large classes**:
 - Tries to do too many different things
	 - Too many instance variables and/or too much code
 - *Extract Class* or *Extract Subclass* to separate out bundles of data and responsibilities
**Long parameter list**:
 - Better to pass in an object, so the method can get the data it needs
 - Shorten list with *Preserve Whole Object* or *Introduce Parameter Object*
**Divergent change**:
 - Occurs when a class changes in distinct ways for differing reasons
	 - Eg. you change 3 methods together for one reason, and 5 other methods for another
	 - Suggests responsibilities of the class are divergent
 - Determine what changes for a single cause, use *Extract Class* to bundle these together
**Shotgun surgery**:
 - A single change causes many little changes to several different classes
 - Use *Move Method* and *Move Field* to put changes into a single class
	 - Sometimes best to *Inline Class*
**Feature envy**:
 - A class does a calculation that belongs elsewhere
	 - ie. uses too much data from another class
 - Put it into the proper class with *Move Method*
**Data clumps**:
 - Data clusters together in fields or parameter lists
 - *Extract Class* to change clumps into an object
 - Shrink parameter lists with *Introduce Parameter Object* or *Preserve Whole Object*
**Primitive obsession**:
 - Often better to use a class instead of a primitive data type
	 - Allows things like range checking, formatting, etc
	 - Done with *Replace Data Value with Object*
 - If the primitive is a type code, use
	 - *Replace Type Code with*
		 - *Class*
		 - *Subclass*
		 - *State/Strategy*
**Switch statements**:
 - Are rare in good OO code
 - If switching on a type code: *Replace Conditional with Polymorphism*
	 - Easier to add subclasses than changing many switch statements
**Parallel inheritance hierarchies**:
 - When you make a subclass of one class, you also make a subclass of another
	 - Special case of shotgun surgery
 - Eliminate one hierarchy by shifting data and responsibilities to the other
	 - *Move Method* and *Move Field*
**Lazy class**:
 - A class doesn't do enough to justify its existence
	 - May result from other refactorings like *Move Method*
 - Eliminate it with *Collapse Hierarchy* or *Inline Class*
**Speculative generality**:
 - You added code for future expansion that never occurred
	 - Remove useless abstract classes with *Collapse Hierarchy*
	 - Remove unneeded delegation with *Inline Class*
	 - Remove unused parameters with *Remove Parameter*
**Temporary field**:
 - An instance variable is set and used only part of the time
 - *Extract Class*, moving over the "orphan variables" and related methods
**Message chains**:
 - A client follows a chain of referring objects, sending a message to the last object
	 - Any change to intermediate relationships causes client code to change
 - *Hide Delegate* on the first object on the chain so it returns the last object
**Middle man**:
 - Where most methods of a class delegate to another class
 - *Remove Middle Man*, so you talk to the delegated object directly
**Inappropriate intimacy**:
 - A class knows too much about another class's private parts
 - *Move Method* and *Move Field* to the first class
 - Or *Extract Class* to put commonality in a safe place
 - *Replace Inheritance with Delegation* if a subclass knows too much about its parents
**Alternative classes with different interfaces**:
 - Two or more classes do the same thing, but have inconsistent interfaces
 - Use *Rename Method* and *Move Method* to give the classes identical interfaces
 - If redundant, *Extract Superclass*
**Incomplete library class**:
 - You can't use *Move Method* on code you can't change
 - *Introduce Foreign Method* into a client class
	 - Best for only one or two methods
 - *Introduce Local Extension* to create a subclass
**Data class**:
 - A class with no behaviour, has only get and set methods
 - *Move Methods* into the data class
	 - May need to *Extract Method* first
**Refused bequest**:
 - A subclass doesn't use all the methods and data that it inherits
 - Reorganize the class hierarchy
	 - *Push Down Method* and *Push Down Field* to create a sibling for the unused behaviour
 - If the subclass does not support the superclass interface: *Replace Inheritance with Delegation*
**Comments that explain bad code**:
 - *Extract Method* on commented blocks of code
 - *Rename Method* to make purpose clearer
