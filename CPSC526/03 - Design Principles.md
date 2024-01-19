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

**Client-Side Mediation**:
 - Many web forms perform client-side mediation
	 - Clicking "submit" triggers JavaScript code that validates data before sending to server
 - Many websites keep client-side state
	 - Data in hidden fields, cookies, URLs
 - Problems with this:
	 - User can disable JS
	 - User can run arbitrary JS
	 - User can edit hidden form fields, cookies, URLs
	 - User can interact with server using JS console, nc, telnet, etc
 - Useful only for friendlier user interfaces
	 - Useless for security purposes
 - Security-relevant mediation must be done at the server
	 - Server should assume nothing about data received from clients
	 - Any data received by server needs to be sanitized

### DP4: Open Design
 - Don't rely on secret designs or an attacker's ignorance
	 - Security through obscurity is a bad idea
	 - Assume the enemy knows your system
 - In software: Algorithms should be publicly available
	 - More eyes on code = less bugs = less vulnerabilities
	 - Related: Security of open-source vs closed-source
 - But leverage unpredictability if there is no disadvantage
	 - No gain to publish vacation schedule, house blueprints, location & model of your safe

**Kerkchoff's Principle**:
 - *It should not require secrecy, & it should not cause inconvenience when it falls into enemy's hands*
 - Claude Shannon: *The enemy knows the system*

### DP5: Separation of Privilege
 - A protection mechanism that requires 2 keys to unlock is more secure than one that requires a single tree
 - Single accident, deception, or breach of trust is insufficient to compromise the system
	 - Double the work of the attacker

### DP6: Least Privilege
 - Analogous to the "need to know" principle
 - Programs and users should operate with as few privileges as possible
	 - Limits damage from mistakes and attacks
 - Programs that need elevated privilege:
	 - Run with lowest privilege for as long as possible
	 - Upgrade privilege only for as long as necessary
	 - Switch back to lower privilege as soon as possible

### DP7: Least Common Mechanism
 - Shared mechanisms might provide unintended communication paths or means of interference
 - Shared mechanisms need the most scrutiny
 - Minimize the number of mechanisms
	 - Common to more than one user, and
	 - Depended on by all users
 - Don't use/force shared mechanisms for convenience
 - Programming examples: Shared variables, global variables, shared storage

### DP8: Psychological Acceptability
 - Interface should be designed for ease of use, so that users routinely and automatically apply the protection mechanisms correctly
 - Avoid accidental irreversible errors
 - Example: Do not enforce ridiculous password policies

### DP9: Time-Tested Tools
 - Rely on established methods to accomplish security
	 - Protocols, primitives, toolkits
 - Heavily scrutinized tools are less likely to be flawed
	 - "Don't roll your own crypto"
	 - Example: Use libcrypto, libopenssl
 - Reinventing the wheel is a great way to learn, not a great way to achieve security

### DP10: Evidence Production
 - Log system activities that can promote accountability
	 - When sudo is used, when someone logs in, when someone plugs in a USB stick, when somebody accesses a file, when certain files or special directories are modified, etc
	 - Have decoy "honey" files that should never be accessed
 - This helps discover attacks, determine effect
 - Help build intrusion-detection tools

### DP11: Remnant Removal
 - Remove all traces of sensitive information ASAP
	 - Don't store password/keys in RAM after done using them
	 - Don't save decrypted data to permanent storage
 - Securely delete files you don't want
 - Don't log all interactions with a program
 - Have a plan for sanitizing long term logs
	 - Could find their way to a backup medium, eventually into a dumpster

### DP12: Reluctant Allocation
 - Be reluctant to expend effort or allocate resources
	 - Especially with unauthenticated external agents
 - Be reluctant to extend privileges or act on someone's behalf
 - Place burden of proof of identity on those who initiate communication
	 - Protects against DOS attacks
