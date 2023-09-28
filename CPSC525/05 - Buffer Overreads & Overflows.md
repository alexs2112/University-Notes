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
