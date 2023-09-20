### Introduction
 - A *unit test* is a technique for testing the correctness of a module of source code
	 - You create separate test cases for every non-trivial method in the module
	 - Unlike most other tests: Done by developers as they code
	 - Is a form of *bottom-up* testing
 - Benefits of unit testing:
	 - Reduces the time spent on debugging by catching bugs early
	 - Eases integration
		 - Bottom-up testing allows you to build a large system on a reliable "foundation" of working low-level code
	 - Documents the intention of the code
	 - Encourages refactoring
		 - Tests are rerun to make sure no new bugs are introduced (regression tests)
 - Goal of unit testing is to determine if the code:
	 - Do what is intended
	 - Works correctly under *all* conditions
		 - Including exceptional conditions like bad input, full disks, dropped network connections, etc
	 - Is dependable
 - Your test code is for internal use only
	 - Is separate from production code and is not shipped
	 - Production code must be "unaware" of the test code that exercises it
		 - However you may have to refactor poorly structured code to make it testable
 - Unit testing frameworks make it easy to build and run tests
	 - Open source frameworks include:
		 - JUnit for Java
		 - NUnit for C#

### Working with JUnit
 - Will describe version 4.8
 - Version 4.0 (2006) and later uses Java annotations
	 - Requires Java 5
 - Can be downloaded from junit.org
	 - `junit.jar`
	 - `hamcrest-core.jar`
 - To install:
	 - Copy the two JAR files into your install directory
	 - Set your classpath to point to these frameworks
 - The JUnit framework does the following:
	 - Sets up conditions needed for testing
		 - Creates objects, allocates resources, etc
	 - Calls the method
	 - Verifies the method worked as expected
	 - Cleans up (deallocates resources, etc)
 - All test methods must be annotated with `@Test`
	 - Are invokes automatically by the framework
	 - With JUnit 3.x, test methods must start with `test` (no annotations)
 - Each method uses various `assert` helper methods
	 - Aborts the test method if the assertion fails
	 - Reports fails to the user
 - JUnit asserts:
	 - `assertEquals([String message], expected, actual)` (message is optional)
	 - `assertEquals([String message], expected, actual, tolerance)` (useful for imprecise floats)
	 - `assertNull([String message], Object object)`
	 - `assertNotNull([String message], Object object)`
	 - `assertSame([String message], expected, actual)` (expected and actual point to same object)
	 - `assertTrue([String message], boolean condition)`
	 - `assertFalse([String message], boolean condition)`
	 - `fail([String message])`
		 - Fails the test immediately
		 - Used to mark code that should not be reached
 - Use `@Before` to mark a method used to initialize the testing environment
	 - Allocate resources, initialize state
 - Use `@After` (or `@AfterEach`) to mark a method used to clean up after a test
	 - Deallocate resources
 - These are invoked before and after *every* test method is run
	 - Tests can be run independently, in any order
 - By default, the test runner uses *all* methods of a class annotated with `@Test`
	 - A *suite* of tests is created for you automatically
 - You can combine tests from several classes into a suite using the `@RunWith` and `SuiteClasses` annotations

### Things to Test
 - Use the mnemonic `Right-BICEP`
	 - Are the results **right?**
		 - Does the code do what is intended?
	 - Check **B**oundary conditions
		 - Beginnings/ends of lists, files, etc
		 - Badly formatted data
		 - Empty or missing values
		 - Out of range values
		 - Duplicates in lists that should have unique data
		 - Ordered lists that arent, vice-versa
		 - Things that arrive out of order
		 - Etc
	 - Check **I**nverse relationships
		 - Square the result of a square root method
	 - **C**ross check by other means
		 - Use a proven sorting algorithm to check the results of a new sorting method
	 - Force **E**rror conditions
		 - Incorrect input parameters
		 - Problems in the environment
			 - Running out of RAM
			 - Running out of disk space
			 - Dropped network connections
			 - High system load
			 - Etc
		 - Can be simulated using mock objects
			 - Objects that stand in for system resources
	 - Check **P**erformance characteristics
		 - Make sure performance doesn't degrade
			 - With large inputs
			 - When adding new functionality
	 - Always ask yourself what else can go wrong
### Example 1: 
 - Method: (contains some bugs)
```java
public class Largest {
    public static int largest(int[] list) {
        int i, max = Integer.MAX_VALUE;

        for (i = 0; i < list.length - 1; i++) {
            if (list[i] > max) {
                max = list[i];
            }
        }
        return max;
    }
}
```
 - Create a test class with an initial test
```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestLargest {
    @Test
    public void testOrder() {
        assertEquals(9, Largest.largest(new int[] {8, 9, 7}));
    }
}
```
 - Your test can be named anything, although convention starts with `Test`
 - All test methods must be annotated with `@Test`
	 - Requirement of JUnit
	 - Will be invoked automatically by the test runner
 - The `assertEquals()` will abort if the `largest()` method does not return a 9 (largest out of 8, 9, 7)
 - Save and compile (`javac *.java`)
 - Run the test with `java org.junit.runner.JUnitCore TestLargest`
	 - Note: The classpath must be set correctly for this to work
		 - Point to wherever junit is installed (covered later)
	 - Is a text UI, some IDEs can run tests within their GUIs
 - An error is reported to the terminal, stack trace is printed
 - Fix the bug in `Largest.java`
	 - Initialize `max = 0;`
 - Recompile and run the test again:
	 - Should report: `OK (1 test)`
 - Adding some more tests:
```java
public class TestLargest {
    @Test
    public void testOrder() {
        assertEquals(9, Largest.largest(new int[] {8, 9, 7}));
        assertEquals(9, Largest.largest(new int[] {9, 8, 7}));
        assertEquals(9, Largest.largest(new int[] {7, 8, 9}));
    }
}
```
 - Recompiling and rerunning the tests fails (boundary is skipping the end of the list `i < list.length - 1`)
	 - Off by one bug
 - Add methods to test for duplicates, lists of size one, negative numbers, empty lists
```java
public class TestLargest {
    @Test
    public void testDuplicates() {
	    assertEquals(9, Largest.largest(new int[] {9, 7, 8, 9}));
    }

	@Test
	public void testOne() {
		assertEquals(9, Largest.largest(new int[] {9}));
	}

	@Test
	public void testNegative() {
		assertEquals(-7, Largest.largest(new int[] {-9, -8, -7}));
	}
	// This will result in another bug as the initial max value is at 0
	// Can fix by setting as Integer.MinValue

	@Test (expected=RuntimeException.class)
	public void testEmpty() {
		Largest.largest(new int[] {});
	}
	/* In the function `largest`, should throw exception on list size 0
	if (list.length == 0) {
		throw new RuntimeException("largest: empty list");
	}
	*/
}
```

### Example 2
 - Before and After tags
```java
public class TestDB {
	private Connection dbConn;

	@Before
	public void setup() {
		dbConn = new Connection(...);
		dbConn.connect();
	}

	@After
	public void teardown() {
		dbConn.disconnect();
		dbConn = null;
	}

	@Test
	public void testReadDB() {
		...
	}
	
	@Test
	public void testWriteDB() {
		...
	}
}
```

### Example 3
 - Combine tests from `TestLargest` and `TestSmallest` classes
```java
// AllTests.java
import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;

@RunWith(Suite.class)
@SuiteClasses({TestLargest.class, TestSmallest.class})
public class AllTests { }

// Run with java org.junit.runner.JUnitCore AllTests
```

