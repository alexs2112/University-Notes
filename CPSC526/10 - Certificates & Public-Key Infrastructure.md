### Public Key Cryptography Problem
 - Alice and Bob want to communicate securely
 - They both have their own public and private keys, but they never met
 - Two important issues:
	 - How does Alice obtain Bob's key?
	 - How does Alice verify the key she has belongs to Bob?
 - Consequences of getting the wrong public key:
	 - Eavesdropping, Impersonation, MITM, ...

**Public-Key Communication Problem**:
 - The first problem can be solved by Bob sending his public key to Alice
	 - eg. at the beginning of the communication session
 - Now we just need a mechanism for Alice to verify Bob's public key
	 - To prevent someone from substituting Bob's key
 - Solution 1 - Centralized online/on-demand service
	 - The service could be used to verify public keys
	 - This is how security is implemented in some organizations, does not scale to the world
 - Solution 2 - Trusted 3rd party
	 - If Alice and Bob share a trustworthy friend, the friend could vouch for Bob's signature
	 - For example, both Alice and Bob know a friend Trent who has a public/private key

### Certificates
**Idea**:
 - Before Alice and Bob start their communication:
	 - Alice and Bob don't know each other yet
	 - They both know and trust Trent, who knows crypto, and has their public-private key pair
	 - They both ask Trent to sign their public keys
		 - Bob gets his public key signed
		 - Alice gets her public key signed
	 - They both obtain Trent's public key
 - During communication between Alice and Bob:
	 - Alice contacts Bob
	 - Bob sends Alice his public key, signed by Trent
	 - Alice verifies Bob's document's signature using Trent's public key
	 - If signature matches, Alice has a good reason to believe she has Bob's public key
	 - Alice can also send Bob her public key, signed by Trent
 - Notice that Trent is not involved in this conversation at all

**Digital Certificate, aka Public Key Certificate**:
 - A digitally signed document containing:
	 - An identity
	 - A public key
	 - Plus some additional useful information
 - Document is signed by a Certificate Authority (eg. Trent) using their private key
 - Used to prove the ownership of a public key by binding an identity and a public key

**Before Alice Can Talk to Bob**:
 - Alice somehow obtains certificate authority's public key and installs it on her computer
 - Alice can now talk to Bob, as long as Bob uses the same CA
 - Bonus: Alice can authenticate anyone who has their public key signed by this CA, not just Bob
