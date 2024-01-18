# A Tour of Computer Systems

## Introduction
- Computer systems are made of hardware and software, which work together to run programs
- Specific hardware and software may vary but their underlying principles do not

## 1.1 Information is Bits + Context
- Lets say we have this simple hello world program in C:
```c
#include <stdio.h>

int main() {
    printf("hello, world\n");
    return 0;
}
```
- The source file is a sequence of bits (0 or 1)
- Bits are organized into 8-bit chunks called bytes
- Each byte represents a different character in the program using ASCII integer values
> Big idea: All information is represented as bits in a computer. The meaning of these bits depends on the context in which they are interpreted.
- **Caveat:** Machine representations of numbers are not the same as $\mathbb{R}$ and $\mathbb{Z}$, as they are finite approximations that may behave in unexpected ways

## 1.2 Programs are Translated by Other Programs into Different Forms
- The C program is translated into machine language by a compiler
- The exact instructions are packaged in a form called an *executable object program* or simply *object file* (also just called a *binary*)
- **C compilation happens in 4 steps**:
    1. Preprocessing: The original C source code is modified according to directives that begin with `#`.
        - For example, `#include <stdio.h>` tells the preprocessor to insert the contents of `stdio.h` into the source file.
        - The result of preprocessing is a pure C program without any preprocessor directives, typically with the `.i` extension.
    2. Compilation: The preprocessed source code is translated into assembly code, typically with a `.s` extension.
    3. Assembly: The assembly code is translated into machine language, typically with a `.o` extension.
        - This file is known as a *relocatable object program*
        - This file would look like gibberish if opened in a text editor
    4. Linking: The object file is combined with other object files to create an executable object program, typically with no extension, or `.out` on Linux, or `.exe` on Windows.
        - The linker combines the object file with the standard C library, which contains functions like `printf` and `scanf`.
        - The linker also combines the object file with other object files that contain functions that are defined in other source files.

## 1.3 It Pays to Understand How Compilation Systems Work
Reasons to understand compilation systems:
- Optimization: Understanding how the compiler works can help you write code that is more efficient.
    - Switch or if-else?
    - While or for loop?
    - Pointer or array?
    - Local variable or pass by reference?
- Understanding link-time errors: Some of the most perplexing errors occur at link time, especially for large projects.
    - Cannot resolve a reference?
    - Static vs dynamic library?
    - Some linker errors don't even occur until runtime.
- Security.
    - For example, buffer overflow attacks are very common on the internet.

## 1.4 Processors Read and Interpret Instructions Stored in Memory
- In Unix-like systems, we can run programs by typing their name in the command line.
    - The shell is an interpreter that reads commands from the command line and executes them.

**Buses**
- A bus is a collection of wires that transmit data from one part of the computer to another.
- Typically designed to transfer fixed-sized chunks of bytes called *words*.
- The *word size* is the number of bytes in a word, which is typically 4 or 8 bytes for 32-bit and 64-bit systems, respectively.

**I/O Devices**
- The system's connection to the external world.
    - For example: keyboard, mouse, display, disk drive, network connection, etc.
- Each device is connected to the I/O bus by either a *controller* or an *adapter*.
    - A controller is a chip that is part of the device or the motherboard.
    - An adapter is a card that plugs into a slot on the motherboard.
    - Regardles, the controller or adapter is responsible for moving the data between the I/O device and the I/O bus.

**Main Memory**
- Temporary storage that holds both a program and the data it manipulates while the processor is executing the program.
- Physically stored in DRAM (dynamic random access memory) chips.
- Logically, memory is a linear array of bytes, each with its own unique address.
- Machine instructions will vary in length
> Clarification: Machine instructions are NOT assembly instructions. Machine instructions are the binary instructions directly understood by the processor. Also, word size is typically defined by the artitecture of the processor (32-bit or 64-bit).

# word size depends on architecture, 32 vs 64 bit, what about x86 vs ARM vs RISC-V etc?

**Processor**
- The CPU executes the instructions in main memory.
- At its core is a word-size storage device called a *register*.
- Each core has a special register called the *program counter*.
    - The program counter points to the address of some machine language instruction in main memory.
    - Each core only has one program counter, but it can have multiple registers to allow for parallelism within a single instruction stream.
- The CPU is constantly executing the instruction pointed to by the program counter from when it is turned on until it is turned off.
- The CPU appears to operate according to a very simple model defined by its instruction set architecture.
    - In this model the CPU executes instructions sequentially.
    - Loop consists of: reading instruction from program counter, interpret bits in instruction, perform operation, update program counter to point to next instruction.
- There are only a few instructions that the CPU can execute.
- These instructions revolve around main memory, the register file, and arithmetic/logic unit (ALU).
    - The register file is a small storage device that consists of a collection of word-size registers each with a unique name.
    - The ALU computes new data and address values.
- Examples of simple CPU instruction operations:
    - Load: copy a byte or word from main memory into a register, overwriting the previous contents.
    - Store: copy a byte or word from a register to main memory, overwriting the previous contents.
    - Operate: copy the contents of two registers to the ALU, perform an arithmetic operation on the two words, and store the result in a register, overwriting the previous contents.
    - Jump: extract a word from the instruction itself and copy that word into the program counter, overwriting the previous value.

## 1.5 Caches Matter
- Systems spend lots of time moving information from one place to another (disk, memory, cache, etc.)
- Much of this moving around slows down the "real work" of the program.
- Larger storage devices are slower than smaller ones.
- Smaller storage devices are more expensive than larger ones.
- This issue is addressed by using a hierarchy of storage devices called *cache memories* or simply caches.
    - L1 cache is the smallest and fastest: nearly as fast as the register file.
    - L2 cache is larger and slower than L1: connected to the processor by a dedicated bus.
    - L1 and L2 are called *static random access memory* (SRAM)
    - Newer systems have an L3 cache that is larger and slower than L2.
- Below the caches is main DRAM memory, then disk storage, then network storage, etc.

## 1.6 Storage Devices Form a Hierarchy
- The storage hierarchy is a great example of the tradeoff between speed and cost.
- The closer a storage device is to the processor, the faster it is and the more expensive it is.

## 1.7 The Operating System Manages the Hardware
- The hello program from earlier did not access the keyboard, display, disk, or main memory directly.
- Instead, it relied on the operating system to provide these services.
- The operating system is a layer of software interposed between the application program and the hardware.
- The operating system has two primary purposes:
    1. To protect the hardware from misuse by runaway applications.
    2. To provide applications with simple and uniform mechanisms for manipulating complicated and often wildly different low-level hardware devices.
- The operating system achieves this by using the fundamental abstractions of *processes*, *virtual memory*, and *files*.

**Processes**
- When a program such as the hello program from earlier runs on a modern system, the OS provides the illusion that it is the only program running on the system.
    - The program appears to have exclusive use of the processor, main memory, and I/O devices.
    - The processor appears to execute the program's instructions sequentially without interruption.
    - The code and data of the program appear to be the only objects in memory.
- These illusions are provided by the notion of a *process*.
- A process is the OS's abstraction for a running program, and multiple processes can run at the same time.
- Most of the time, there are more processes than CPUs to run them.
- The OS accomplishes this by something called *context switching*.
- For a *uniprocessor* system:
    - The OS keeps track of all the state info needed for the process to run
    - This info is called the *context* of the process
    - The context includes the current values of the PC, register file, and contents of main memory.
    - When the OS decides to transfer control from one process to another, it saves the context of the old process and restores the context of the new process, called a *context switch*.
- In the hello program example:
    - Initially only the shell is running
    - When the user types `./hello`, the shell invokes a special function called a *system call* that causes the OS to create a new process to run the hello program.
    - The OS saves the shell's context, creates a new context for the hello program, and transfers control to the hello program.
    - When the hello program terminates, the OS restores the shell's context and transfers control back to the shell.
- The transition from one process to another is managed by the OS *kernel*, which is the one program that is always in memory.
- Whenever a program needs to perform a privileged operation, it must ask the kernel to do it on its behalf by making a system call.
> The kernel is not a separate process, but a collection of code and data structures that is used to manage all processes.

**Threads**
- Threads are a way of having multiple execution units within a single process.
- Both threads share the same code, global data, and context.

**Virtual Memory**
- Virtual memory gives the illusion that each process has exclusive use of the main memory.
- Each process has the same uniform view of memory, called *virtual address space*.
- The virtual address space seen by each process consists of a collection of well-defined areas each with a specific purpose.
    - *Program code and data*: Code begins at the same fixed address for all processes. The code and data areas are initialized from the executable object file.
    - *Heap*: The code and data areas are followed immediately by the run-time heap, which grows and shrinks dynamically at run time, whereas the code and data areas are fixed in size.
    - *Shared libraries*: Near the middle of the address space is a region containing the code and data for shared libraries.
    - *Stack*: At the top of the users virtual address space is the stack. Grows each time a function is called and shrinks when the function returns.
    - *Kernel virtual memory*: The top of the address space is reserved for the kernel. This cannot be accessed by user programs.
- The basic idea of virtual memory is to store the contents of memory in a file on disk and use the main memory as a cache for the disk.

**Files**
- A file is a sequence of bytes.
- All I/O devices are modeled as files.
- All input and output in Unix is done by reading and writing files, using syscalls known as Unix I/O.

## 1.8 Systems Communicate with Other Systems Using Networks
- Modern systems are often connected to other systems via a network.
- A network can be viewed as just another I/O device.

## 1.9 Important Themes
- A system is more than just hardware, but a tapestry of hardware and software that work together to run programs.

### 1.9.1 Amdahl's Law
- Amdahl's law describes the potential speedup from improving the performance of a particular part of a system.
    - Say that some application requires time $T_{old}$ to run.
    - Some part of this system requires a fraction $\alpha$ of the time and we improve the performance of this part by a factor of $k$.
    - The component originally required time $\alpha T_{old}$, but now requires $\alpha T_{old}/k$.
    - The total time is now $$\begin{align*}T_{new} &= (1-\alpha)T_{old} + \alpha T_{old}/k \\ &= T_{old}[(1-\alpha) + \alpha/k]\end{align*}$$.
    - The speedup is $$\begin{align*}S &= T_{old}/T_{new} \\ &= \frac{1}{(1-\alpha) + \alpha/k}\end{align*}$$.
- If we consider the limit as $k \to \infty$, we get $S_{\infty} = 1/(1-\alpha)$.

### 1.9.2 Concurrency and Parallelism
- Concurrency is the general concept of a system doing more than one thing at a time.
- Parallelism is the use of concurrency to make a system run faster.
- Parallelism can be exploited at multiple levels of abstraction.

**Thread-Level Concurrency**
- Threads allow for multiple controls flows within a single process.
- Traditionally, concurrent execution was only simulated by the OS by rapidly switching between processes, like a juggler with many balls in the air.
- Until recently, most systems had only one processor switching between multiple tasks.
- This configuration is called a *uniprocessor* system.
- Modern systems have multiple processors, called *multiprocessor* systems.
- Multi-core processors have several CPUs or *cores* on a single chip.
    - L1 cache is split into two parts: one to hold instructions and one to hold data.
    - L1 and L2 caches are private to each core, while L3 cache is shared.
- *Hyperthreading*, or *simultaneous multithreading* allows for a single CPU to execute multiple flows of control.

**Instruction-Level Parallelism**
- At a lower level, modern processors can execute multiple instructions at a time.
- Processors that can sustain execution rates faster than one instruction per clock cycle are called *superscalar*.

**Single-Instruction, Multiple-Data (SIMD) Parallelism**
- Many modern processors have special hardware to allow for a single instruction to perform multiple operations in parallel.


### 1.9.3 The Importance of Abstractions in Computer Systems
- Abstractions are one of the most important concepts in computer science.
- For example, the use of APIs allows for programmers to use code without knowing how it works.
- The *instruction set architecture* abstracts the hardware.
- We also introduced files as an abstraction for I/O devices, virtual memory as an abstraction for program memory, and processes as an abstraction for a running program.
- *Virtual Machines* abstract the hardware of a computer.

## 1.10 Summary
"A computer system consists of hardware and systems software that cooperate
to run application programs. Information inside the computer is represented as
groups of bits that are interpreted in different ways, depending on the context.
Programs are translated by other programs into different forms, beginning as
ASCII text and then translated by compilers and linkers into binary executable
files.

Processors read and interpret binary instructions that are stored in main memory. Since computers spend most of their time copying data between memory, I/O
devices, and the CPU registers, the storage devices in a system are arranged in a hierarchy, with the CPU registers at the top, followed by multiple levels of hardware
cache memories, DRAM main memory, and disk storage. Storage devices that are
higher in the hierarchy are faster and more costly per bit than those lower in the
hierarchy. Storage devices that are higher in the hierarchy serve as caches for devices that are lower in the hierarchy. Programmers can optimize the performance
of their C programs by understanding and exploiting the memory hierarchy.

The operating system kernel serves as an intermediary between the application and the hardware. It provides three fundamental abstractions: (1) Files are
abstractions for I/O devices. (2) Virtual memory is an abstraction for both main
memory and disks. (3) Processes are abstractions for the processor, main memory,
and I/O devices.

Finally, networks provide ways for computer systems to communicate with
one another. From the viewpoint of a particular system, the network is just another
I/O device."