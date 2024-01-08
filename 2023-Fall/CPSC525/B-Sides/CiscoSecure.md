I have been stuck in appointments for most of BSides this year and have had very limited time to join presentations remotely. There was supposed to be another presentation at 4-5 on Friday that I was able to make (this would have been my 6th presentation and report) but I think they got the scheduling wrong because it was already finished when I joined.

These notes are from a recording of BSides 2022 instead, found here: [CiscoSecure - BSides Calgary](https://www.youtube.com/watch?v=yY2B246eYc8&list=PL_bQvKglE89BD2WX9AOn_MplMjXiUP3Xb&index=10&ab_channel=BSidesCalgary)

### Defensive Outcomes Through Risk-Based Cybersecurity:
 - Risk-based cyber security distills top managements risk reduction into:
	 - Precise & Pragmatic implementation programs
	 - Clear alignment from the board to the front line
	 - Optimizes Defensive Layers for risk reduction & cost
 - Affects how we design and deploy security controls over an enterprise
	 - Following the risk-based approach, a company will be able to prioritize where these controls are built
	 - Increasing efficiency as they build appropriate controls for the worst vulnerabilities instead of attempting to cover everything with limited resources.

**Practical Approach**:
 - TBS: Time-Based Security
 - Quantitative model describing effective security systems, originally published in 1999
 - Focuses on describing a security system as the union of Protection, Detection, and Response (PDR)
	 - When P > D + R then this system is effective, otherwise when P < D + R then the system is defective

**Defender**:
 - Focus on building appropriate controls for the worst vulnerabilities to defeat the most significant threats
 - Anticipate, Identify, and Confront these vulnerabilities
 - Need to understand relationships between observed datapoints to decide what actions counteract the threat
	 - They don't only see isolated symptoms, they comprehend the systematic impact from threats
 - Defenders need sufficient context to take effective actions to degrade the impact of the threat
	 - Context: Circumstances forming the scenario, in terms of which it can be fully understood and evaluated

**Expressive Threat Capabilities Model**:
 - 13 specific dimensions within a computer system that an attacker can be able to abuse
	 - Device, Group, Identity, Filesystem, Memory, Registry, Network, etc
 - An intensity range represented as different offensive actions that an attacker can make
	 - Execute, Read, Enumerate, Write/Create, Delete, Encrypt
	 - An adversary begins to move up in intensity as they begin to attack more systems
	 - Example: They may be able to read memory, which allows them to execute system calls and enumerate processes.
 - This has a corresponding counteract range of defensive actions the defender can take
	 - Observe, Detect, Disable, Restore, Restrict, Block
	 - Example: The adversary attempts to gain privileges and the defender can restrict their access in response.
	 - Making these defensive actions can change outcomes based on how far the adversary has gotten.
		 - Restricting access before an attack has been made can be seen as proactive/preventative, whereas restricting access during the attack could be seen as reactive or containing.

### Summary
 - Technology must afford the flexible & granular access to conduct technical actions that formulate defensive plans
 - Defenders must evaluate "when" the technology capabilities are most effective during the attack lifecycle
 - Risk-Based cybersecurity enables precise and pragmatic implementations of effective cyber programs
 - Time-Based Security (TBS) provides a practical approach to designing effective and measurable security systems
 - Defenders require context to pursue effective security system design, measured with TBS (P > D + R)
	 - Defenders use context to learn, understand, and evaluate defensive actions (controls) against the threat's impact
 - Defenders need technology that affords granular and flexible usage of controls in order to design effective security systems
