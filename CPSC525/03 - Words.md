**Asset**: A thing we want to protect (software, hardware, data)
**Vulnerability**: A weakness that could potentially be exploited to cause loss or harm (fileserver that does not authenticate its users)
**Threat**: A loss or harm that might befall a system (personal files are revealed publicly)
**Attack**: An action that exploits a vulnerability to effect a threat (telling a fileserver that you are a different user in order to read or modify that users files)
**Control**: Removing or reducing a vulnerability (requiring users to authenticate with a password)

### Writing Secure Programs
 - All sufficiently complex programs have bugs -> all sufficiently complex, security-relevant programs have bugs

### The Three Fs
 - **Flaw**: A problem with a program
	 - A security flaw is a flaw that affects security in some way
	 - Flaws come in two flavours: Fault, Failure
 - **Fault**: A mistake behind the scenes (a potential problem)
	 - An error in the code, data, specification, process, etc
 - **Failure**: Something that actually goes wrong
 - Flaws are sometimes called **defects**, many kinds of flaws/defects:
	 - Just plain wrong, missing requirements, extra implementations, errors, bugs
 - Every failure stems from a fault, but not every fault manifests as a failure
 - Finding and patching faults: *Penetrate and Patch*
	 - Patching sometimes makes things worse, pressure is higher, planning and testing is lower
	 - Narrow focus on observed failure vs broad look at underlying fault
	 - The patch may introduce new faults, here or elsewhere

### Extra Behaviour
 - Software specs usually say what the program must do
 - Often implementers add additional functionality
 - From a security & privacy perspective, extra behaviour is bad
 - When implementing a security or privacy relevant program, you should consider "and nothing else" to be implicitly added to the spec
