### Diffie-Hellman Key Exchange (DHKE)
 - Alice and Bob want to communicate securely (eg. using AES-256-GCM)
	 - Need to set up a shared secret key
 - One of the first public key protocols (1976)
	 - Used for generating a shared secret between two parties
	 - The secret can then be used as a key for symmetric encryption
 - Relies on the assumption that the Discrete Logarithm Problem (DLP) is difficult
	 - And on the assumption that DHKE is as hard as the DLP
 - Used to this day:
	 - When you visit a secure website, browser and server use Diffie-Hellman to establish a shared key
	 - After exchanging secret keys your browser immediately switches to a symmetric key system for data encryption (often a stream cipher, AES-GSM)

**Algorithm**:
1. Alice and Bob publicly choose a large prime number `p` and number `g`, where `g` is a primitive root modulo `p`
2. Alice chooses a random number `a`, and sends Bob (`g^a mod p`)
3. Bob chooses a random number `b`, and sends Alice (`g^b mod p`)
4. Bob computes shared key `K = (g^a mod p)^b mod p`
5. Alice computes shared key `K = (g^b mod p)^a mod p`
	1. At this point `a` and `b` should be destroyed
6. Alice and Bob now have  the same key `K`, and can use it to operate a symmetric cipher
 - Note, an eavesdropper cannot compute `K = g^(ab) mod p` because the only known values are `g`, `p`, `(g^a mod p)`, and `(g^b mod p)`.
 - Eavesdropper would need to reverse-engineer either `a` or `b`, but cannot as DLP is a hard problem

**Modular Congruence**:
 - If `a, b, n in Z` such that `n > 0` then:
	 - `a` and `b` are congruent modulo `n` iff `a mod n = b mod n` iff `a ≡ b (mod n)`

**Multiplicative Inverse Modulo n**:
 - Question: If `17 * x ≡ 1 (mod n)`, what is `x`?
	 - x is the multiplicative inverse of `17 (mod n)`
	 - `x = 17^(-1) (mod n)`
 - Depending on `n`, there will be either:
	 - Infinitely many multiplicative inverses modulo n; or
	 - no multiplicative inverses modulo n
 - Suppose `x in Z_n` (x is a member of a set of integers modulo n)
	 - `x^-1` exists in `Z_n` whenever `gcd(x, n) = 1`
	 - Can be computed using the Extended Euclidean Algorithm
 - Note: If n is prime, then every integer x has `gcd(x, n) = 1` except if `x ≡ 0 (mod n)`

**Computing gcd(a,b)**:
 - Around 300 BC, Euclid noticed that if `a>b` then `gcd(a, b) = gcd(a-b, b)`
 - A more efficient observation: `a>b` then `gcd(a, b) = gcd(a mod b, b)`
```
while b != 0:
	(a,b) <- (b, a mod b)
return a
```
 - Example: `gcd(1071, 462) = gcd(462, 147) = gcd(147, 21) = gcd(21, 0) = 21`

**Primitive Root Modulo p**:
 - If `p` is a prime, an integer `g in Z` is a primitive root modulo p if:
	 - `{g^1 mod p, g^2 mod p, ..., g^(p-1) mod p} = {1, 2, 3, ..., p-2}`
	 - ie. every number `{1, 2, ..., p-1}` can be written as `g^k mod p` for some `k`
	 - ie. if we raise `g` to powers `1, 2, ..., p-1 (mod p)` we get every number `1, 2, ..., p-1` exactly once
	 - ie. `g` is a generator of `Z_p`
 - Example:
```
	p = 7, g = 3
	3^1 ≡ 3, 3^2 ≡ 2, 3^3 ≡ 6, 3^4 ≡ 4, 3^5 ≡ 5, 3^6 ≡ 1 (mod 7)
	-> 3 is a primitive root modulo 7
```
 - Example:
```
	p = 7, g = 2
	2^1 ≡ 2, 2^2 ≡ 4, 2^3 ≡ 1, 2^4 ≡ 2, 2^5 ≡ 4, 2^6 ≡ 1 (mod 7)
	-> 2 is not a primitive root modulo 7
```
