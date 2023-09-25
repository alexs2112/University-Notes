# 2023-09-22
`valgrind <program>`:  Scans program executables for memory bugs, should run whenever dealing with a program
`gcc -g -o <output> <file.c>`: Compile c code with extra debug information, `valgrind` will tell you extra information from the compiled executable (otherwise it just tells you the error exists, not anything about it)
`strings [-n length] <binary>`: Search a binary for human readable strings (of length >= length)
`gdb <binary>`: Debugger for c code