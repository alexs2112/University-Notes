### Security Triad
 - Must have at least these 3 properties
	 - Confidentiality
	 - Integrity
	 - Availability

**Confidentiality**:
 - Non-public information is accessible only to authorized parties
 - Stored (at rest) or in transmission (in motion)
	 - Technical means: Encryption
	 - Procedure means: Offline storage in secured sites (physically guarded or locked)
 - Example: Only you should be able to read your emails

**Integrity**:
 - Data, software, and hardware remains unaltered
	 - Checksums to detect this
	 - Preventing changes is harder
	 - Includes integrity of people (bribery, blackmail)
 - Sometimes prevention is impractical, may have to settle for detection
 - Example: Nobody but you should be able to delete your email

**Availability**:
 - Information, services, and resources can be used when you need it
 - Protect against intentional deletion or denial of service (DoS)
 - Most difficult to achieve
 - Example: You should have 24/7 access to your emails

**Authorization**:
 - The above are not sufficient on their own, many other properties are required for security
 - Resources accessed only by authorized entities
	 - Approved by (resource) owner
	 - Achieved by access control  mechanisms (passwords, keycards)

### Security Policies and Attacks
 - Security protects *assets* (information, software, hardware, computing, communication services)
 - A *security policy* specifies system's rules and practices
	 - What is and is not allowed
	 - Determined by owners
 - A *security mechanism* implements a security policy
	 - Ideally enforces the rules outlined in policy
	 - Can include protocols humans should follow (locking valuables in a safe)
 - Security policies have assumptions
	 - Locked compartments can only be accessed by owner
	 - Locks are strong, the user knows how to use a lock

**Security Mindset**:
 - Security mechanisms are created to implement a policy, you need to think of it the other way around
 - Every security mechanism *implies* a policy objective
 - When you see a mechanism:
	 - Figure out the policy
	 - Figure out which assumptions are wrong
	 - Design an attack

### Theoretical Security
 - System has states
 - Policy defines with states are authorized/secure and unauthorized/insecure
	 - eg. "Lock the door when nobody's home" policy
	 - Four states defined via two binary variables:
	 - `bool someone_home, door_locked;`
 - Policy is violated if the system moves into an unauthorized state
 - Goal of a security mechanism is to prevent any action that would transition from secure state to an insecure state
![[house_security_states.png|400]]
```c
struct State { int n_people = 0; ... };

bool perform_action(Action &action, State &state) {
	if (action == ARRIVE) {
		state.n_people++;
		return true;
	}
    
	...
	
	return false;
}
```

**Security Attack**:
 - Deliberate action, if successful it causes a security violation
 - Attack vector is a sequence of steps leading to security violation
 - Attacks exploit vulnerabilities
	 - Misconfigurations
	 - Unsafe defaults
	 - Implementation flaws
	 - Design flaws
 - Source of attack (threat agent) is called adversary (theory) or attacker (systems)

**Security Threat**:
 - Any combination of circumstances and entities that may harm assets through a security violation
 - The mere existence of a threat agent and a vulnerability do not imply an attack
	 - Indifference, insufficient incentive, insufficient resources
 - Attacker has a goal and a budget
	 - Goal: Extract data, deny service, tampering with data, causing mischief ...
	 - Budget: Time, money, abilities ...

**No Perfect Security**:
 - Security violations have causts
 - Security countermeasures or protections have costs
 - Risk assessment analyzes these factors to estimate risk
 - Quantitiative risk assessment computes numerical estimates of risk
	 - Not a perfect science, roughly `risk = probability of security violation * damage`
	 - Probability & damage are estimates
 - Qualitative risk assessment ranks or orders risks
	 - Very low to very high for probability and cost
	 - Establish priorities for fixing vulnerabilities
