### Stored Program Computer
 - Must be possible to erase the contents of the memory and store new data in place of the old
 - Must be possible to store information for long periods of time
 - Must be inexpensive to construct, needed in large quantities
 - Must be possible to get at the information being stored in very short periods of time, no point in producing high-speed electronic arithmetic and control units if you cannot get at the instructions and data with the same high speeds
 - ABC: Not programmable
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
	 - Experimented with thermal memories. Heat part of the bar, to be detected by a heat detector. A fan used to cool the bar
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
 - **Parallels**:
	 - Avoiding corrupting memory
	 - For parallel machines (parallel memory access) each bit of word was stored on separate CRTs
 - **Timeline**
	 - Summer 1946: Eckert mentions idea of using CRT as a farm of memory ("iconoscope")
		 - ideas were only rudimentary, far from being put into practice
	 - End of 1946:
		 - Frederick C. Williams applies for a patent, starts work at Manchester University
		 - Later Tom Kilburn joins work as his assistant
		 - They developed the first truly high-speed random access memory
	 - 1947: Working model is completed, can store up to 1000 bits of information (125 bytes)
	 - 1948: Working model is completed that can store several thousand bits for several hours
 - **The Selectron**
	 - Developed at RCA by a team lead by Jan Rajchman
	 - Looks like a vacuum tube, full of a 2d grid of holes to allow electrons through
	 - Originally was to be the main memory for the Institute for Advanced Study (IAS) machine
	 - When that order was canceled, memory used in the "Johnniac" computer (named after John Von Neumann)
	 - More reliable and faster than the Williams' tube memory, high cost and lack of availablity, only used in one computer
	 - Both forms of electrostatic memory were eventually replaced by magnetic core memory: Cheaper, more compact

### Rotating Magnetic Memories
 - Magnetic recording (tapes) proved that audio information could be recorded magnetically
 - Slow access time of tape (on a long drum) made them impractical for use as main memory with electronic computers
 - Idea of adding a magnetic coating (nickel or ferrite) to a rotating drum occurred to many people at the same time
 - Even with a rotating drum, access time was slow as compared to computing speeds
 - Two level memory model:
	 - Slower speed, high capacity, stored in a magnetic drum
	 - High speed, low capacity, stored in Williams' tube

### Booth's Magnetic Memory: Disk
 - Andrew Donald Booth (again)
 - Developed a floppy disk based memory
	 - Mail a voice: used oxide coated paper (mailing magnetic coating on paper recording someones voice)
	 - Had a bunch of these samples, figured might as well give it a try
 - 1947: After going through all free samples from Mail-A-Voice, Booth and his father developed their own form of magnetic drum memory
 - The drum was installed and working in the experimental computer ARC (Automatic Relay Computer)
 - 1952: Booth was producing large drum memories for others to use

### Static Magnetic Core Memories
 - 1940s: Prototypes of this technology first developed
	 - WWII: German warships used core memory in their fire control systems
	 - After the war, technology was brought to the US and disseminated to many: IBM, Harvard, MIT, ...
	 - Crossed wires over the magnetic core, detection wire overtop to see where parts of the core was magnetized

### Static Core Memories and Transistors
 - Static Core Memory: Consists of an array of these guys, origin for "Segmentation fault: Core dumped"
![[static_core_memory.png|200]]
 - 1959: Transistors became cheap and reliable enough for use in computers
	 - Transistors can represent a binary state by acting as a switch
 - The development of magnetic core memory and transistors is what made computers cost effective
	 - Magnetic core memory allowed for the stored program computer to be eventually developed
 - **Significance of Core Memory**:
	 - Eg. Whirlwind Computer
	 - Computer speed multiplied
	 - Maintenance time for memory fell from 4 hours per day to 2 hours per wek
		 - Increased the mean time passing between failures from 2 hours to 2 weeks
		 - Increased reliability of memory allowed an entire group of skilled technicians to work on another project
 - **Advantages**:
	 - Cores can be small (reduces the size of computers)
	 - The memory is non-volatile:
		 - William's tube: Requires electricity to refresh the information
		 - Rotating drum (ABC): Requires constant mechanical power for the rotation
	 - Above all: Allow for random access of memory (CD vs Cassette: faster)
 - **Machines with Static Core Memory**:
	 - Harvard Mark IV:
		 - An Wang (student of Aiken) invented the memory used in that machine
	 - ENIAC 1952: Upgraded to a 2D array of cores
	 - Whirlwind: Upgraded to a 3D array of cores
		 - Pre-1953: Used Williams' tubes
		 - 1953: Installed core memory with the aforementioned changes
			 - Doubled operating speed
			 - Memory maintenance time: 4 hours per day -> 2 hours per week
		 - IBM SAGE computers (Whirlwind II)
			 - Generated $500 million in contract revenue for IBM in 1950s
