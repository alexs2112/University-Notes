### Introduction
 - Developed under the guidance of Howard Aiken (1900-1973)
	 - Studied at University of Wisconsin, eventually earned his PhD at Harvard
	 - Military background
	 - Envisioned a device that could complete many tedious calculations
	 - Current technology wasn't up to the task by an order of magnitude
	 - Familiar with Babbage's biography
	 - Suggested several ideas to others (for funding) but found no takers
	 - With some help: Harlow Shapley (astronomer) and Theodore Brown (Harvard business school prof)
 - Managed to get an appointment with Thomas J.Watson (1937)
 - Watson agreed to have IBM fund the project, Watson's goals differed from Aiken's
 - Machine (originally "IBM Automatic Sequence Controlled Calculator" eventually "Harvard Mark I") was demonstrated to be operational in 1944, donated to Harvard
	 - Aitkin's military background, immediately employed in the war effort
		 - Navy commander in the reserves, in charge of the navy computational project
		 - Grace Hopper assigned as Aitken's aide
	 - Major rift developed between Aiken and Watson
 - Aiken was aware of the problems faced by his predecessors (Babbage)
	 - Avoided constructing machines that were too cutting edge, employing untested/unproven technologies
	 - Mechanical components used were slower than the relay-based machines
	 - Pragmatic, would work with anyone's technology if it worked
	 - When designing Mark I Aiken originally approached (rejected), The Monroe Co - producer of traditional mechanical desktop calculators
		 - Had this agreement been successful, the Mark I may have been purely mechanical instead of electricity

### Harvard Mark I
 - Built from parts from standard IBM accounting machines
 - It was huge, 51' long x 8' high, requiring 500 miles of wiring
 - Very expensive: $400k - $500k
 - Program control came from instructions on punched tape (not rewritable)
 - **Specifications**:
	 - Motor powered
	 - Contained 72 'registers', each could store 23 decimal digits (plus one for the sign)
		 - Could change the position of the decimal by rewiring it (15-16th place by default)
	 - Mechanical calculator
	 - Speed:
		 - Additions: 0.3 seconds
		 - Multiplication: <= 6 seconds
		 - Slower but more accurate than many of its peer machine
		 - Comparable speeds to the Z3
 - **Uses**:
	 - Immediately enlisted in the war effort when it was completed in 1944
		 - World War II (1939-1945), Aiken held commander rank
		 - Used entirely for military purposes for the duration of the war
	 - Afterwards, Mark I was employed for research purposes
	 - Eventually made obsolete by newer machines, dismantled in 1959
	 - Major impact: Design model rather than the applications it was used for ot the results it produced
		 - Design model lasted until RAM was invented

### Grace Hopper (1906-1992)
 - Young lieutenant, assistant to Commander Aiken
 - Curious and inquisitive child, taking things apart (dismantled 7 clocks)
 - Found the first bug in a computer program
 - Degree in Mathematics and Physics from Vassar (New York), eventually a PhD from Yale
	 - 1943 enlisted in naval reserves
	 - Graduated at the top of her military class in 1994
	 - Assigned to the project at Harvard as a junior grade naval lieutenant
 - Made many contributions to the development of the first compilers and the standardization of the COBOL programming language
 - Continued to be promoted through the ranks of the Navy
	 - At Commodore/Rear Admiral Lower Half (1980) she was the oldest serving member

### Harvard Mark II
 - 1945, Navy asked Aiken to construct another machine for use at the Naval Proving Grounds (Virginia)
 - Aiken had flexible and pragmatic approach, as it was requested by the Navy he had access to different and better resources
 - Based entirely on relay technology (considerably faster)
	 - Mechanical locks (rather than magnets), no electricity to lock
	 - 0.01 second motion
	 - $15 each (x13000)
 - Similar to Bell Model V, split into two separate and independent parts
	 - Early parallel computing, or both could work on one problem
 - Specifications:
	 - 50 data registers
	 - 2 tape readers for instructions
	 - 4 tape readers for data
 - Speed
	 - Addition: 125 milliseconds
	 - Multiplication: 750 milliseconds

### Harvard Mark III
 - After the war, Aiken continued working on developing machines at Harvard
 - Focus was on ease of use over having an ultra high speed machine
	 - Mark I & II: Machine speed increased by factor of 10, throughput only increased by 2-3
 - Consequenty, Mark III (and IV) were designed more for accuracy and ease of use than hardware-based increases in speed
 - **Mathematical Button Board**:
	 - Special board designed to increase the ease of use for mathematicians
	 - Buttons labeled in special mathematical notation, would produce resulsts by automatically calling the appropriate sub-routine
 - **Technical Specifications**:
	 - First of the Aiken computers to have a stored program
		 - Stored data on 8 magnetic drums (4350 - 16 bit numbers)
		 - Instructions were stored on a separate drum
		 - Separation of data and memory was known as the Harvard architecture
	 - Further move away from mechanical parts
		 - Technology split between electronic (vacuum tubes) and electro-mechanical components
	 - Operational speed:
		 - Multiplication: 12.75 milliseconds

### Harvard Mark IV
 - Completed in 1952
 - Incorporated many of the features of the Mark III, employed a different type of memory (magnetic core)
 - Resided at Harvard, used extensively by the US Air Force
 - After finishing the Mark IV, Aiken retired from designing and contructing new computer equipment
	 - Harvard instructor
	 - 1961: Founded his own company (Aiken Industries)

# IBM Calculators
### Punched Card Systems
 - Before producing computers, IBM in business of calculating machines under different names
	 - IBM (North America), Hollerith Equipment (Europe)
	 - Formed by 4 separate companies
 - Early punched card machines were used to enter/encode data so it could be stored and tabulated
 - Advantages over electircally driven desk calculators:
	 - Speed (slight)
	 - Accuracy (reduced human intervention)
 - **Applications**:
	 - Early applications:
		 - Compiling statistics
		 - Accounting/bookkeeping
		 - Leslie J. Comrie: First use of the Hollerith machines for large scale scientific calculation (lunar motion)
	 - 1929: Columbia University convinced Thomas J. Watson (senior) into founding COlumbia University Statistical Bureau
	 - 1930: Statistical Bureau expanded to include wokr on Astronomical calculations
	 - Early machines based on the same principles as Babbage's Difference Engine

### Multiplying Punch Card IBM Models
 - The IBM 601 (1935) was a punch based system that could also quickly perform multiplications
	 - Relay based, could complete multiplications ~1 second
 - 601 rapidly evolved into several models:
	 - Each successive model came with increasing abilities or improved technologies
	 - Relay based machines: 602, 602A, 603
	 - Vacuum tube based machines with programmable plug boards: 604, 605

### Plug Board Programming
 - 604 could be programmed through two plug board control panels
	 - Essentially rewiring the device when needed

### IBM's Market Position
 - Very little competition int he production of punch card equipment
	 - Remington Rand was one competitor, much less convenient so vast majority of the market went with IBM

### Large IBM Calculators
 - First was the Harvard Mark I
 - With this machine's success, IBM developed their own series of computers (all relay based)
 - IBM Pluggable Sequence Relay Calculator (IBM PSRC)
	 - All were relay-based computers controlled by a combination of IBM plug boards and punch cards
	 - Arithmetic unit: The 4 standard mathematical operations plus square roots
	 - Faster than regular desktop punched card machines (x10 the speed of the IBM 602)
		 - ~100 ms

### The Selective Sequence Electronic Calculator (SSEC)
 - One of the really large mechanical monsters produced by IBM
 - Unveiled in 1948, completed and running test programs before that
 - Known as "Poppa", not the terrible name it was given
 - As the SSEC was being designed, another machine (ENIAC) had shown that vacuum tubes could reliably be used in a computer
 - IBM engineers had extensive eperience with relay-based technology (punched card machines, up to and including IBM 603)
 - Final design:
	 - Vacuum tubes were used in parts of the machine where speed was essential
	 - Relays were used in all other parts of the machine
	 - 8 high speed registers and the arithmetic unit ~13000 vacuum tubes
	 - 150 slower speed registers ~23000 relays
	 - Employed BCD for efficiency (only 4 vacuum tubes) were required to store a single digit
 - The use of vacuum tubes in the arithmetic unit made the SSEC the fastest of the mechanical monsters (addition: 4 ms)
 - When IBM developed the first electronic stored program computer (IBM 701) the SSEC was switched off
	 - IBM 701s capabilities exceeded that of the SSEC
