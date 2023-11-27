# 2023-09-22
`valgrind <program>`:  Scans program executables for memory bugs, should run whenever dealing with a program
`gcc -g -o <output> <file.c>`: Compile c code with extra debug information, `valgrind` will tell you extra information from the compiled executable (otherwise it just tells you the error exists, not anything about it)
`strings [-n length] <binary>`: Search a binary for human readable strings (of length >= length)
`gdb <binary>`: Debugger for c code

### 2023-10-13
`env -i` runs the next command as though your environment variables are back to default
 - eg. `env -i ./offbyone`
 - Makes sure the stack is consistent between people running your code

Can pad inputs to programs with similar printf commands
`env -i ./offbyone "$(printf "%64c" '0')"` to pad the param as 64 characters

Keep things in little endian
`\x0b\x2b\xef\xbe\xab\xde\xed\xfe` = `0xfeeddeadbeef2b0b`

### 2023-10-23
 - Examples stored in `~/lecture0f`
`argv_envp_example.c`
 - `int main(int argc, char **argv, char **envp)`
	 - `envp` are environment variables
 - Run programs with `env -i ./<program>` to clear them
	 - `gdb --args env -i ./<program>`
		 - gdb sets some environment variables when it starts, this doesn't play nice with rerunning the program
 - gdb: `p argv` after breakpoint returns pointer to list of pointers
	 - `p argv[0]` will print the data in `argv[0]` (including the pointer to it)
	 - `x/10s <0xaddress>` prints the next 10 strings after the given address
		 - environment variables are stored after parameters
 - `info frame` prints frame data
`fake_argv0_example`
 - You can just set `argv[0]` to be something different
 - You can set a symlink to make it think its name is different (`fake_argv0_example_ln.sh`)
`stack_example`
 - x/10xg $rsp
 - Easiest way to specify values on the command line: `$'0x30'`
	 - $ followed by single quotes
`printf_example`
 - `env -i ./printf_example $'a%97$n%p%p%p%p%p%p' $'\x1f\xed\xff\xff\xff\x7f' "" "123456"`

### 2023-10-27
 - The first 6 arguments are passed into registers that are either integral or pointer type
	 - Doubles and floats are passed differently
	 - Everything after those are passed onto the stack
 - For a printf call, that is the string and then the next 5 variables, the next ones are passed onto the stack
 - See `lecture0f/invalid_func_args.c`
```c
printf("%lx, %lx, %lx, %lx, %lx, %lx, %lx, %lx\n",
	0x1111111111111111,
	0x2222222222222222,
	0x3333333333333333,
	0x4444444444444444,
	0x5555555555555555,
	0x6666666666666666,
	0x7777777777777777,
	0x8888888888888888);
printf("%lx, %lx, %lx, %lx, %lx, %lx, %lx, %lx\n");
```
```output
these 8 are given values into printf
1111111111111111, 2222222222222222, 3333333333333333, 4444444444444444, 5555555555555555, 6666666666666666, 7777777777777777, 8888888888888888

these 8 are read from memory
5555555592a0, 0, 0, 0, 8f, 0, 7ffff7dda083, 200000008
```
```gdb
(gdb) x/10i $rip
 - prints assembly calls
(gdb) si
 - step into
(gdb) info registers
 - print values stored in current registers
(gdb) x/10xg $rsp
 - Print values off the stack, these will be the 6th, 7th, + arguments in printf
```
 - The following example, you can see it moving given values into registers
```
(gdb) start
...
Temporary breakpoint 1, main () at invalid_func_args.c:6
6           printf("%lx, %lx, %lx, %lx, %lx, %lx, %lx, %lx\n",
(gdb) si
0x0000555555555155      6           printf("%lx, %lx, %lx, %lx, %lx, %lx, %lx, %lx\n",
(gdb) x/10i $rip
=> 0x555555555155 <main+12>:    push   $0xffffffff88888888
   0x55555555515a <main+17>:    movl   $0x88888888,0x4(%rsp)
   0x555555555162 <main+25>:    push   $0x77777777
   0x555555555167 <main+30>:    movl   $0x77777777,0x4(%rsp)
   0x55555555516f <main+38>:    push   $0x66666666
   0x555555555174 <main+43>:    movl   $0x66666666,0x4(%rsp)
   0x55555555517c <main+51>:    movabs $0x5555555555555555,%r9
   0x555555555186 <main+61>:    movabs $0x4444444444444444,%r8
   0x555555555190 <main+71>:    movabs $0x3333333333333333,%rcx
   0x55555555519a <main+81>:    movabs $0x2222222222222222,%rdx
(gdb) info register
// I do not understand how to see these values in the actual registers
```

### 2023-11-24
```c
void foo() {
	printf("foo invoked by uid: %u\n", geteuid());
}

int main(int argc, char* argv[]) {
	pid_t child = fork();
	if (!child) {
		signal(SIGUSR1, foo);
		while (1);
		// Wait until we can catch any signals, inefficient but works
		/*
		pause();
		pause();
		
		// or
		while(1) pause;
		*/
		// pause(); does nothing until a signal is given, much better than busy looping
	} else {
		uid_t ruid = getuid();
		setresuid(ruid, ruid, ruid);
		foo();

		sleep(1);
		kill(child, SIGUSR1);
		sleep(1);
		kill(child, SIGUSR1);
		sleep(1);
		kill(child, SIGKILL);
	}
	return 0
}
```
```
>>> ./setuid
foo invoked by uid: 1011
foo invoked by uid: 1058
foo invoked by uid: 1058
```
 - To share memory between processes:
	 - malloc won't work as each process has its own memory space
	 - https://man7.org/linux/man-pages/man2/mmap.2.html
```c
// Define the shared memory
char * shared_memory; // This should be a global var
shared_memory = (char *)mmap(NULL,
							 4096,
							 PROT_READ|PROT_WRITE,
							 MAP_SHARED|MAP_ANONYMOUS,
							 -1,
							 0);	

// Now children can print into shared memory
fprintf(shared_memory, "foo");

// And then the parent can print the shared memory at a future date
printf("%s", shared_memory);

// And then you should always unmap your shared memory at the end
munmap(shared_memory, 4096);
```