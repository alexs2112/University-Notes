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
