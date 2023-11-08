```c
// fopen_passwd()
...
snprintf(passwd_path, MAX_PATH_LENGTH, "%.243s/etc/passwd", homedir);
...
```
 - This is the only `printf` that allows an extremely large string that we can control
