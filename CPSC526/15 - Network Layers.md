![[Network-Layers.png|600]]
 - HTTP(s), packaged into TCP, packaged into IP, packaged into MAC, sent over the internet
### Internet Layering
 - Internet design is partitioned into layers
	 - Each layer relies on services provided by the layer below
	 - Each layer provides services to the layer above
 - Analogy: Software you write
	 - Code you write
	 - Run-time library
	 - System calls
	 - Device drivers
	 - Voltage levels
 - AKA Protocol Stack
 - Has the layers:
	 - Application
	 - Transport (eg. TCP)
	 - (Inter)Network (eg. IP)
	 - Link (eg. Ethernet)
	 - Physical (eg. Radio Waves)
 - Network packets reflect these layers
![[Network-Packet.png|600]]

**Physical Layer**:
 - Encodes bits to send over a single physical link
	 - Voltage Levels
	 - Photon Intensities (fibre)
	 - RF Modulations
 - Electrical engineering

**Link Layer**:
 - Framing and transmission of a collection of bits
 - Individual messages sent within a single subnetwork
	 - This may involve multiple physical links (Ethernet, Fiber, WiFi)
 - Often supports broadcast transmission, every node receives a frame
 - Typically uses MAC addresses (48-bit integers)

**Network Layer**:
 - Bridges multiple subnets
 - Provides global addressing
 - Provides end-to-end connectivity between nodes
 - Works across different link technologies
 - The link and physical layers can change for each "hop"
 - The data for the network layer and above stays the same

**Transport Layer**:
 - End-to-End communication between processes
 - TCP: Reliable byte stream
	 - Provides guaranteed in-order delivery
	 - Provides congestion control
 - UDP: Unreliable datagrams
	 - Datagram is a single packet message

**Application Layer**:
 - Communication of whatever you want
	 - Write to a stream at one end
	 - Read from a stream at the other
 - Freely structured:
	 - eg. TLS, HTTP, IRC, Fortnite, Minecraft

### IP Packet
**Format**:
![[IP_Packet_Format.png|300]]

**IP Packet**:
 - Has two IP Addresses
 - Destination address:
	 - Unique identifier (locator) for the receiving host
	 - Allows each node (router) to make forwarding decisions
 - Source address:
	 - Unique identifier (locator) for the sending host
	 - Recipient can decide whether to accept packet
	 - Allows recipient to send a reply back to source

**IP Packet Delivery - Best Effort**:
 - At each hop, router looks at destination address
 - Locates next hop in forwarding table
 - Only gives a "I'll give it a try" delivery service
	 - Packets may be lost
	 - Packets may be corrupted
	 - Packets may be delivered out of order

**IP Address Spoofing**:
 - Destination address controlled by socket API (`connect()`)
 - Sender can put whatever they want for IP source address
	 - Does not have to be their actual IP address
	 - Spoofing, Imposturing, Masquerading
 - Source address can only be set with a raw socket
	 - Instead of OS creating TCP/IP headers, the program writes them all
	 - A privileged operation, requires root or `cap_net_raw`
 - Sender can make a packet appear as though it came from elsewhere
	 - Sender won't likely get a reply
	 - If attacker doesn't need a reply, then this is enough to attack
 - If attacker can also eavesdrop on reply, then this is a powerful attackc
 - *Blind Spoofing*: Spoofing without eavesdropping
 - *On Path*: Traffic goes through attacker
 - *Off Path*: Traffic does not go through attacker

**Anti-Spoofing Mechanism**:
 - For end-users, spoofing is easy to detect
	 - Your ISP assigns you an IP address
	 - Your ISP sees all your network traffic
	 - Your ISP can check if your IP matches
	 - Analogy: Letter dropped in Calgary mail box with return address in Edmonton
	 - Reject the packet instead of sending it on network
 - Harder to do between ASes in general however
	 - Analogy: Letter received on a particular airmail flight to a sorting facility
		 - Maybe someone didn't do a check earlier
		 - Maybe they would send you mail but you wouldn't send it to them

**Physical and Link Layer Threats**:
 - *Eavesdropping* (also called *sniffing*)
	 - Subnets using broadcast (WiFi), it's "free"
	 - Any attached NIC (network interface card) can capture communication on the subnet
	 - Cheap "ethernet hubs" worked like this
 - `tcpdump` is a handy command-line tool to do that
 - `wireshark` is a GUI tool that does protocol analysis
 - Any router on-path can look at or export traffic
 - Anyone on-path can "tap" a link
	 - On optical cable: If you bend a wire, without fully breaking it, then some photons will escape and can be read

### Dynamic Host Configuration Protocol (DHCP)
 - A new host doesn't have an IP yet
	 - Doesn't know what source address to use
 - Host doesn't know who to ask for IP address
	 - Doesn't know what destination address to use
 - Host broadcasts a server-discovery message (link layer)
	 - Servers send replies offering an address
1. New Client -> DHCP server: DHCP discovery (broadcast)
2. DHCP Sever -> New Client: DHCP offer
	- Offer contains IP, DNS, gateway router
	- How long client can use them (lease time)
	- DNS resolves hostnames (like gmail.com) to IPs
	- Gateway is router that acts as first hop to reach out to the Internet
3. New Client -> DHCP Server: DHCP Request (Broadcast)
4. DHCP Server -> New Client: DHCP Acknowledgement
 - 3 an 4 are to confirm that's the IP the client will use

**DHCP Spoofing**:
 - Broadcast allows any local attacker to race to reply
 - Attacker reply can give a bad DNS server
	 - Redirect any domain searches to attackers choice
	 - eg. reroute google.com to attacker's computer
 - Attacker reply can give a bad gateway router
	 - Puts attacker on path
	 - MITM to sniff or modify traffic
 - Victim has no idea it is happening
	 - DHCP offer looks legitimate
	 - Multiple replies can happen benignly
 - Switches can be configured to reject replies from fake DHCP servers
