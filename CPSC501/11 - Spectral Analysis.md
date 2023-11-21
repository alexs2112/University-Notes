### Spectral Analysis
 - Fourier Theorem:
	 - Any continuous, periodic waveform can be expressed as the sum of a series of sine and cosine terms, each having specific amplitude and phase coefficients
	 - Any physical function that varies periodically with time with a frequency *f* can be expressed as a superposition of sinusoidal components of frequencies: *f, 2f, 3f, 4f, ...*
 - Pure tones can be added together to form a complex tone (*additive synthesis*)
 - *Fourier analysis* decomposes a complex signal into its component parts
	 - ie. its *spectrum*
	 - The *Fourier transform* calculates the spectrum of a continuous signal
		 - Transforms from the *time domain* to the *frequency domain*
 - The *Discrete Fourier Transform* (DFT) calculates the spectrum of a digital signal
	`DFT[x(n)] = X(k)`
	`sum(n=0 -> N-1) { x(n)e^(jωkn) }`    `0 <= k <= N-1`
	 - `N` is the number of samples per period of the waveform
	 - `k` is the harmonic number
	 - `ω = 2(pi)/N`
	 - `j = i = sqrt(-1)`
	 - `e = 2.718...`
	 - Since `e^(jx) = cos(x) + j sin(x)`, can be expressed as (Euler's identity)
	   `sum(n=0->N-1) { x(n) cos(ωnk) } - j sum(n=0->N-1) { x(n) sin(ωnk) }`    `0 <= k <= N-1`
	   (Real part `a_k`)                                         (imaginary part `b_k`)
		 - We must calculate the real part and the imaginary part separately
