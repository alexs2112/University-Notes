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
