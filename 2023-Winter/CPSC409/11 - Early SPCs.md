### Stored Program Computer
 - Must be possible to erase the contents of the memory and store new data in place of the old
 - Must be possible to store information for logn periods of time
 - Must be inexpensive to construct, needed in large quantities
 - Must be possible to get at the information being stored in very short periods of time, no point in producing high-speed electronic arithmetic and control units if you cannot get at the instructions and data with the same high speeds
 - ABC? [todo, is this SPC?]
 - Punch cards and punched tape machines (Zuse)? No, instructions rewritable, were very very slow

### How Did Machines Receive Their Instructions
 - Before stored program computers:
	 - Tape or punched cards
	 - Hard wired connections
	 - Redesigning, creating whole new machine (Pascaline, Difference Engine, etc)

### Who Came Up With the Concept of the SPC
 - Why it's important: Fundamental part of modern computers
 - Answer: Shrouded in great deal of controversy
	 - Werent necessarily concerned about credit, just trying to advance science
 - Location: The Moore School (team that developed the ENIAC)
 - Person most widely credited: John Von Neumann
	 - Received so much notoriety that modern computers are sometimes referred to as Von Neumann Machines
 - In 1947, military lawyer made a ruling on the case
	 - Von Neumann wrote down ideas while people were discussing the SPC, put himself as the sole author
	 - The other workers didn't write anything down, they didnt get their name on it
	 - Von Neumann given the rights to the machine by the lawyer

### John Von Neumann (1903-1957)
 - Born into a wealthy family in Hungary
 - Privately educated until 11
 - Greatly impressed his teachers in regular school system
 - At age 6:
	 - Tell jokes in classic Greek
	 - Memorize telephone directories on sight
	 - Divide two eight digit numbers accurately
 - Age 8:
	 - Mastered calculus
 - Age 15:
	 - Studied advanced calculus, displayed such a depth of understanding he was reported to have brought his tutor, the world renowned Mathematician Gabor Szego, to tears
 - Age 19: 
	 - Publishing his own papers in Mathematics
 - Age 30:
	 - Youngest member of the newly opened Institute for Advanced Study (IAS at Princeton)
 - During WWII, he was a part of many scientific projects (atomic bomb research)
 - One important dude spent all night using a desktop calculator to do five math questions, Von Neumann did 4 of them in five minutes in his head. Didn't realize the other guy did them overnight in advance
 - Also had the ability to write well about complex topics
	 - His name eventually associated with the architecture of the modern computer (von Neumann architecture)
	 - Never claimed to have invented the ideas by himself

### Von Neumann and the Moore School
 - Early designs of the ENIAC
	 - Machines of the day (Zuze, Aiken Harvard, Sibitz Bell) used paper tape (read only storage)
	 - Such designes rejected for the early ENIAC
		 - Too slow
		 - Programming (wiring) only infrequently changed
		 - Extra design complications
 - January 1944 (Moore School)
	 - Mauchly and Eckert ironed out problems in the basic design, gave them time for reflection
	 - Eckert: Wrote three page document about a magnetic calculating machine
		 - Instructions could be stored (and modified) on magnetic disks
		 - Frequently used instructions could be permanently etched onto disk
 - September 1944:
	 - Von Neumann became a regular visitor at the Moore schoole (too late to participate in the ENIAC design)
	 - Participated in discussions in the design of a new machine (eventually called the EDVAC)
		 - Instructions stored on tape
		 - Speed of the storage devices comparable to the electronics of the EDVAC
 - October 1944:
	 - Army Ordinance department gives $100k to the ENIAC budget to research developing the EDVAC
		 - Lt Herman Goldstine (made an earlier request)
		 - John Von Neumann (funding likely at his request)
	 - From this point onwards, von Neumann actively participated in the design of the EDVAC
		 - Made many contributions
		 - The idea of a SPC existed before his involvement
 - June 1945: "The First Draft of a Report on the EDVAC"
	 - Described in great detail the concept of a stored program digital computer
	 - Von Neumann was listed as the sole author
		 - Just wanted to write down the progress so the progress wasn't lost
		 - Others at the Moore school were annoyed
	 - Draft report meant as a progress report to be given to military sponsors
		 - But was circulated within the Moore School, even to some outsiders
	 - First document describing in detail the architecture of a modern computer, the term Von Neumann Machine was coined
 - 1946: Eckert and Mauchly left the Moore school to found their own company (Electronic Control Company)
 - Summer 1946:
	 - "Theory and Techniques for the Design of Electronic Digital Computers"
	 - Disseminated information about the design of the EDVAC to developers on both sides of the Atlantic
		 - First conceived of SPC

# Computer Memory Types/Technologies
### Thermal Memories
 - Andrew Donald Booth (1918-2009, United Kingdom)
	 - Experimented with thermal memories. Heat part of the bar, to be detected by a heat detector. A fan used to cool the ba
	 - Experiment was a failure (unreliable)

### Mechanical Memories
 - Used on a large scale by Zuse in the Z1 (sliding plates)
 - Another example: Relays
	 - Used in several other machines (Z2+, Bell machines)
 - Much slower than the internal workings (arithmetic unit) of the electronic computer
 - Andrew Donald Booth (again): Disk-pin mechanical memory
	 - Wasn't fast enough for electronic machines, access time of about 0.25 seconds

### Delay Line Systems
 - First type of memory to gain widespread acceptance
	 - Used in many machines: EDVAC, EDSAC, UNIVAC I, Pilot ACE, SEAC, LEO I, etc
 - Types:
	 - Mercury Acoustic
	 - Air Based Delay Lines
	 - Slinky Delay Lines
	 - Magnetostrictive Delay Lines
 - **Mercury Acoustic Delay Line**:
	 - A binary number is represented using a series of pulses (like a binary morse code)
	 - After a brief delay, the pulses would be resent
	 - Repeatedly pulsing the signal would allow for long term storage of the information
	 - Developed by William Shockley (during WWII)
		 - Bell Labs, one of the developers of the electronic transistor
	 - Refined by Presper Eckert (mid 1940s)
		 - Radar related research at the start of WWII
	 - Relying on acoustics, sound from quartz, through mercury, to be picked up by quartz, then amplified to be read
	 - Technical issues:
		 - Getting good contact between the mercury and the quartz
		 - The speed of sound in mercury is greatly affected by changing temperature (inconsistent)
 - **Air-Based Acoustic Delay Line**:
	 - Booth (yet again): Inexpensive and theoretically possible
	 - Sending the acoustics through the air, constant speed of sound through air
	 - Lots of interference, distortion and echoing
 - **The Slinky Delay Line**:
	 - Used slinky, Booth (yet again)
	 - Electrical pulse through a metal slinky
	 - Didn't know electrical properties in metal well enough, the electricity made the electrically charged slinky oscillate wildly, a danger for users
 - **Magnetostrictive Delay Line**:
	 - Thin metal wire like nickel, less temperature sensitive than the mercury delay line
	 - A pulse on one end would send a compression wave down the wire
 - Drawbacks of delay line technology: The delay
	 - Information stored in the delay mechanism was only available after a delay (0.5-1 ms)

### Electrostatic Memory (Williams' Tube)
 - 1946: Frederic C. Willians and Tom Kilburn developed first truly high speed RAM while at Manchester University (England)
 - Idea of using CRT (Cathode Ray Tube) technology as a form of memory was mentioned by Eckert in a Moor School lecture (summer 1946)
	 - Ideas were still primitive at this stage
 - First high speed memory (form of vacuum storage)
	 - Bit access time in microseconds (1 millionth of a second)
 - Electron gun would send an electron beam, diverted by deflector to where it needed to be. Beam sent into phosphor and would energize it
 - Binary states of Dot (zero) and Dash (one)
 - Would decay 5x a second, would need to keep refreshing
	 - Biggest problem, read around problem
 - A tube would have many displayed bits in the screen, the computer would then read the screen of dots and dashes
