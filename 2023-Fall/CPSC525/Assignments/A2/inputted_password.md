 - There is an off-by-one error when `fgets` is called
```c
// pseudo.c:274
MAX_PASS_LENGTH = 32;
...
char inputted_password[MAX_PASS_LENGTH];
...
fgets(inputted_password, MAX_PASS_LENGTH+1, stdin);
```
 - 33 characters can be written into the 32 byte long buffer
 - `fgets` takes the string and end it with a null terminator, so this will always change the least significant bit of `euid` to be 0 (change `euid[0]`)
 - This also makes the next `inputted_password` keep reading until 32 chars, even though your `\n` from the previous attempt will randomly show up
	 - I don't think this is relevant
```
(gdb) p inputted_password
$6 = "00000000\n\000", '\060' <repeats 22 times>
```
 - `255 = ff`, overwriting the least significant digits will set the euid to 0
	 - Anything > 255 will not work?
```
(gdb) p euid
$1 = {255, 2028}
(gdb) n
password for VladimirRootin: 1234567890123456789012345678901234567890
275                             attempts++;
(gdb) p euid
$2 = {0, 2028}
```
 - I have no idea what to do with this but it is here
