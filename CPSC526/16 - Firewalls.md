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
	 - Source & Destination Port
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

**Stateful Packet Filters**:
 - Most common type of packet filter today
 - Firewall maintains per-connection state
	 - States: *new* or *established* connection
 - When a packet is sent out, firewall records it in an internal state table
 - When an inbound packet arrives, it can be looked up and associated with a state
 - Most firewalls have limited memory, this can be used for DOS attacks
 - Solves many problems of simple packet filters
	 - Can handle UDP query/response, can associate ICMP packets with connection
 - Still not able to handle more complex protocols, such as RPC
	 - Although many firewalls come with extra tools (helpers) to handle more complex protocols

**Network Address Translators**:
 - Many firewalls have NAT functionality built in
 - Translates source address/port numbers
 - Hosts behind the firewall can have unrouteable IP addresses (private range)
 - Original purpose was to cope with limited number of global IPv4 addresses
 - Can be used to add a little bit of extra security
	 - The addresses behind the firewall can be hidden from the attacker
	 - Makes network reconnaissance more difficult

**Application Layer Firewalls**:
 - Inspect packets at application level
 - Can understand the contents of the packets better
	 - But does not replace packet filters
 - Example: Web Application Firewall (WAF)
	 - Understands HTTP protocol
	 - Can do input validation
	 - Could do regex whitelisting/blacklisting
		 - Can prevent SQL injection and XSS attacks
	 - Popular open source WAF: https://modsecurity.org/

**Personal and Distributed Firewalls**:
 - Dedicated firewalls rely on topological assumptions (require dedicated hardware)
 - Instead, why not install protection on the end system and let it protect itself
 - A simple firewall software is installed on every host,
	 - *inside*: is the host
	 - *outside*: is everything else
 - Rules can be set by an individual user (personal firewall), or administrator (distributed firewall)
 - Many personal firewalls allow rules to be configured per application

**Firewall Evasion**:
 - Many draconian administrators/organizations only allow HTTP
 - Consequently, a lot of newer software can be configured to run over HTTP ports
 - Since HTTP usually gets through most firewalls, firewalls are increasingly less and less effective
 - But not useless, they still offer good amount of security for not a lot of extra cost

**Firewall Access Rules**:
 - Simple Packet Filter: IP addresses, ports, TCP flags
 - Stateful Packet Filter: Also connection states
 - Application Level: Understanding and filtering at application level protocols, based on packet contents
 - Circuit Level Gateway: User identity (authentication)
 - Plugins/Helpers: Time of day, rate of requests, number of unsuccessful logins
 - Additional features: Selective logging

**Linux Firewalls**:
 - `netfilter`: A framework inside the Linux kernel, extensible networking functionality
	 - Has a set of hooks for which kernel modules can register actions
	 - Can be used to implement firewalls, NAT, port translation
 - `iptables`: Set of modules & related user space programs to manipulate firewall rules
	 - Example: Allow all incoming SSH
	   `$ iptables -A INPUT -p tcp --dport 22 -j ACCEPT`
 - `nftables`: Newer generation of iptables
	 - Example: Allow all incoming SSH
	   `$ nft add rule inet global input tcp dport 22 accept`
 - UFW: Uncomplicated firewall
	 - Command line frontend for iptables, meant to be simpler for novice users
	 - Example: Enable firewall, allow ssh access, enable logging, check status of the firewall
```bash
$ sudo ufw allow ssh/tcp
$ sudo ufw logging on
$ sudo ufw enable
$ sudo ufw status
Firewall loaded
To                  Action  From
--                  ------  ----
22:tcp              ALLOW   Anywhere
```

### Virtual Private Network (VPN)
 - Allows private networks to be safely extended over the internet
 - Creates virtual connection, usually through encrypted tunnels
 - Implementations usually based on IPSec or SSL/TLS
 - If encrypted: Provides data confidentiality, integrity, and authentication to all traffic
 - From user's perspective, when connected via VPN, remote resources are available the same way as if connected locally
 - Implemented on many modern routers
 - Many open source software implementations available (OpenVPN)
 - Require OS support, but do not require any special application support

**VPN Types**:
 - Point-to-Point
	 - Single host connects remotely to a private network
	 - Example: An employee accessing company resources from home
 - Site-to-Site
	 - Provide a secure bridge between two or more physically distant networks
	 - Example: Can make two offices appear to be on the same local network

**Why Use a VPN**:
 - Access business network at home
 - Access home network while travelling
 - Hide browsing/communication activity, including IP address, from your ISP
 - Access geo-blocked websites
 - Bypass internet censorship

**Issues with VPNs**:
 - Only protects communication between you and VPN server
	 - Your activity on the website may still be recorded
	 - Even if communication can't be easily linked/traced to you
 - Must trust the VPN server
 - Using VPN may arouse suspicion, may even be illegal
