### Secure Shell Protocol
 - RFC4251
 - Secure Shell (SSH) is a protocol for secure remote login and other secure network services over an insecure network
	 - Similar to how TLS is implemented
 - Consists of three major components:
	 - The *Transport Layer Protocol* provides server authentication, confidentiality, integrity
		 - May optionally also provide compression
		 - Transport layer will typically be run over a TCP/IP connection, but may be used on top of any reliable data stream
	 - The *User Authentication Protocol* authenticates the client-side user to the server
		 - Runs over the transport layer protocol
	 - The *Connection Protocol* multiplexes the encrypted tunnel into several logical channels
		 - Runs over the user authentication protocol
 - Client sends a service request once a secure transport layer connection has been established
	 - Second service request sent after user authentication is complete
	 - This allows new protocols to be defined and coexist with the protocols listed above
 - The connection protocol provides channels that can be used for a wide-range of purposes
	 - Standard methods are provided for setting up secure interactive shell sessions
	 - And for forwarding (tunneling) arbitrary TCP/IP ports and X11 connections
![[SSH_protocol.png|150]]

**Secure Shell (ssh)**:
 - `ssh` is a very popular tool
	 - It uses the SSH protocol to connect to the `sshd` server
	 - Allows users to execute commands on a remote machine and establish generic tunnels
 - Interesting case study in deployability
	 - We will look at both SSH-1 and SSH-2 versions
 - Many useful features:
	 - Encrypted login and shell connection
	 - Easy drop-in replacement for `rlogin`, `rsh`, and `rcp`
	 - Multiple means of authentication
	 - Secure communication channels for other applications
		 - `sshfs`, `rsync`, `sftp`, `SOCKS proxy`, `VPN`, `X11`

### SSH-1
**Simple Connection Sequence**
 - Client contacts server (TCP socket)
	 - Indicates SSH protocol version and implementation version
 - Server replies:
	 - Sends its public RSA "host-key" (1024+ bits)
		 - This is a permanent and unique key, stored in a config file
	 - Random RSA "server-key" (768+ bits)
		 - Changed hourly, never saved to a file
	 - List of supported ciphers (opposite of TLS, in TLS the client sends this list)
 - Client authenticates server
 - Client generates a session key, encrypts it using server's public and random-key
 - Server decrypts session key and uses it for traffic encryption
 - Client authenticates to the host

**Server and Host Key**:
 - Attempt to have perfect forward secrecy
 - The shorter random key provides an approximation to perfect forward secrecy
	 - If someone gets a hold of it, they can only see messages from the last hour at most
 - The permanent host-key is used by client to authenticate server
 - Note that only an owner of a matching private key will be able to decrypt the session key
 - Why not use Diffie-Hellman?
	 - 768-bit RSA is faster than 1024-bit Diffie-Hellman, and computers used to be slower
	 - or maybe it's because SSH's inventor was only an amateur in 1995
	 - SSH-2 now uses DH

**Authenticating the Server**:
 - How does the client authenticate the server?
	 - Why should the client trust the server's public key?
	 - The server is sending a key, not a certificate, therefore no one is vouching for the key
	 - In SSH-2, it is possible to send a certificate and use trusted CA system (different than PKI)
 - The first time a key is received, the user is prompted whether to accept it
 - The client caches the result in a "known hosts" file
 - This is called a TOFU model (trust-on-first-use)
	 - Pro: Very simple
	 - Con: First contact can be intercepted (MITM)
	 - There are alternatives
 - The user does not know if the server key is correct
	 - But they know if it is the same as the last time
	 - Vulnerability is present only during initial login
 - but, users must be taught what to do about that message
	 - Does not always indicate a MITM
	 - Server reconfiguration can cause the server key to change, which happens a lot
 - You can remove the key manually, or `ssh-keygen -R <hostname>`

**What Should Users Do?**
 - The system administrator can populate a system-wide known hosts file
 - Or, system administrators can publish a digitally-signed list of their hosts' keys
	 - Then users can get the keys out of band and verify them
 - Users can visit sysadmin in person and write down the key on a piece of paper
 - Users can ask each other
 - Do people actually attack SSH like this?
	 - Most attacks on SSH are brute force password guessing attacks
	 - MITM attacks against SSH have been seen in the wild

**A List of Ciphers**:
 - Server transmits a list of ciphers at the start, client picks one
 - What if an attacker substituted a list containing only weak or cracked ciphers?
	 - Downgrade attack
 - Solution: Disable weak ciphers
	 - Edit `/etc/sshd_config` files for the server, and/or `~/.ssh/ssh_config` for clients
		 - SSH hardening
	 - Disable backwards compatibility with SSH-1, only allow SSH-2
		 - Automatic on many modern SSH implementations
 - Note: In SSH-2, after starting the encryption, client/server verify the original cipher lists
 - `ssh -Q cipher`, `ssh -Q kex` to see which ciphers and key exchange algorithms are supported
