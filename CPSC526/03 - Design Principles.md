### DP1: Economy of Mechanism
 - Keep designs small and simple
	 - Easier to analyze, test, and validate
 - Minimize functionality
	 - Disable unused functionality
	 - Disable by default
 - This minimizes the attack surface
 - Well-used code tends to be less fragile
	 - More code paths means less testing per path
 - Example: UNIX design philosophy
	 - Each program does exactly one thing really well
### DP2: Fail-Safe Defaults
 - Use safe default settings
	 - Design assuming they will never be changed
 - Examples:
	 - Firewall blocks all ports by default
	 - Encrypt by default, use HTTPS by default
	 - Traffic lights blink red on failure
	 - Doors unlock during fire alarm
 - Prefer whitelist over blacklists

### DP3: Complete Mediation
 - Every access to every asset must be checked for authority
 - Access rights must be re-validated every tme
	 - Authority may change
	 - Access levels may change
	 - Attacker may have bypassed earlier validation
	 - Note: UNIX file access does not do this (permissions only checked during `open()`)
 - Inputs to programs are often supplied by untrusted users
	 - Eg. Web applications and authentication dialogs can sometimes have mistyped input
 - Verify all received data conforms to expected or assumed properties
	 - Never assume anything about input data
	 - Especially when it is spurious input from the internet
 - Sanitize inputs
