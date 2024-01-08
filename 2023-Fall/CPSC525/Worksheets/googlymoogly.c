// this is /srv/googlymoogly.c
// gcc -o googlymoogly googlymoogly.c

#include <stdint.h> // uint64_t
#include <string.h> // strlen
#include <stdio.h>  // printf

int main(int argc, char * argv[])
{
	// make a string
	const char foo[] = "Great googly moogly!";
	// print the string
	printf("%s\nfoo: ", foo);
	// print the hex representation of each ASCII char in foo
	for (int i = 0; i < strlen(foo); ++i) printf("%x", foo[i]);
	printf("\n");

	// TODO 1: use a cast to make bar point to the *exact same address* as foo
	uint64_t * bar = (uint64_t)&foo;

	// TODO 2: print the hex representation of bar[0], bar[1], bar[2]
	printf("bar: %x%x%x\n", bar[0], bar[1], bar[2]);

	// TODO 3: print strlen(foo) and sizeof(foo) and sizeof(bar)
	printf("baz: %zu =?= %lu =?= %lu\n", strlen(foo), sizeof(foo), sizeof(bar));

	return 0;
}
