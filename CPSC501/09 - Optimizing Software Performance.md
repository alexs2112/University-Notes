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
