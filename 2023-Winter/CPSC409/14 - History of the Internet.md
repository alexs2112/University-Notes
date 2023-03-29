### World War II
 - Germany split into West Germany and East Germany
 - West Germany: Administered by the allies of the West (USA and some Western European nations)
 - East Germany: Administered by the USSR
 - Eventually the former allies were lined up in opposing alliances:
	 - NATO: Canada, France, Italy, Spain, Turkey, USA, West Germany, etc
	 - Warsaw Pact: Albania, Bulgaria, Czechoslovakia, GDR (East Germany), Hungary, Poland, Romania, USSR

### Need for Research
 - Military recognized benefits of research
 - Seeds of the internet came out of WWII
	 - President Roosevelt (before US entry of WWII): believed technological edge (via airpower) was an alternative to fielding a large army
	 - 1944: President wanted to support research so it could continue at its wartime levels even after the war
	 - Vennevar Bush (chief scientific researcher for the government) recommended:
		 - General principle of the open sharing of knowledge rather than restriction
		 - Government support (but not control) of research)

### Early Forms of Networks
 - SAGE (Semi Automatic Ground Environment) radar system (1950s)
	 - Used for North American air defense
	 - Computers from different sites would communicate via modem
 - SABRE airline reservation system (1960s):
	 - Two IBM 7090 mainframes were connected
 - Unlike the internet, these networks consisted of a single network

### Origins of the Internet
 - 1950s: The Cold War between USSR and the USA
	 - Both sides wanted to be dominant in space, tried to be the first to send a satellite into space
 - Appeared that the USSR had a technological advantage over the USA
	 - Americans in 1957: A sophisticated three stage rocket was planned as the first human-made vehicle to be sent into space
	 - The USSR in 1957: Surprised the world by launching Sputnik I (first artificial satellite)
		 - Hacked together some military rockets instead of developing something new
 - Launch of Sputnik helped motivate the creation of ARPA (Advanced Research Projects Agency) in the US
 - Later in 1957 the USSR launched another satellite carrying the dog Laika ("Bark"/"Barker") on a way one trip into space
 - Events shook the image of the US as a technological super power (who had the technological lead in the Cold War)
	 - It was believed that if the soviets could launch artificial satellites into space they could launch nuclear armed missiles at North America
	 - Believed that the math and science requirements would have to be revamped in high school (so the Americans could out think their Soviet counterparts)
 - To close the perceived technological gap, president Dwight Eisenhower brought together the best technological minds and ARPA was created (arm of the department of defense)

### ARPA
 - Branch of the ministry of defense
 - Focus was on getting different types of computers communicating
 - Funded research at several universities across the US
 - Size and mandate of ARPA:
	 - Very small, no physical labs
	 - Issued research and development contracts to other organizations
 - 1962: ARPAs director, Jack Ruina (focus on ballistic missile defense, nuclear test detonation) recruited JCR Licklider to work on "command and control, and behavioural sciences"
 - Licklider's influence on ARPA:
	 - User friendliness: Focus on usability he saw the need for all ARPA research centers to agree on the development language and/or develop common conventions
	 - Beginnings of the Internet: (Network/Connectivity), collaboration between researchers was emphasized (previously this was not the norm)
 - Bob Taylor (successor to Licklider's successor)
	 - Focus on efficiency: When he took over ARPA, 3 separate and incompatible networks needed to to communicate with 3 different research centers that worked with ARPA
	 - Proposed that ARPA begin work on a significant networking project (a significant push to the eventual creation of the Internet)
	 - The proposed network was eventually known as the ARPANET
		 - Was the beginning of the internet, baby internet
 - The other leaders (at ARPA funded research centers) werent enthusiastic about the networking project (unknown entity, few could perceive its benefits)
 - Wesley Clarke (one of the founding fathers of the microcomputer) placated the researchers by stating that ARPA would pay for a small intermediary computer to be installed at each research center that would act as an intermediary between the computer used by the facility and the network (reduce load of the facility computer)
 - ARPAs method of motivating research groups to support work on developing a network continued
	 - Facility computer = Host
	 - Intermediary computer = IMP (Interface Message Processor)
	 - Prior to this suggestion, the idea was to have a central computer control the ARPANET (a significant difference than how the internet turned out)
 - Work at ARPA was influenced by the work of other researchers
	 - Paul Barans "nuclear war proof" network to be developed at RAND
	 - The ARPANET was to be a robust connection
		 - Along with other factors may have lead to the belief that the Internet was built to withstand an all out nuclear war
	 - Also influenced by Leonard Kleinrock: who wrote his PhD thesis on the principles of packet switched network
	 - Work at NPL (National Physics Laboratory: Term "packet" was adopted from their work)
 - **Major focus of the ARPANET**: Computer resource sharing and packet switched communications (although the term wasn't used at the time)
	 - Opposition to the belief that the motivation for developing the Internet was to have a nuclear proof network
 - **Packet Switched Network**:
	 - Message broken into parts (packets)
	 - Packets from a single message might take different paths to reach the same destination
	 - Each packet is given enough information so it can reach its destination and be reassembled with other packets back into the original data
	 - If packets were missing then the packets could be resent
	 - Slower than telephone networks, but more robust

### Origins of Packet Switching
 - Leonard Kleinrock (MIT) developed a theory behind a packet switched network. Published a paper on that theory in 1961, book in 1964
 - Independently: Paul Baran (RAND) developed similar principles for a voice network that would survive a nuclear strike
	 - Research often confused with work done for ARPA
 - Licklider (at MIT) introduced a concept he called the "Galactic Network (1962)"
 - Donald Davies & Roger Scantelbury (NPL: UK) presented a paper on a packet network concept
	 - Term "packet" adopted from the work at NPL

### Connecting the Nodes
 - First host location chosen was UCLA
	 - Kleinrock's early development of packet switching theory, his Network Measurement Center at UCLA was selected to be the first
 - Second host was located at Stanford
	 - Douglas Engelbart's lab SRI (Stanford Research Institute)
 - At the end of 1969: Hosts were connected and information was transmitted between them
	 - Birth of the Internet

### First Data Sent on the Internet
 - Originally the message "login" was to be transmitted
	 - But the transmission died after the first two characters
	 - Thus "LO", the internet was born!

### ARPANET Growth
 - Later additional hosts were added to the network (end of 1969):
	 - University of California (Santa Barbara)
	 - University of Utah
 - Doubled in size by the end of the year, two more hosts

### The UCLA Lab
 - Headed by Leonard Kleinrock
 - Graduate students included:
	 - Mike Wingfield (hardware engineer)
	 - Steve Crocker and Vinton Cerf (who were to establish and refine the network communication protocols)
	 - The Internet:
		 - Big network (network of networks)
		 - Built on the protocols (makes the connections possible)
 - Essentially this key research group consisted mostly of students and their (prof) supervisors, no official charter
	 - No seasoned veterans in the creation of the Internet protocols, kept waiting for professionals to take over
 - Six graduate students were left to develop the software that would govern how the computers would communicate
	 - Steve Crocker: Grade student (bachelors of the previous year) became the default leader
	 - Two other grad students were classmates of Crocker at Van Nuys High (graduate students of Kleinrock)
	 - Vint(on) Cerf: Another early participant of the group

### RFCs
 - The students would issue notes on the (eventual) Internet protocols under the name RFC (Request For Comments)
	 - Established by Crocker as an informal way to share ideas with other network researchers to get feedback
 - Conventions for issuing the notes were informal to minimize claims over the different parts of the work, encourage participation
 - In this vein, the first RFC was generated in rather humble circumstances by Crocker (night of April 7, 1969)
	 - Trying to develop these, didn't want to disturb roommate, went to the bathroom in the middle of the night to write up the description of the first RFC
 - The RFCs were in a perpetual beta state
	 - Constantly updating, no text considered authoritative, no final edit
	 - Democratic, authority was merit based rather than a fixed hierarchy
 - NCP (Network Control Protocols) was the first fruit of their labours, governed communication between machines
	 - December 1970: Network Working Group (NWG) under S. Crocker produced the first Host-Host Protocol
 - First packet sent using the NCP was in 1976
	 - Sent from Zott's beer garden
	 - Tested by sending from the field, device wired to a van with a radio transmitter
	 - Van transmitted to the PRENET which was connected to the ARPANET

### Vinton Cerf and Robert Kahn
 - Some regard Vint Cerf (and perhaps Robert Kahn) as the grandfather of the Internet
	 - Al Gore's influence
 - Eventually Cerf left ARPA to become a professor at Stanford
 - Robert Kahn was an MIT mathematics professor on leave to work on the ARPANET project (1972)
	 - By this time, ARPA renamed to DARPA (D=Defense)
 - NCP relied on the ARPANET's stability to provide reliability of the connection and transmission of information
 - Having the ARPANET responsible for the reliability of the network of networks was acceptable when the ARPANET was not connected to other networks
 - This was no longer acceptable when other networks were connected to the ARPANET
	 - ARPANET
	 - PRNET (Packet Radio Network)
	 - SATNET (Satellite Radio Network)
	 - NCP only worked on certain types of computers
 - 1973-1974: Kahn and Cerf published an outline of the new protocol to allow the 3 networks to communicate
	 - Known as TCP: Transmission Control Protocol
	 - Would allow different types of computers to communicate despite varying packet sizes and different hardware capabilities
 - With this new protocol, the host computers (and not the less powerful IMP computers) were now responsible for the connections
 - Similar to Baran's (nuclear weapon-proof) network, TCP focused on robustness over central control (source of confusion for the purpose of the internet)
 - Late IP (Internet Protocol) was developed, added to handle communications between networks
 - 1977: Testing the robustness of the protocol by streaming music from USA to the UK without losing any packets
 - January 1, 1983: Transition made from NCP to TCP/IP
