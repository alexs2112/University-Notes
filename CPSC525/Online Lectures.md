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
