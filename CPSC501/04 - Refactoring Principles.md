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
