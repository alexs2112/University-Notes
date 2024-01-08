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
 - Examples of ways to format `printf`
```
("%010x\n", 1) = 0000000001

("%2$s\n", "first", "second", "third") = "second"

("%60$x\n", 1, 2, 3, ..., 64) = 3c

(%d%n -> ", 31337, &digits)
("%d", digits) = 31337 -> 5

("%s%s%s%s%s%s%s") = Segmentation fault (core dumped)
// Making the code seg fault shows the code is exploitable
// This keeps assuming data on the stack is a pointer up until it crashes

("%p %p %p %p %p %p %p %p") = 0x7fffffffe4a8 0x7fffffffe4a8 ...
// Printing memory addresses
// They should remain consistent until you hit the canary (which will change every time). After that should be the frame pointer and return address
```
 - Format String => Buffer Overflow
```c
void err(char* fmt_string) {
	char outbuf[512];
	char buffer[512];

	// sprintf prints stuff into the buffer
	sprintf(buffer, "ERR Wrong command: %400s", fmt_string);
	sprintf(outbuf, buffer);
	// The first call is fine, the second call is hugely problematic
	// If you insert format string calls into fmt_string, they will still be there after the first call.
	// The second call will then interpret the inserted set of format string calls	
}

Assign: fmt_string = "%497d\x3c\xd3\xff\xbf<nops><shellcode>"
// Burns 497 chars to overwrite the full buffer, everything afterwords overflows it
// Write 0xbfffd33c over return address
	// Address 0xbfffd33c chosen to reside within NOP slide
// Executes the shellcode
```

### Format String Vulnerabilities
 - http://phrack.org/issues/49/14.html
 - These are an example of a more general phenomenon

### User-Supplied Data
 - Inputs to programs are often supplied by untrusted users
	 - web applications, authentication dialogs
 - Users sometimes mistype the data they input
**Input Mediation**:
 - *Mediation*: The process of identifying and (possibly) correcting data input by users
 - The data may:
	 - Not be well-formed: DOB <- 1980-04-31
	 - Contain unreasonable values: DOB <- 1876-10-12
	 - Be inconsistent: DOB <- 2003-06-08; Age <- 21
 - Malicious users might craft special inputs to alter the intended behaviour of the program
	 - `msg <- "%065512x\xde\xad\xbe\xef%13$n"`
		 - Format string vulnerability?
	 - `DOB <- 98764890217508983473801928374`
		 - Buffer overflow?
	 - `length <- (1ULL<<63)-17`
		 - Integer overflow?
**Example**:
```php
<?php
if (isset($_GET['ip'])) {
	$ip = $_GET['ip'];
	$output = shell_exec("ping -c 3 $ip");
	echo "<pre>$output</pre>";
}
?>
```
 - The user enters a value which is stored as an argument to ping, then executed as a shell command
 - Inputting something like `8.8.8.8 && head /etc/passwd` it will ping a lot of extra data
**Shellshock**:
 - aka Bashdoor (September 2014)
 - Fault in the Unix Bash shell prior to 2014
 - Vulnerable servers processed input from web requests
	 - Passed (user-provided) environment variables to CGI script
	 - Maliciously crafted environment variables exploited a bug in Bash to execute arbitrary code
 - Within hours of disclosure, botnets were active exploiting the vulnerability
**Other Injection Vectors**:
 - User inputs
 - Cookies
 - Environment variables
 - Stored data
 - ...
**Client-side Mediation**:
 - Many web forms perform client-side mediation
	 - Clicking submit triggers JavaScript code that validates data before sending to the server
 - Relatedly, many websites keep client-side state
	 - Store data in hidden fields, cookies, or URLs
 - Problems:
	 - User can disable JavaScript
	 - User can edit hidden form fields, cookies, URLs
	 - User can interact with server using something else (telnet)
 - Useful for friendlier user interfaces, *useless for security purposes*
	 - Always do security-relevant mediation at the server
 - For values entered by the user
	 - Carefully check the values of all fields
	 - Values can be arbitrary -> don't assume text fields only contain valid ASCII

