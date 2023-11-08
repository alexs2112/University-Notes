```c
//pseudo.c:237
snprintf(username, MAX_USER_LENGTH, "%s", argv[1]);
// MAX_USER_LENGTH = 32
// username is a 32 char buffer
// Could probably overflow it with a username of length 32 (no null end)
```
### `printf()`
`pseudo:271`
```c
if (euid[1] != 0) // root needn't authenticate
{
	printf("password for %s: ", username);
	...
}

// check if (either root or) password digests match
if (!euid[1] || !strncmp(expected_digest, actual_digest, DIGEST_HEX_LENGTH)) {
	...
	switch (euid[0])
	{
		case 255: // VladimirRootin
			execvp("/usr/bin/exec_as_VladimirRootin", argv);
			break;
		...
	}
}
```
 - Use printf vulnerability

### Trying to buffer overflow `inputted_password` from `fgets`
After the first attempt of inputting a password:
```
(gdb) info locals
euid = {255, 2028}
inputted_password = "Hello\000\000\000PiUUUU\000\000\000\000\000\000\000\000\000\000\340TUUUU\000"
username = "VladimirRootin\000\000\340\025\375\367\377\177\000\000\235iUUUU\000"
actual_digest = "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
expected_digest = "4252fb208a3bcbb14d46a9be43966219650c38132a43ab4c326c603ccc1dbdc8"
tty = <optimized out>

(gdb) p &euid
$24 = (uid_t (*)[2]) 0x7fffffffed20
(gdb) p &inputted_password
$25 = (char (*)[32]) 0x7fffffffed00
(gdb) p &username
$26 = (char (*)[32]) 0x7fffffffece0
(gdb) p &actual_digest
$27 = (char (*)[64]) 0x7fffffffeca0
(gdb) p &expected_digest
$28 = (char (*)[64]) 0x7fffffffec60
```
 - Each of these addresses are 20 bytes apart
 - Attempt to set `euid[1]` to be `0` (to avoid authenticating the next time) and `euid[0]` to be a user we want
 - Not sure if this will work

### `sha256_hex`
 - This function is weird as fuck
```c
// pseudo.c:118
void sha256_hex(char digest[DIGEST_HEX_LENGTH], char password[MAX_PASS_LENGTH])
{
	unsigned char buf[DIGEST_BYTE_LENGTH];
	char buf2[DIGEST_HEX_LENGTH+1];
	calc_sha_256(buf, password, strlen(password));
	char * c = &buf2[0];
	for (int i = 0; i < DIGEST_BYTE_LENGTH; ++i)
	{
		c += sprintf(c, "%02x", buf[i]);
	}
	memcpy(digest, buf2, DIGEST_HEX_LENGTH);	
}
```
 - Sets up a 65 character buffer as `buf2`, calculates the sha of `password` into `buf`, then creates a string at the location of `buf2` and builds that string in place
 - In theory `buf2` should never overflow
 - Still, very weird