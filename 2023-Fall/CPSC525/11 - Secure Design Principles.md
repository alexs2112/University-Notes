### #1 Economy of Mechanism
 - A simpler design is easier to analyze, test, and validate
	 - Prioritize simplicity and necessity
 - Minimizes attack surface
 - Well-exercised code tends to be less fragile
	 - More code paths -> less exercise per path
 - Just do a single simple thing really well, then you can string together a bunch of these simple things together in linux to do what you want
### #2 Fail-Safe Defaults
 - Base access decisions on permission rather than exclusion
 - When deciding what to allow, the default should be to not allow it
	 - Specifically add rules and permissions to allow what you want to allow
 - The reverse (finding reasons to exclude) is risky
	 - You might not think of all reasons
 - Easier to find and fix errors on a whitelist
	 - Legitimate users denied access will complain
	 - Illegitimate users granted access probably won't
 - On catastrophic failure, ensure the system defaults to a safe state

### #3 Complete Mediation
 - Every access to every asset must be checked for authority
 - Access rights are completely validated every time an access occurs
	 - TOCTTOU attacks
	 - Authority may change
	 - Access levels may change
	 - Attacker might bypass earlier validation code

### #4 Open Design
 - The design should not be secret
 - Security mechanisms should not depend on the ignorance of potential attackers
 - This principle reflects recommendations by the 19th century cryptographic writer Auguste Kerkchoffs, as well as Claude Shannon's 1948 maxim:
	   "The enemy knows the system"
 - Fine to leverage unpredictability, just don't rely on it
	 - No need to publish blueprints, vacation schedule
 - Kerkchoff's Principle:
	 - It must not require secrecy, and it can easily fall into the hands of the enemy

### #5 Separation of Privilege
 - Where feasible, a protection mechanism that requires 2 keys to unlock it is more robust and flexible than one that allows access to the presenter of only a single key
 - A protection mechanism is more flexible if it requires two separate keys to unlock it, allowing for two-person control and similar techniques to prevent unilateral action by a subverted individual

### #6 Least Privilege
 - Every program and user should operate while invoking as few privileges as possible
	 - Limits damage from error or attacks
 - Minimize interactions among privileged programs
 - Minimize unexpected use of privilege
 - Analogous to the "need to know" principle

### #7 Least Common Mechanism
 - Minimize the amount of mechanism (a) common to more than one user and (b) depended on by all users
	 - Eg. Shared variables
 - Users shouldn't share system mechanisms except when absolutely necessary
	 - Shared mechanisms might provide unintended communication paths or means of interference

### #8 Psychological Acceptability
 - It is essential that the human interface be designed for ease of use, so that users routinely and automatically apply the protection mechanisms correctly
 - Least surprise: Align design with mental model
	 - Beware of designs that require end-user training

### Use Time-Tested Tools
 - Prefer established methods to accomplish security
	 - Protocols, primitives, toolkits, paradigms...
 - Heavily scrutinized tools are less likely to be fatally flawed
 - Do not roll your own crypto
 - Reinventing the wheel is a great way to learn, but a poor way to achieve security

### Evidence Production
 - Logging systems can promote accountability
	 - When sudo used by an authorized party
	 - When somebody logs in to a server
	 - When somebody plugs in a USB drive
	 - When somebody accesses a file or network resource
	 - When file permissions or special directories are modified
 - Helps discover attacks, determine effect
 - Help build intrusion-detection systems

### Reluctant Resource Allocation
 - Be reluctant to expend effort or allocate resources
	 - Especially with unauthenticated, external agents
 - Be reluctant to elevate privileges for, or act on behalf of, another agent
 - Place burden of proof on those who initiate communication
	 - Remember complete mediation

### Know Thy Enemy
 - Security threats and defenses defined relative to an adversary
 - Adversary wants to break security
	 - Has specific goals/motivation, budget, capabilities, (inside) knowledge
 - You must understand potential attackers to make wise security decisions
