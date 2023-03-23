### Development in SPC by Country
 - England
	 - The Manchester Machine
	 - Cambridge Machine: The EDSAC
	 - The NPL Pilot Ace
 - America
	 - The EDVAC
	 - The Institute for Advanced Study (IAS) Machine
	 - The Eckert/Mauchly Machines: UNIVAC and the BINAC
	 - SEAC/SWAC
	 - Project Whirlwind

### English Developments
 - The British were ahead of the Americans in the development of stored program computers
	 - The Americans lost their early lead to the British
 - While the Americans were still working out the design of their computers, British were working debugging programs on their own machines
	 - The British projects were of a smaller scale but were still counted as SPCs
	 - This put the early British researchers ahead of their American counterparts, issues that came up while developing software drove the design of the next generation hardware

### The Manchester Machine
 - After the end of the war, many researches ended up working at Manchester University
	 - Code breakers working on the Colossus (and the Colossi)
	 - Alan Turing (Enigma)
	 - Freddy Williams and Tom Kilburn (Williams' Tubes)
	 - In 1948: First fully electronic machine that operated based on the instructions stored in its memory
 - Official title of the lab: Royal Society Computer Laboratory
	 - Unofficial description of the lab: late lavatorial
 - Initial machine was extremely limited in its capabilities (operational in 1948)
	 - Access to stored information was serial
	 - Instruction set consisted of subtractions, conditional branches, stop instruction
	 - 32 words of (Williams' tube) memory (32 bits per word)
	 - Meant to be used as a testbed for Williams' electrostatic memory ideas
 - First operational on June 21, 1948
	 - The first machine to execute a stored program
	 - Was it the first true SPC?
		 - Very limited capabilites
		 - No real problems were ever solved using the machine (only tests)
		 - Not a fully working SPC
 - After getting the prototype working the machine was upgraded
	 - April 1949:
		 - Step 1: 2 CRT Williams' tubes (128 words x 40 bits/word)
		 - Step 2: Magnetic drum (1024 words)
		 - Built on multiple floors, data brought between floors of the building
 - Machines which were modified versions o the prototype were used for actual work
 - Ferranti Limited:
	 - Saw the prototype, asked for properly engineered version to be completed
	 - Ferranti machine, Ferranti Mark I, completed Feb 1951
	 - Copy sold to University of Toronto for $300k (design of St Lawrence Seaway)
	 - Improved specifications:
		 - Level 1 (CRT) memory: 256 words x 40 bits each
		 - Level 2 (drum) memory: 16384 words
	 - Speed of improved machine:
		 - Addition: 1.2 milliseconds
		 - Multiplication: 2.16 milliseconds
	 - Probably the first machine to implement a form of virtual memory, 1 million 48 bit words (core + drum)

### Cambridge Machine: The EDSAC
 - Maurice Wilkes
	 - Student at Cambridge before the war
	 - Assisted in the war effort (mathematical projects)
	 - Returned 1945 as the director of the UML (University Mathematical Library)
	 - Received and copied a copy of von Neumann's "First Draft on a Report on the EDVAC"
		 - First conceptual SPC, the one that got him credit on the machine
	 - Participated in a series of lectures at the Moore School (summer 1946)
 - Wilkes' Goal: Run real programs for actual work over spectualiting on what it would be like to build certain designs of machines
 - Used the technology of the day (vs developing a new untested technology)
	 - Used mercury-based acoustic delay lines
	 - 16 steel tubes containing mercury
	 - Each tube could store 17 bits (16 bit digit plus a sign bit)
 - Funding was provided by J. Lyons and Co. Ltd.
	 - Started as big baking business
	 - Needed bookkeeping/accounting
	 - Needed a computer to automate it, so successful they went into the computer business
 - The "Electronic Delay Storage Automatic Calculator" (EDSAC) was completed in 1949 at Cambridge
 - Named after the theoretical machine, the EDVAC, written about in Von Neumann's paper
 - In order to complete the machine in a useful period of time and cost, Wilkes was pragmatic
	 - Timing speed was reduced from1 Mhz to 500 kHz
 - First SPC?
	 - EDSAC completed a year later than Manchester Prototype (1949 vs 1948)
	 - Another machine, EDVAC, conceptualized before this but still largely theoretical (US)
	 - Unlike the Manchester machine, the EDSAC was used to solve real problems
	 - Speed:
		 - Addition: ~1.4ms
		 - Multiplication: 4.5ms
 - DJ Wheeler: Designed it to allow the address of subparts of the program to be stored in memory, rather than storing the binary instructions for that part repeatedly
	 - The Wheeler Jump was the predecessor of the modern function/subroutine call
 - J Lyons and Co Ltd produced a version of the EDSAC for their own use: LEO (Lyons Electric Office)
	 - Lead off to a series of machines (LEO I, LEO II), company was spun off from the parent: LEO Computers Ltd
	 - Construction on the LEO began in 1949, completed in 1951
	 - Used to solve many problems: Payroll (1.5 seconds vs 8 minutes by hand), determining the optimal mix in different brands of tea, etc.

### The NPL Pilot Ace
 - After end of WWII, Alan Turing joined the National Physical Laboratory in 1945 with the goal of constructing an electronic computing machine: The Automatic Computing Engine (ACE)
	 - Preliminary designs (V1-4) were completed by Turing
	 - 1946: James Hardy Wilkinson and Mike Woodger joins the project, assists Turing in the design process (V5-7)
 - Design effort occurred between 1945-1948
 - Actual production of the hardware was subcontracted out
	 - Little progress was made
	 - 1947: Harry Husky joined the project
	 - Because of the lack of progress (and the addition of Husky) Turing became quite frustrated with the work
 - Eventually both Turing and Husky left the project
 - Turing returned in 1948, then left for good to join Williams and Kilburn on the Manchester machine
 - Finally it was decided that V5 of the design should be the one to implement Ted (1949)
 - Eventually known as The Pilot ACE
 - The first program would turn on the output lights in succession ("suck digs" program as standard test)
 - Derivative machines:
	 - 1954: English Electric: DEUCE (Digital Electronic Universal Computing Engine)
	 - 32 more were manufactured in the 1950s and 1960s
	 - Inside of the DEUCE machines built to allow easy servicing
	 - Space was rumored to be put into some unexpected and unorthodox uses (change room, clothes dryer, dangerous liaisons)
 - The NPL-based machines were often faster than its contemporary computers, even ones with greater memory resources
	 - Timing clock operated at a speed that was faster
	 - Allowed for some complex programming optimizations

### American Developments
 - End of the second world war, Americans attained many advancements in electronics
	 - Completion of the first fully functional electronic computer: the ENIAC
 - Moore School lectures outlined the design of the stored program computer (1946)
 - Believed the Americans would develop the first SPC in a matter of months
 - Early lead lost to the British because of a number of factors:
	 - Loss of post-war funding for electronics research
	 - Feuding: Eckert and Mauchly vs John von Neumann (paper seen as an attempt to take credit)
 - Eckert and Mauchly were the main leads behind the development of the ENIAC, formed the concept of the SPC long before von Neumann visited the Moore School
 - US Official Secrets Act: Prohibited Moore School personnel from publishing anything about either the ENIAC or the EDVAC (von Neumann wasn't a member of the team, under no constraints)
 - Disputes over patent rights:
	 - Eckert/Mauchly believed main people behind the work should be the owners of any patents
	 - University of Pennsylvania believed the university should own the rights
	 - Moore School required all staff to sign over their patent rights, Eckert and Mauchly left in 1946
		 - Electronic Control Company, built BINAC and UNIVAC, eventially taken over by Remington Rand

### Lecture: Theory and Techniques for the Design of Electronic Digital Computers
 - Free lectures about the idea of an SPC in 1946
 - Many notable attendees: Eckert and Mauchly, Stibitz, von Neumann, Aiken, Maurice Wilkes
 - Lecture marked a major turning point in the development of computers
	 - Many projects directly advanced as a result (Wilkes working on the EDSAC)

### The EDVAC
 - Electronic Discrete Variable Arithmetic Computer
 - Funded by US Army Ordnance
 - Conceived of by the Moore School staff while they were still working on the ENIAC
	 - First SPC to be conceptualized
	 - Informal discussions, many staff members involved in discussions
	 - Formal description: "First Draft of a Report on the EDVAC" (von Neumann)
	 - Was to use mercury delay line memory, single bit accessed at a time (serial) to keep design simple
 - Eckert and Mauchly resigned in March 1946: ENIAC engineer Kite Sharpless took over the EDAC project
	 - Herman Lukoff assigned to solve problems with the mercury delay line technology (radar left on, scrambling the bits)
 - Spring 1947: Delay line memory for the machine was working well enough for a demonstration
 - Project progressed until summer 1947, Kite Sharpless and others left to form their own company (Technitrol Engineering)
 - Morale sank earlier with the problems with Eckert, Mauchly, von Neumann, fell again with the loss of the projects leader once more
	 - Finally, Richard Snyder appointed the chief engineer, saw the project to its conclusion in 1952
 - First conceived of SPC, not the first one completed
	 - Plagued with personnel and political problems
	 - Unlike many contemporary machines the EDVAC project required many components to be developed alongside the machine
	 - Extraordinary mechanisms used to ensure the accuracy of the results
 - **Specifications**:
	 - Mercury delay-line memory: 1024 word capacity, 44 bits/word
	 - Magnetic drum memory: 4000 words
	 - Clock pulses at the rate of 1 million per second
	 - Speeds:
		 - Addition: ~1 ms
		 - Multiplication/Division: 3 ms

### Institute for Advanced Study (IAS) Machine
 - John von Neumann and Herman Goldstine ended association with Moore Schoole to return to the IAS
 - Funding obtained from the same military groups that funded the ENIAC and EDVAC
	 - Von Neumanns "pull" within the military
	 - Wasn't clear which machine would be superior (IAS vs UNIVAC)
 - Other funds came from the Atomic Energy commission and RCA
 - March 1946: Eckert and Mauchly going through patent problems with the Moore School
 - Von Neumann invited Eckert to join him as project leader
	 - Wanted open research, Eckert wanted inventors patent rights
	 - Julian Bigelow finally offered the position
 - Memory:
	 - Designed to access memory in parallel (instead of contemporary serial based machines)
	 - Originally to use RCA Selectron memory
	 - Delays in production of working Selectron tube required a switch to Williams' Tube memory
 - June 1952: Machine officially unveiled publically, enhancements still made after this
 - Machine processed data in parallel, was very fast:
	 - Additions: 60 microseconds (EDVAC = 1000 microseconds)
	 - Multiplications: 300 microseconds (EDVAC = 3000 microseconds)
 - 1960: Original machine donated to the Smithsonian
 - Von Neumann believed in open research project, copies of plans sent to many other groups to make other copies
 - Many copies were made ("IAC"/"AC" series based on the "IAS" machine)
	 - JOHNNIAC (Rand Corporation)
	 - MANIAC (Los Alamos Laboratiory)
	 - AVIDAC, ORACLE, GEORGE (Argonne National Laboratory)
	 - ORDVAC, ILLIAC (University of Illinois: Former for the Aberdeen Proving Grounds, latter for own use)
	 - SILLIAC (Sidney Australia)

### UNIVAC/BINAC
 - **Background**:
	 - 1946: Eckert and Mauchly could see deteriorating situation at the Moore School, took appropriate measures to secure their own future (with some self promotion)
	 - When Eckert and Mauchly left the Moore School they founded the Electronic Control Company
		 - Groundwork laid to allow them to get a warm reception from the Census bureau
		 - Unfortunately, law prevented the Census bureau from contracting research work (only purchase a fully working machine)
	 - Set up a 3 way agreement between their company, Census bureau, National Bureau of Standards
		 - Army Ordnance ($300k) -> Census Bureau -> National Bureau of Standards ($75k) -> Eckert and Mauchly
		 - Only got $75k out of the $300k requested
	 - Originally called an EDVAC type machine, problems with Moore School, changed to UNIVAC (Universal Automatic Computer)
	 - Finances: Cost $400k, Census Bureau Funding $300k, National Bureau of Standards $75k
		 - Short by about $25k-$100k
	 - 1947: Eckert and Mauchly changed their business partnership to a formally incorporated entity: Eckert-Mauchly Computer Corporation to attract outside investment
		 - Incorporating: Separate financial entity to sell stocks
	 - Government funding only brought limited cash flow
	 - October 1947: Northrop Aircraft Company agreed to fund the development of a BINary Automatic Computer (BINAC)
		 - $80k upfront, $20k upon completion
		 - Target completion date: May 15, 1948 (would have been first working SPC)
		 - Actual completion date: 1949 (first SPC in North America)
 - **BINAC**:
	 - Memory:
		 - Main: Mercury Delay lines: 512 words (for each half) x 31 bit/word
		 - Secondary: Nickel-coated bronze (magnetic) tape
	 - Accounting:
		 - Amount paid by Northrop: $100k
		 - Actual cost to produce the machine: $278k
		 - Problem: $-178
	 - Completion of a working machine allowed prospective clients to put in orders for the (still theoretical) UNIVAC
		 - 3 government agencies
		 - AC Nielsen
		 - Prudential Insurance
	 - Contract price was insufficient to cover the research and development costs
 - **UNIVAC**:
	 - 1950: Imminent insolvency, the Eckert-Mauchly Computer Corporation was sold to Remington Rand
		 - Senior Remington Rand executive put in charge, Eckert and Mauchly kept on staff
		 - Remington Rand attempted to renegotiate the 5 contracts
		 - 2 private sector contracts were cancelled, 3 government contracts successfully renegotiated
		 - First UNIVAC delivered to the Census Bureau March 1951
		 - Second (after the Ferranti Mark I) electronic computer to be produced under contract for a commercial costumer
	 - At first Remington Rand didn't fully understand the significance of the technology it had bought
		 - Didn't think it was useful, their customers clamored for computers
	 - Total of 44 UNIVAC computers produced for government and industry
	 - Made Remington Rand the first large scale computer company, for several years "computer" was equivalent with "Remington Rand"
	 - CBS used a UNIVAC computer to predict the 1952 US presidential election, ran simulations
		 - First Run: Landslide victory for Eisenhower, didn't want to broadcast it so tweaked it, most accurate one
		 - Second Run: Still a solid win for Eisenhower
		 - Third Run (broadcast on network TV): Relatively close, Eisenhower slightly wins
	 - **Specifications**:
		 - Memory: 1000 words
		 - Timing Clock: 2.2 MHz
		 - Speed: Addition: 0.5ms, Multiplication: 2ms, Division: 4ms
		 - Similar to the BINAC, each operation completed independently by half of the computer and then the results were compared

### SEAC/SWAC
**SEAC**:
 - During the Great Depression, a US government - National Bureau of Standards (NBS) - stimulus program involved hiring the unemployed to create mathematical tables
 - National Applied Mathematics Laboratories was set up as a special division
	 - Nathional body to lead the development of new computational technology, perform large-scale calculations
 - One of the leaders on the project (chief mathematician) George Dantzig tired of the delays in the development of the UNIVAC and the IAS machine
 - Late 1948: Dantzig convinced the US Air Force to provide funding to the Applied Mathematics Laboratories to produce a small computer as a stop gap
	 - Initially known as the National Bureau of Standards Interim Computer
	 - Later became known as the SEAC (Standards Eastern Automatic Computer)
 - **Specifications**:
	 - Mercury delay line memory
	 - Input/Output: hexadecimal, via a single teletype, paper type punch and reader
	 - Simple instruction set: Addition, subtraction, multiplication, division, comparison, input, output
	 - Clock: 1 MHz
	 - Memory: 512 words x 45 bits/word
 - **Construction**:
	 - Consisted of a simple design that was constructed as quickly as possible to avoid major technical problems
	 - Low clock speed to avoid interference between electronic components
	 - Soldering was sometimes poorly done, required unique and ingenious maintenance techniques
		 - Needed to jump up and down to shake up the soldering
	 - SEAC was fully operational during the first demonstration (April 1950)
		 - Contrast: BINAC ran some test programs in August 1949 but was still incomplete
**SWAC**:
 - Standards Western Automatic Computer (SWAC)
 - Intitute for Numerical Analysis (INA) was a research group within the (National) Applied Mathematics Laboratories
 - 1948: Harry Husky came over from the National Physical Laboratory (Britain) and initiated the INA computer construction project Jan 1949
	 - To reduce the risk of investing in an unproven technology (Williams Tube) the NBS opted to make the SWAC a parallel machine using Williams Tubes (primary) and magnetic drum (secondary)
 - Similar to the SEAC, the SWAC was meant as a stop-gap computer
 - **Specifications**:
	 - Memory:
		 - Primary: 256 words x 37 bits/word
		 - Secondary: 8000 words
	 - Speed:
		 - Addition: 64 microseconds
		 - Multiplication: 384 microseconds
		 - As of its completion date (July 1950) it was the fastest machine in the world (until IAS machines a year later)

### Project Whirlwind
 - 1943: Louis de Florez (US Navy, Aeronautics)
 - Flight simulator with real time responses
 - 1944: Jay Forrester, graduate student with the Servomechanisms Laboratory (MIT) was asked to look into the project
	 - Initially, analog technology was investigated but it proved to be too slow for the simulator
 - Late 1945: Machine's design was switched entirely to digital electronic
 - Early 1950s: Focus of the Whirlwind computer switched from acting as a flight simulator to coordinate a defense against the possibility of an enemy bomber attack (Cape Cod)
	 - Tracking incoming bombers
	 - Scrambling fighter interceptors
 - First went online on April 20, 1951
 - First computer to utilize magnetic core memory
 - Successful, many of the Whirlwind staff were transferred to work on a continent wide system: SAGE (Semi Automatic Ground Environment) Air Defense System
	 - Work contracted out to IBM
	 - Machines known as AN/FSQ7 (first mass produced machine to utilize core memory)
	 - Referred to as Whirlwind II, of a different design
	 - The AN/FSQW7 machines provided the central air defense radar system (North America) until the 1980s

### Comparison of the First SPCS:
|Name|Completion|Addition (ms)|Multiplication (ms)|
|---|---|---|---|
|Manchester Machine|**June 1948**|1.2 ms|2.16 ms|
|EDSAC|**1949**|1.4 ms|4.5 ms|
|NPL|DEUCE 1954, Pilot ACE 1959|NA|NA|
|EDVAC|1952|1 ms|3 ms|
|IAS Machine|1952|**0.06 ms**|**0.3 ms**|
|UNIVAC|1951|0.5 ms|2 ms|
|SEAC|April 1950|NA|NA|
|SWAC|July 1950|0.064 ms|0.385 ms|
|Project Whirlwind|April 1951|NA|NA|
