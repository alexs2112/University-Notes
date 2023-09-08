### The Need for Complex Numbers
 - Design of electrical devices and apparatus (telephone lines) involves extensive calculation and manipulation of complex numbers
	 - Awkward to work with complex numbers on a standard computer
	 - Telephone company (Bell) developed a specialized computer to work with these values
	 - Problems involving the calculation of complex numbers began to hamper growth

### George Stibitz (1904-1995)
 - York, Pennsylvania
 - Bachelors degree from Denison University, Masters degree from Union College (1927), PhD in Mathematical Physics in 1930 from Cornell University
 - Later years (1980s-1990s) turned to non-verbal uses of the computer
	 - Computer art: Commodore Amiga
	 - Art on display at Denison University
 - 1937: Mathematician working for Bell labs
 - Noticed a similarity between telephone circuit diagrams and binary numbers
 - In spare time with cast-off parts he would experiment with electronics

### The Bell Relay Based Computers
 - Stibitz prototype (1938)
	 - Battery powered
	 - Power -> Relays -> Output
 - Dr TC Fry (Head of Stibitz group) happened to be notified of the problems the company was having dealing with its calculating load

### The Complex Number Calculator
 - Work began in late 1938 after SB William was appointed to oversee the project
	 - Stibitz came up with the idea
	 - Williams had the necessary engineering training to design the relay circuits
 - Completed Jan 8, 1940, remained in daily use until 1949
 - Operations on complex numbers: Add, subtract, multiple, divide
 - Operation:
	 - Keyboard operator, type in the calculation into an actual terminal which is sent to the complex number calculator through phone lines
	 - Output then printed out
 - Significance:
	 - First machine to allow for more than one terminal connection, other terminals could connect to it but were given a busy signal (would have to wait for it to be freed up)
	 - Remote access to the machine at a vastly difference through the landlines
 - Details:
	 - Only required 450 telephone relays
	 - Logic was simplified by using a special form of binary (Binary coded decimal)
		 - Harder UI for the operators, easier for the design of the hardware logic
		 - Operators were cheap, hardware was expensive
 - Post Results:
	 - A technical success, Bell Labs didn't think it would be a commercial success ($20k to develop the first model)
	 - No other machines were developed
|Decimal Value|BCD Value|
|---|---|
|0|0011|
|1|0100|
|2|0101|
|3|0110|
|4|0111|
|5|1000|
|6|1001|
|7|1010|
|8|1011|
|9|1100|

### The Relay Interpolator (Model II)
 - After the Complex Number Calculator, Stibitz and Williams returned to their regular jobs
 - The US enters WWII in 1941: Dec 7, 1941, Japanese attack on Pearl Harbour
 - George Stibitz was recruited to work on the National Defense Research Council (NDRC)
 - Doing artillary and anti-aircraft calculations by hand was not feasible, needed a device to do it for them
	 - Referred to as "The Model II Relay Calculator"" or "Model II Relay Interpolator"
 - Completed and fully operational Sept 1943
	 - 493 relays in two racks (5' high x 2' wide)
	 - It could produce results for addition and subtraction (through negate and add)
 - Not only adequately performed the task for which it was created (AA-gun tracking) it became a general use computer for the rest of WWII
 - After, donated to the US Naval Research lab where it was productively used until the Relay Interpolator was shut down in 1961
 - Reliability:
	 - Telephone and Computer Relays would eventually fail through wear and tear
	 - Stibitz was concerned that a failed relay would give an incorrect result with no way to realize the error
	 - Consequently: Used a bi-quinary system of encoding information stored on the machine, each relay would store 1 bit of info

### Bi-Quinary Encoding
 - Each decimal would require 7 relays
 |Digit|Bi-quinary Encoding|
 |---|---|
 |0|01 00001|
 |1|01 00010|
 |2|01 00100|
 |3|01 01000|
 |4|01 10000|
 |5|10 00001|
 |6|10 00010|
 |7|10 00100|
 |8|10 01000|
 |9|10 10000|
  - Machines implementing this method of encoding information were extremely reliable
	  - If an erroneous result was found and removed the machine could take up the calculation from the point it had been interrupted without an effort
	  - The (later model V) was used continuously for 167 hours (during most of that time it was unattended)

### Model III ("The Ballistic Computer")
 - The third of Stibitz's relay computers were designed for the same uses as the Relay Interpolator (Model II)
 - Under design (1942) before the Model II was complete
 - Specifications:
	 - Over 1300 relays (5 frames each 5' high x 3' wide)
	 - Doubled memory: 5 to 10 registers
	 - Could perform addition and subtraction in the same was as its predecessors, also did multiplication and division
	 - Multiplication: ~1 second
	 - Took input of Airplane Position, Gun, Table of Ballistic Functions, Program Instructions
 - Based on the same relay technology and bi-quinary storage of numbers with some upgrades
 - Completed June 1944, remained in service until 1958

### Model IV
 - Second Ballistic Computer (officially known as "Bell Laboratories Relay Calculator Model IV" or "Error Detector Mark 22")
 - Completed in March 1945, used for ballistics calculations
 - Only difference from Model III is that it added features to allow for the calculation of negative angles (for warships)

### Model V ("The Two In One")
 - The Relay Interpolator and Ballistic Computers were so successful, US Government decided to back the creation of a much larger relay based system
	 - Also backlog of needed calculations to be completed
 - Two nearly identical machines built to fulfill the need
	 - Each half could work on a separate problem, both halves could work together
 - Reliability:
	 - Data encoded using the bi-quinary method
	 - Could handle the case when an error was detected while an instruction was executed
		 - Extra reliability slowed operations (essentially big try/catch block)
		 - Slowest machine (other than the Harvard Mark I)
 - Specifications:
	 - 44 registers
	 - 9000 relays
	 - 1000 square foot 'footprint'
	 - 10 tons
	 - Could handle 7 digit numbers
 - A CADET (Cant Add Doesnt Even Try) architecture for mathematical problems
 - Fate:
	 - After the war, one used at Fort Bliss and later given to University of Arizona
	 - Other donated to Texas Technology College in 1958, truck ended up in car accident, machine was destroyed
	 - Wrecked machine used for spare parts for the University of Arizona

### Model VI
 - After the end of WWII, Stibitz left Bell
 - Bell still constructed another version of the Stibitz machines in 1950
	 - Used for the same purpose as the original Complex Number Calculator
 - Essentially a Model V
	 - Main difference was that it could store 10 (rather than 7) digit numbers
	 - Late 1950s, donated to the Polytechnique Institute (Brooklyn), later in 1961 donated to the Bihar Institute of Technology (India) where it eventually became a historical display
