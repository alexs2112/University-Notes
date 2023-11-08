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
### Processing Diagram
![[digital_signal_processing.png]]