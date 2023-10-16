### `-z execstack`
 - Disables non-executable stack defense (generally ill-advised)

### Non-Executable Stack (W+X)
 - Prevent shellcode from running by marking stack (and/or heap) as non-executable
	 - NX (no execute) bit set in Page Table Entry (PTE)
		 - Intel marks this as the XD (eXecute Disable) bit
		 - AMD markets this as the EVP (Enhanced Virus Protection) bit
		 - ARM calls it the XN (eXecute Never) bit
 - Alas:
	 - Some legacy code requires executable stack
	 - Some code (JIT) requires executable heap
