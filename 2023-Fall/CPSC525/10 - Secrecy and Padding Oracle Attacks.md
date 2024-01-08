### Encryption
 - An encryption scheme has three algorithms:
	 - `Gen` creates one or more keys
	 - `Enc` locks messages under a given key
	 - `Dec` unlocks messages using an associated key
 - To be useful, the scheme `(Gen, Enc, Dec)` must give correct decryptions
	 - If `(K1, K2)` is a pair of keys created by `Gen` and `M` is a valid message, then
	   `Dec(K2; Enc(K1; M))=M`
 - Public-Key (asymmetric) encryption, there are two keys:
	 - A *public key* used (by anyone) to encrypt
	 - A *private key* used to decrypt
 - In symmetric-key encryption, there is only one key used both to encrypt and decrypt

### Secrecy
**Definition**: Secrecy as a game
 - Secrecy is highly dependent on:
	 - What the defender *definitely* does
	 - What the attacker *might* do
 - Model interplay between attackers and defenders as a game with well-defined rules
	 - Encryption is secure iff the attacker loses regardless of their strategy


**One-Time Indistinguishability Game**:
![[one-time_indistinguishability_game.png]]
 - Definition: An encryption scheme has indistinguishable encryptions in the presence of an eavesdropper if, for every `PPT` algorithm `A`, there exists a negligible function `ε: N -> R+` such that
		`Adv^(one-time)(A) <= ε(n)`
	 - `PPT`: Probabilistic Polynomial Time
		 - Roughly: Running time isn't ludicrous (compared to input size)
	 - `negligible`: Roughly: `ε(n)` is practically equal to 0 (except perhaps if `n` is tiny)
**Stronger Notions of Security**:
 - This definition is amenable to mathematical proofs
 - But is far too simplistic to be useful for most cryptographic scenarios
**Multi-Message Indistinguishability Game**:
![[multi-message_indistinguishability_game.png]]
 - Attacker is allowed to adaptively choose messages it would like to see encrypted
	 - Basically: The attacker can try to probe for weaknesses in the key to inform its choice of `(m0,m1)`
	 - Likewise, let the attacker make more queries after learning `c`, in case these help it deduce `b`
 - Models the case where many things (some of which are known to the attacker) were encrypted under the same key
**IND-CPA Security**:
 - Definition: An encryption scheme has indistinguishable encryptions under chosen plaintext attacks (IND-CPA) if, for every PPT algorithm A, there exists a negligible function `ε: N -> R+` such that 
   `Adv^(cpa)(A) <= ε(n)`
 - Considered the bare minimum for useful encryption, often insufficient
 - In the real world, the attacker can sometimes trick users into revealing information by presenting them with malformed ciphertexts
	 - Eg. A TLS server that spits out errors when it receives a malformed ciphertext
**IND-CCA Security**:
 - Definition: An encryption scheme has indistinguishable encryptions under chosen ciphertext attacks (IND-CCA) if, for every PPT algorithm A, there exists a negligible function `ε: N -> R+` such that 
   `Adv^(cca)(A) <= ε(n)`
	 - Chosen ciphertext attacks essentially allow the attacker to submit ciphertexts to be decrypted by the defender
 - In practice, there is rarely a party who will literally decrypt for the attacker
 - Instead, the attacker relies on side channels
	 - How long it takes for the server to respond
	 - What actions the server takes upon receiving the ciphertext
	 - Etc

### Block Ciphers & Modes of Operation
 - One of the most common types of encryption scheme is called a block cipher
 - Takes as input:
	 - A fixed-size block of plaintext (say, 16 bytes) and
	 - A fixed-size key (say, 16 bytes)
 - And it outputs
	 - A fixed-size block of ciphertext (same size as the input)
 - The block cipher is invertible, given the key and the fixed-size ciphertext output by the block cipher, one can recover the plaintext
 - On their own, they do not provide IND-CPA (let alone IND-CCA) security
	 - Encrypting the same message repeatedly always yields the same ciphertext
	 - Likewise, block ciphers alone cannot encrypt arbitrary-length messages
	 - Splitting a message into fixed-size parts and encrypting them works only if we have IND-CPA security
**Cipher-Block Chaining (CBC) Mode**:
 - Choose something called `IV` (initialization vector)
	 - Needs to be random every single time, should never be hardcoded
 - Break the message `M` into several chunks (`M1, M2, M3, ...`)
	 - Essentially one-time padding the first chunk of the message with the IV, and then encrypting that
	 - This turns the output `c1` into a different message each time it is run through the encryption scheme, looks random as IV is random
 - `c1` is then XORd with the next block of the message and encrypted, continue this process until you have encrypted the whole message
	 - The resulting ciphertext will always have a size that is exactly one block longer than the provided message as the IV must be included
	 - Message: `M1, M2, M3, M4`, Ciphertext: `IV, C1, C2, C3, C4`
![[cbc_encyption.png|400]]
 - Decryption:
	 - Go in reverse order, have to decrypt the last block first
	 - Decrypt `C4` and that needs to be XORd with `C3` which gives us `M4`
	 - Decrypt `C3` and that needs to be XORd with `C2` which gives us `M3`
	 - Continue, until you get `M1`
![[cbc_decryption.png|400]]
**CBC Mode -> IND-CPA**:
 - The CBC mode operation yields an IND-CPA secure, by submitting an altered ciphertext you can see how the decryption affects the output plaintext, and you can tell which one of the two messages submitted were decrypted
	 - ie. Modifying `ci` yields predictable changes to `m(i+1)`
 - To get IND-CCA security, it is common to add a message authentication code (MAC) to detect modifications
	 - Essentially a hash function with a secret key
**CBC With a MAC-then-encrypt**:
 - Typically a bad idea, MAC's should come last, but this is how the third assignment is done
 - Essentially the entire message is XORd with the hash of the entire message
 - So when you decrypt, if the message has been altered then the hash of the message will be different and when you XOR those two you will get gibberish
![[cbc_mac_then_encrypt.png|400]]
 - For the assignment: The attack lets you learn everything except for the first block of the message, by putting the mac at the start of the message we can learn everything that we actually care about

### PKCS `#5/PKCS #7 padding`
 - The previous examples assume that `m` can be decomposed into an integral number of blocks
	 - If `|m|` is not a multiple of the block length, some sort of padding is needed
 - The padding must be unambiguously identifiable by a computer
**Idea**:
 - Each padding byte is equal to the total number of padding bytes
 - If `m` is a multiple of block length, add a block that consists entirely of padding bytes (a block in which each byte is `16`)
- Example: 10 bytes of plaintext, 6 bytes of padding: `ABCDEFGHIJ666666`
- Example: 10 bytes of plaintext character `6`, 6 bytes of padding: `6666666666666666`
**To remove padding:
 - Read last byte
 - Check that each of the last `n` bytes are all `n`
	 - If not, ciphertext is malformed, abort
	 - Else, discard the last `n` bytes
 - Then be sure to check the MAC

### Padding Oracles
 - The term *padding oracle* refers to the fact that a TLS server can sometimes be made to leak information about how a ciphertext is malformed
	 - Either the padding is incorrect
	 - Or the MAC is incorrect
 - Leverages a timing channel: Checking the padding is super-duper fast, checking the MAC is merely quite fast
	 - If error message comes very quickly, padding was probably bad
		 - Use this to learn 1-byte of plaintext
**Idea with CBC mode**:
 - When you are decrypting `C4`, if you flip a bit in `C3` we will flip the equivalent bit in resulting `M4`
	 - This also blows up the rest of the decryption, but that doesn't matter if we get infinite tries
	 - As we have made a predictable change to the last block of the plaintext, the padding check may fail and abort before going on to decrypting `C2`
**Padding Oracle Attack**:
`M4 = DK(C4) XOR C3`
 - Change last byte of C3 => predictable change to last byte of M4
 - If this last byte is wrong, then the padding check will probably fail
 - If the expected byte is a 1, the padding check will pass but then the MAC check will fail
	 - We now know that the byte is a 1, we know the bytes we had to change to make it as a 1, so we can deduce what it started as
	 - So we know what the padding looks like
 - We can then XOR the last n bytes with `n XOR (n+1)`, which will change the padding bytes into the padding + 1. Now the padding is incorrect again, but we can start flipping bytes in the new byte until it passes the padding check again.
	 - You can then deduce the `n+1` byte of the plaintext
	 - Then change the padding bytes into `n + 2`
 - Continue until you have learned the entire block of 16 bytes
	 - Then you can just cut the last block off the ciphertext and start playing the same game again
**Essentially**:
 - Start messing with the last byte of the last block until the padding check succeeds
 - Once the padding check succeeds, you know you have turned it into a 1
	 - You know that you have turned it into a 1 by XORing it with a fixed value, so you know what the original value is
 - Then you can turn it into a 2, try to figure out the next byte in the block, then rinse and repeat
	 - Take the resulting value, XOR it with 0x01 to get 0x00, then XOR that with 0x02 to set it to 0x02 to then check the next segment
		 - Will look something like `Dk(C4) XOR C3 XOR 0x01 XOR 0x02 = 0x02`

Example process in [[worksheet11.pdf]]
