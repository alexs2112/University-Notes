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

