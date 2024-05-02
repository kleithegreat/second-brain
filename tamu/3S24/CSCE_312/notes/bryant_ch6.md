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
- We can estimate the average access time as average seek time + average rotational latency + average transfer time
- Access times are dominated by the seek time and rotational latency
#### Logical Disk Blocks
- Modern disks abstract away the complex physical layout of the disk from the operating system with **logical disk blocks**
- They present a simpler view of a sequence of $B$ sector-size logical blocks, numbered from $0$ to $B-1$
- A small hardware/firmware device in the disk package called the **disk controller** translates logical block numbers to physical sector numbers
- The OS will request a read or write of a logical block, and the disk controller will translate this to a physical sector number using a fast lookup table
- Logical block numbers get translated into a (*surface*, *track*, *sector*) triple, which effectively identifies a sector on the disk
#### Connecting I/O Devices
- Input/output (I/O) devices like GPUs, monitors, mice, keyboards, and disks are connected to the CPU and main memory with an **I/O bus**
- The I/O bus is unlike the system bus and memory buses since its design is CPU independent (recall that the system bus connects the CPU to the IO bridge, and the memory bus connects the IO bridge to main memory)
- The I/O bus is slower but must accomodate a wide variety of devices
- Here are some examples of devices that can be attached to the I/O bus:
    - A *universal serial bus* (USB) can connect a wide variety of devices
    - A *graphics card* can paint pixels on the display on behalf of the CPU
    - A *host bus adapter* can connect disks to the I/O bus, and the two most popular interfaces are *SATA* and *SCSI*
    - *Network adapters* can be plugged into *expansion slots* on the motherboard
#### Accessing Disks
- I/O is actually quite complicated, but this is a simplified rundown
- The CPU issues commands to I/O devices using **memory-mapped I/O**
    - A block of address space is reserved for I/O devices, and each of these addresses is known as an **I/O port**
    - Each device has one or more I/O ports when it is connected to the I/O bus
- Example: Suppose a disk controller has an address of `0xa0`
    - The CPU can read the disk by executing three store instructions to the address `0xa0`
    - The first instruction tells the disk to initiate a read and other parameters like whehter to interrupt the CPU when the read is complete
    - The second instruction tells the disk the logical block number to read
    - The third instruction tells the disk where to store the data in main memory
- The CPU will typically do working while the disk is reading (recall that disks are slow)
- After receiving the read command from the CPU, the disk controller will translate the logical block number to a sector address, read the sector, and transfer the data to main memory
    - This does not require CPU intervention
    - This is called **direct memory access (DMA)**
- After the DMA the disk controller will interrupt the CPU to let it know that the read is complete
    - This will cause the CPU to stop what it is doing and jump to an OS routine to handle the interrupt
    - After the interrupt is handled, the CPU will resume what it was doing
### 6.1.3 Solid State Disks
- A solid state disk (SSD) is based on flash memory
- They usually plug into USB or SATA
- An SSD consists of flash memory chips and a **flash translation layer** which serves the same purpose as the disk controller for a disk (translates logical block numbers to physical sector numbers)
- A flash memory consists of a sequence of $B$ **blocks** and each block consists of $P$ **pages**
    - Typically pages are 512 byte to 4KB
    - Blocks are typically 32-128 pages
- Pages can only be written to after the entire block it belongs to has been **erased**
- Being erased typically means all the bits in the block are set to 1
- Blocks wear out after a certain number of writes
- Random writes are slower for two reasons:
    - Erasing a block is slow
    - Writing to a page with existing data outside of the block requires copying the entire block to a new block and then writing the new data
## 6.2 Locality
- Well written programs exhibit good **locality**
- This means it uses data that are near other data that have been used recently or recently used itself
- Locality has two main forms:
    - **Temporal locality**: If a data item is referenced, it will tend to be referenced again soon
    - **Spatial locality**: If a data item is referenced, data items whose addresses are close to it will tend to be referenced soon
- Programs with good locality run faster
- We speed up memory accesses with small fast memories called **cache memories**
### 6.2.1 Locality of References to Program Data
- Consider the following function:
    ```c
    int sumvec(int v[N]) {
        int i, sum = 0;
        for (i = 0; i < N; i++) {
            sum += v[i];
        }
        return sum;
    }
    ```

| Address | 0 | 4 | 8 | 12 | 16 | 20 | 24 | 28 |
|---|---|---|---|---|---|---|---|---|
| Contents | $v_0$ | $v_1$ | $v_2$ | $v_3$ | $v_4$ | $v_5$ | $v_6$ | $v_7$ |
| Access order | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

- To determine if the program has good locality, we should look at the reference pattern for each variable
- This function has good spatial locality since it accesses $v_i$ in order
- This function has poor temporal locality since it only accesses each $v_i$ once
- This kind of function is said to have a **stride-1 reference pattern** (with respect to element size)
- Visintg every *k*th element of a contiguous array is called a **stride-k reference pattern**
    - Stride-1 pattersn are common and a good source of spacial locality
    - Generally, as stride increases, locality decreases
- Stride is an important issue for multi-dimensional arrays
    - For example, consider the following function:
        ```c
        int sumarrayrows(int a[M][N]) {
            int i, j, sum = 0;
            for (i = 0; i < M; i++)
                for (j = 0; j < N; j++)
                    sum += a[i][j];
            return sum;
        }
    - This reads the array in **row-major order**, i.e. it reads the first row, then the second row, etc.
    - This function has good spatial locality since it reads the array in order
    - Indexing by column-major order would have poor spatial locality, with a stride of $N$
### Locality of Instruction Fetches
- We can also evaluate the locality of a programs instruction fetches
- For example, the `sumvec` function from before has good spatial locality since it reads the instructions in order with a for loop
- Since the for loop also repeats, it has good temporal locality
## 6.3 The Memory Hierarchy
> "In one of the happier coincidences of computing, these fundamental properties of hardware and software complement each other beautifully. Their complementary nature suggests an approach for organizing memory systems, known as the **memory hierarchy**, that is used in all modern computers."
- The storage devices get slowerm cheaper, and larger as we move down the hierarchy
- L0: Registers
- L1: L1 cache (SRAM)
- L2: L2 cache (SRAM)
- L3: L3 cache (SRAM)
- L4: Main memory (DRAM)
- L5: Local secondary storage
- L6: Remote secondary storage
### 6.3.1 Caching in the Memory Hierarchy
- Generally, a **cache** is a small and fast storage device used as a staging area for frequently accessed data from a larger and slower storage device
- Using a cache is called **caching**
- The *central* idea of the memory hierarchy is that for each $k$, the faster and smaller storage device at level $k$ is a cache for the slower and larger storage device at level $k+1$
#### Cache Hits
- When a program wants some data from level $k+1$, it first checks if the data is in the cache at level $k$
- If the data is in the cache, this is called a **cache hit**
- Cache hits are faster than accessing the slower storage device
#### Cache Misses
- If the data is not in the cache, this is called a **cache miss**
- During a miss, the cache at level $k$ is updated with the data from level $k+1$, possibly overwriting some other data if the cache is full
- This process is called **replacing** or **evicting**
- The removed block is called the **victim** block
- How a cache decides which block to replace is called the **replacement policy**
    - Random replacement is a simple policy
    - Least recently used (LRU) performs well in practice
#### Kinds of Cache Misses
- Distinguishing between different kinds of cache misses can be useful
- An empty cache is called a **cold cache**
    - The first access to a block in a cold cache is called a **cold miss** or **compulsory miss**
    - These are often transient and not a big deal, as they won't occur in a steady state
- Whenever there is a cache miss, the cache must implement some **placement policy** to decide where to put the block
    - The most flexible would be to allow any block from the lower level to be placed in any block in the cache
        - This is too expensive for caches higher in the hierarchy
        - Randomly placed blocks are expensive to find
    - Hardware caches typically restrict the placement to a small number of blocks
        - For exampe, we might decide a block $i$ at level $k+1$ must be placed in block $i \mod 4$ at level $k$
        - This means that blocks 0, 4, 8, 12, etc. at level $k+1$ must be placed in block 0 at level $k$
- Cache misses due to restrictive placement policies are called **conflict misses**
    - This is where the cache is large enough to hold the referenced data, but the placement policy maps the data to the same cache block as some other data
    - For example if we keep on referencing blocks 0, 4, 8, 12, etc. at level $k+1$, they will all be placed in block 0 at level $k$, causing conflict misses
- Programs tend to run as a sequence of phases (like loops, or just different parts of the program that do different things)
- Each phase may reference some reasonably constant set of cache blocks, which is called the **working set** of the phase
- When the working set is larger than the cache, we call that a **capacity miss**
#### Cache Management
- Some kind of logic must manage the cache
- Something must partition the cache into blocks, transfer blocks between levels, decide when there are hits and misses, and how to deal with misses
- This logic can be hardware, software, or a combination of both
- For example, the compiler manages the register file, decides when to issue loads for misses, and where to store the data in
## 6.4 Cache Memories
- Early computer systems only had three levels in the memory hierarchy: registers, main memory, and disk storage
- The growing gap between the speed of the CPU and the speed of main memory led to the development of cache memories
- The **L1 cache** is a small SRAM cache memory between the register file and main memory
    - L1 is connected to the bus interface
    - Recall the bus interface is connected to the register file and the memory bus
    - L1 can be as fast as the registers
- As the performance gap between the CPU and main memory grew, more levels of cache were added
    - **L2 cache**: A larger and slower cache between L1 and main memory
    - **L3 cache**: An even larger and slower cache between L2 and main memory
### 6.4.1 Generic Cache Memory Organization
- Suppose we have a computer with $m$ bit memory addresses and thus $M = 2^m$ unique memory addresses
- A cache for this computer would have $S = 2^s$ **cache sets**
- Each cache set consists of E **cache lines**
- Each line consists of
    - A data **block** of $B = 2^b$ bytes
    - A **valid bit** that indicates whether the block contains meaningful data
    - $t = m - (b + s)$ **tag bits** that unique identify the block
        - This is a subset of the current blocks memory address
- Generally a cache's organization can be described as the tuple $(S, E, B, m)$
    - The size (or capacity) of a cache $C$ is in terms of aggregate size of all blocks (i.e. tag bits and valid bits are not included)
    - This is given by $C = S \times E \times B$
- When the CPU needs to access memory, it first checks the cache
    - The cache is organizes so that it can find the requested word by inspecting the bits of the address
    - This is similar to how a hash table works
- The parameters $S$ and $B$ induce a partitioning of the $m$ address bits into three fields
    - The address has the form of Tag, Set index, and Block offset
    - The $s$ **set index bits** in the memory address form an index that selects one of the $S$ sets
        - The first set is 0, the second is 1, etc.
        - The set index bits are used to select the set
    - After indexing the set, the $t$ tag bits in the memory address tell us which line (if any) contains the word
    - A line in the set contains the word if and only if the valid bit is set and the tag bits match the tag bits in the address
    - The $b$ **block offset bits** in the memory address tells us the offset of the word within the block
### 6.4.2 Direct-Mapped Caches
- Caches are grouped into different classes based on $E$: number of cache lines per set
- A **direct-mapped cache** is a cache with $E = 1$, or one cache line per set
- These are the simplest to implement and understand
- Say we have a CPU, register file, and L1 cache
    - The CPU reads a memory word *w*
    - It first checks the L1 cache
        - Cache hit: The CPU reads *w* from the cache
        - Cache miss: The CPU reads *w* from main memory and updates the cache
- Determining if a memory word is in the cache has three steps: set selection, line matching, and word extraction
#### Set Selection in Direct-Mapped Caches
- The cache extracts the $s$ set index bits from the middle of the address
- This is an unsigned integer and is used to index the set
- We can think of the cache as a 1D array of sets
#### Line Matching in Direct-Mapped Caches
- Line matching is easy in a direct-mapped cache, since there is only one line per set
- If the valid bit is set and the tag bits match, the cache has a hit
#### Word Selection in Direct-Mapped Caches
- Once we have a hit, we know *w* is somewhere in that block
- The block offset bits tell us where *w* is in the block
- We can think of a block as an array of bytes, and the block offset bits tell us which byte to select
#### Line Replacement in Direct-Mapped Caches
- When there is a miss, the cache must replace the line in the set
- The replacement policy is trivial in a direct-mapped cache: the cache line is replaced with the new block
#### Putting It Together: A Direct-Mapped Cache in Action
#### Conflict Misses in Direct-Mapped Caches
### 6.4.3 Set-Associative Caches
- The issue of common conflict misses in direct mapped caches comes from the fact that they have one line per set
- A cache with $1 < E < C/B$ is called an **E-way set-associative cache**
#### Set Selection in Set-Associative Caches
- Identical to direct-mapped caches
#### Line Matching and Word Selection in Set-Associative Caches
- An associative memory is an arrya of key-value pairs
- The keys of the pairs are the concatenation of the tag bits and the valid bits, and the values are the data contained in the block
- The cache must search each line for a matching tag
#### Line Replacement on Misses in Set-Associative Caches
- If there is an empty line in the set, the block is placed in the empty line
- The simplest policy is random replacement
- **Least recently used (LRU)** and **least frequently used (LFU)** are more complex and require more hardware
- The cost of cache misses become more expensive further down the hierarchy
### 6.4.4 Fully Associative Caches
- A **fully associative cache** is a cache with $E = C/B$
- In other words, one set containing all the cache lines
#### Set Selection in Fully Associative Caches
- Trivial--there is only one set
- There are no set index bits in the address here, and it only gets partitioned into a tag and block offset
#### Line Matching and Word Selection in Fully Associative Caches
- Works the same as set-associative caches
- However, since the cache must search for many lines in parallel, these caches are typically smaller
### 6.4.5 Issues with Writes
- Updating caches on writes is more complicated than reads
- Suppose we have a write to a memory word *w* that exists in the cache
    - The cache and memory must be updated
    - This is called a **write-through** policy
    - While simple, this can cause a lot of traffic on the memory bus
- A **write-back** policy only updates the cache, and only updates the memory when the block is replaced
    - Write back can significantly reduce memory traffic
    - This way the cache must contain an additional **dirty bit** that indicates whether the block has been modified
- We must also deal with write misses
- A **write-allocate** policy fetches the block from memory on a write miss and updates the cache
- The alternative is a **write-no-allocate** policy, which writes the block to memory without updating the cache
- Write back caches are typically write-allocate
- Optimizing caches is very difficult
- Lower level caches should tend to use write-back policies due to transfer times
### 6.4.6 Anatomy of a Real Cache Hierarchy
- Caches can hold not only data but also instructions
    - An instruction only cache is called an **i-cache**
    - A data only cache is called a **d-cache**
    - A cache that holds both is called a **unified cache**
- Modern processors have separate i-caches and d-caches
    - This allows for simultaneous instruction and data fetches
    - i-caches are also typically simpler and smaller than d-caches since they are read-only
    - Reduces conflict misses
### 6.4.7 Performance Impact of Cache Parameters
- Cache performance can be measured with the following metrics:
    - **Miss rate**: The fraction of memory accesses that result in a miss. Computed as $\frac{\text{\# misses}}{\text{\# accesses}}$
    - **Hit rate**: The fraction of memory accesses that result in a hit. Computed as $1 - \text{miss rate}$
    - **Hit time**: The time to deliver a word from the cache to the CPU on a hit, which includes the time for set selection, line identification, and word selection
    - **Miss penalty**: Any additional time required due to a miss
#### Impact of Cache Size
- A larger cache will increase hit rate
- However, a larger cache will also increase hit time
#### Impact of Block Size
- Larger blocks can help hit rate due to spatial locality
- Larger blocks may also imply less cache lines, which can hurt hit rate
- Larger blocks can also increase miss penalty
#### Impact of Associativity
- This is the choice of $E$: the number of cache lines per set
- Higher associativity can help prevent thrashing due to conflict misses
> Recall that thrashing is when the cache is constantly replacing blocks right after they are used
- Higher associativity is expensive to implement and hard to make fast
    - Requires more tag bits per line
    - Additional LRU state bits per line
    - Additional control logic
- Higher associativity can also increase hit time due to increased complexity
- The choice of associativity comes down to a trade-off between hit time and miss penalty
- Typically high performance systems use less associativity for high level caches and more associativity for lower level caches
#### Impact of Write Strategy
- Write-through caches are simpler and can use a **write buffer** independent of the cache
- Write-through also make read misses less expensive since they don't need to write the block back to memory
- Write back results in fewer transfers
- Decreasing transfers is more important lower in the hierarchy, since transfer times are higher
- Caches further down are more likely to use write-back