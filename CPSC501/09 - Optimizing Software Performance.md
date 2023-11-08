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
 - Order tests by frequency in switch and if-else structures
	```java
	if ((c == '+') || (c == '-'))
		processMath(c);
	else if ((c >= '0') && (c <= '9'))
		processDigit(c);
	else if ((c >= 'a') && (c <= 'z'))
		processLetter(c);
	```
	 - Rearrange these tests based on how common different inputs are
- Substitute switch statement for if-else construct, or vice-versa
	 - In Java, an if-else construct is about 6 times faster than a switch
	 - But in Visual Basic, its 4 times slower
- Substitute table lookups for complicated expressions
	 - Can be implemented using complicated logic
	```java
	if ((a && !c) || (a && b && c))
		category = 1;
	else if (b && !a) || (a && c && !b)
		category = 2;
	else if (c && !a && !b)
		category = 3;
	else
		category = 0;
	```
	 - But is faster with a lookup table:
	```java
	// Define category table
	static int categoryTable[2][2][2] = {
		// !b!c    !bc     b!c     bc
			0,      3,      2,      2,      // !a
			1,      2,      1,      1,      // a
	};
	...
	category = categoryTable[a][b][c];
	```
	 - Use lazy evaluation
		 - Eg. A 5000-entry table could be generated when the program starts
			 - But if only a few entries are ever used, may be better to compute values as needed and then store them in the table
			 - Cache them for further use
**Loop Techniques**:
 - Unswitching:
	 - Switching is where a decision is made inside a loop on every iteration
    ```java
    for (i = 0; i < count; i++) {
	    if (type == NET) { netSum += amount[i]; }
	    else { grossSum += amount[i]; }
    }
	```
	 - The if construct should be held outside of the loop as `type` never changes
		 - Note this likely requires that two loops must be maintained in parallel
 - Jamming (fusion)
	 - Combines two or more loops into one
		 - Their loop counters should be similar
	 - Reduces loop overhead
	```java
	for (i = 0; i < length; i++)
		employeeSalary[i] = 0.0;
	for (i = 0; i < length; i++)
		employeeCode[i] = 'C';
	```
	```java
	for (i = 0; i < length; i++) {
		employeeSalary[i] = 0.0;
		employeeCode[i] = 'C';
	}
	```
 - Unrolling
	 - A *complete unrolling* replaces a loop with straight-line code
		 - Practical only for short loops
	```java
	for (i = 0; i < 10; i++) { a[i] = i; }
	```
	```java
	a[0] = 0;
	a[1] = 1;
	...
	a[9] = 9;
	```
	 - With *partial unrolling*, two or more cases are handled inside the loop instead of just one
		 - The above example unrolled once becomes:
		```java
		for (i = 0; i < count - 1; i += 2) {
			a[i] = i;
			a[i + 1] = i + 1;
		}
		if (i == count - 1)
			a[count - 1] = count - 1;
		```
		 - Unrolled twice becomes
		```java
		for (i = 0; i < count - 2; i += 3) {
			a[i] = i;
			a[i + 1] = i + 1;
			a[i + 2] = i + 2;
		}
		if (i == count - 2)
			a[count - 2] = count - 2;
			a[count - 1] = count - 1;
		if (i == count - 1)
			a[count - 1] = count - 1;
		```
	 - Minimizing work inside loops
		 - Put calculations that result in a constant before the loop
	```java
	for (i = 0; i < rateCount; i++) {
		netRate[i] = baseRate[i] * rates.discount() / 0.93;
	}
	```
	```java
	quantityDiscount = rates.discount() / 0.93;
	for (i = 0; i < rateCount; i++) {
		netRate[i] = baseRate[i] * quantityDiscount;
	}
	```
 - Sentinel Values
	 - Are used to simplify loop control
		 - Replaces expensive compound tests
	 - A sentinel is a special value that marks the end of an array
		 - Is guaranteed to terminate a search through the loop
		 - Declare the array one element bigger so it can hold the sentinel
	```c
	found = FALSE;
	i = 0;
	while (!found && (i < count)) {
		if (item[i] == searchKey)
			found = TRUE;
		else
			i++;
	}
	if (found) { ... }
	```
	 - With a sentinel, becomes:
	```c
	item[count] = searchKey;
	i = 0;
	while (item[i] != searchKey)
		i++;

	if (i < count) { /* Item is found */ }
	```
 - Putting the busiest loop on the inside
	```c
	for (column = 0; column < 100; column++) {
		for (row = 0; row < 5; row++) {
			sum += table[row][column];
		}
	}
	```
	- Loop operations: (Outer = 100) + (Inner = 100 * 5) = 600
	- Switching the inner and outer loops end up with: (Outer = 5) + (Inner = 100 * 5) = 505
 - Strength Reduction
	 - Replace an expensive operation with a cheaper operation
		 - Eg. Replace multiplication with addition
	```java
	for (i = 0; i < saleCount; i++)
		commission[i] = (i + 1) * revenue * baseCommission * discount;
	```
	 - After strength reduction:
	```java
	increment = revenue * baseCommission * discount;
	cum = increment;
	for (i = 0; i < saleCount; i++) {
		cum += increment;
		commission[i] = cum;
	}
	```
**Routines**:
 - Rewrite routines inline
	 - C++ has the `inline` keyword
	 - With other languages, use macros
	```c
	#define SQUARE(x) ((x) * (x))
	...
	int a = 5, b;
	b = SQUARE(a);
	```
 - Recode in a low-level language
	 - In Java, use a native method written in C
	 - If in C or C++, use assembly
	 - Portability is lost
	 - Best applied to small routines or sections of code
	 - Eg. SPARC Assembly
    ```
		    .global cube
	cube:   smul   %o0, %o0, %ol
			smul   %o0, %o1, %o0
			retl
			nop
	```
 - Rewrite expensive system routines
	 - Eg. `double log2(double x)` may give more precision than you need
		 - Rounding integer version:
		```
		unsigned int log2(unsigned int x) {
			if (x < 2) return 0;
			if (x < 4) return 1;
			if (x < 8) return 2;
			...
			if (x < 2147483648) return 30;
		}
		```
 - Data transformation techniques:
	 - Replace floating point numbers with integers
	```Visual Basic
	Dim x as Single
	For x = 0 to 99
		a(x) = 0
	Next
	```
	 - Is faster as
    ```Visual Basic
    Dim x As Integer
	```
**Arrays**:
 - Reduce array dimensions where possible
	```C
	for (row = 0; row < numRows; row++) {
		for (column = 0; column < numColumns; column++) {
			matrix[row][column] = 0;
		}
	}
	```
	 - Is faster as a 1D array
	```C
	for (entry = 0; entry < numRows*numColumns; entry++) {
		matrix[entry] = 0;
	}
	```
 - Minimize array references
	```java
	for (i = 0; i < size; i++)
		for (j = 0; j < n; j++) 
		rate[j] *= discount[i];
	
	for (...) {
		temp = discount[i];;
		for (...)
			rate[j] *= temp;
	}
	```
 - Use supplementary indices:
	 - Length index or arrays
		 - Add a string-length field to C strings
		 - Faster than using `strlen()` which loops until `null` is found
	 - Parallel index structure
		 - Often easier to sort an array of references to a data array, then the data array itself
		 - Avoids swapping data that's expensive to move (ie. is large or on disk)
**Expressions**:
 - Use caching:
	 - Save commonly used values, instead of recomputing or rereading them
	```java
	private double cachedH = 0, cachedA = 0, cachedB = 0;
	public double Hypotenuse(double A, double B) {
		if ((A == cachedA) && (B == cachedB)) { return cachedH; }
		cachedH = Math.sqrt((A*A) + (B*B));
		cachedA = A;
		cachedB = B;
		return cachedH;
	}
	```
 - Expressions
	 - Exploit algebraic identities
		 - Replace expensive expressions with cheaper ones
		 - `not a and not b = not (a or b)`
		 - `if (sqrt(x) < sqrt(y)) = if (x < y)`
 - Strength reduction

| Original | Replacement |
| --- | --- |
| Multiplication | Repeated Addition |
| Exponentiation | Repeated Multiplication |
| Trig Routines | Trig Identities |
| Long Ints | Ints |
| Floats | Fixed Point Numbers/Ints |
| Doubles | Floats |
| Mult/Div by Power of 2 | Left/Right Shift |
 - Initialize at compile time
	 - Use constants where possible
	```java
	unsigned int Log2(unsigned int x) {
		return (unsigned int)(log(x) / log(2));
	}

	const double LOG2 = 0.69314718;
	unsigned int Log2(unsigned int x) {
		return (unsigned int)(log(x) / LOG2);
	}
	```
 - Use the proper data type for constants
	 - Avoid runtime type conversion
	```java
	double x;
	...
	x = 5;

	// Better as
	x = 5.0;
	```
 - Eliminate common subexpressions
	 - Assign to a variable, use it instead of re-computing
	```java
	p = (1.0 - (r / 12.0)) / (r / 12.0);
	
	// Better as
	y = r / 12.0;
	p = (1.0 - y) / y;
	```
 - Precompute results
	 - Often better to look up values than to recompute them
	 - Values could be stored in constants, arrays, or files
**I/O Techniques**:
 - Minimize disk and network accesses
	 - Use buffered I/O, instead of single reads/writes
 - Use RAM instead of disk whenever possible
	 - Cache commonly used data
 - Localize memory accesses
	 - Reading/writing registers is faster than cache memory, faster than DRAM
	 - C and C++ provide the `register` keyword
		 - Is a hint to the compiler to use a register instead of RAM (`register int x;`)
**Assembly Language Techniques**:
 - Specific to a CPU architecture
	 - Not generally portable
 - Goal is to minimize the number of clock cycles it takes to execute an algorithm
	 - Generally: Code the algorithm using the fewest number of instructions possible
	 - A *clever* programmer can usually beat the best optimizing compiler
 - We can quantify execution time precisely, as each instruction takes a defined number of clock cycles to complete
	 - A fixed number on a RISC CPU
	 - A variable number on a CISC CPU
		 - Some assemblers produce output files showing this *cycle count*
 - Eliminate instructions where possible
	 - SPARC example
	```
	cube:   save    %sp, -96, %sp
			smul    %i0, %i0, %l0
			smul    %i0, %l0, %i0
			restore
			ret
			nop
	```
	 - Eliminate 2 instructions by converting into a leaf subroutine
	```
	cube:   smul    %o0, %o0, %o1
			smul    %o0, %o1, %o0
			ret
			nop
	```
 - Reorder instructions to keep the pipeline full or to avoid pipeline stalls
	 - Above code can be changed to
	```
	cube:   smul    %o0, %o0, %o1
			retl
			smul    %o0, %o1, %o0     // filled the delay slot
	```
 - Use macros to inline subroutines
	 - Avoids call/return overhead
	```
	...
	mov     5, %o0
	call    cube
	nop
	...     // 6 instructions executed
	```
	 - A macro such as
	```
	define(cube,   `smul    $1, $1, %g1
					smul    $1, %g1, $1`)
	...
	mov     5, %o0
	cube(%o0)
	...
	```
	 - This gets expanded to
	```
	mov     5, %o0
	smul    %o0, %o0, %g1
	smul    %o0, %g1, %o0
	// 3 instructions executed
	```
 - In extreme cases, one might try to inline *every* subroutine
	 - Usually results in a much bigger executable (more RAM is used, trading memory for speed)
 - Note that some compilers allow one to inline assembly code into C or C++ code
	 - `sdcc` example:
	```c
	unsigned char counter;
	...
	counter = 0;
	__asm
		inc     _counter
	__endasm;
	```
 - Use SIMD instructions to move data while calculating
	 - Single Instruction, Multiple Data
	 - Motorola DSP56001 example:
	```
	MPY     X0, Y1, A
	MOVE    X:(R0)+, X0
	MOVE    Y:(R4)+, Y0
	MAC     X0, Y0, A
	// 4 cycles, can be improved to
	MPY     X0, Y1, A    X:(R0)+, X0    Y:(R4)+, Y0
	MAC     X0, Y0, A
	// 2 cycles
	```
 - There are libraries available that use SIMD instructions on vectors of data
	 - May be able to exploit the parallelism of multi-core CPUs
	 - Intel Vector Math Library (VML)
		 - C/C++ API for Windows, Linux, OSX
		 - Part of the Intel Math Kernel Library (MKL)
	 - Accelerate Framework
		 - Is a C API for OSX
