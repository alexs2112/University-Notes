### Meltdown
 - Allows attackers to read arbitrary physical memory (including kernel memory) from an unprivileged user process
 - Lets an attacker leak arbitrary memory from:
	 - The process being exploited
	 - Other processes
	 - The kernel
 - Operates at the hardware level, software mitigations can only do so much
 - Abuses the out of order instruction execution to leak data via a processor covert channel (cache lines)
	 - Was fully patched (in Linux) with KAISER/KPTI
**Page Tables**:
 - Contain the mappings between virtual memory (used by process) and physical memory (memory manager)
 - For performance reasons, most modern OS's map kernel addresses into user space processes
	 - Under normal circumstances, the kernel memory can't be read from user space, an exception is triggered
**Meltdown Attack**:
 - Step 1: User process reads a byte of arbitrary kernel memory
	 - This should cause an exception but will leak data to a side channel before the exception handler is invoked (out of order instruction execution)
 - Step 2: The value of the secret data is used to populate data in an array that is readable in user space memory
	 - The position of the array depends on the secret value
 - Step 3: An exception is triggered that discards the out of order instructions
	 - The secret cannot be read from the user space array
 - Step 4: The unprivileged process iterates through array elements
	 - The cached element will be returned much faster, revealing the contents of the secret byte read
	 - The array is realy 4kb elements
**Kernel Page Table Isolation**:
 - aka KPTI, aka the KAISER patch
 - Removes mapping of kernel memory in user space processes
	 - The patch reduces performance by 30%
 - The kernel memory is no longer mapped, it cannot be read by Meltdown
 - Does not address the core vulnerability, it simply prevents practical exploitation

### Spectre
 - Abuses branch prediction and speculative execution to leak data from via a processer covert channel (the cache lines)
 - Spectre can only read memory from the current process, not kernel or other physical memory
 - Spectre has not been patched
**Speculative Execution**:
 - Modern processors perform speculative execution
	 - Execute instructions in parallel that are likely to be executed after a branch in code (if/else)
	 - Instructions that are not executed cause a pseudo CPU snapshot to be taken, to roll back to if necessary
 - Branch prediction algorithms are trained based on current execution
	 - The CPU learns which branch will be executed from previous executions of the same code
**Spectre Attack**:
 - Does not allow an unprivileged process to read privileged memory (as we saw with Meltdown)
 - Does not allow code executing in the victim process to access data it should not have access to
 - Train the branch prediction algorithm by constantly accessing memory you own so that it knows to always return the value
	 - Then ask to access somewhere else and by the time it has denied it it has already fetched the data into the cache
