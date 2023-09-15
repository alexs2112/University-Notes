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

**Example Method**: (contains some bugs)
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