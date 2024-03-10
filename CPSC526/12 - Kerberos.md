### Kerberos
 - Network authentication protocol
	 - Can authenticate a user to the rest of the network
	 - User authenticates once in a while using password
	 - After this, user can use any services on network without re-authenticating
 - Uses centralized authentication service
 - Build mostly using symmetric key crypto
	 - Can be configured to use public keys instead of passwords

**Symmetric Key Management**:
 - `n` people want to communicate
 - Need `O(n^2)` keys, too many
 - Solutions:
	 - Public keys: only need `O(n)` keys; or
	 - centralized key management

**Centralized Key Management in an Organization**:
 - Without centralized management, each connection needs a password
	 - Not scalable
	 - Not secure
	 - Someone can break into a printer and learn all associated passwords
 - With centralized management, each user only needs 1 password
 - Use a central server, trusted by all entities, and called a Key Distribution Center (KDC)
 - KDC shares a secret key with every client
	 - It knows all keys
	 - Everyone else only knows their own key
	 - For `n` clients, only `n` keys are needed
 - Clients obtain session key `K` from server, then talk to each other using the key
 - cons/pros
	 - + Centralized authentication
	 - - Single point of failure
	 - - Performance bottleneck

### Passwords
 - A short text, typically memorized and then used for authentication
	 - Desirable properties: hard to guess AND easy to remember

**Password Authentication**:
 - User sends `(username, password)` to system
	 - How? Unencrypted?
 - System looks up `(username, password)` in password file
 - If entered `(username, password)` in password file, authentication succeeds. Otherwise, it fails

**Password Guessing Attack**:
 - A common way to learn user's password is to guess it
	 - Manually or automated
 - Brute-force attack:
	 - Targets a particular user and tries every possible password, one-by-one
	 - "aaaaa", "aaaab", "aaaac", ...
 - Dictionary attack:
	 - Bit more efficient - tries passwords from some dictionary
	 - English words, most common passwords, previous data breaches
 - Dictionary + brute force attack:
	 - Use words from dictionary + common modifications
	 - "orange7", "orang3", "Orange", "ORANGE!"
 - Reverse brute force attack:
	 - Try common passwords (from previous leaks) on all users
 - Online guessing:
	 - Send guesses to the system one-by-one
	 - Equivalent to trying every possible combo on a lock
	 - Slow, fairly easy to defend against
 - Offline guessing:
	 - Step 1: Steal the password file (this is the hard part)
		 - If the passwords are stored in plaintext, attacker wins
	 - Step 2: Test guesses against the stolen password file offline
		 - Much more efficient than online guessing, potentially billions/trillion guesses/s
		 - Use reverse brute force & dictionaries
	 - Step 3: Use the learned password online
		 - Password will likely work on other sites, since users like to reuse passwords
	 - Step 4: Remember any guessed password, and add it to dictionary for future attacks

**Username Guessing**:
 - Attacker also needs to guess usernames (online attacks)
 - Error messages could reveal information about usernames
 - Example of bad response: "no such user found"
	 - Helps attacker figure out list of valid usernames
	 - eg. try invalid username on mail.ucalgary.ca
 - Example of good response: "invalid username or password"
	 - Does not help attacker
 - Careful with forgotten password mechanisms
	 - Could reveal information about existence of a user
	 - Or worse: Reveal email or other personal information
		 - eg. via custom recovery questions

**Other Methods of Finding Passwords
 - Directly obtain them
 - Malware (software keyloggers)
 - Hardware keyloggers
 - Shoulder-surfing
 - Network attacks, eg. public WiFi & HTTP
 - Social engineering, rubber-hose cryptanalysis

**Recommended Password Policies**:
 - Require at least 8 characters (upper/lower case letters, digits, all symbols)
	 - If number of symbols, # of possible passwords is 94^8 = ~2^52
 - Allow very long passwords, with as few restrictions as possible
 - Disallow common passwords
 - Do not force users to change passwords regularly/just because
	 - Instead, run password crackers regularly to identify weak passwords
 - Do not implement password hints, these are usually easily guessable
 - Make password entry friendly to password managers
 - Support MFA/Passkeys
 - Do not store passwords in plaintext, make offline attacks difficult

### Password Storage
**Plaintext Passwords**:
 - Passwords are stored as entered by the user
 - Early versions of UNIX stored passwords this way
 - Problems: Leaked password file exposes all user passwords

**Encrypted Passwords**:
 - All passwords are encrypted using the same secret key
 - eg. Bob's password "123" is encrypted and stored as "d3f3ea9" in the password file
 - Problem: Leaked secret key can decrypt all passwords

**Hashed Passwords**:
 - Instead of storing passwords, we store their hashes instead
 - A stolen password file won't reveal the actual passwords
 - Even root user (administrator) cannot figure out your password
 - Problem: Dictionary attack
	 - Passwords in real world aren't very random, no need to try every password
	 - Many passwords are the same, humans like to reuse passwords
	 - Attacker can assemble list of probably passwords and pre-compute their hashes
		 - Precomputation only needs to be done once, then reused every attack
		 - Once password file is obtained, cracking is very fast/instantaneous
		 - Rainbow tables is a common technique to store very large lists of precomputing hashes, reducing storage using space-time tradeoff

**Salted Hashed Password - Combatting Rainbow Tables**:
 - System creates random salt string for each user
 - Password stored as H(password + salt)
 - Salt stored in  plaintext
 - 2 users with same password p has different salted hashes
 - Salt length should match or exceed hash output length
 - Salting makes offline attacks more difficult because precomputation is impossible
	 - Tables would be too big

**Salting is not Enough**:
 - Salting frustrates precomputation-based attacks, but not targeted brute-force attacks
 - Regular cryptographic hash functions are super fast (by design)
 - For password storage, we need to use a hash function that is slow/inefficient by design
 - A possible solution: Iterated hash function
	 - Constructed from regular (fast) cryptographic hash function
	 - Hashed password = H(H(H(H(H(...H(password))))))
	 - 10μs per hash × 5000 iterations = 50ms
	 - Normal user won't notice the delay, but attack is 5000x slower
	 - PBKDF2 is a typical example

**PBKDF2**:
 - A key derivation function
	 - A cryptographic hash function that converts a short secret to a longer one
	 - `derived_key = KDF(short_key, desired_length, salt, slowness)`
	 - Can be designed to be deliberately slow to slow down brute-force attacks
	 - Slowness can be controlled by a parameter, often called *work factor*
 - Can be used to:
	 - Convert DHKE secret to AES key
	 - Convert password to AES key
	 - Salt passwords
 - Converts short key to long key by iteratively hashing the password
	 - `prf` = pseudorandom function, typically HMAC
	 - `p` = password
	 - `s` = salt
	 - `C` = number of iterations
	 - `i` = desired length of the derived key
	 - `DK` = derived key
![[PBKDF2.png | 400]]

**Salting is not Enough**:
 - PBKDF2 weakness: Can be implemented on cheap hardware and then parallelized (GPU)
 - Better solution is to use a hash function designed for password hashing
	 - Designed to be difficult to implement ton GPUs & other cheap hardware
		 - eg. may require lot of memory or L2 cache
	 - Example: bcrypt*
		 - has CPU work factor
		 - Limited max, password length
	 - Example: scrypt**
		 - Can configure min memory & work factor
	 - Example: Argon2id***
		 - Can configure min memory & work factor
		 - Winner of 2015 competition
	 - The order is not absolute, there are situations where one is more suitable than the other

**Passwords Peppering**:
 - Salted passwords can be peppered before storage
	 - `password -> hash(password + salt + pepper)`
	 - `password -> Enc_hardware(hash(password+salt), pepper)`
 - Pepper is different from salt
	 - Is kept secret
	 - Is usually the same for all users
	 - Is stored separately from password file
 - Peppering provides extra layer of protection, on top of salt and hashing
	 - Attacker must obtain both the password file and pepper
	 - To make it impossible* to steal pepper, it can be stored in specialized hardware (TPM)
 - Can pepper your password manager by adding/subtracting your own memorized secret pepper to/from each password in the manager before use

### Kerberos
**Key Distribution Center (KDC)**:
 - A central trusted party
 - Knows all nodes
 - Has authentic channel with all the nodes
 - Allows for mediated key exchange

**Notation**:
 - `A`lice, `B`ob, `S`erver (trusted by both `A` and `B`)
 - `A -> B : message`: A send B a message
 - `Kxy`: Symmetric key known only by X and Y
 - `Kx`: Session key generated by X
 - `PKx`: Public key for X
 - `SKx`: Private key for X
 - `Nx`: Nonce generated by X
 - `{data}Kxy`: Symmetric encryption of data
 - `{data}PK(X)`: Public-key encryption of data
 - `{data}_SK(X)`: Data signed by X using X's private key `K^SX`

**KDC Operation (in Principle)**:
 - Assuming server has keys `Ksa, Ksb` for Alice and Bob
```
A   -> KDC : "I want to talk to Bob"
KDC -> A   : {use Kab with Bob}Ksa  // invents random key Kab
KDC -> B   : {use Kab with Alice}Ksb
```
 - Some issues:
	 - Should B be expecting a message from KDC?
	 - When can A assume KDC is finished talking to B?

**KDC Operation (in Practice)**:
```
A   -> KDC : "I want to talk to Bob"
KDC -> A   : {use Kab with Bob}Ka  // Kab = random key
KDC -> B   : {use Kab with Alice}Kb
A   -> B   : "Hi I'm Alice! ticket={use Kab for Alice}Kb"
```
 - Ticket: Given to Alice so that she can pass it onto Bob
	 - Alice cannot decrypt it, only Bob can

### Needham-Schroeder Protocol
 - Goal is key mediation on untrusted networks
	 - eg. You print document at UofC
 - Uses trusted third party
	 - You don't need to do a key exchange with everyone before communicating
 - Two types:
	 - Symmetric key - goal: Establish session key between Alice and Bb
	 - Public key - goal: Provide mutual authentication between Alice and Bob
 - Both original protocols were insecure as proposed (crypto is hard)

**Original (1978) Needham-Schroeder Protocol - Symmetric**:
 - Assumes server S is a trusted entity
	 - ie. Server shares secret key `Ksa` with Alice and `Ksb` with Bob
![[needham_schroeder_original.png|400]]
 - Original protocol is vulnerable to replay attack
 - If attacker learns `Kab`, no matter how old, he can replay `{Kab,A}Ksb` to Bob, making him accept the old `Kab`

**Updated (1987) Needham-Schroeder Protocol - Symmetric**:
![[needham_schroeder_updated.png|400]]
 - Note: Kerberos fixes this protocol differently, using timestamps and duplicate detection

**Needham-Schroeder Protocol - Public-Key**:
![[needham_schroeder_public_key.png|450]]
 - This original version suffers from a MITM attack
 - If an imposter Ives convinces Alice to contact Ives instead of Bob, Ives can pretend to be Bob
 - This type of MITM attack is sometimes called Mafia Fraud attack

**Mafia Fraud**:
 - Alice connects to Ives willingly
	 - Eg. maybe Ives runs website that Alice likes to visit (tiktak.com)
 - Ives then connects to Bob pretending to be Alice
 - Bob issues "Alice" (Ives) a challenge to sign
 - Ives uses that as a challenge for Alice pretending it's Ives website
 - Also known as the Grandmaster Problem
	 - Chess against two grandmasters, copy the first's move against the second, copy the second's response back to the first
 - Typical MITM attack involves victims unknowingly communicating with the attacker

**Fixed Needham-Schroeder-Lowe Protocol - Public-Key**:
![[needham_schroeder_lowe_protocol_public_key.png|450]]

### Kerberos (RFC4120)
 - Authentication protocol built with symmetric cryptography
 - Originally developed at MIT, now essential part of Windows authentication infrastructure
 - Designed to authenticate users to servers
	 - Users use passwords initially
 - Based on Needham-Schroeder, with timestamps to limit key lifetimes

**Design Goals & Assumptions**:
 - Users only have passwords to authenticate themselves
	 - Same for all clients actually (including printers, etc)
 - The network is insecure
	 - Must be Eavesdropping & Tampering safe
 - It is possible and necessary to protect the Kerberos server
	 - The server stores all secret keys for the entire organization
 - Clients are not trusted
	 - User workstations, printers, file-servers, etc
 - Users have to authenticate themselves only infrequently (eg. in the morning)

**Basic Authentication Server (AS) Idea**:
 - Scenario: Alice wants to print
	 - AS knows Alice's password, AS knows printer's secure key, Alice never printed before
 - 1. Alice contacts AS and requests access to printer
	 - Alice includes her identity, and the identity of the print server
	 - Plus some additional info (nonce)
 - 2. Server replies to Alice with Session Key and Ticket
	 - Session Key:
		 - Encrypted using Alice's password (PBKDF2)
		 - Alice & Printer can use it to encrypt their communication
	 - Ticket for printer server:
		 - Includes Alice's and printer's identities, and a copy of session key
		 - Encrypted using a key only the printer knows
		 - Alice cannot decrypt the contents of the ticket
	 - Additional info is included as well:
		 - Encrypted nonce, expiry time, etc
 - 3. Alice sends to printer:
	 - Ticket and Authenticator
	 - Authenticator = Proof she knows the session key (something encrypted by session key)
	 - Printer decrypts ticket, extracts session key, and verifies Alice's authenticator
 - 4. Printer sends Alice proof it knows session key
 - 5. Alice & Printer communicate using session key
 - Alice repeats steps 1-5 to talk to other services (eg. email or file server)
 - Tickets are reusable, so Alice does not have to retype password every time she prints to the same printer
 - Tickets include expiry time
	 - In case Alice loses or changes job
	 - They can also include start-time (post-dated ticket)
 - Tickets must be accompanied with a unique authenticator
	 - To prevent replay attacks
	 - Authenticator = client-ID + timestamp, encrypted using session key

### Tickets
 - Ticket contains:
	 - Server name ("email", "printer", "TGS")
	 - Client name
	 - Client network address
	 - Current time
	 - Expiry time
	 - Session key
 - Encrypted using server's secret key `Ks`
 - Users must present ticket to server to obtain a service
	 - Ticket is only valid for one user and one service
	 - To prevent replay, tickets must be accompanied with authenticators
	 - Tickets can be reused for the same service, but they have expiry times
 - Tickets are encrypted messages containing session keys and identities
	 - Encrypted so that only the service can decrypt them
	 - ie. ticket for printer can only be decrypted by printer
	 - Clients, or anyone else, cannot decrypt tickets
 - Kerberos uses symmetric Needham-Schroeder to obtain tickets

**Authenticator**:
 - To prevent replay attacks (reused tickets), each ticket must be accompanied by an authenticator
 - Authenticator contains:
	 - Client's identification (cname, crealm)
	 - Current time (ctime)
	 - Plus some other fields (authorization data, unique sequence numbers)
 - Authenticator is encrypted with the session key `Ksc`
 - Authenticator proves:
	 - The client knows the session key `Ksc`
	 - The ticket is fresh
 - Authenticator must be unique
	 - Server remembers used authenticators in authenticator cache
	 - Deleted when upon expiry

**Basic Authentication Server Idea**:
 - Main problem with the basic idea as described so far:
	 - To print to a different service, Alice needs to type her password again
	 - Alice enters password to print
	 - Alice enters password to check email
	 - Alice enters password to access file server
	 - etc.
 - We need single-sign-on mechanism
	 - Kerberos implements this by adding a special ticket
	 - Alice uses her password once to get a special ticket
	 - The special ticket proves she knows her password
	 - The special ticket can be used to get tickets to servers without a password

### Ticket Granting Service (TGS) & Ticket Granting Ticket (TGT)
 - 1. Alice contacts AS:
	 - AS replies with a Ticket-Granting-Ticket (TGT) and session key for TGS
	 - TGT is to be used with the Ticket Granting Server (TGS)
	 - TGT is long lasting (eg. obtained in the morning, expires at night)
	 - Session key is encrypted using Alice's password (PBKDF2)
	 - AS is the only server that uses Alice's password
 - 2. Alice wants to print:
	 - Alice's computer automatically contacts TGS
	 - Sends TGT
	 - Receives service ticket for printer
	 - Alice does not need to reenter passwords
 - 3. Alice's computer uses service ticket to talk to printer
 - 4. When Alice wants to check her email:
	 - Alice's computer automatically contacts TGS again
	 - Sends TGT to receive service ticket for email
 - 5. Alice's computer uses service ticket to check email
 - AS + TGS = KDC, typically run on the same physical server

**Ticket Granting Ticket (TGT)**:
 - User sends their name to AS
 - AS responds with:
	 - Session key for future communications with KDC (TGS)
	 - And TGT encrypted with key only known to KDC
	 - Both encrypted with user's password (key derived from user password)
 - TGT contents:
	 - Identity of KDC (KDC1@UCALGARY)
	 - User's name & IP address (john1337@ucalgary.ca, 136.159.7.12)
	 - Timestamp + lifetime
	 - Session key (same as above)
 - The client uses TGT to obtain tickets for other services
 - To get a ticket for some service (printing) you send a request to TGS `("Printer", TGT)`
 - Request is accompanied with an authenticator
	 - Authenticator = {client identity + time} encrypted with session key for the service
 - TGT replies with a service ticket, and session key for the service

**TGS Verifying TGT**:
 - TGS decrypts TGT to recover session key
 - TGS uses recovered session key to decrypt the authenticator
 - TGS verifies the contents of authenticator and key (IP address and timestamp)
	 - Permissible clock skew is typically a few minutes
 - If everything matches, KDC knows that request came from a real client, since only it would have access to session key that was in ticket
 - KDC then issues and sends service ticket back to the client plus session key

**Service Tickets**:
 - Service tickets are almost identical to TGTs
 - The difference is that they have a name of a different service
	 - `sname="printer"` instead of `sname="TGS"`
 - They're encrypted by a secret key shared by the KDC and the service
	 - Only the service knows the key
 - User sends the service ticket and a matching authenticator to the service
 - The service decrypts the ticket, using its own key
 - The service knows it's genuine, because only the KDC knows the key used to produce it
 - The service verifies that the ticket is for it, and not some other service
 - It uses the enclosed key to decrypt and verify the authenticator
 - The service extracts the user's name from the ticket
 - The service can now decide whether to grant access to the service
	 - Or authorization may be included in the ticket

**Bidirectional Authentication**:
 - Sometimes, the client wants to be sure of the server's identity
 - The server extracts the timestamp from the authenticator, optionally increments it, re-encrypts it with the session key, and sends it back
 - The client can verify the answer

**Ticket Lifetime**:
 - TGTs typically last about 8-12 hours
 - Service tickets can be long or short lived, depending on service
	 - Don't outlive the TGT
	 - When TGT expires, so do the tickets issued with it
 - Live tickets are cached by the cclient
 - Expired service tickets can be automatically and transparently renewed

**Authentication, Not Authorization**:
 - Kerberos is mostly an authentication service
 - The services know a genuine name for the client, vouched for by the KDC
 - Services can make their own authorization decision based on this name

**Putting Authorization into Tickets**:
 - Tickets can contain authorization information known or supplied to KDC
	 - Authorization is an optional part of tickets (RFC4120)
 - Windows KDCs use this, to centralize authorization data
 - As a result, Windows and open source Kerberos KDCs don't interoperate without additional steps

**Inter-Realm Tickets**:
 - A ticket from one realm can't be used in another, since a KDC in one realm doesn't share secrets with services in another realm
 - But two (or more) realms can be linked together by adding TGS of one as a service in the other
 - Client of realm 1 can then request a TGT that will work in realm 2
	 - Realm 2 essentially trusts KDC of realm 1 to vouch for the user's identity
	 - Realm 2 then issues service tickets with the realm 1 user id, not its ow

**Proxy Tickets**:
 - Suppose a user wants to print a file
 - The print spooler doesn't want to copy the user's file, that's expensive
 - The user obtains a proxy ticket granting the print spooler access to its files
 - The print spooler uses that ticket to act as the user and read the user's file
 - The user can put file restrictions in the proxy ticket to give the print spooler access only to a single file

### Kerberos Limitations
 - Single point of failure (accidental or malicious)
 - Time synchronization is important
 - Virtualization is not simple
	 - On demand service replication, test deployments
 - TGTs have known plaintext, making offline password guessing possible
	 - If successful, attacker can impersonate users or services
	 - Kerberos uses passphrases instead of passwords (longer passwords)
 - Also, by default anyone can request and obtain any number of TGTs for analysis
	 - This can be made more difficult by enabling preauthentication
		 - Initial request must include a timestamp encrypted with hash of password
 - Cached tickets are often stored in `/tmp`, is the OS protection good enough?
	 - Less of an issue on single-user workstations; bigger threat on multi-user machines
	 - `/tmp` needs to be on a local disk, not something mounted on NFS
