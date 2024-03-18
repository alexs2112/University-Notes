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

### Client Authentication (RFC4252)
 - How does the client authenticate itself to the server?
 - Server sends client a list of allowed authentication methods
	 - Client can use any of them (even multiple)
 - Most common are password-based and public-key based
 - Many extensions are available
	 - OpenSSH can be configured to use LDAP, Kerberos, and even 2FA
 - Can find which authentication methods are supported by the server:
   `nmap --script ssh-auth-methods csx2`

**Password Authentication**:
 - Simplest form: Ordinary username and password
 - The password is protected from eavesdropping
 - There is no bullet-proof protection against brute-force password guessing
	 - Account Locking -> Inconvenience legitimate users
	 - IP Locking -> Does not work against botnets
 - Strong passwords are a must

**Public Key Authentication**:
 - User on a client prepares and saves a public/private key pair
 - Client sends user's public key to server
 - Server verifies the client is in possession of a matching private key
	 - Server sends a 256-bit random number encrypted with client's private key
	 - Client decrypts it and sends back a cryptographic hash of the random number
 - Server must trust the client's key
	 - Client's key is not a certificate
	 - Server has a per-client list of authorized public keys
	 - If client's key is in that list, it's accepted (provided the challenge was successful)
 - How does the server create the list of authorized keys?
	 - Could be installed by a server admin (user would not even need a password)
	 - User could download private key from password-protected secure website
	 - Could be uploaded by user to a password-protected secure website
	 - Or, most commonly, user logs in using a password first time, then uploads public key

**Host-Based Authentication**:
 - If client and  server share the same admin, host-based authentication can be used
 - Admin creates and installs a public/private-key on client (global for all users)
 - Admin adds client's public key to authorized hosts file on server
 - Any user authenticated from that client will be automatically accepted
 - This is only useful if the two machines are under common administration, and are secure against insider attacks
 - Clusters in HPC environments often use this mechanism, allowing users to login to all nodes without having to type in a password and without setting up keys beforehand
 - Note: on CPSC Linux machines, `~/.ssh` directory is shared via NFS between all machines

**Storing Private Keys on Clients**:
 - Private keys are stored in the `~/.ssh` directory
 - If private key is compromised, all security bets are off
 - Extra care must be taken to correctly cope with NFS-mounted home directories
 - Minimum protection:
	 - All private key files must be read-protected
	 - Open-SSH client will refuse to use unprotected keys
	 - If users store their keys under their home directories, and use NFS, someone can eavesdrop on the NFS traffic
 - Better protection:
	 - Admin sets up encrypted NFS traffic (Kerberos + NFS4)
 - Recommended protection:
	 - User encrypts the private key with some symmetric cipher
	 - `ssh` will prompt user for a `passphrase` when needed
	 - You can use the same password for all your keys
 - This results in being prompted for passphrase constantly
 - Solution: Use `ssh-agent` (built in password manager)
	 - Run process that prompts for the password once
	 - `ssh-agent` decrypts key in memory, performs public key operations on behalf of SSH client
	 - Can even use hardware security key (yubikey)
	 - Many tutorials available (from Github)
 - SSH client still needs to communicate with this ssh-agent

**Securing the SSH Agent**:
 - Communications with `ssh-agent` are via a Unix-domain socket
	 - System call, local "socket", implemented through a file
	 - Domain sockets live in the file system
 - Not all systems enforce file permissions on IPC (Inter-Process Communications) sockets
	 - Fortunately, all systems verify permissions on parent directories
 - Generic solution: Put the socket in a protected directory, use shell environment variables to pass the location to clients

### Port Forwarding (SSH Tunneling)
 - SSH can forward TCP connections from the local machine to the remote, or vice-versa
 - Can be used to access resources that are behind firewalls, and/or on non-routable IPs
 - Example: Talking to an inaccessible MySQL server from home computer:
	 - `ssh -L 1234:192.168.30.22:3306 rsx1.cs.ucalgary.ca`
	 - Then from my home machine, I can point my DB client to:
	   `dbclient localhost:1234`
 - You can do the same for any other service: telnet, mail, web servers, etc
 - Tunnels can be used to circumvent organizational security policies
	 - As long as SSH port is available, you can access anything behind a firewall, no matter what the policy says

**Forwarding the Authentication Agent**:
 - Idea: Login to server A using your agent, then from A you login to B using the same key
 - *"SSH agent forwarding can be used to make deploying to a server simple. It allows you to use your local SSH keys instead of leaving keys (without passphrases!) sitting on your server."*
 - To do this, you edit a file `~/.ssh/config` and add the lines:
```
	Host serverA.com
	   ForwardAgent yes`
```
 - Warning: If Server A is compromised, root on A can use your domain-socket to talk to anyone that will accept your key! (without learning your key)
 - Lesson: Do not forward SSH agent via untrusted machines

**X11 Forwarding**:
 - SSH can be used to forward X11 window system connections too
 - How it works: The X-server controls the keyboard, screen, and mouse
 - X-applications open a connection to the X-server via Unix-domain sockets or TCP
 - The environment variable DISPLAY tells the application which port:
	 - `DISPLAY=:0.0` connects to localhost on port 6000 via IPC
	 - `DISPLAY=rsx1.cs.ucalgary.ca:20.0` connects to `rsx1` server on port 6020 via TCP
 - How is this connection authenticated?
	 - Some people don't
	 - Can use Kerberos
	 - Usually by magic cookies (secret value stored in file that is sent to the X server)
 - SSH has X11 forwarding built-in
	 - Remote sshd generates random cookie, stores it in magic cookie file, sets DISPLAY to point to `localhost:N` (automatically picks port `N`)
	 - When X11 application attempts to connect to the X-server, it actually connects to sshd and sends the saved magic cookie (reverse tunnel)
	 - sshd server verifies the cookie, and forwards connection over ssh tunnel to client
	 - Client replaces remote cookie with local one, and contacts local X-server
	 - Warning: If remote server is compromised, cookie can be read and attacker gains full access to your X-server
		 - Don't forward X11 to untrusted machines

### Why Did SSH Succeed?
 - SSH1 and SSH-1 protocol developed in 1995 by a victim of a password-sniffing attack
	 - When beta versions started gaining attention, realized his security product could be put to wider use
	 - Not a cryptographer, just some lab researcher
 - Perfect drop-in replacement for the insecure `rlogin`, with extra security
 - Easy to deploy on as many machines as desired, with minimal user training
 - Had nice bonus features (tunnels, X11 forwarding, compression, scp, sftp, etc)
 - Defended against real attacks, ran on more Unix variants than its competitors
 - No infrastructure needed (no PKI, no CAs, no KDS)
 - Professional cryptographer would probably design it better, with certificates and CAs
	 - And it would likely be undeployable
 - SSH offers more real security from a partially-secure implementation that is compatible with real-world deployment patterns
 - Note: OpenSSH does support certificates for authentication since 2010

**Weaknesses**:
 - SSH-1 made a number of silly choices for ciphers, but were addressed in SSH-2
 - User education w.r.t. warning messages
 - User education w.r.t. trojan replicas of SSH/SSHD
 - X11 and ssh-agent forwarding can be intercepted on compromised hosts
 - Potentially yummy target for ssh worms
 - Password guessing
