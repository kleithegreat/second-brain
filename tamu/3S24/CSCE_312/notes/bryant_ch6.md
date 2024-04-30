# The Memory Hierarchy
- To this point, we have studied a simple model of a computer that uses a single memory system as a linear array of bytes
- This is effective to a point, but it is not how modern computers are designed
- A **memory system** is a *hierearchy* of storage devices with different capacities, costs, and access times
    - Registers hold the most frequently accessed data
    - Small **cache memories** near the CPU hold some of the more frequently accessed data from the main memory
    - Main memory holds the data and instructions that are currently being used
    - Persistent storage (e.g. disk drives) holds data that is not currently being used, and is used for long-term storage
- Programs must be designed around the concept of **locality** to take advantage of the memory hierarchy
> Understanding how the system moves data between the different levels of the memory hierarchy allows you to use the system more effectively
## 6.1 Storage Technologies
Computers have made lots of progress in terms of storage technology.
### 6.1.1 Random Access Memory
- **Random Access Memory (RAM)** comes in two varieties:
    1. **Static RAM (SRAM)**: Faster and significantly more expensive than DRAM
    2. **Dynamic RAM (DRAM)**: Slower and cheaper than SRAM
- SRAM is used for cache memories and main memory, both on and off the CPU
- DRAM is used for main memory and the frame buffer of a graphics system
- Typically, we have much more DRAM than SRAM

| | Transistors per bit | Relative access time | Persistent? | Sensitive? | Relative cost | Applications |
|---|---|---|---|---|---|---|
| SRAM | 6 | 1x | Yes | No | 1000x | Cache memory |
| DRAM | 1 | 10x | No | Yes | 1x | Main memory, frame buffers |

#### Static RAM
- SRAM stores each bit in a *bistable* memory cell
- Each cell is a six-transistor circuit
    - This circuit can stay in one of two states indefinitely
    - This kind of memory is analogous to a seesaw
        - The seesaw can stay in one of two states indefinitely
        - It can remain balanced, but the smallest disturbance will cause it to tip (this is called a *metastable state*)
    - SRAM will retain its value as long as power is applied
#### Dynamic RAM
- DRAM stores each bit in a capacitor
- These capacitors are typically around 30 femtofarads ($30 \times 10^{-15}$ farads)
- DRAM storage can be made very dense--each cell is a capacitor and an access transistor
- Unlike SRAM, DRAM is very sensitive to disturbances
    - When the voltage is disturbed, it will never recover
    - Exposure to light will cause voltage disturbances
    > Camera sensors are essentially DRAM cells
- DRAM cells must be refreshed periodically to maintain their value
#### Conventional DRAMs
- The cells(bits) in a DRAM chip are partitioned into **d supercells**
    - Each d supercell consists of $w$ DRAM cells 
    - A $d \times w$ DRAM stores a total of $d \times w$ bits
- Supercells are organized as a rectangular array with $r$ rows and $c$ columns
    - We have that $rc = d$
    - Each supercell has an address of the form $(i, j)$ where $i$ is the row and $j$ is the column
> Storage has never steeled on a standard name for a DRAM array element; Computer architects tend to call it a "cell", or a DRAM storage cell. Circuit designers tend to call it a "word", or a word of main memory. Here we use "supercell" to avoid confusion.
- Each DRAM chip is connected to the **memory controller* that can transfer $w$ bits at a time to and from each DRAM chip.
- Reading the contents of a supercell requires the memory controller to send the row and column addresses to the DRAM chip
- The DRAM chip responds with the contents of the supercell
- The row address $i$ is called a **RAS (row access strobe)** request
- The column address $j$ is called a **CAS (column access strobe)** request
> The RAS and CAS requests share the same DRAM address pins, so they must be sent sequentially
- For example, to read the contents of supercell $(i, j)$:
    1. The memory controller sends the RAS request for row $i$
    2. The entire contents of row $i$ are copied into the internal row buffer
    3. The memory controller sends the CAS request for column $j$
    4. The internal row buffer is read and the contents of column $j$ are sent to the memory controller
- Designing DRAMs as a 2D array rather than a linear array allows for more efficient access
- The disadvantage of a 2D array is that the memory controller must send two requests to read the contents of a supercell, which takes more time
#### Memory Modules
- DRAM chips are packaged into **memory modules** that plug into the motherboard
- The most common memory module is the **dual inline memory module (DIMM)**
- For example, say we have a 64-bit memory system with 8 DRAM chips on a DIMM
    - Each supercell stores 1 byte of *main memory*; each 64-bit word at byte $A$ in main memory is stored in the supercells with addresses $(i, j)$
        - e.g. DRAM 0 stores the first (lowest) byte, DRAM 1 stores the second byte, etc.
    - To retrieve the 64-bit word at byte $A$, the memory controller converts $A$ to a supercell address $(i, j)$
    - Each DRAM outputs the 8-bit contents of its supercell at address $(i, j)$
    - The memory controller assembles the 64-bit word from the 8 bytes
- Main memory can be aggregated by connecting multiple memory modules to the memory controller
    - In this case the memory controller would receive the address $A$ and select the appropriate memory module that contains $A$
#### Enhanced DRAMs
- There have been some enhancements made to DRAM memories, but they all remain based on the basic DRAM cell
    - **Fast page mode DRAM (FPM DRAM)**: Allows the memory controller to read from the same row multiple times without discarding the row buffer
    - **Extended data out DRAM (EDO DRAM)**: An enhanced FPM DRAM that allows for CAS signals to be closer together in time
    - **Synchronous DRAM (SDRAM)**: Conventional, FPM, and EDO DRAMs are asynchronous, since they have no clock and are controlled by explicit control signals. The net effect of using a clock signal here is faster access times
    - **Double data rate SDRAM (DDR SDRAM)**: An enhancement of SDRAM that allows for data to be transferred on both the rising and falling edges of the clock signal, effectively doubling the data rate
        - DDR2, DDR3, and DDR4 are further enhancements of DDR SDRAM
        - DDR has a 2-bit prefetch buffer, DDR2 4-bit, DDR3 8-bit, and DDR4 16-bit
    - **Video RAM (VRAM)**: Used in the frame buffers of graphics systems. Similar in spirit to FPM DRAM
        - VRAM output is produced by shifting the entire contents of the internal row buffer in sequence
        - VRAM allows for concurrent read and write operations, which enables the display to be refreshed while the CPU is writing to the frame buffer
#### Nonvolatile Memory
- DRAMs and SRAMs are *volatile* in the sense that they lose their information when power is removed
- **Nonvolatile memory** retains its contents when power is removed
- For historical reasons, nonvolatile memory is called *read-only memory (ROM)*, even though it is not read-only
- ROMs are distinguished by the number of times they can be reprogrammed and the mechanism for reprogramming them
- **Programmable ROM (PROM)**: Can be programmed where each memory cell is a fuse that can be blown once with a high current
- **Erasable Programmable ROM (EPROM)**: Can be erased by exposing it to ultraviolet light
    - Written to with a special device
    - Can be reprogrammed about $1000$ times
    - *Electrically Erasable Programmable ROM (EEPROM)* can be erased and reprogrammed electrically, with printed circuit boards
    - EEPROMs can be reprogrammed around $10^5$ times
- **Flash memory** is a type of EEPROM that has become popular for nonvolatile storage
- Programs are stored in ROMs are often called *firmware*
#### Accessing Main Memory
- Data goes between the processor and DRAM main memory using shared electrical conduits called **buses**
- Each transfer of data between the CPU and memory is accomplished with a **bus transaction**
    - A **read transaction** transfers data from memory to the CPU
    - A **write transaction** transfers data from the CPU to memory
- A **bus** is a collection of parallel wires that carry address, data, and control signals
    - Data and address signals can share the same wires or be separate
    - More than two devices can be connected to a bus
    - Control wires synchronize the transaction and identify the type of transaction
### 6.1.2 Disk Storage
- Disks store enormous amounts of data at a low cost
- However, accessing data on a disk is much slower than accessing data in main memory
#### Disk Geometry
- Disks are constructed from a stack of **platters**
- Each platter has two sides or **surfaces**
- A rotating **spindle** holds the platters in place and spins them at a constant **rotational rate**, typically between $5400$ and $15000$ revolutions per minute (RPM)
- Disks will typically contains one or more platters in a sealed container
- Each surface consists of a large number of concentric **tracks**
- Each track is partitioned into **sectors**
- Each sector has a fixed size, typically $512$ bytes
- Sectors are typically separated by gaps
- Gaps store formatting information and are used to separate sectors
- The entire assembly is called a **disk drive**, commonly just a **disk**
#### Disk Capacity
- The maximum number of bits that can be stored on a disk is called the **disk capacity**
- Capacity is determined by the following:
    - **Recording density (bits/inch)**: The number of bits that can be stored in a 1-inch segment of a track
    - **Track density (tracks/inch)**: The number of tracks that can be stored in a 1-inch segment of the radius of the disk
    - **Areal density (bits/inch^2)**: The product of the recording density and track density
- As areal densities increased, the gaps between sectors became unacceptably large
- To solve this, modern disks use **multiple zone recording**
    - Each zone consists of a contiguous collection of cylinders
    - Each track in each cylinder in a zone has the same number of sectors
- Capacity can be calculated as follows:
$$ \text{Capacity} = \frac{\text{\# bytes}}{\text{sector}} \times \frac{\text{average \# sectors}}{\text{track}} \times \frac{\text{\# tracks}}{\text{surface}} \times \frac{\text{\# surfaces}}{\text{platter}} \times \frac{\text{\# platters}}{\text{disk}} $$
#### Disk Operation
- Disks read and write using a **read/write head** connected to the end of an **actuator arm**
- The actuator arm can move the read/write head to any track on the disk
- This action is called a **seek**
- The read/write head at the end of the arm flies (literally) on a thin cushion of air above the surface of the disk (about 0.1 microns above the surface) at a speed of about 80 km/h
- Disks read and write data in sector-size blocks
- The **access time** for a sector has three main components:
    - **Seek time**
        - The arm first positions the head over the track with the target sector
        - The time to do this is called the seek time
        - This depends on the previous position of the arm and the speed of the arm
        - Average seek time is the average of all possible seek times, typically 3-9 ms
    - **Rotational latency**
        - The drive must wait for the first bit of the target sector to pass under the head
        - In the worst case, the head must wait for an entire rotation of the disk
        - The max rotational latency is given by $T_{\text{max rotation}} = \frac{1}{\text{RPM}} \times \frac{60 \text{ secs}}{1 \text{ min}}$
        - The average rotational latency is half of the max rotational latency
    - **Transfer time**
        - The transfer time for one sector depends on the rotational speed and the number of sectors per track
        - The transfer time can be estimated by $T_{\text{avg transfer}} = \frac{1}{\text{RPM}} \times \frac{1}{\text{(average \# sectors/track)}} \times \frac{60 \text{ secs}}{1 \text{ min}}$
- We can estimate the average a
#### Logical Disk Blocks
#### Connecting I/O Devices
#### Accessing Disks
### 6.1.3 Solid State Disks
## 6.2 Locality
## 6.3 The Memory Hierarchy
## 6.4 Cache Memories
