### Fallacy #1
**A system is either secure or it is insecure.**
 - Security is a gradient
 - No such thing as a "perfectly secure" system
	 - All systems are vulnerable to attacks
	 - Interested in the *level* of security a system provides

### Fallacy #2
**There has never been an attack; therefore, there never will be an attack.**
 - The above reasoning is intuitive but incorrect
	 - Equivalent: "I've never had cancer, so I do not need to avoid carcinogens"
 - Problems:
	 - Maybe you have been attacked and didn't realize
	 - Maybe the first attack is coming tomorrow
 - Capabilities, incentives, and context evolve over time

### Fallacy #3
**We use proprietary algorithms! The bad guys will never figure out how to attack us!**
 - Bad guys can learn the algorithms
	 - Insiders, consultants, dumpster divers, corporate espionage, reverse engineering
 - Security through obscurity
	 - Proprietary algorithms have a terrible track record
	 - You may not be smarter than the sum total of all experts

### Fallacy #4
**We're secure because we use standardized algorithms like RSA and AES.**
 - Using standardized algorithms is good but insufficient
 - Analogous to saying your home is impenetrable because you have a standardized door lock
	 - What about the windows?

### Fallacy #5
**We've addressed all known security concerns, so our system is now secure.**
 - Counterexample: Diebold voting machines
	 - 2003: Serious security problems identified
	 - 2004: Diebold introduces defenses against specific problems
	 - 2004: Fixes found to introduce new security problems
	 - 2007: Diebold patches the issues their last patches created
	 - 2007: Latest patches found to introduce more vulnerabilities
	 - 2007: Diebold changes its name...

### Fallacy #6
**Our system is secure because we had it audited by third-party consultants.**
 - History says otherwise
	 - Diebold machines are regularly audited, yet researchers routinely find problems
 - It can be hard to misuse crypto bad enough to fail Apple's AppStore "audits"

### Fallacy #7
**In order to increase security, we'd have to decrease safety and/or usability.**
 - No you wouldn't
 - Balancing these goals is challenging, not impossible
 - To make educated decisions and arguments:
	 - Explore solution space
	 - Gauge what is possible
	 - Assess levels of security and usability provided by each option

### Fallacy #8
**We don't need client devices to be secure, because our backend is heavily fortified.**
 - That’s great! Let me congratulate you with this handmade wooden horse!
 - Security is only as strong as the weakest link

### Fallacy #9
**Only sophisticated adversaries will be able to successfully attack our system.**
 - Attacks only get easier to mount over time
 - Some bad guys are rather sophisticated
 - Sophisticated attackers make tools, unsophisticated attackers use them

### Fallacy #10
**Insiders are not going to be adversaries.**
 - r/antiwork
 - Humans are alarmingly sentient beings

### Fallacy #11
**We've thought of everything.**
 - No

### Fallacy #12
**Our system is secure because we followed a checklist and are PCI DSS compliant.**
 - No checklist is sufficient
	 - Arguably encourage doing the "bare minimum"
 - Certifications -> last decades bare minimum

![[security_tips.png|400]]