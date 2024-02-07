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
 - `g` is selected to be a primitive root `(mod p)` in order to maximize the number of possible shared keys
	 - The math still works if `g` is not a primitive root, however it is less secure

**Calculating `a^n` Efficiently**:
 - an intuitive algorithm to calculate `a^n` uses `O(n-1)` multiplications
	 - `a -> a^2 -> a^3 -> ... -> a^(n-1) -> a^n`
 - This is impractical for modern cryptography with very large `n` (`n = 2^4096`)
 - There is a much faster algorithm using only `O(log n)` multiplications
 
 **Exponentiation by Squaring**:
  - Example: Calculate 2^358
  - Convert 358 to binary from right to left (repeated division by 2), simultaneously calculate powers of 2 by repeated squaring
```
358 in Binary: 1     0     1    1    0    0    1    1    0
2^powers of 2: 2^256 2^128 2^64 2^32 2^16 2^8  2^4  2^2  2^1
```
 - Now multiply the powers of 2^k in second row in columns corresponding to digit 1
	 - 2^358 = 2^256 * 2^64 * 2^32 * 2^4 * 2^2
	 - Total multiplications: 9 + 4 = 13 instead of 357

**Modular Exponentiation by Squaring**:
 - Nearly identical to regular exponentiation by squaring, but with 2 more improvements
 - 1. When p is prime, reduce exponent by applying Fermat's Little Theorem
	 - `g^a mod p = g^(a mod (p-1)) mod p`
	 - Example: `15^898 mod 173 = 15^(898 mod 172) mod 173 = 15^38 mod 173`
 - 2. Apply (mod p) to each multiplication result
	 - All intermediate calculation results will e < p, which makes this much more efficient
 - Example: Calculate `15^898 mod 173`
 - 173 is prime -> `15^898 mod 173 = 15^38 mod 173`
```
	38 in Binary:   1    0    0    1    1    0
Repeated Squares: 15^32 15^16 15^8 15^4 15^2 15^1
				= 22^2  117^2 109^2 52^2 15^2
				= 138   22    117  109  52  15
```
 - Result = `15^38 mod 173 = 15^32 * 15^4 * 15^2 mod 173 = 138 * 109 * 52 mod 173 = 51`

**Modular Exponentiation by Squaring in Python**:
```
$ ipython
In [1]: help(pow)
pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

In [16]: %timeit 1111**2000134 % 10007
3.71 s ± 41.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [17]: %timeit pow(1111,2000134,10007)
1.13 µs ± 24 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
```

**Exponentiation by Squaring**:
 - Exponentiation by squaring O(log n) is not the most optimal algorithm, but it is not significantly slower than the optimal one
	 - Much easier to understand and to implement

### Computing Discrete Logarithms
 - Given `g`, `a`, and `p`, computing `g^a mod p` is easy due to fast exponentiation by squaring
	 - This is the computation Alice and Bob do to obtain shared secret using DHKE
 - If we know `g`, `p`, and `g^a mod p`, we cannot efficiently figure out `a`
	 - This is what the attacker would do to obtain a private key
	 - Eg. Find `k` such that `15^k ≡ 51 (mod 173)`
	 - This is the discrete logarithm problem
 - Simplest idea to solve DLP
	 - Keep computing `g, g^2, g^3, ..., g^k` until `g^k ≡ a (mod p)`
	 - Requires O(k) multiplications

**Exhaustive Search**:
 - Keep trying different values for `k = {0, 1, 2, ..., p-1}` until we find a solution
 - Solving `15^k ≡ 51 (mod 173)` requires 38 multiplications, as `k=38` is the solution
 - Solving `15^k ≡ 150 (mod 173)` requires 171 multiplications, as `k=171` is the solution
 - On average, if `p` is prime, exhaustive search would require `p/2` multiplications
	 - If `p = 2^4096`, it would take the fastest supercomputer `10^1000` years to compute

**Solving DLP with Faster Search**:
 - There are faster algorithms than exhaustive search
	 - "Baby-Step Giant-Step" algorithm requires on average `O(sqrt(p))` multiplications
 - Even the best known algorithms are much slower than exponentiation
	 - Eve has to do much much more work than Alice and Bob
 - This leads us to believe DHKE is secure, as long as we pick very large `p`
	 - As of 2023, `p>2^2048` is considered secure, and `p>2^4096` is even more secure
	 - Until someone shows DHKE is less difficult than DLP, or someone finds a more efficient way to solve DLP

**Baby-Step Giant-Step**: Example using `15^k = 51 (mod 173)`
 - Exhaustive Search: Start with 1 and move up
	 - `1 -> 15^1 -> 15^2 -> 15^3 ... -> 15^37 -> 15^38 = 51 (mod 173)`
 - Alternatively, we can start at 51 and work backwards, counting how many times we have to multiply 51 by 15^-1 to reach 1
	 - `51 -> 51 * (15^1)^1 -> 15 * (15^-1)^2 -> ... -> 51 * (15^-1)^k = 1 (mod 173)`
	 - n^-1 mod p can be calculated using the Extended Euler Algorithm
	 - If p is prime, can use Euler's theorem + fast exponentiation by squaring
 - If we start at both ends of the sequence: (Meet in the Middle)
	 - Correct result, but not any more efficient
 - We can adjust the end condition
	 - We precompute the last 15 entries of the sequence by tracing backwards (step = 15^-1)
	 - `31←119←55←133←92←169←113←138←167←83←34←164←38←51`
	 - Ten use a giant-step (step=15^14) to compute the beginning of the sequence
	 - After each giant step, we check against the 14 precomputed endings
		 - Use a hash table for O(1) time
		 - `1 -> ... -> 47`, 47 is not in the precomputed entries of the sequence
		 - `47 -> ... -> 133`, 133 is in the precomputed entries of the sequence
![[baby_step_giant_step.png]]
 - Solution: `k = 2*14 + 10 = 38`, with a total of `2 + 14 = 16` multiplications
	 - Note this does not include multiplications for the fast exponentiation of 15^14 and 15^-1 = 15^171
 - We pick giant-step size of 14 as `14 = ceil(sqrt(173))`
	 - By picking `sqrt(p)` step, we get best worst case number of multiplications `2sqrt(p)`
