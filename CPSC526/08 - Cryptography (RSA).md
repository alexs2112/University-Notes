### Plain RSA (1977 Rivest, Shamir, Adleman, 1973 Cocks)
 - Public Key is a pair of numbers `(e,n)`
 - Private Key is a pair of numbers `(d,n)`
 - `Enc(e,n,m): c = m^e mod n` <- Where message `m` is integer `0 <= m < n`
	 - Can be calculated fast using fast modular exponentiation
 - `Dec(d,n,c): m = c^d mod n` <- Where ciphertext `c` is integer `0 <= c < n`
 - `Gen()`: selects `e, d, n` so that `m = m^(ed) mod n` for any `m`
	 - While simultaneously making it difficult for anyone to recover `m` from `m^e mod n`
		 - Similar to DHKE, instead of Discrete Logarithms it uses Factoring
	 - Security of RSA relies on factoring `n` (large integer, usually 4096+ bits long)
		 - `n` is actually a product of two very large primes
	 - Key generation is the complicated part of RSA
 - Typically used to establish a shared key, and then switch to symmetric key encryption (due to RSA issues and that symmetric key crypto is much faster)

**RSA - Key Generation**:
 - Select two different large random prime numbers `p` and `q`
	 - Note: Couple of additional requirements for `p`, `q` are needed for RSA to be secure
 - Calculate `n=p*q` and `t = lcm(p-1, q-1) = (p-1)(q-1)/gcd(p-1,q-1)`
 - Select `e` such that `2 < e < t` and `gcd(e,t)=1`
	 - eg. Keep trying different values `e=3,4,5,6,7,...`
 - Calculate modular multiplicative inverse of e, `d = e^(-1) (mod t)`
	 - eg. Using extended euclidean algorithm, or fast modular exponentiation
 - Notes:
	 - `(e,n)` are public, `(d)` is kept secret, `p` and `q` are destroyed
	 - `e` and `d` could be swapped, but we prefer `e` so that it is small and has minimal number of 1s in its binary representation (Hamming weight), to make encryption (modular exponentiation) as fast as possible
		 - Typical value for `e = 2^15 + 1 = 65537`
		 - This makes encryption really fast, and decryption really slow

**Plain RSA Example**:
1. Pick 2 random primes `p` and `q` (`p=3, q=11`)
2. Calculate `n = p*q` and `t = lcm(p-1, q-1)` (`n=33, t = 20/gcd(2,10) = 10`)
3. Select `e > 2` such that `gcd(e,t)=1` (`e=3, gcd(3,10) = 1`)
4. Calculate `d` such that `e*d = 1 (mod t)` (`d=7, (3*7)%10=1`)
5. Encrypt message `m, c = m^e mod n` (`m=5, c = 5^3 mod 33 = 26)
6. Decrypt ciphertext `c, m = c^d mod n` (`m=26^7 mod 33 = 5`)

**There is No Proof that RSA is Secure**:
 - No proof that integer factoring is hard
	 - One day we may discover a fast algorithm to factor integers -> RSA will be broken
 - No proven other methods to find the message without factoring `n`
	 - We believe that in order to extract `m` from `m^e mod n`, we need to factor `n=p*q`
	 - One day someone could discover a faster way to do this (without factoring integers)
		 - RSA will be broken
 - For now, RSA with `n > 2^2048` is considered secure

**RSA Factoring Challenge**:
 - RSA Laboratories (company started by same people that invented RSA) put out a challenge
 - Released several numbers of increasing sizes
 - Each number was created as a product of two primes p, q (which were not published)
 - Offered money to the first person able to factor the published numbers
 - 830 bit number took 6000+ years of computing hours to calculate

**RSA and Tiny Messages**:
 - When `m` is tiny and `e` is small, we could end up with `m^e < n -> c = m^e mod n = m^e`
	 - ie. then `m` could be recovered by calculating the `e`th root of `m`
 - Example: Encrypting 128 bit message `m` using public key (`e=17, n>2^4096`)
	 - Message `m` would encrypt to `c = m^17 mod n`
	 - But since `m < 2^128`
		 - `m^17 < (2^128)^17 = 2^2176 < 2^4096 < n`
		 - `c = m^17 mod n = m^17`
	 - An attacker that observes `c = m^17` and knows that public key `e = 17` could recover `m = c^17`
 - We need to make sure `m^e > n` -> `m > n^(-e) > 2^(b/e)` if `b` is bit-length of `n`
	 - Either we pick larger `e` (eg. `e=65537`)
	 - or we do not encrypt tiny messages
	 - or we add padding to the messages

**RSA Padding**:
 - Padding is an *essential* component of a secure RSA implementation
 - Industry standard is Optimal Asymmetric Encryption Padding (OAEP)
	 - Performed on every message, not just small `m`
	 - Plaintexts padded before encryption (`ciphertext = (m + padding)^e mod n`)
	 - Padding contains some randomness
		 - Some plaintext encrypted multiple times yields different ciphertexts
	 - Since padding uses up few bytes, the maximum size of `m` is actually few bytes smaller than `n`
 - RSA-OAEP is IND-CCA2 secure (under certain assumptions)

**RSA Common Pitfalls**:
 - `p, q` must be unique (truly randomly generated)
 - `p, q` must be large, but not too similar
 - `p-1,q-1` must not be multiples of small primes
 - Public exponent `e` cannot be too small
 - Private exponent `d` cannot be too small
 - Missing or incorrect padding used
 - Checking padding during decryption not implemented correctly
	 - Error messages can leak information
	 - Even taking longer/shorter time depending on valid/invalid padding can leak information
	 - This can lead to padding oracle attacks (CCA2 attacks)
 - TLS 1.3 removed much support for RSA (except for signatures)

**Encrypting Large Amounts of Data Using RSA**:
 - In order for RSA encryption + decryption to work, `m < n`
	 - If `m > n`, we would be encrypting only `m mod n` as all operations are `mod n`
	 - We would be losing information
 - What if we need to encrypt large amounts of data (`m > n`)
	 - Typical RSA implementation uses `n > 2^2048` which means our message can contain at most 256 bytes
	 - For messages longer than 256 bytes, we would need to split message into 256-byte blocks
	 - Or we could combine RSA with AES (hybrid crypto)

**Hybrid Cryptography**:
 - To achieve the same security, public key ciphers are much slower than symmetric ciphers
 - Consequently, public key ciphers are often used in combination with symmetric ciphers, resulting in hybrid cryptosystems
 - eg. secure communication:
	 - Alice chooses a random secret key (eg. for AES)
	 - Alice encrypts the key using Bob's public key and sends it to Bob
		 - Bob decrypts the key using his own private key
	 - Alice and Bob switch to symmetric cryptography for the rest of the communication
	 - Similar mechanism used in SSL/TLS (HTTPS)

**Alternative: Elliptic Curves**:
 - Elliptic curves (mod p) are used increasingly more than integers (mod p) (eg. RSA)
 - Elliptic curves DLP is believed to be as hard as possible for properly chosen curves (BS-GS is best known algorithm)
 - Elliptic curves can use smaller keys for the same amount of security
	 - Also easier to implement, harder to get small issues with
 - To achieve the same level of security as AES for 128/192/256 bits:
```
AES Key                128 bits   192 bits   256 bits
Elliptic Curve Modulus 256 bits   384 bits   512 bits
RSA or DH Modulus      3072 bits  8192 bits  15360 bits
```

**Post-Quantum Cryptography**:
 - Quantum computers pose a problem for public-key crypto
	 - Integer factorization, DLP, elliptic curve DLP could be solved efficiently by QC
 - Cryptographers are actively searching for replacements that resist quantum computing
	 - QCs are not yet powerful enough, but there is the harvest-now decrypt-later surveillance threat
 - Candidates:
	 - Lattice-based cryptography
	 - Isogeny-based cryptography (algebraic curves)
	 - Error-correcting codes
	 - Constructions using hash functions
 - Most symmetric crypto & hash functions are quantum resistant
