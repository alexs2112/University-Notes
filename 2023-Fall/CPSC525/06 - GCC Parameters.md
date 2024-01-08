### `-std=c99`
 - Compile with 1999 version of C standard
 - Many C stdlib string func's are unsafe
 - `gets` is so ridiculously unsafe that it was forcibly deprecated in some compilers
	 - Reads until the first null byte into a buffer, literally no way to limit it in size
	 - `gets_s` lets you specify the max buffer length
	 - Same for `strcpy`, `strncpy`, `memcpy`, `memmove` (add `_s` to the end of each of them)

### `-fno-stack-protector`
 - Disables gcc stack protection features (generally ill-advised)
 - Performs runtime tests for stack integrity
	 - Embed canaries in stack frames and verify their integrity prior to function return
 - To overflow the stack buffer, the first thing it overflows is the canary which kills it
	 - More of a hurdle than an actual barrier
**StackGuard & ProPolice**:
 - `gcc` has had canary support since version 4.1 (2005)
 - Based on StackGuard & ProPolice
	 - In addition to canaries, ProPolice rearranges stack layout to thwart ptr overflows
**gcc Stack Protection**:
 - `fstack-protector`
	 - Default
	 - Emit extra code to check for buffer overflows
	 - Uses heuristics to apply a guard variable to functions with vulnerable objects
		 - Guards are initialized when the function is entered, then checked when it exits
		 - If a guard fails, an error  message is printed, the program exits
 - `fstack-protector-all`
	 - Like `fstack-protector` except that all functions are protected
 - `fstack-protector-strong`
	 - Like `fstack-protector`, includes additional functions to be protected
		 - Those that have local array definitions, or references to local frame addresses

### Stack Ornithology: Canaries Types
 - Three common species of stack canary:
1. Random Canaries:
	 - The canary is a random string chosen at program launch
	 - Same canary inserted in every stack frame
	 - Verify canary before returning from function
		 - If canary is wrong, throw error and crash
	 - To smash stack frame, attacker must first figure out current random canary value
	 - Random canaries aren't perfect:
		 - Overwrite function pointers to modify control flow without touching canary
		 - Exploit format string vulnerabilities to learn the canary
		 - Forge your own master canary
2. Terminator Canaries
	 - Observation: Many (most?) buffer overflow attacks based on string operations
	 - Canary is a string terminator (`\0`, `\n`, `CR`, `LF`, `EOF`)
		 - Prevents unsafe string operations (eg. `strcpy`) from reading past canary
	 - Terminator canaries aren't perfect
		 - Only thwart attacks using functions that halt upon reading a string terminator
		 - Canary value is known to attacker, making it easy to pass canary check code after successful attack
3. Random XOR Canaries
	 - A random canary that is XOR-scrambled using some or all of the control data
	 - Canary OR control data changes -> Dead canary
	 - Random XOR canaries aren't perfect:
		 - Susceptible to roughly the same attacks as random canaries, only reading the canary from the stack is harder
		 - Attacks require significantly more care, but are fundamentally unchanged
		 - Much higher overhead to check the canaries

### MS Visual Studio `'/GS'` (Buffer Security Check)
 - Microsofts Visual Studio does something similar
	 - Use a GS Cookie as a canary
	 - Added to all functions unless compiler can prove it is unnecessary
 - Can overwrite the exception handlers and then cause an exception to be thrown to hijack control
**Another Layer of Defenses**:
 - SEH <=> Structured Exception Handler
 - `/SAFESEH` (linker flag)
	 - Linker produces table of safe exception handlers, places it at start of data segment
	 - System will not jump to an exception handler not on list
 - `/SEHOP` (platform defense)
	 - SEH Overwrite Protection
	 - Similar to adding a canary to the SEH list
