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

|     | Step                                   | Description                                                                                                                                                                  |
| --- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.  | `A -> S : A, B, Na`                    | Alice identifies herself to server<br>Sends a nonce<br>Tells server she wants to talk to Bob                                                                                 |
| 2.  | `S -> A : {Na, Kab, B, {Kab,A}Ksb}Ksa` | Server generates new Session key `Kab`<br>Sends it back to Alice<br>Includes nonce `Na`, Bob's identity, sealed ticket for Bob<br>All encrypted using pre-arranged key `Ksa` |
| 3.  | `A -> B : {Kab, A}Kbs`                 | Alice sends sealed ticket to Bob                                                                                                                                             |
| 4.  | `B -> A : {Nb}Kab`                     | Bob sends Alice a nonce<br>As challenge to prove she knows `Kab`                                                                                                             |
| 5.  | `A -> B : {Nb-1}Kab`                   | Alice increments it and sends result to Bob<br>Verifies she can decrypt it                                                                                                   |
