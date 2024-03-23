### Firewall
 - Firewall monitors packets coming from the outside into the network (inbound)
	 - Can also monitor outbound packets (inside to outside the network, less common)
 - Firewall decides which network traffic gets through and which does not
 - Can operate at any protocol level, and in both directions
 - A network barrier between "us" and "them"
	 - Us: Good guys, on private network
	 - Them: Bad guys, on public network
 - Enforces restrictions on communication with the outside world
 - Can be deployed as a software, or on dedicated hardware
 - Has at least two interfaces: One for private network, one for public network
	 - Normally h/w NICs, but could be virtual
 - Offers good amount of security for a relatively low cost
	 - Not perfect, but very cheap
 - Typically set up as a barrier between the LAN and the Internet

**Why Firewalls**:
 - Main motivation: Most software has bugs and security vulnerabilities
	 - Most computers have security holes
	 - Most computers accessible from outside network are security risks
 - Computers connected to the outside world should be protected
 - Firewalls can offer some protection for vulnerable hosts
	 - Based on much less code, hence have fewer bugs
	 - Can be centrally & professionally administered
	 - Are a great place to do network monitoring and logging
	 - Can partition private network into separate security domains, each domain with its own security policy
 - Many modern firewalls combine multiple functionalities
	 - eg. Routing, DHCP, NAT, VPN, other useful services
	 - Check out any recent home WiFi router for examples
 - We use firewalls because we don't know how to write secure and easy to administer software
 - Better network protocols will not eliminate the need for firewalls
 - Even the best cryptography in the world will not guard against buggy code

**Typical Organization Firewall Setup**:
 - Assuming everyone on LAN is a good guy, and bad guys live only on WAN
 - *Demilitarized Zone* (DMZ) contains necessary servers that are potentially dangerous
	 - eg. Mail and Web Servers
 - Hosts on LAN can access DMZ, but DMZ has limited/no access to LAN
 - DMZ is protected from the outside via firewall
 - Usually, two firewalls are used
	 - Or one firewall with three interfaces
 - Internet -> Firewall -> DMZ network -> Firewall -> Internal Protected Network
	 - LAN switches behind each firewall to coordinate traffic between these three zones

**Positioning Firewalls**:
 - Firewalls enforce policy
 - Policies reflect administrative boundaries
 - Internal firewalls between domains
 - Example domains: Administrative, research, students

**Firewall Approaches**:
 - Blacklisting: Block only dangerous traffic
	 - Less disruptive
	 - Not a very good approach in general
	 - Requires sysadmin to be smarter than the attacker
 - Whitelisting: Block everything by default, only allow necessary traffic
	 - Can be very disruptive
	 - Much more secure

**Blocking Outbound Traffic**:
 - Firewalls can limit outgoing traffic as effectively as inbound traffic
 - Many organizations permit all outbound traffic
 - Some organizations decide to limit outbound traffic
	 - Child friendly content in schools or libraries
	 - Preventing exfiltration
	 - Cutting down on social media activities

### Firewall Types
**Simple Packet Filters**:
 - The original firewall
 - Cheap to deploy, does not need sophisticated hardware
 - Individual packets are inspected, then either accepted or rejected
 - Rejection: Either silently ignore (drop) or send error response (reject)
 - Packet fields inspected:
	 - Source & Destination Address
	 - Source & Destination Porrt
	 - Protocol & TCP Flags
 - Mostly works on layer 3, with a little bit of peeking into layer 4 (ports and flags)
 - No notion of state/sessions
	 - Does not work well with protocols like FTP and RPC
 - Handle outgoing connections without state:
	 - If we want to permit outgoing connections we have to permit `reply` packets
	 - To do this without managing state we should only allow inbound traffic with ACK set
		 - From TCP Handshake: SYN, SYN-ACK, ACK, then all packets have ACK set
 - UDP has no notion of connection
	 - If we want any outgoing UDP, we need to allow all UDP packets
	 - But only on safe ports (to services that are secure)
 - ICMP needs special attention
	 - Okay to block some ICMP packets
		 - `ping` (echo reply/request)
		 - `traceroute` (time exceeded)
	 - Probably not okay to block MTU discovery or source quench
 - Rules are usually organized in a table/list
	 - First rule that matches is applied
	 - `x.y.z.0/24 = x.y.z.*`
	 - `x.y.0.0/16 = x.y.*.*`
![[Simple_Packet_Filter_Example_Rules.png|400]]

