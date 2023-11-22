### Spectral Analysis
 - Fourier Theorem:
	 - Any continuous, periodic waveform can be expressed as the sum of a series of sine and cosine terms, each having specific amplitude and phase coefficients
	 - Any physical function that varies periodically with time with a frequency *f* can be expressed as a superposition of sinusoidal components of frequencies: *f, 2f, 3f, 4f, ...*
 - Pure tones can be added together to form a complex tone (*additive synthesis*)
 - *Fourier analysis* decomposes a complex signal into its component parts
	 - ie. its *spectrum*
	 - The *Fourier transform* calculates the spectrum of a continuous signal
		 - Transforms from the *time domain* to the *frequency domain*

### Discrete Fourier Transform (DFT)
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
 - C implementation:
```c
#define PI      3.141592653589793
#define TWO_PI  (2.0 * PI)

void dft(double x[], int N, double a[], double b[]) {
	int n, k;
	double omega = TWO_PI / (double)N;

	for (k = 0; k < N; k++) {
		a[k] = b[k] = 0.0;
		for (n = 0; n < N; n++) {
			a[k] += (x[n] * cos(omega * n * k));
			b[k] -= (x[n] * sin(omega * n * k));
		}
	}

	// Scale a_k and b_k by N
	for (k = 0; k < N; k++) {
		a[k] /= (double)N;
		b[k] /= (double)N;
	}
}
```
  - The *magnitude* or *amplitude* `|X(k)|` is given by:
    `|X(k)| = sqrt((a_k)^2 + (b_k)^2)`
```c
for (k = 0; k < N; k++) {
	amplitude[k] = sqrt( (a[k] * a[k]) + (b[k] * b[k]) );
}
```
 - The DFT gives amplitude for both positive and negative frequencies (harmonics)
	 - If N = 8:
```
| k | Harmonic |
| 0 |   0(DC)  |
| 1 |   1      |
| 2 |   2      |
| 3 |   3      |
| 4 |   4      |
| 5 |  -3      |
| 6 |  -2      |
| 7 |  -1      |
```
 - Add these together to get the amplitude of a harmonic
```c
x[0] = amplitude[0];
x[N/2] = amplitude[N/2];
for (k = 1, j = N-1; k < N/2; k++, j--) {
	x[k] = amplitude[k] + amplitude[j];
}
```

### Fast Fourier Transform (FFT)
 - The DFT is `O(N^2)`
	 - Not practical for large data sets
	 - Can be calculated more efficiently with the *fast Fourier transform* (FFT)
		 - Is `O(N log N)`
		 - Fast enough to process sound in real time
 - There are many variants of the FFT
	 - Most work by reordering the data, then recursively subdividing it in half
		 - Thus data size must be a power of 2
 - Most FFTs work with complex numbers (in programming, just a pair of numbers)
	 - The signal is the real part
	 - The imaginary part is set to 0
	 - This data is packed into an array of `size * 2`
![[fft_diagram.png|400]]
 - Diagram:
	 - Input (left) and output (right) arrays for FFT
	 - Input with N samples in array of length 2N, alternates between real and imaginary parts
	 - Output contains complex Fourier spectrum at N values of frequency, real and imaginary parts alternate
		 - Array starts at 0 frequency, works up to most positive frequency (ambiguous with most negative frequency)
		 - Negative frequencies follow, from second most negative up to frequency just below 0

### Convolution using the FFT
 - Time-domain convolution can be very slow, especially if `h[n]` is large
	 - Is `O(N*M)` where `N` and `M` are the sizes of `x[n]` and `h[n]`
 - *High-speed* or *FFT Convolution* uses the principle that convolution in the time domain corresponds to *multiplication* of spectra in the frequency domain
	 - This is the *convolution theorem*, and is expressed mathematically as:
	```
	x[n] * h[n] => X[k] x H[k] using DFT
	X[k] x H[k] => x[n] * h[n] using IDFT
	
	where x[n] * h[n] is in the time domain
	and X[k] x H[k] is in the frequency domain
	```
	 - Where `X[k]` and `H[k]` are the spectra of `x[n]` and `h[n]`:
		 - `X[k] = DFT[x[n]]`
		 - `H[k] = DFT[h[n]]`
