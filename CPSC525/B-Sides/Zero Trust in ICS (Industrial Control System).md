### Operational Technology (OT) Cybersecurity
 - Component for protecting uptime, security, and safety of industrial environments and critical infrastructure
 - A focus on OT Cybersecurity is intended to protect operating technology assets, systems and processes in a way that comply with strict regulatory requirements
### Zero Trust
 - Firewall vendors provide zero trust network access (ZTNA)
 - Identity vendors use people and identities as a single control point
 - Chat GPT: Never trust, always verify the importance of identity verification and identity + integrity of users and devices
 - Often driven by capabilities rather than requirements or outcomes
 - System architecture along with passive and active defenses against OT Cybersecurity threats provide the highest value for the lowest cost of implementation

**Defensible Architecture**:
 - Supports Visibility, log collection, asset identification, segmentation, industrial DMZs,  and process communication enforcement
 - High value for a low cost
 - Start at the IT/OT/Internet boundary
 - Must understand and document requirements of both cybersecurity and business operations

### ICS Architecture - Key Tenets
 - No Internet in OT: Keep dedicated business computers for email, internet, etc
 - Create strong enforcement boundaries: Separate authentication for all ICS access, secure file transfer in and out of OT
	 - Block all communication by default, permit what is required. Monitor and log all communication in both directions
 - Leverage AD (Active Directory for management of organization network) to authenticate and secure workstations
	 - Keep AD completely independent of the business

### Critical Controls for ICS Cybersecurity
 - ICS Incident Response
	 - Operations informed IR plan focused on system integrity and recovery during an attack
 - Defensible Architecture
	 - Supporting visibility, log collection, asset identification
 - ICS Network Visibility and Monitoring
	 - Continuous network security monitoring of ICS environment
	 - Continuous network security monitoring of the ICS environment, leveraging choke points and configuration groups to identify vulnerabilities
 - Secure Remote Access
	 - Identification and inventory of remote access points and allowed destination environments
	 - Key Components: Distinct credentials, MFA, file transfer mechanisms, access limited by user/group (zero trust), and detailed auditing.
 - Risk Based Vulnerability Management
	 - Understanding cyber digital controls in place that aid in risk-based vulnerability management decisions
		 - This aids in patching the vulnerability, mitigating the impact, and monitoring for possible exploitation

### Summary of Vulnerabilities & Patching
 - Not all vulnerabilities need to be patch
	 - Start patching where attacks originate
 - Vulnerabilities don't matter if commands are accepted
 - Easier to patch Windows than proprietary software
 - Leverage redundancy and virtualization
	 - Prioritize what needs to be done as it can be difficult to patch
