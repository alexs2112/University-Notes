### `-z execstack`
 - Disables non-executable stack defense (generally ill-advised)

### Non-Executable Stack (W⊕X)
 - Prevent shellcode from running by marking stack (and/or heap) as non-executable
	 - NX (no execute) bit set in Page Table Entry (PTE)
		 - Intel marks this as the XD (eXecute Disable) bit
		 - AMD markets this as the EVP (Enhanced Virus Protection) bit
		 - ARM calls it the XN (eXecute Never) bit
 - Alas:
	 - Some legacy code requires executable stack
	 - Some code (JIT) requires executable heap
**Countering W⊕X with `return-to-libc`**:
 - W⊕X thwarts shellcode in buffers/env. vars/argv
	 - Instead, return to executable code (eg. the `system()` call to spawn a shell)
 - Attackers must set up stack frame so that appropriate arguments are passed to a libc function
 - Idea:
	 - Set up synthetic stack frame
	 - Jump somewhere arbitrary (like printf), setup another synthetic stack frame for your next jump
	 - Do a tiny bit of useful work and return, this jumps into the new stack frame and sets up another one to do some more tiny useful work
		 - Have a limited amount of time to do something, most of that is to set up the next stack frame, then the rest can do your work (which will be very little)

### Chaining RETs
 - Overwritten return value need not point to the beginning of a function
	 - Any instruction in the code will do
 - What if there is a return shortly after the instruction?
	 - Execution will soon be transferred to another instruction of the attacker's choosing
		 - This is called Return Oriented Programming (ROP)
 - There are compilers that can look at a binary and catalogues all the places you can jump and what the impact of jumping into those places will be
 - This is essentially the modern version of buffer overflows as the defenses for those are very effective now
**Address Space Layout Randomization (ASLR)**:
 - Defense against ROP:
	 - Map shared libraries, stack, heap, code segment, etc. to random locations in process memory
	 - Attacker cannot jump directly to the exec function
 - Booting twice loads libraries into different locations based on an offset
 - If you can leak a single address, then you know what the offset is and you can find everything else

### Attacking the Heap
 - Buffer overflows also occur on the heap
	 - However there are no return addresses or frame pointers on the heap
 - We can still exploit buffer overflows on the heap to manipulate control flow
**C++ Object Layout**:
![[cpp_object_layout.png|400]]
 - Inside the instance of the object that contains all the virtual functions and their implementations
 - Laid out this way to support dynamic method dispatching (dynamic binding of virtual methods)
 - This can be exploited by making your own table, buffer overflow the `vtable ptr` to point to your table.
	 - When this function is called, it will go to the `vtable`, which points it to your table to be executed
	 - Overflow the heap buffer so that the `vtable ptr` of a nearby object is overwritten to a table of shellcode function pointers
![[cpp_object_layout_evilt.png|400]]

### Heap Spraying
 - Problem: The heap is rather large, hard to predict where the shellcode will end up
 - Solution: Allocate many large memory blocks, place NOP sled + shell code in each
	 - If we fill enough memory, then a randomly chosen memory address probably points into a NOP sled
```c
<script language="text/javascript">
	shellcode = unescape("%u4343%u4343%u4343...");
	var nop = unescape("%u9090%u9090");
	while (fullblock.length < 0x100000) {
		nop += nop;
	}
	sprayContainer = new Array ();
	for (i = 0; i < 1000; i++) {
		sprayContainer[i] = fullblock + shellcode;
	}
</script>
```

### TOCTTOU
 - Time Of Check To Time Of Use
	 - **Check**: Establish some precondition
	 - **Use**: Act, assuming precondition is (still) satisfied
 - Essentially, a race condition against the attacker
 - Dangers: Validating if a user can access a file, and then opening the file
	 - The file can be switched out between checking and using the file
```c
void main() {
	int fd;
	// N.B.: setuid program; check if
	// user has permission to read “foo”
	if (access(“foo”, R_OK) != 0)
		exit(-1); // Danger, Will Robinson!

	// symlink("secret", "foo")

	fd = open(“foo”, O_RDONLY);
	//...
}
```
 - Attack program must run concurrently with victim, switch link at precisely the right moment
**The Fix**:
 - Idea: Force victim program to perform an expensive I/O operation
	 - While waiting for I/O to complete, victim will yield CPU to attacker, giving an opportunity to switch symlinks
 - But how:
	 - Make sure file being accessed is not in file system cache
	 - Force victim to traverse very deep directory structures
 - Symlink attack: Each symlink directing to a huge number of other symlinks and inodes, causing the executable to sleep until the intended file is fetched
	 - While it is traversing the maze to check if the file is safe to open, you can replace the first symlink.
	 - It will see that the original file is safe to open, then goes to open the symlink again which is now pointing at an evil file
**Defenses**:
 - When performing privileged actions, ensure all access control information remains constant between time of check and time of use
	 - Keep a private copy of requests so it can't be altered
	 - When possible, act directly on object, not on some level of indirection
		 - Make access control decisions based on file handles, not filenames
	 - Use locks to ensure state cannot be changed
