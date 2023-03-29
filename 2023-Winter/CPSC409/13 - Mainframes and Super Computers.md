### IBM
 - As previously discussed: Around the early 1900s IBM developed a reputation producing large calculators
	 - By 1950s, produced several different lines of scientific and business computers
	 - Were a leader with a US market share of 70% from 1950s onward
	 - Done by extensive spending on research and development, estimated to be around $500m with laboratories from coast to coast (US) and in Europe
		 - High entry barriers to the industry (expensive R&D)
		 - Almost no manufacturers save IBM made a profit selling large computers in the 1950s
**The NORC**
 - Naval Ordinance Research Calculator
 - Goal was to produce the fastest machine possible
	 - Few customers for such an expensive undertaking
	 - Fastest computers of the time: The NORC is generally regarded as the first super computer
 - The US Navy's Bureau of Ordnance was having trouble finding someone to produce a machine capable of this type of large scale computational problem
	 - To help generate good-will and a positive corporate image, IBM agreed to develop the machine even though it wouldn't make any money
 - Ready for delivery for the US navy at the end of 1954
 - **Specifications**:
	 - Memory:
		 - 264 Williams tubes
		 - 3600 words x 16 bit words (17th bit for error checking)
	 - Speed:
		 - Addition: 15 microseconds (4x faster than IAS)
		 - Multiplication: 31 microseconds (10x faster than IAS)
		 - Focus on reliability over brute speed for this machine
 - **Significance**:
	 - Changes in technology that came about as a result of the work on the NORC
	 - Significant improvements in the design of the magnetic tape drives (x5 speed)
	 - Improvements in the design of the memory (read around problem)
**IBM 701**
 - Designed at the same time as the NORC
 - Targeted towards defense agencies for the Korean War effort "Defense Calculator"
	 - Eventually known as the 701 computer
 - 1951: The decision was made to produce the 701
	 - Many design issues had been worked out earlier: Feasibility of Williams' Tube memory and the desire for improved input (replacement of standard punched cards with tape)
 - 1953: The 701 was complete
	 - Working out the design issues had given IBM an advantage over its competitors
	 - Original quote was $8000/month with 50 pre-orders
	 - After completing the 701 the quote had to be revised to $15000/month, sign ons dropped to 5
 - **Specifications**:
	 - Memory:
		 - Williams' Tubes
		 - 4096 words x 36 bit word size
		 - Unfortunately the memory tubes were visible through glass and doors, problems arose during formal unveiling (1953)
			 - Running a demo for the press
			 - One reporter came too close, the flash of the camera screwed up the Williams Tubes (light sensitive)
	 - Speeds (according to IBM):
		 - Addition: 60 microseconds
		 - Multiplication: 456 microseconds
 - **Successors**:
	 - 702 (along with 701, part of the first group)
	 - 704, 705 (second group)
	 - 709 (replacement for machines in the second group)
**The Stretch**:
 - After the completion of the NORC, IBM initiated a research project to determine the feasibility of developing a machine at least 100x faster than the current technology
	 - Actual: only 30x faster
 - Official Name: IBM 7030
 - Common name: Stretch (Stretch the state of the art in processing speed)
 - Technical improvements employed in the Stretch
	 - Use of high speed transistors in the process (x10 speed increase over the 704)
	 - Used improved high speed core memory employed in the SAGE
 - Technical improvements coming out of work on the Stretch:
	 - Improved magnetic storage devices (multiple read/write arms in a disk pack over magnetic drum)
	 - Pipelining
 - **Instruction Pipelining**:
	 - Memory is sometimes idle
	 - To increase speed as one instruction was decoded and executed, the next 5 would be accessed and partially decoded
	 - Memory locations that were numerically adjacent were stored in different banks
 - **Specifications**:
	 - Addition: 1 microsecond
	 - Multiplication: 1.8 microseconds
 - **Completion**:
	 - 1961: First one delivered
	 - Later: Seven others were delivered (mostly for atomic energy or defense-related research)
		 - One modified for use by the NSA (National Security Agency) for use in code breaking
	 - Resulted in many technological advances
	 - However not as fast as hoped or promised, not regarded as financially stable
	 - Not enough demand for such a high end (and expensive) machine to justify the development cost

### LARC
 - Livermore Atomic Research Computer (LARC)
 - IBM and UNIVAC were the only major players in the production of computers
 - When IBM was starting the Stretch, UNIVAC was working on the LARC for the Lawrence Radiation Laboratory (Livermore, California)
 - **Specifications**:
	 - Memory, divided into eight independent banks:
		 - Each bank could store 2500 words x 11 decimal digits/word = 20k words, upgradable to 97.5k words
	 - Two computers:
		 - 1. Input/output
		 - 2. Arithmetic
	 - Speed:
		 - Addition: 4 microseconds
		 - Multiplication: 8 microseconds
	 - Comparable Computational Times:
		 - Stretch < Atlas < LARC < UNIVAC 1103A < IBM 704
 - **Success?
	 - It is very fast
	 - Similar to the Stretch, a combination of high development costs and minimal demand
		 - Lawrence Radiation Labs (Livermore, California)
		 - US Navy Research and Development Center (Washington DC)

### Ferranti Atlas
 - University of Manchester: Fred Williams and Tom Kilburn produced the initial "Manchester Machine"
	 - Joined with Ferranti to produce several others: Mercury, Pegasus, Orion (Greek series)
 - 1956: Kilburn leads a team to investigate the construction of the Ferranti Atlas
	 - Atlas: Holds up the world, powerful machine for a powerful titan
	 - A powerful machine requires a great deal of memory
 - **Memory**:
	 - Used a design that gave the illusion of a single-level fast memory of large capacity (virtual memory)
		 - Implementation of virtual memory allowed for a total memory of 100k words * 48 bits/word
		 - 16k words in magnetic core memory
		 - 96k words in magnetic drum memory
		 - (Up to 1 million locations were addressable)
 - **Speed**:
	 - Comparable computation times: Stretch < Atlas < LARC
	 - Addition: 1.4-2 microseconds
	 - Multiplication: 4.7 microseconds
 - **Success?**:
	 - Not a commercial success either, only three were installed
		 - University of Manchester
		 - University of London
		 - Atlas Computer Laboratory (Chilton Oxford shire, England)
			 - "Alien"
	 - One of the planned abilities: Time sharing terminals were scrapped due to budget limitations
		 - Could have made the design financially feasible, made mass time-sharing available earlier

### IBM 360 Machines
 - Problems with existing computer market:
	 - Machines were not backward compatible (incompatible peripherals and software)
	 - Most computers were designed either for commercial data processing or scientific applications (massive calculating power needed)
		 - For many organizations, often a need to solve problems in both areas
 - 1961: IBM decided to produce a family of computers (360)
	 - Small and inexepensive to ones more powerful than the Stretch (addition in 200 microseconds to 1 microsecond)
	 - Each would run the same operating system (variants of 360, with some subvariants)
		 - Basic operating system 360, Tape operating system 360, Disk operating system 360, etc
	 - This ensured all the machines were capable of the same operations
	 - Character and numeric information were stored in a standard form: 8 bit bytes
		 - IBM: EBCDIC (Extended Binary Coded Decimal Interchange Code)
		 - Everyone else: ASCII
	 - Eventually a number of different machines had similar operations to the IBM System/360 line
 - This resulted in many other companies producing their own lines of machines that were compatible with the IBM 360

### IBM and Computers of the 1960s-1970s
 - IBM Dominated the mainframe (computer) market in and around the 1950s-1960s
	 - 70% market share with yearly sales in the billions
	 - Next closest competitor was Sperry Rand (UNIVAC) with sales ~100 million
	 - BY 1970s, other companies like General Electric and RCA left the market, leaving the BUNCH
		 - Burrows
		 - UNIVAC
		 - NCR
		 - Control Data
		 - Honeywell
	 - This group remained stable until the 1980s and the advent of the microcomputer

### High End Competition: Seymour Cray
 - Initially helped design super computers for CDC (Control Data Corporation)
 - Eventually left to form his own company: Cray Computers
 - On the high end of computing for customers like the NSA, sheer performance over compatibility was of importance
	 - IBM unable to effectively compete on this high end

### 360 Clones
 - IBM provided a great deal of technical specifications to its customers and to software developers
 - IBM became powerless from preventing others from building what it referred to as a "clone" of the 360
	 - Companies like RCA could sell clone versions of 360 for less than IBM (no development costs)
	 - Later UNIVAC (part of Sperry-Rand) bought out RCA's market, sold their own 360 clones
	 - Soviet Union: Building 360 compatible computers became a quick way for the USSR to construct powerful mainframes

### IBM 370
 - Finally the 160 architecture could no longer meet with the needs of the times
	 - Timesharing (360 wasn't incompatible with it, not built to take advantage of it)
		 - Did allow it, just not very well
	 - Timesharing: Multiple users on one computer
	 - Allow access to a computer to groups who couldnt afford to buy one
	 - Reduced inefficient computer use (rare that any one developer would really push the hardware)
 - Late 1960s: IBM System/370 came out as a replacement for the 360 design
	 - Better support for time sharing
	 - Among other things: Helped IBM's problems with 360 cloning
		 - RCA sold its market to Sperry-Rand after the withering effect from the release of the 370
