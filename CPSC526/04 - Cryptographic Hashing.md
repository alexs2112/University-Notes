### Cryptographic Hash Functions
 - Special hash functions
 - Workhorse of modern cryptography
 - Many uses, even outside of cryptography
	 - Pseudorandom data generators
	 - Verifying data integrity
	 - Combat email spam (hashcash)
	 - Data deduplication
	 - Password storage
	 - Cryptocurrency
	 - Git, rsync

**Hash Functions**:
 - A function that maps data of arbitrary size to data of fixed size
 - The output of a hash function is called a *hash value* or *hash*
 - Denotes as `h(x)=y` where `x` is the data and `y` is the hash
 - Must be deterministic:
	 - `x1 = x2 => h(x1) = h(x2)`
	 - The reverse is not true
	 - `h(x1) = h(x2) !=> x1 = x2`
 - Collisions are unavoidable (smaller output set than input set)
 - Other desirable properties:
	 - Quick
	 - Uniformly distributed hash
 - Depending on uses, may need to have other properties

**Cryptographic Hash Functions**:
 - Cryptographic hash functions are hash functions with some extra properties
 - Input is called a *message*
 - Output is called a *message digest* (or *digest*, *fingerprint*, *hash*)
 - Cryptographic hash functions:
	 - Should be infeasible to invert (brute force only)
	 - Should be infeasible to find multiple messages with the same digests
	 - Small change in message should result in big change in digest
	 - Should appear to be random (pass pseudo-randomness tests)
 - Must be immune to all known cryptanalytic attacks
	 - Collision attacks
	 - Preimage attacks
	 - Others attacks (extension attacks)
 - "Immune" is related to computational security
	 - The higher the value of information, the more resources the attacker will spend
	 - We want attacker to be forced to use brute-force (i.e. O(2^n))
 - 256-bit hash values should be able to defend against most practical brute-force attacks

### Hash Collisions
**Collision Resistance**:
 - One of the most important properties of a hash function
	 - Almost always related to the other properties, having this property most likely means you have the other ones
	 - Likewise, not having this property means you likely are missing other properties
 - It should be difficult to find *any* two messages that hash to the same digest
	 - Difficult to find any pair `(x,y)` such that `h(x) = h(y)`
 - Collision attacks alone usually do not have direct practical applications
	 - But they can signal a weakness in the hash function
 - Note: Finding collisions via brute force attack does not have complexity of `2^n`

**Pigeon-Hole Principle**:
 - Number of possible inputs is much larger than number of possible outputs, collisions are inevitable
 - More pigeons -> more collisions
	 - This is okay, as long as they are very rare and not easy to find

**Birthday Attacks on Hash Functions**:
 - Probability of at least 2 people in a group of n people sharing the same birthday:
	 - `p(n) = 1 - (365!)/((365-n)! * 365^n)`
 - Same principle applies to hash functions
 - Suppose hash function has `b`-bit digest, there are `M = 2^b` possible hash values
 - If we calculate hashes for `n` random messages, the probability of at least 1 collision is:
	 - `1 - M!/((M-n)! * M^n)`
	 - Expected number of messages we need to try to find a collision is `!2^(b/2)`
 - Even ideal hash functions with `b`-bit digest provides only `~b/2` bits of security for collision resistance, as attacker only needs `2^(b/2)` evaluations of the hash function
 - If we want 128-bits worth of security against collision attacks, we need 256-bit digests
	 - Security is almost always measured in bits as most systems can be broken by brute force attacks using bits
	 - An attacker needs to perform 128-bits worth of work to find a collision
	 - Important to know when mixing and matching multiple different security mechanisms

### Preimage Resistance
 - Cryptographic hash functions should be non-invertible
 - For a given digest `h(x)` is should be difficult (impossible) to find message `x`
	 - `x` is called the preimage of `h(x)`
	 - "Difficult" means that brute force attacks are the only viable way to determine `x` from `h(x)`
	 - Brute force attacks have a complexity of `2^n`, where `n` is the bit size of the digest
 - Example: Consider a 128-bit has function
	 - The attacker would need to perform ~2^127 = 10^38 evaluations
		 - Collision attacks are only half of this
	 - Assuming one trillion evaluations per second -> 10^19 years
	 - If digest is 129 bits long (adding one extra bit), an attacker would need to spend twice as long to find an inverse
		 - 256-bit hash function multiplies `10^19` by `2^128`

### Second Preimage Resistance
 - Given a message, it should be difficult to find another message with same digest
	 - For a given `x` it should be difficult to find `y` such that `h(x)=h(y)`
 - Weaker version of collision resistance (collision of particular digest)
	 - If you have collision resistance, this is already implied
	 - If it is difficult to find any collisions, it is difficult to find a particular collision
 - Second preimage resistance does not guarantee preimage resistance
	 - Even if it is difficult to find a particular collision, it could be possible to invert a hash

### Message-Digest Algorithm 5 (MD5)
 - Developed by Ron Rivest in 1991, uses 128-bit hash values
 - Considered insecure, full collisions found in 2004
 - Still used in many legacy applications
 - In 2008, targeted collisions were found (algorithm was completely defeated)
	 - People were able to find 2 pdf files that hashed to the same value, but were different
	 - Practical attack was found to be able to create rogue certificates. Allowing them to impersonate any website on the internet, including banking and e-commerce sites secured using HTTPS protocol
 - Finding collisions took about 1-2 days on a cluster of 200 PS3s in 2008
	 - Sony tried to ban researchers from buying their PS3s for performing computations
 - In 2015: MD5 was still used by Microsoft for code updates
 - Most companies quickly migrated to SHA1

### Secure Hash Algorithm (SHA)
 - Family of cryptographic hash functions, published by NIST as a federal standard

**SHA-1**:
 - Developed by NSA, 160-bit output
 - Considered insecure, although more secure than MD5, still used in legacy systems
 - As of 2017, practical attacks (non-theoretical attacks) were reported
	 - Previously it would cost $100ks to break a single hash

**SHA-2**:
 - Developed by NSA
 - 256 and 512 bit output, still considered secure today
 - No significant attacks are reported

**SHA-3**:
 - Winner of public competition
 - Very different from SHA-1 and SHA-2
 - Output sizes: 224, 256, 384, 512 bits

### SHA1 Broken, 2017
 - shattered.io
 - 100k faster than brute-force birthday paradox attack
 - Produced 2 working PDF files with same hash but different contents
 - Team included the same person that broke MD5
 - git still uses SHA1 (hardened version)
 - In 2020, a chosen prefix attack was described
	 - Estimated $45k to generate collision for a chosen prefix

### MD5 Length Extension Attack on Signed Code
 - Append some extra stuff at the back of some code signed by an MD5 signature
	 - Ends up with the same MD5 signature even though there is additional (malicious) code
 - Add random data into a comment to produce the same signature

### Hashing Arbitrary Long Messages
 - Hash functions are often constructed from simpler one-way compression functions
 - Compression functions have the same properties as a general hash function
	 - Fast, deterministic, uniformity, preimage+2nd preimage + collision resistant
	 - The input has a fixed length (input block size)
 - Compression functions are then combined to implement cryptographic hash functions that accept variable length input

**Merkle Damgard Hash Function Construction**:
 - Method of building collision resistant crypto-hash function from simpler one-way compression functions
 - Property: If compression function is collision resistant, then the constructed function is also collision resistant
 - Many crypto hash functions are based on this method: MD5, SHA1, SHA2
 - The full message + padding is broken into blocks, combined with an Initialization Vector, and then hashed together
 - Common padding: 1 followed by many 0s followed by the length of the message
	 - `1000...0|message_length`

### Message Digest
 - Similar to checksum, but calculated using a cryptographic hash function
 - Can be used to detect malicious modifications
	 - Unless message & digest are both susceptible to tampering
 - Very useful for comparing data
	 - File deduplication
	 - Detection of file changes (git, verify downloads from mirrors)
	 - Synchronizing filesystems over network (rsync)
	 - Password storage (hashed & salted & peppered passwords)
 - Can be calculated from the command line
	 - `md5sum` `sha256sum`
 - Can be used to check message integrity
 - Messages are sent together with its digest
	 - Send the pair `(m, d)` where `m` is the message and `d = h(m)`
	 - Recipient receives `(m', d')` and computes his own digest `h(m')`
	 - Recipient compares his digest `h(m')` to the received digest `d'`
	 - Integrity is verified if they match
 - This does not guarantee if the message has been modified
	 - If someone can modify both message and digest, they can just change both
	 - The digest can be sent through some other channel
		 - Big file downloads will tell you the SHA of the file when you download it

**Computing SHA256 Digest Using Python**:
```python
import hashlib

f = open("test.data", "rb")
sha = hashlib.sha256()
while True:
	data = f.read(4096) # 4096 is a common size, file might be greater than RAM
	if not data:
		break
	sha.update(data)
f.close()

print(sha.hexdigest())
```

### Message Authentication Code (MAC)
 - MAC is similar to a digest, but can only be computed and verified knowing a secret
 - MAC is sometimes called a tag, or authentication tag
 - Possible (but not very good) implementation:
	 - `MAC(message, secret) = h(secret | message)` (`|` is concatenation)
	 - Insecure: Weak against some attacks for some hash functions (SHA3 is secure, else not)
 - MAC confirms
	 - Integrity of the message, AND
	 - Authenticity of the message
 - Same idea as digest, but requires knowing a secret to compute

**Keyed-Hash Message Authentication Code (HMAC)**:
 - Currently recommended implementation of MAC
 - Defends against length-extension attacks
 - `HMAC(m, k) = h(k1 | h(k2 | m))` where `k1, k2` are derived from `k`
	 - Requires application of `h()` twice
	 - Freedom to choose any `h()`
	 - Even HMAC-MD5 does not yet have practical attacks
	 - Most common is HMAC-SHA256
![[HMAC.png| 400]]

**Pseudocode**:
```
function hmac(key, message, hash) {
	// keys longer than input blocksize are shortened
	if (length(key) > blocksize)
		key = hash(key)

	// keys shorter than input blocksize are zero-padded
	if (length(key) < blocksize)
		key += [0x00 * (blocksize - length(key))]

	o_key_pad = [0x5c * blocksize] XOR key
	i_key_pad = [0x36 * blocksize] XOR key

	return hash(o_key_pad || hash(i_key_pad | message))
}
```

**Command Line**:
`echo -n "Hello World." | openssl dgst -sha1 -hmac "secret"`

**Python**:
```python
import hashlib
import hmac

key = "secret"
data = "Hello World."

m = hmac.new(key.encode('utf-8'), digestmod=hashlib.sha512)
m.update(data.encode('utf-8'))
print(m.hexdigest())
```