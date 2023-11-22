### Sampling and Quantization
 - A continuous signal may be *sampled*
	 - Measured periodically at small intervals of time, converted into a series of numbers (samples)
		 - Such a series is a *digital signal*
	 - An *analog-to-digital converter* (ADC) does the sampling
		 - Eg. Sampling an audio signal
 - A *digital-to-analog* converter converts the digital signal back into an analog signal
**The *Sampling Theorem*:
 - The sampling frequency must be greater than twice the bandwidth of the signal in order to recreate it perfectly
	 - `f_h < R/2`, where `f_h` is the frequency of the highest component of the signal, and `R` is the sampling rate
 - If you sample at too low a rate, `aliasing` or `foldover distortion` results
 - The frequency of the alias is calculated with:
![[alias_frequency_formula.png|300]]
 - To avoid aliasing, the signal is low-pass filtered before `A/D` conversion, eliminating any frequency components above `R/2`
 - Common audio sample rates:
	 - CD: 44.1 kHz
		 - Note: Range of human hearing is 20 Hz to 20 kHz
	 - Pro Audio: 48 kHz, 96 kHz, 192 kHz
	 - Speech codecs: 8000 Hz
**Quantizing**:
 - The A/D converter *quantizes* the instantaneous amplitude of each sample
	 - ie. Represents it using N-bit binary number
		 - Normally a signed integer
	 - The more bits the better, to improve the signal-to-noise ratio
		 - Eg. 16 bits gives SNR of about 96 dB
 - Common sample sizes:
	 - CD: 16-bit
	 - Pro Audio: 20-bit, 24-bit
	 - Speech codecs: 8-bit, 12-bit

### Digital Signals
 - Are a function of discrete values of time (`n`)
	 - The samples are uniformly spaced in time
	 - Notation: `x(nT), N_1 <= n <= N_2, n in I`
		 - Where `T` is the sampling period (`1/R`)
		 - `T` is often assumed, so commonly written more simply as `x(n)`
 - Example: One second sine wave at 100 Hz
	 - Continuous representation:
		 - `f(t) = sin(ωt), 0 <= t <= 1`
		 - Where `ω = 2πF` is the angular (radian) frequenc
			 - `F` is the frequency in Hz
	 - Digital representation (500 Hz sample rate):
		 - `x(n) = sin(ωn), 0 <= n <= 499`
		 - Since `T` is assumed, we actually calculate with:
			 - `x(n) = sin(ωn/R)`

### Audio File Formats
 - A digital signal can be stored in a file for later playback or processing
 - Common file formats for uncompressed audio include:
	 - WAVE (file suffix is `.wav`)
	 - AIFF: Audio Interchange File Format (`.aiff`)
	 - Sound Designer II (`.sd2`)
	 - Sun & NeXT computers: (`.au` or `.snd`)
 - Most formats have two basic parts:
	 - Header: Describes sample rate, sample size, number of channels, encoding, etc
	 - Data: The sound samples
		 - If multichannel, the samples for each channel are normally *interleaved*
**WAVE File Format**:
 - Is a subset of RIFF (Resource Interchange File Format) for multimedia files
	 - Has a header plus a variable number of "chunks"
 - A WAVE file usually has a single WAVE chunk divided into 2 sub-chunks
	 - Format chunk: describes the format of the samples that follow
	 - Data chunk: ChunkID + ChunkSize + samples
 - Numeric values are 2-byte or 4-byte integers in little-endian format
	 - Special processing is necessary on a big-endian CPU
 - Strings are written to file in natural order, one ASCII character at a time
![[WAVE_file_format.png|450]]

### Time-Domain Convolution
 - *Convolution* is a mathematical operation that takes 2 input signals, `x[n]` and `h[n]`, to produce a 3rd signal `y[n]`
	 - Represented mathematically as:
	   `x[n] * h[n] = y[n]` (`*` is used in this case to represent convolution, not multiplication)
 - Input Side Algorithm, (array implementation):
```java
void convolve(float x[], int N, float h[], int M, float y[], int P) {
	int n, m;

	/* Clear output buffer y[]*/
	for (n = 0; n < P; n++) {
		y[n] = 0.0;
	}

	/* Outer Loop: Process each input value x[n] in turn */
	for (n = 0; n < N; n++) {
		/* Inner Loop: process x[n] with each sample of h[n] */
		for (m = 0; m < M; m++) {
			y[n+m] += x[n] * h[m];
		}
	}
}
```
 - Note:
	 - N, M, and P are the number of elements in each array
	 - P *must* equal N + M - 1
	 - The signals `x[n]`, `h[n]`, and `y[n]` are floating point numbers scaled to the range: -1.0 to +1.0
		 - You may need to convert to/from signed integers
	 - This algorithm can be adapted to deal with samples stored in audio files
 - Convolution is a *commutative* operation
	 - That is: `x[n] * h[n] = h[n] * x[n] = y[n]`
 - The signals `x[n]` and `h[n]` can be any arbitrary kind of signal
	 - However, `x[n]` is usually an input signal that you want to process
	 - And `h[n]` is the *impulse response* (IR) of a system you want model
 - The IR of a system is found by inputting a normalized impulse (*delta function*) into the system, and measuring or calculating the output
 - If the system is *linear* and *time-invariant* (LTI), the impulse response perfectly characterizes the system
	 - That is, we know how the system will respond to *any* input it receives
	 - We can thus simulate how a system would respond to an input signal by convolving the input signal with the system's IR
 - The IR of a concert hall can be found by firing a starting pistol (an approximate delta function), and using a microphone to record to the system's response
	 - Convolving a "dry" recording of an instrument with the IR results in an output signal where it sounds like the instrument is playing in the hall
		 - This is the basis for a *convolution reverb* digital effect

### Processing Diagram
![[digital_signal_processing.png]]