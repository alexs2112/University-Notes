### Historical Ciphers
 - Caesar Cipher
	 - Shift cipher
 - Polyalphabetic/Polygraphic Ciphers
	 - Caesar cipher, each letter maps to multiple potential characters
 - Vigenere Cipher
	 - Each letter maps to the associated letter of the key
 - One Time Pad (OTP, immune to brute force attacks)
	 - Can be done manually using modular arithmetic (addition mod 26)
	 - Practical issues: Key must be long, secret, truly random, and securely destroyed
 - Permutation/Transposition Ciphers
	 - Plaintext characters are permuted
	 - Example: HELP WE ARE UNDER ATTACK
		```
		HELPW
		EAREU
		NDERA
		TTACK
		```
	 - Ciphertext: HENTEADTLREAPERCWUAK
	 - Susceptible to statistical analysis
 - Substitution-Permutation Networks
	 - Several rounds of substitution and permutation ciphers
	 - Basis of many modern symmetric ciphers

### Confusion & Diffusion
 - Desireable properties of ciphers:
	 - Should be hard to figure out the plaintext from the ciphertext
	 - Should be hard to figure out the key from any amount of plaintext and ciphertext
 - Need to defend against any attacker
	 - The attacker could know the frequency distribution of plaintext
	 - Or attacker could know certain words or phrases that are used in the plaintext
 - 1945: Claude Shannon identified two important properties of ciphers
	 - If both are present, they make statistical analysis very difficult
	 - These properties are also desirable in cryptographic hash functions

**Confusion**:
 - Relationship between key and ciphertext must be complex
 - Any change in key should result in unpredictable change in ciphertext
 - Key cannot be deduced even from many different plaintext-ciphertext pairs
 - Generally implemented by some form of substitution

**Diffusion**:
 - Relationship between the plaintext and ciphertext is very complex
 - Any change in plaintext should change every bit of ciphertext with equal (50%) probability, and vice verse (avalanche effect)
 - Generally implemented by some form of permutation

### Encryption Scheme (Cipher)
Consists of three algorithms:
 - `Gen()` - Key generation algorithm
	 - Some ciphers require keys with special properties
	 - May create 2 different keys, one for encryption and a different one for decryption
 - `Enc()` - Encryption algorithm
	 - `ciphertext = Enc(key, plaintext)`
 - `Dec()` - Decryption algorithm
	 - `plaintext = Dec(key, ciphertext)`

**Symmetric Key Encryption**:
 - Use a single key
 - The key must be known by both parties, but otherwise must remain secret
 - The secret key is used for encryption and decryption
 - Classical ciphers are symmetric

**Public Key Encryption**:
 - Use two different keys
 - A public key used to encrypt, should be known by everyone
	 - Tricky to make this fully public, attackers can otherwise pretend to be them
 - A private key used to decrypt, must remain secret to the receiver
 - Sender only needs to know receivers public key
 - Example: Alice encrypt using Bob's public key -> Bob decrypts using Bob's private key

### Cryptanalytic Attacks
 - Attackers goals:
	 - Recover the key (ultimate)
	 - Recover the plaintext (often good enough)
	 - Learn something about the key or plaintext (partial information extraction)
 - The more information the attacker has, the more likely he is to succeed
 - We always assume that the attacker knows at least one ciphertext

### Secrecy
 - Eve wants to find out what's in a box
 - Eve knows its either a feather or a bowling ball
 - Eve could try to perform experiments to help her decide what the box contains
 - Box is secure if Eve's best strategy to distinguish between any two objects is equivalent to tossing a coin

**Secrecy as a Game**:
 - Secrecy is highly dependent on:
	 - What the defender definitely does
	 - What the attacker might do
 - We can think about this by modelling interactions between attackers and defenders as a game with well-defined rules
	 - Encryption is secure iff attacker loses, regardless of the strategy used
	 - We try to give the attacker as much freedom as possible

**Basic Cryptanalytic Attack Types**:
 - Ciphertext-Only Attack
	 - Attacker only knows ciphertext, or set of ciphertexts
	 - This one is always assumed
 - Known-Plaintext Attack (KPA)
	 - Attacker also observes one or more (plaintext, ciphertext) pairs
 - Chosen-Plaintext Attack (CPA)
	 - Attacker is able to choose any number of plaintexts to encrypt
 - Chosen-Ciphertext Attack (CCA1)
	 - Attacker is able to select any number of ciphertexts, then decrypt them
 - Adaptive Chosen-Ciphertext Attack (CCA2)
	 - Attacker is able to repeat CCA1 as many times as he likes

**IND-CPA**:
 - Indistinguishable under Chosen Plaintext Attack
 - Eve chooses two plaintexts and sends them to Alice
	 - Alice encrypts one of them at random and sends the ciphertext to Eve
	 - Alice wins if Eve has a 50% chance to guess which plaintext was encrypted
 - Example of Computational Security - Attacker limited to polynomial time algorithm
	 - Most modern ciphers are only computationally secure
	 - Assumes some problems are and will continue to be difficult to solve
	 - Not immune to attacks with infinite computational power
		 - Not information-theoretically secure
 - Perfect Secrecy: No limitations on algorithm for correct guesses
	 - Algorithm is allowed unbounded computational capacity
	 - Algorithm is allowed limitless storage capacity
	 - Algorithm is assumed to be the cleverest algorithm in existence

### DES - Data Encryption Standard
 - Developed by IBM and adopted by NIST in 1977 (competition)
 - Declared as federal standard for unclassified sensitive data
 - Used 64-bit and 56-bit keys
	 - Small key space makes exhaustive search attack feasible since late 90s
 - Not secure at all today, brute-force attack is feasible due to short 56-bit key
	 - About 1 day to brute force a key in 2012
 - Generated a lot of interest in cryptographic community, they wanted to break it because they knew the key was way too short
 - No longer a standard, replaced by AES

**Algorithm**:
 - DES uses a Feistel Network
 - Approach: Generate complexity by repeating a simple operation (rounds)
 - Round `i` uses a sub-key `Ki` derived from `K`
 - Encryption and decryption are the same algorithm, but using the subkeys in reverse order
 - 16 rounds in total
 - Security depends on the function `F` (Feistel Function)
![[DES_algorithm.png|300]]

### Triple DES (3DES)
 - 3DES is a nested application of DES with three different keys (`KA, KB, KC`)
	 - `ciphertext = Enc(KC, Dec(KB, Enc(KA, plainted)))`
	 - `plaintext = Dec(KA, Enc(KB, Dec(KC, ciphertext)))`
 - Effective key length is 168 bits, making exhaustive search attacks infeasible
 - Still used today and considered secure

**Meet-in-the-Middle Attack**:
 - Different from MITM (man-in-the-middle attack)
 - Space-time tradeoff attack on schemes using repeated encryption
 - Example: 2DES with two keys: K1, K2
	 - encryption: `C = Enc(K2, Enc(K1, P))`
	 - decryption: `P = Dec(K1, Dec(K2, C))`
 - Brute force attack with O(1) memory would require `2 ^ (56 + 56) = 2 ^ 112` tries
 - With `O(2^56)` memory, we can execute meet-in-the-middle attack
	 - Requires precomputing all `Enc(K1, P)` and `Dec(K2, C)` possibilities to identify key candidates
 - 2DES despite having 112 bit key size, only offers 57 bit security
 - 3DES is also vulnerable to meet-in-the-middle attacks
	 - Key size is 168 bits, offers 112 bit security, provided O(2^56) space is feasible
	 - NIST predicts 3DES should remain safe until ~2030

### Perfect Secrecy
 - Tells us something about eavesdropping attacks
	 - Namely, that they cannot succeed
 - But it tells us nothing about message integrity
	 - If Eve modified our encrypted messages, would we know?
	 - Resulting plaintext would likely be gibberish, but not always

**Malleability of the OTP**:
 - OTP is malleable
	 - It is possible to replace ciphertext with a different one that decrypts to a related plaintext
	 - Without knowing the key
 - Consider the following pair of messages `m0=0` and `m1=1`
 - Suppose ciphertext `c=Enc(m0)` or `c=Enc(m1)`, but we don't know which
 - We can undetectably swap out one plaintext for the other
	 - We can replace `c` with `c'` so that the decryption of `c'` will yield the opposite plaintext
	 - In this case, flip the bit. `c' = !c`
 - Second example: Following pair of messages `m0 = "Friday"` and `m1 = "Monday"`
	 - Again, `c` is an encryption of either `m0` or `m1`
	 - We can perform several XORs on the OTP to change the ciphertext
	 - `c' = c XOR m0 XOR m1`, such that `c'` is now flipped to the other message
		 - `c` XOR `m0` or `m1` becomes nothing, resulting in the other message

### Advanced Encryption Standard (AES)
 - Selected by NIST in 2001 through open international competition and public discussion
 - Block size: 128-bits
 - Key lengths: 128, 192, 256 bits
 - AES-256 is currently the symmetric encryption algorithm of choice

**Overall Structure**:
 - Based on permutation-substitution network
 - AES encryption algorithm proceeds in 10-14 rounds
 - Each round performs an invertible transformation on a 128-bit block
 - The initial state `X0` is the XOR of the plaintext P with the key K
 - Round `i` receives state `X_(i-1)` as input and produces state `X_i`
 - The ciphertext `C` is the output of the final round: `C = X_n`
 - Decryption: Reverse the rounds

**AES Rounds**:
 - 4 steps per round
 - `SubBytes`: An S-Box substitution step
 - `ShiftRows`: A permutation step
 - `MixColumns`: A matrix multiplication step, skipped in last round
 - `AddRoundKey`: An XOR step with a round key derived from the 128-bit encryption key

### Block Ciphers
 - Modern ciphers operate on fixed-length blocks (128 bits)
 - To encrypt messages of arbitrary length, we split the message into blocks
	 - A plaintext of length n is partitioned into a sequence of m blocks
	 - Each block has length of b
	 - Last block may require padding to make its length also b
 - The message is then encrypted block by block

 **Block Cipher Mode of Operation**:
  - A mode of operation describes the way a block cipher encrypts and decrypts a sequence of message blocks
  - Standardized modes: ECB, CB, OFB, CFB, CTR, GCM

**Electronic Code Book (ECB)**:
  - Simplest block cipher mode
  - Plaintext block `p[i]` encrypts into ciphertext block `c[i] = Enc(k, p[i])`
  - You can easily parallelize the encryption and decryption, otherwise this algorithm is very bad (nothing determines on anything else)
	  - ECB is just a substitution cipher (on 128 bit blocks), with all its weaknesses
  - Recall IND-CPA, ECB is not IND-CPA
	  - Choose `m0 = {0}^n || {0}^n` (two zero blocks) and `m1 = {0}^n || {1}n`
	  - Because each block is independently:
		  - `Enc(k, m0)` consists of two identical ciphertext blocks
		  - `Enc(k, m1)` consists of two different blocks
	  - We can tell them apart and win the game 100% of the time

**Counter Mode (CTR)**:
 - Mimics the OTP
 - CTR turns a block cipher into a stream cipher (eg. using AES-256)
	 - Encryption: Ciphertext block `c[i] = Enc(k, nonce+i) XOR p[i]`
	 - Encryption: Ciphertext block `p[i] = Enc(k, nonce+i) XOR c[i]`
 - CTR mimics the OTP cipher, creating the pad by encrypting consecutive numbers nonce + 0, nonce + 1, nonce + 2, etc. 
	 - The variable nonce is a randomly chosen number to make sure the pad is never re-used
	 - The nonce is sort of a second key, both parties must also know the nonce
 - CTR can be parallelized

### Chosen Ciphertext Attacks
 - Chosen Ciphertext Attack (CCA1)
	 - Adversary is allowed to get decryptions of any number of ciphertexts
	 - Ciphertexts must be selected before decryption
	 - Make a bunch of ciphertexts, then decrypt them all at once and cannot decrypt any more
 - Adaptive Chosen Ciphertext Attacks (CCA2)
	 - Adversary can select and decrypt any number of ciphertexts, and then repeat the process forever
 - Gold standard for encryption secrecy is IND-CCA2

**Galois Counter Mode (GCM)**:
 - CTR does not detect tampering with the ciphertext, but otherwise is a pretty good cipher
	 - Note: CTR can be combined with an authentication mechanism, but it's inefficient
 - GCM is an authenticated encryption mode
	 - Uses CTR for the encryption
	 - and GHASH hash function for authentication
	 - Computes ciphertext and an authentication tag directly
	 - IND-CCA2, therefore non-malleable for some block ciphers (AES)
 - Advantages of GCM vs CTR + authentication
	 - Very fast (2.5 GPU cycles per byte)
 - Current best practice for block cipher usage
	 - Used in modern Wi-Fi, SSH, TLS (https), OpenVPN, ...

### Applications of Secret Key Cryptography
 - Mutual authentication via challenge-response
	 - Prove knowledge of a key without revealing it
	 - Alice and Bob want to prove to each other they both know secret key K
1. Alice creates and sends unique challenge `Ca`
2. Bob creates and sends unique challenge `Cb`
3. Alice computes and sends back `Ra = Enc(K, Cb)`
4. Bob computes and sends back `Rb = Enc(K, Ca)`
5. Alice verifies `Dec(K, Rb) = Ca`
6. Bob verifies `Dec(K, Ra) = Cb`
