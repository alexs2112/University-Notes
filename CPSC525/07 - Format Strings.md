### Off-by-One Faults
```c
void bar(const char* str) {
	char buf[256];
	strcpy(buf, str); //Overflow by at most one byte
}
void foo(const char* str) {
	if (strlen(str) > 256) {
		exit(-1);
	}
	bar(str);
}
```
 - `strlen` ignores the null terminator, so you can overflow `buf` by at most one byte
 - Overflow doesn't reach the return address, stack remains unsmashed
 - Would kill one byte of the frame pointer
	 - We can write nothing but the null terminator
	 - Will clobber the least significant byte of the frame pointer and replace it with 0
		 - Points to lower memory
	 - Might then point partway into the next frame, instead of the start of it
	 - When the current stack frame pops, it will point the frame pointer into the buffer we just overflowed
		 - Can make the buffer a synthetic frame that has been injected into memory

### Two's Complement
```c
int printcat(char* str1, char* str2, unsigned short size1, unsigned short size2) {
	char buffer[16];
	unsigned short lentotal = size1 + size2;
	if (lentotal > 16)
		return -1;
	strncpy(buffer, str1, size1);
	strncpy(buffer + size1, str2, size2);
	printf("%s\n", buffer);
	return 0;
}
void main(int argc, char* argv[]) {
	printcat(argv[1], argv[2], atoi(argv[3]), atoi(argv[4]));
}
```
 - If you input two sufficiently large strings then the sum of their sizes will wrap around to less than 16, this causes a buffer overflow
	 - Should add up to 65536 to 65536 + 16
**Integer Overflows (and Underflows)**:
 - Machine integers can only take on values in a finite range
	 - Might not match programmers mental model
 - Some overflow faults turn into security failures
	 - Pointer arithmetic (array indexing)
		 - Read/write memory outside of array bounds
	 - Memory allocation
		 - Allocate buffer smaller than expected -> Buffer Overflow

### Format-string Vulnerabilities
```c
void print1(char* str) {
	printf("%s", str);
}
// Versus
void print2(char* str) {
	printf(str);
}
// You should never do this second one
```
 - `void printf(char* fmt, ...)`
	 - Variadic function: Doesn't know how many arguments it has
	 - Inferred at runtime from format string
```stack
arg3
arg2
arg1
char* fmt
return address
frame pointer
```
 - Example:
	 - input: `printf("Color %s, Number %d, Float %.2f", "red", 123456, 3.1415);`
	 - output: Color red, Number 123456, Float 3.14
	```stack
	(float) 3.1415
	(int) 12345
	(const char*) "Red"
	(char*) "Color %s, Number %d, Float %.2f"
	return address
	frame pointer
	```
 