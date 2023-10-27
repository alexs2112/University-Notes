### Introduction
 - Optimization is the process of modifying a program to improve its efficiency
	 - Increases its speed
	 - Reduce its size (memory usage)
**Efficiency**:
 - Program requirements
	 - Does the program really need to run at a certain speed?
	 - Is it worth the extra effort?
 - Program design
	 - If performance is important, design a performance-oriented architecture
		 - Set resource goals for individual subsystems and classes
 - Class and routine design
	 - Choose efficient algorithms and datatypes
		 - Quicksort vs bubble sort
		 - Binary search vs linear search
 - Operating system interactions
	 - Working with files, dynamic memory, or I/O devices means using system calls
		 - May be slow or fat
 - Code compilation
	 - Good compilers produce optimized machine code
		 - May have options for different optimization levels
 - Hardware
	 - A hardware upgrade may be the cheapest way to improve a program's performance
		 - Not always possible
 - Code Tuning
	 - Small-scale changes made to code to make it run more efficiently
		 - At the level of a single routine, or a few lines of code
	 - Tends to produce hard-to-understand code
		 - Obscures design

### General Guidelines
 - Don't optimize as you go
	 - Focusing on optimization during initial development detracts from achieving correctness, readability, design quality
	 - Jackson's Rules of Optimization:
		 - Rule 1: Don't do it.
		 - Rule 2 (for experts only). Don't do it yet - that is, not until you have a perfectly clear and un-optimized solution.
	 - Code tuning should be done only as a last step
		 - Knuth: "Premature optimization is the root of all evil"
 - Optimize bottlenecks
	 - The 80/20 rule: 20% of the program's routines consume 80% of its execution time.
		 - Knuth found 4% of a FORTRAN program accounted for over 50% of its run time
	 - Spend your time fixing these "bottlenecks"
 - Measure performance when optimizing
	 - Use a profiler to find bottlenecks
	 - Use timers to measure CPU time
		 - Make sure a change actually improves speed
			 - May actually make things worse when using a different compiler, OS, or processor
 - Run regression tests after each optimization
	 - Make sure your program is still correct

### Measuring Performance
**Profiling**:
 - Used to find how much time is spent in each function of a program
	 - Helps find bottlenecks
	 - Helps you compare the performance of algorithms or programs
 - Works by sampling the program counter (PC register)
	 - Periodically queries the program, recording the function in which it is running
 - Is *statistical* in nature
	 - Somewhat inexact, will vary from run to run
 - Available UNIX profilers for programs compiled with `gcc`:
	 - `prof` (most commonly used)
	 - `gprof`
	 - `pixie`
	 - etc.
 - Using `prof`:
	 - Compile the program with the `-p` option
		   `gcc -c myprog.c`
		   `gcc -o myprog -p myprog.o`
	 - Run the program (`./myprog`)
		 - Produces the file `mon.out`
	 - Print the profile report to stdout
		   `prof myprog mon.out`
**Timing measurements**:
 - In UNIX, can use the `time` command to time an entire program
	 - Eg: `time java Test`
		   `1.09u 0.12s 0:01.27 95.2%`
		- User CPU time, System CPU time, Real time
- In C and C++, use the `clock()` function to measure the CPU time used by a function or section of code
	- Eg:
    ```c
	#include <time.h>
	#include <stdio.h>
	...
		clock_t before;
		double elapsed;

		before = clock();
		long_running_function();
		elapsed = clock() - before;
		printf("function used %.3f seconds\n", elapsed/CLOCKS_PER_SEC);
	```
	 - If the function takes a fraction of a second, run it in a loop to get a more accurate measurement
	```c
		before = clock();
		for (int i = 0; i < 1000; i++)
			short_running_function();
		elapsed = (clock() - before) / double(i);
	```
 - In Java, use the `nanoTime()` method
```java
long startTime = System.nanoTime();
longRunningMethod();
long elapsedTime = System.nanoTime() - startTime;
// Result in nanoseconds (10^(-9)s)
```

### Algorithm-Based Optimization
 - Choosing a more efficient algorithm or data structure is often the best way to improve program efficiency
 - Look for algorithms that reduce the order of complexity
	 - Eg. Binary search `O(log n)` vs linear search `O(n)`
	 - Eg. Merge sort `O(n log n)` vs bubble sort `O(n^2)`
 - Do this first before attempting other optimizations
	 - Hand tuning an `O(n^2)` algorithm won't yield near the same gains as using an `O(n log n)` algorithm
 - Beware of situations that trigger worst-case performance
	 - Some algorithms may not achieve their average Big-O performance under certain conditions
	 - Eg. Quicksort degenerates to `O(n^2)` with nearly-sorted inputs
 - Sometimes an inefficient algorithm is fine for small inputs
	 - The overhead of a complicated algorithm may make it slower than a simple one
	 - And harder to debug and maintain
 - Measure performance to make sure you've made the right choice

### Compiler-Level Optimization
 - Enabling compiler optimization can improve speed by as much as 2 times
 - Most compilers turn off optimization by default
	 - Optimized code tends to confuse debuggers
 - Works best with straightforward code
	 - Hand tuned code may actually be harder for the compiler to optimize
 - Some compilers optimize better than others
 - Aggressive optimizers may introduce bugs
	 - Rerun regression tests to ensure correctness
 - `gcc` optimization flags:
	 - Optimize: `-O` or `-O1`, `-O2`, `-O3`
	 - Don't optimize (default): `O0`
	 - eg. `gcc -O2 -o myprog myfile.c`

### Code Tuning
**Guidelines**:
 - Save each version of your code using version control
 - Use the profiler to find a bottleneck
 - Tune the bottleneck, using just one technique
 - Measure the improvement
	 - If none, revert to the prior version
 - Repeat until desired performance is achieved
**Logic Techniques**:
 - Stop testing when answer is found (break out of loops as soon as possible)
	```java
	negFound = false;
	for (int i = 0; i < count; i++) {
		if (input[i] < 0) {
			negFound = true;
			break;
		}
	}
	```
