### Punch Card Based Machines
 - Different machines would use different forms of encoding
 - Programmer would use a machine to punch the information for a program into card or tape
 - Typically the program would then be given to a computer operator so the program would be run
	 - Results then returned to the programmer for analysis

### The Zuse Machines
 - Machines: Z1, Z2, Z3, Z4
 - Originally the V1 (Versuchsmodell-1/Experimental model-1)
	 - After war changed to Z, avoid confusion with weapons being developed by Wernher von Braun

### Konrad Zuse (1910-1995)
 - Born in Berlin, dreamed of designing rockets to reach the moon, or planning out great cities
 - Trained as a civil engineer, labour intensive calculations in the field using the slide rule
 - Zuse was the first person to construct an automatically controlled calculating machine
	 - Not electronic
	 - Didn't have a stored program in memory, instructions from external tape
 - Many earlier machines were personally financed, or funded by friends + family (limited money)
 - After school, began working in the aircraft industry

### Zuse: Early Designs
 - Envisioned a mechanical machine
	 - Table of instructions of punched media on a table
	 - A mechanical arm that acts as a read/write mechanism
	 - Next to the actual calculator
 - Based on this early design, came up with a design that included only three parts:
	 - Control: Program control with subroutines and loops
	 - Memory: Storing instructions
	 - Calculator: LIke ALU, performs the calculations

### Z1
**Origins**
 - Not familiar with the design of other mechanical computers
	 - Good thing, Zuse had to largely build his designs from scratch
	 - Current technology: 10 states, gears, decimal system
	 - Zuse's approach: 2 states, on or off, 0 or 1
**Memory**
 - Consisted of solid strips of metal with slots cut into them
 - A pin would rest on one side of the slot, touching 0 or 1
 - The metal plates would shift and move, mechanical memory, allow memory to pass through different plates
 - Worked well but the complex routing of the ALU made the transport of information between the parts of the machine problematic
**Development Lab (1936)**
 - Pre WWII, couldn't collaborate with others due to the impending war
 - Built lab in his living room
**Specifications**
 - Storage Capability: Memory 64 x 22 bit locations
 - Clock Speed: 1 MHz
**Overview of the Architecture**
 - Input (decimal) -> Arithmatic (binary) -> Output (decimal)
 - Control: Data and instructions on 35 mm film tape (low on resources, used random things)
	 - Helmut Schreyer, buddy and assistant

### Z2
 - Designed the overcome the signal routing and reliability problems of the mechanical memory by using relays
	 - Bendable material that is held open by a spring, end of it is metal to conduct electricity
	 - Push it down to make contact
 - Completed in 1939
**Relay Memory**
 - More reliable than the mechanical metal sheets
	 - Resources were easier to obtain than vacuum tubes (expensive)
 - Initial design was to entirely use relays but was unfeasible
	 - $2/relay at thousands of relays
	 - Rebuilt secondhand relay were used instead
 - Even the Z2 was not reliable enough to be put into actual use
 - One major contribution was to get funding to allow for further work (Z3)
**Alternate Memory**
 - Schreyer wanted to build the Z2 with vacuum tube memory
	 - Demo of a portion of the computer did use vacuum tubes
	 - During the war, tubes were scarce, would have needed 1000
	 - Military wouldn't provide the tubes because of the development time needed
**Specifications**
 - Very similar to the Z1
 - Clock Speed: 3 MHz
 - Memory: 64 memory locations (each 16 bits in size)

### Z3
 - Work funded by the German Aeronautical Research Institute
	 - Not provided with a workspace or technical staff
 - As was the case with Z1, completed his work with limited resources in 1941
	 - Still in his living room with Schreyer
 - Similar to the Z1 and Z2 (input, output, control)
 - Overcame the reliability problems of the relay technology, sparks, wear/tear
 - Relatively fast machine (considering the limited resources and isolation of Zuse)
	 - Additions: 0.25-0.3 seconds
	 - Multiply: Two numbers every 4-5 seconds
	 - Comparable to the Harvard Mk I developed 2 years later with much greater resources
 - Developed on a relatively modest budget:
	 - 1940s currency: 25000 RM (~$6500 US)
 - Wasn't practicle for large scale problems (limited memory): 64 words
 - 5-10 MHz
 - Original destroyed by the allies in 1943-1944
	 - Zuse made a copy in the 1960s, display in a museum

### Z4
 - Essentially the same as the Z3, larger word size
	 - Z3: 22 bits (1=sign, 14=mantissa, 7=exponent), 5-10 MHz
	 - Z4: 32 bits, 40 MHz
 - Construction at the end of WW2
	 - Detained by the allies, working on cutting edge technology, language barrier
 - After the war, the Z4 was completed with a few upgrades (conditional branch)
 - In 1950, only operational computer in Europe and one of the few in the entire world
 - Continued to provide useful service until 1960

### Significance of the Zuse Machines
 - First automatically controlled calculating machines that were actually functional
 - Comparable speeds to machines developed later
 - Also remarkable considering the working conditions (limited resources, funding, isolation)
