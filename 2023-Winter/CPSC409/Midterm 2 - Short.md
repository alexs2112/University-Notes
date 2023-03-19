# People:
### Babbage (1791-1871) (Differential Analyzer, Analytical Engine):
 - Grandfather of the computer age due to advanced ideas and speed of devices
 - Background: Wealthy banking family, member of two royal societies
 - Tried to summon satan to confirm beliefs, boarding school -> snuck out to check math textbooks
 - Translated, added substantially to calculus textbook by LaCroix, became English standard
	 - Co-contributors: George Peacock, John Herschel
 - Active social life with many social clubs, Lucasian Professor of Mathematics in Cambridge (but bitter at school)
 - 1862: Published most accurate set of logarithms to reduce misreading of information
 - British Rail System: Cow catcher, sail above railcars to recover lost ones on windy days
 - Ran for political office to ban street performers, meant to travel to US but ship sank and never planned to try again

### Konrad Zuse (1910-1995) (Zuse):
 - Berlin civil engineer, first person to construct automatically controlled calculating machine with limited funds
 - Worked on the Zuse Machines in his living room with friend **Helmut Schreyer**

### George Stibitz (1904-1995) (Bell Labs):
 - York, Pennsylvania. PhD in Mathematical Physics. Later years: non-verbal uses of computer, computer art
 - 1937: Worked for Bell Labs, similarity between telephone circuit diagrams and binary numbers, experimented in free time

### Howard Aiken (1900-1973) (Harvard):
 - PhD at Harvard, Military Background, suggested ideas for calculators but no takers
 - Got help from Harlow Shapley (astronomer) and Theodore Brown (Harvard business prof), funded by IBM after appointment with Thomas J Watson
 - Avoided using cutting edge/unproven technologies

### Grace Hopper (1906-1992) (Harvard):
 - Assistant to Commander Aiken
 - Dismantled 7 clocks as a child, found the first bug in a computer program, eventual PhD from Yale
 - 1943: Enlisted in naval reserves, top of military class, assigned to project at Harvard
 - At **Commodore/Rear Admiral Lower Half** (1980) she was the oldest serving member of the Navy

### John Atanasoff, Clifford Berry (ABC)
 - Atanasoff: Professor at Iowa State College
 - Berry: Graduate student under Atanasoff
 - Motivation: Drudgery of current calculators for physics equations
	 - Modified loaned IBM calculator, convinced that mechanical technology isn't fast enough
	 - Particularly frustrating night led to break from lab and breakthrough: Use binary instead of current decimal system

### John Mauchly (1907-1980) (ENIAC):
 - PhD, Professor of Physics at Ursinus College. Designed the ENIAC
 - Other staff left Moore School for war, Mauchly recruited, met Eckert (lab instructor)
 - 1940: American Association for the Advancement of Science: Mauchly met Atanasoff, impressed by his work, visited the ABC
 - 1942: Mauchly wrote his ideas in a paper to contrast electronic vs mechanical approaches, nobody realized the significance of the paper (electronic was way faster), eventually they needed the paper and needed to find it again
 - 1944: Mauchly and Eckert ironed out problems in basic ENIAC design, wrote about magnetic calculating machine (instructions stored and modified on magnetic disks)
 - 1946: Eckert + Mauchly left the Moore School to found their own company (Electronic Control Company)
 - "On Computable Numbers with an Application to the Entscheidungs-problem"
	 - Design of the EDVAC helped developers on both sides of the Atlantic

### J Presper Eckert (1919-1995) (ENIAC):
 - Radar tech, designed individual circuits for the ENIAC
 - Virtually a TA at the time, considerable hands on research from radar, tried and true brute force solutions

### Alan Turing (1912-1954) (Enigma, Bletchley Park):
 - Mathematician from Cambridge, produced famous paper "On Computable Numbers with an Application to the Entscheidungs-problem"
 - During the war, worked at Bletchley park as a cade-breaker, contributed to design, applied mathematical knowledge

### John Von Neumann (1903-1957) (SPCs, EDVAC)
 - Widely credited with coming up with the concept of the SPC at the Moore School
 - Life:
	 - Child: Jokes in classic Greek, memorize telephone directories on sight, divide two eight digit numbers accurately, mastered calculus, advanced calculus (tutor Gabor Szego to tears)
	 - Adult: Published papers in mathematics (19), youngest member of the Institute for Advanced Science (IAS, 30)
 - Regular visitor to the Moore School, too late to participate in ENIAC design, discussed machine with instructions on tape (EDVAC)
 - **First Draft of a Report on the EDVAC**
	 - Described concept of an SPC, listed as only author and got all the credit, meant as military report
	 - First document describing architecture of modern computer (von Neumann Machine)

# Machines:
### Difference Engine (Babbage)
 - Use property of differences to compute series of numbers
 - Pre-Babbage: Mr E Klipstein first reference to a device (1786), Captain JH Muller included in publication
 - Motivation: Only foolproof method of preventing errors in mathematical tables. 
 - Requested support from Royal Society, denied finances from Lords of Treasury, handshake deal to be reimbursed by government
 - Worked with Samuel Clement, eventual falling out due to housing situation, Clement got the tools, machines, designs
 - End: Machine wasn't complete, overly extensive description very difficult to follow (eventually implemented by **Dr Dionysus Lardner**)

### Analytical Engine (Babbage)
 - New concept: Computing machine controlled by external program
 - Never completed, many iterations continuously produced until his death
 - Recreated by Major General HP Babbage (1906) (his son)
 - Components: Store (RAM, registers by gears to store digits), Mill (calculations), Control Barrel (control unit), Counter Mechanism (loop control)
 - **Significance**: Didn't realize how useful it would be. Much faster and more advanced
 - **Ada Augusta Countess of Lovelace**: Friend of Babbage, translated his Italian description, conceived of using for purposes other than calculating numbers (First Programmer)
 - Another version designed, may have been constructed by **Percy Ludgate** (1908), entirely mechanical

### Zuse Machines (Zuse)
 - Originally V1, changed to Z to avoid confusion with weapons during the war
 - Z1: Used binary system instead of 10 state gears. Memory as solid strips of metal with a slot cut in it, plates would move around allowing data to pass through different plates
	 - Input (decimal) -> Arithmetic (binary) -> Output (decimal)
 - Z2: Designed to overcome routing/reliability problems by using relays instead of plates
	 - Not reliable enough to put to use, got funding for further work
 - Z3: Funded by German Aeronautical Research Institute. Destroyed by allies in 1943-1944. Relatively fast
	 - Improved on relay technology by protecting against sparks + wear/tear
 - Z4: Essentially the Z3 with a larger word size. Detained by allies (language barrier), after war completed with upgrades
	 - 1950: Only operational computer in Europe, one of the few in the entire world
 - **Significance**: First automatically controlled calculating machines that were actually functional. Comparable speed to later machines despite poor working conditions

### Bell Lab Relay Computers (Stibitz)
 - Stibitz Prototype (1938): Battery power, Dr TC Fry (head of Stibitz group) notified of problems company had with calculating load
 - Complex Number Calculator:
	 - SB Williams appointed to oversee project, Stibitz came up with idea, Williams to engineer the relay circuits
	 - Performed operations on complex numbers, operators sent calculations to computer remotely through phone lines
	 - Used Binary Coded Decimal as it was easier for hardware design (harder for operators, operators are cheap)
	 - Technical success, Bell Labs didn't think it would be commercial success, no other machines developed
 - The Relay Interpolator (Model II):
	 - WWII, Stibitz recruited to work on National Defense Research Council (NDRC)
	 - Artillery and anti aircraft calculations needed device to do it for them, eventually general purpose calculator
	 - Specifications: Two racks (5' high x 2' wide), could produce results for addition and subtraction
	 - Bi-quinary system of encoding information, each relay stores 1 bit, each decimal requires 7 relays
 - The Ballistic Computer (Model III):
	 - Same uses as Relay Interpolator, under design before Model II was even complete
	 - Larger and more powerful, included multiplication and division
	 - Took input of Airplane Position, Gun, Table of Ballistic Functions, Program Instructions
 - Second Ballistic Computer (Model IV):
	 - Officially known as "Bell Laboratories Relay Calculator Model IV" or "Error Detector Mark 22"
	 - Same as Model III but added calculations of negative angles (warships)
 - The Two In One (Model V):
	 - Two nearly identical machines, could work on same or different problems
	 - Error detection at runtime (essentially big try/catch block), extra reliability made it the slowest machine (besides Harvard I)
	 - Fate: One used at Fort Bliss -> Given to University of Arizona, other donated to Texas Tech College but got in car crash
 - Model VI:
	 - After the war, Stibitz left Bell, Bell constructed another machine
	 - Essentially a Model V, main difference was to store 10 (rather than 7) digit numbers

### Harvard Machines (Aiken, Hopper)
 - Harvard Mark I:
	 - Huge: 51' long x 8' high, very expensive. Program control through punched tape (immutable)
	 - **Motor powered mechanical calculator**, slower but more accurate than its peer machines (comparable to Z3)
		 - Used mechanical components (slower than relay based machines)
	 - Uses: Entirely for military purposes during the war. 
	 - Major impact: Design model, lasted until RAM was invented
 - Harvard Mark II:
	 - Naval Proving Grounds (Virginia), access to better resources and **based entirely on relay technology**
	 - Similar to Bell Model V, two separate parts for early parallel computing
 - Harvard Mark III:
	 - After the war, Aiken continued working on machines, focus on ease of use over high speeds
	 - Mathematical Button Board: Buttons labeled in math notation to automatically call subroutines
	 - First of Aiken computers to have a stored program, data and instructions on separate drums
		 - Harvard Architecture: Separation of data and memory
	 - Further move away from mechanical parts, split between electronic vacuum tubes and electro mechanical bits
 - Harvard Mark IV:
	 - Magnetic core memory, Aiken retired from design + construction of computers, became Harvard instructor and founded his own company

### IBM Calculators
 - Early punched card machines, slight speed and accuracy advantage over electric desk calculators
 - Leslie J Comrie: First use of Hollerith (European IBM) machines for large scale scientific calculation
 - 1929: Columbia University convinced Thomas J Watson to found Columbia University Statistical Bureau, then expanded to include work on astronomical calculations
 - Multiplying Punch Card IBM Models:
	 - IBM 601: Punch-based + relay based, quickly performed multiplications
	 - Similar relay based machines: 602, 602A, 603
	 - Vacuum tube based machines w/ programmable plug boards: 604, 605 (rewired when needed through plug boards)
 - IBM Pluggable Sequence Relay Calculator (IBM PSRC):
	 - Controlled by plug boards and punch cards, much faster than regular desktop punched card machines
 - The Selective Sequence Electronic Calculator (SSEC, Poppa):
	 - Vacuum tubes used where speed was essential, relays used everywhere else
	 - Employed Binary Coded Decimal (BCD) for efficiency, only 4 vacuum tubes for a single digit
	 - Use of vacuum tubes made the SSEC the **fastest of the mechanical monsters**
	 - Switched off after IBMs first electronic stored program computer (IBM 701)

### The ABC (Atanasoff, Berry)
 - First **prototype** electronic computer in 1942
 - First machine to incorporate regenerative memory, needed to be constantly refreshed to not lose its charge
	 - Rotating Drum Memory: Rotating drums with capacitors to do additions/subtractions, rotating to refresh charges
 - WWII: Atanasoff left the project, ABC never fully operational
 - Controversy: ENIAC was derivative of ABC but ABC was never finished, which was the first electronic computer?
	 - Atanasoff failed to get patent for it (filing issues), brought to court but didn't have anyone to collaborate with (Berry maybe-suicide)
 - Significance: First to demonstrate use of electronics in digital calculating machine (excluding Zuse)
	 - First to incorporate regenerative memory

### The ENIAC (Mauchly, Eckert, Chedaker, Goldstine)
 - Electronic Numerical Integrator and Computer, first fully operational electronic computer
 - Moore School of Electrical Engineering entered relationship with US Army to construct another Differential Analyzer
	 - Aberdeen Proving Ground, Maryland
 - Needed to fill in ballistic tables, otherwise extremely slow to fill in by hand
 - John Mauchly: Designed the ENIAC
 - J Presper Eckert: Designed individual circuits for the ENIAC
 - **Joseph Chedaker**: Supervised the construction team
 - **Lt Herman H Goldstine**: Acquired parts for the project through the army
 - Size: Huge, 100x bigger than the other machines of the time, most complex bit of electronics ever put together (100' long wall)
 - Component Units: Divided into separately programmable units, each unit contained its own memory and control
	 - Multiplication through **partial products** (very fast)
	 - Punch cards were the greatest source of breakdowns (input, output), normally a very reliable technology
	 - Bottlenecked by Accumulators as limiting speed factor, partial results sometimes needed to be printed and fed back in
 - Cooling: Vacuum tubes get very hot, computer air cooled, eeach panel had own thermometer.
	 - Servicing: Panels opened (air leak) and failsafe disabled)
 - Programming: Rewiring cables between sockets
	 - Bus wires determine which units are activated, data transmission, instructions to repeat, reset memory
	 - Numerical buses transmit numbers and their complements, 12 wires (10 for digit, 1 for sign, 1 for grounding)
 - After completion: Test mode, run actual ballistic programs, calculations for atomic energy group
	 - Dismantled and shipped to Ballistics Lab (Aberdeen, Maryland), after the war put to work on general problems)
 - Later Enhancements: Metal core memory to store intermediate results, not originally conceived as SPC
 - End: 10 years at Aberdeen, Maryland: Completed more calculations than entire human race prior to 1945

### British Projects (Turing, Flowers, Newman, Wynn-Williams):
 - Enigma: Commercial and military versions, possessing one wasn't sufficient for decryption, key letters to get lit up encryption, send encryption to receiver, they punch in encryption and get lit up decryption if they have the same settings
 - British Code and Cipher School: Deciphering German codes at Bletchley Park (London)
	 - Staffing levels required different sections, each section in a hut, only hut supervisors could talk
 - The Robinsons:
	 - General post Office (Telephone Division): Dollis Hill, West London
		 - **TH Flowers**, commissioned machinery for Bletchley Park, constructors assumed it was for telegraphs
	 - **MHA Newman**: Envisioned machine to automate part of decryption process
	 - **Dr CE Wynn-Williams**: Designed machine envisioned by Newman
	 - Heath Robinson (after unusual cartoonist), at least 3 in total (Heath Robinson, Peter Robinson, Robinson and Cleaver)
	 - Evaluated boolean operations on information from two endless loops (punched paper)
	 - Quickly constructed but unreliable, proved high speed electronic devices could be use in decoding process
 - The Colossus (The Savior Machine):
	 - Mr TH Flowers brought on directly to redesign Robinson machinery for reliability (using vacuum tubes vs relays)
	 - Good planning, the second Colossus was built in less than a year, believed up to 10 were fully functional by WWII end
	 - Similar to Robinsons: high speed bool calculations on data read from tape
	 - **Forerunner of the modern computer**: Basic math via bool logic, general purpose machines, conditional branching possible

### Early Stored Program Computers (SPCs) (von Neumann)
 - Conditions: Must have rewritable memory, long-term storage of information, inexpensive to build
 - Most Important: Must be possible to get at stored information very quickly
 - EDVAC:
	 - First conceived of SPC
	 - Lt Herman Goldstine (ENIAC) requested $100k to ENIAC budget to help develop the EDVAC
	 - Neumann now actively participating in the design

### Computer Memory Types/Technologies
 - Thermal Memories: **Andrew Donald Booth**, heat parts of bar to be read by heat detector, fans used to cool the bar
	 - Experiment was a failure, unreliable
 - Mechanical Memories: Zuse in Z1 with sliding plates, also used in other machines in the form of relays
	 - Much slower than the arithmetic unit of the electronic computer, Disk-Pin mechanical memory also not fast enough (Booth)
 - Delay Line Systems: First to gain widespread acceptance (EDVAC)
	 - Mercury Acoustic Delay Line: Quartz -> Mercury -> Quartz, electronic pulses, **William Shockley** + refined by Eckert
		 - Contact between quartz and mercury was hard (use alcohol, Turing), sound in mercury affected by heat (inconsistent)
	 - Air-Based Acoustic Delay Line: Booth, inexpensive, acoustic pulses through air is constant
		 - Lots of interference, distortion, echoing
	 - Slinky Delay Line: Booth, electrical pulses through metal slinky to add delay
		 - Electricity made the slinky oscillate wildly, dangerous for users
	 - Magnetostrictive Delay Line: Tightly coiled thin metal wire (nickel), less sensitive than mercury delay line, wave down coil
	 - Drawbacks of Delay Line Systems: The delay
 - Electrostatic Memory (Williams' Tube):
	 - First high speed memory: Electron gun -> Deflector -> Phosphor screen to energize it (binary state of dot = 0, dash = 1)
	 - Parallels: Avoid corrupting memory and parallel memory access: Each bit of word stored on separate CRTs
	 - 1946: Eckert proposes using CRT (Cathode Ray Tube) tech as a form of memory (**Frederic C Williams**, **Tom Kilburn** develop)
	 - First working model is completed (1000 bits, 1947) then upgraded to store many thousand bits for several hours (1948)
 - Selectron:
	 - Developed at RCA by team lead by Jan Rajchman, 2d grid of holes to allow electrons through, energized spots as data
	 - More reliable and faster than Williams' Tube, high cost and lack of availability, only used in Johnniac Computer
 - Rotating Magnetic Memories:
	 - Tape used for audio, slow access time so impractical for use
	 - Magnetic coating (nickel or ferrite)  on rotating drum, access time relatively slow
	 - Two level memory model: Slow speed + High capacity: Stored in magnetic drum, High speed + Low capacity: Williams' Tube
 - Booth's Magnetic Memory: Disk
	 - Floppy-disk based memory using free samples of Mail-a-Voice (ran out, developed new form of magnetic drum memory)
	 - Installed and working in experimental computer ARC (Automatic Relay Computer)
 - Static Magnetic Core Memories:
	 - First used in WWII: German warships used in fire control memory
	 - After war, brought to the US, disseminated to many, crossed wires over magnetic core to detect which were magnetized
	 - **Transistors**:
		 - 1959: Transistors became cheap and reliable, used for magnetic core memory, computer speed multiplied and maintenance time drastically fell. Smaller cores, non-volatile memory, fast random access of memory
