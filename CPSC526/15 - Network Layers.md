![[Network-Layers.png|600]]
 - HTTP(s), packaged into TCP, packaged into IP, packaged into MAC, sent over the internet
### Internet Layering
 - Internet design is partitioned into layers
	 - Each layer relies on services provided by the layer below
	 - Each layer provides services to the layer above
 - Analogy: Software you write
	 - Code you write
	 - Run-time library
	 - System calls
	 - Device drivers
	 - Voltage levels
 - AKA Protocol Stack
 - Has the layers:
	 - Application
	 - Transport (eg. TCP)
	 - (Inter)Network (eg. IP)
	 - Link (eg. Ethernet)
	 - Physical (eg. Radio Waves)
 - Network packets reflect these layers
![[Network-Packet.png|600]]

**Physical Layer**:
 - Encodes bits to send over a single physical link
	 - Voltage Levels
	 - Photon Intensities (fibre)
	 - RF Modulations
 - Electrical engineering

**Link Layer**:
 - Framing and transmission of a collection of bits
 - Individual messages sent within a single subnetwork
	 - This may involve multiple physical links (Ethernet, Fiber, WiFi)
 - Often supports broadcast transmission, every node receives a frame
 - Typically uses MAC addresses (48-bit integers)

**Network Layer**:
 - Bridges multiple subnets
 - Provides global addressing
 - Provides end-to-end connectivity between nodes
 - Works across different link technologies
 - The link and physical layers can change for each "hop"
 - The data for the network layer and above stays the same
