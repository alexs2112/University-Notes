### Remote Access Technologies
 - Types: Remote Desktop Solutions, Virtual Private Networks (VPN), Zero Trust Network Access (ZTNA)
 - VPN: Extend a remote network anywhere, commonly implemented with a tunnel to enable privacy
	 - All or Nothing: Once you are on the network, you have unlimited access 
 - ZTNA: Extends enterprise network similarly to a VPN with engrained Zero Trust principles
	 - May leverage tunnel-based technologies
		 - Many tunnel vulnerabilities are equally applicable
	 - Fine-grained, identity and context based controls

### TunnelCrack
 - Combination of two *widespread* security vulnerabilities in many tunnel-based remote access technologies
	 - These vulnerabilities being exploited results in clients sending traffic outside of their protected tunnel
 - Tunneling: A device with a VPN/ZTNA will typically have a virtual adapter installed, the client directs packets through the virtual adapter to ensure privacy and security.
	 - Security inspection is often located on the receiving end of the tunnel
	 - Tunnels (VPNs) are synonymous with privacy for a reason
	 - Typical MitM attacks are significantly hindered by VPNs
 - Enhancing MitM attacks to silently bypass the VPN tunnel:
	 - TunnelCrack takes advantage of the inherent trust between the client and its LAN (LocalNet Attack), and the client and the remote tunnel termination point (ServerIP Attack) 

**LocalNet Attack**:
 - By default: Packets sent to the LAN will not be sent through the tunnel
 - The adversary assigns a *public* IP address and subnet to the client. This causes the VPN client to think that other public addresses are on its local network.
 - Example attack:
	 1. Execute Rogue AP or DHCP attack
	 2. Assign IP to victim of a public subnet
	 3. Client establishes its tunnel as usual
	 4. When client attempts to access specific public addresses, the attacker can intercept it

**ServerIP Attack**:
 - Client requests for the remote tunnel endpoint cannot be sent through the tunnel (the tunnel doesn't exist yet)
 - The remote tunnel endpoint is often represented by a fully-qualified DNS name in the client configuration
 - Idea: Spoof the DNS response, force traffic to be sent outside the tunnel
 - Example attack:
	 1. Execute Rogue AP or DHCP attack
	 2. Assign malicious DNS server
	 3. Attacker spoofs DNS of the tunnel endpoint, tunnel established via spoofed endpoint
	 4. Requests for public addresses bypass the tunnel
 - Potentially force any domain to bypass the tunnel

### How This Works
 - LocalNet Attack:
	 - MitM attack via Rogue DHCP Server
	 - Gain control over IP and router assignment
 - ServerIP Attack:
	 - Detect the presence of a tunnel
	 - DNS spoof the VPN endpoint
 - Force the public address traffic that we want to access outside of the tunnel

**Demo**:
 - Kind of unwatchable remotely
 - LocalNet attack: Requests for ACME.com were compromised, sent outside the tunnel to a malicious site
	 - Used public IP DHCP assignment to trick the endpoint
 - ServerIP attack: Requests for VPN enpoint were spoofed as ACME.com domain, allowing successful bypass

**Possible Mitigations**:
 - Update software if a fix exists
 - LocalNet: Disable local network access when a Public IP is assigned
 - ServerIP: Application-aware enforcement instead of IP
	 - Verify or communicate the Public IP address in band
	 - Authenticated DNS (DOH, DNSSEC)
 - HTTPS: Generally helpful, not a complete mitigation
