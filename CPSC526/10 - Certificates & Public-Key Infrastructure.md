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

**Before Bob Can Reply to Alice**:
 - Bob asks the CA to sign his public key
 - CA verifies Bob's identity
	 - CAs used to charge Bob money for this service
	 - We hope they verify Bob's identity
 - CA then signs Bob's key using CA's private key
 - CA then gives Bob the certificate
 - Certificate includes Bob's public key & CA's signature

### Certificate Authorities
 - How does Alice obtain a CA's public key?
	 - CA's public key (trust anchor) must be obtained out-of-band
	 - via different channel than one used for communication, authenticated using the certificate
	 - Several CA certificates are often included with your browser and/or operating system

**CA Hierarchy**:
 - Most CAs are hierarchical
	 - The root CA endorses intermediate CAs
	 - Forms a tree structure
 - Creates a chain of trust
	 - A certificate includes chain of certificates, of all intermediate CA's up to the root
 - There are multiple root CAs, each with their own hierarchies
	 - Validate up the chain of CAs until you reach one that you trust

**Root Certificates on your Computer**:
 - Your browser ships with many root certificates
 - How did the browser vendor decide to include a particular CA's certificates?
 - Your browser likely also uses certificates that were included with your OS

**Proving Identity to a CA**:
 - CAs can use any method to verify identity of a web server owner
	 - They typically want a proof that the person requesting the certificate owns the web server
 - Manual methods used in the recent past:
	 - CA gives the requester a challenge, which must be placed in a specified location on the server
		 - Then verifies the challenge is on the server at the requested location
	 - CA gives the requester a challenge, which must be placed in the DNS record
	 - CA emails the requester a challenge, which then must be returned to the CA
 - Automated methods (eg. using Let's Encrypt) require operator to install and run an interactive script on the web server's hardware

**Certificate Authorities**:
 - If any single link in the CA chain becomes compromised, a MITM attack can successfully impersonate every encrypted web site someone might visit
 - By using a web browser, you are trusting all CAs from which they included certificates
	 - And their employees
	 - And anyone for whom they signed intermediate certificates
 - You are also trusting the browser vendor and developers
	 - Chrome has ~35 million lines of code, this is a lot of developers
 - And the website/store where you downloaded your browser
	 - Their system administrators and their friends (if the admins work remotely and don't lock their computers when they go to coffee)
 - Most browsers allow you to add/remove certificates manually
	 - They are trying to legislate this away in the future

### Assignment
 - Remember how OTP works
	 - OTP is emulated using the CTR mode of operation, generate a pseudorandom key to create an infinitely long pseudorandom pad
 - We are given the encryption and must do the decryption
 - First 16 bytes will be IV, next 16 bytes are the salt, followed by the ciphertext
	 - To read the file, extract first 16 bytes as IV, then the salt, then initialize the CTR using the IV and Salt, then just redo the encryption loop but decrypting instead of encrypting

**AES-CTR Encryption in Python**:
```python
def encrypt(password: str, nonce: int | None = None):
  if nonce == None:
      iv, salt = os.urandom(16), os.urandom(16)
  else:
      iv = nonce.to_bytes(32)[:16]
      salt = nonce.to_bytes(32)[16:]
  key = key_stretch(password, salt, 16)
  sys.stdout.buffer.write(iv+salt)
  encryptor = Cipher(algorithms.AES(key), modes.CTR(iv)).encryptor()
  while True:
      data = sys.stdin.buffer.read(4096)
      if len(data) == 0: break
      cblock = encryptor.update(data)
      sys.stdout.buffer.write(cblock)
  cblock = encryptor.finalize()
  sys.stdout.buffer.write(cblock)

def key_stretch(password: str, salt: bytes, key_len: int) -> bytes:
  key = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=key_len,
    salt=salt,
    iterations=100,
  ).derive(password.encode())
  return key
```
