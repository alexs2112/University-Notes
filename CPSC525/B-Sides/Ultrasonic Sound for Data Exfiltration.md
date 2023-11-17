### Intro
 - Problem: If a system isn't connected to the network, how do we exfiltrate data from it?
 - Definition: Side channel attacks exploit indirect information, such as physical emissions or system behavior, to gain insights into a systems operation and extract data without direct access to the target system itself.
 - Ultrasonic Spectrum: Human ear typically hears between 20 Hz to 20 kHz. Ultrasonic frequencies start from 20 kHz upwards, not detectable by the human ear but can be captured by certain microphones and devices.

**Idea**:
 - Playing a sound on a frequency higher than most people can hear, using different frequencies to represent binary data, allowing it to bypass traditional network security measures undetected.
 - Use this technique to covertly broadcast information from an airgap device that can then be recorded on another device in relatively close proximity

### Payload Delivery
 - MouseJacking: Wireless attack that exploits vulnerabilities in non-Bluetooth wireless mice and keyboards
	 - Intercepts and injects malicious packets into the target's wireless communication, attacker can gain unauthorized access and control over the victim's computer.
	 - This is the method used for the demonstrations in the presentation
 - Bad USB: Exploits inherent trust between a computer and USB devices
	 - Reprogramming the USB device firmware, attacker can create a seemingly benign device that can execute malicious activities when connected to a computer
 - Modified USB: Use of physically altered USB devices to compromise a target system
	 - Can be engineered to bypass security measures, deliver malicious payloads, or exfiltrate data without raising suspicion

**Process**:
1. Find the Target: Use Bettercap to listen for vulnerable devices.
2. Inject Malicious Script: Use Bettercap to start injecting keystrokes into the victim machine.
3. Volume Control: Script mutes the volume to hide UAC sound, then sets volume to 100 in admin powershell.
4. Admin Powershell: Once in admin powershell, main script is written, policies changed to allow it to run at a later date. This makes the malware persistent.
5. Ultrasonic Sound: Script plays data using beeps in a frequency that can't be heard, but is detectable by microphones.
6. Record the Data: Record ultrasonic sound data using a cell phone to be decoded later.
7. Reconstruction: Reconstruct the exfiltrated file with a Python script.

### Data Reconstruction
 - Other programs, such as Audacity, can be used to clean up background noise and automatically reduce noise outside of the range that you want
 - As the frequency of the transmitted data is so high, cleaning up noise outside of that range will leave very clear data points.
 - A python script is then used to analyze the soundwave from the recorded file of the raw sound data
	 - Slices the data into small chunks, then analyzes the frequencies to see if they are within a certain range

### Conclusion
**Challenges**:
 - Transmission reliability
 - Background noise during recording
 - Data transfer speed
 - Error correction

**Improvements**:
 - Data transfer speed
 - Reliability of injection

**Where From Here**:
 - Other delivery methods outside of MouseJacking should be explored
 - Other side-channeling methods could be added to make it a more rounded attack vector on airgap systems
