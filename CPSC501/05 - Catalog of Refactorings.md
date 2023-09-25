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
