# Machine-Level Representation of Programs
## Introduction
- Computers execute **machine code**.
- These are sequences of bytes that encode low-level operations.
- These low level operations can:
    - Manipulate data
    - Manage memory
    - Read and write data to storage devices
    - Interact with the network
    - etc.
- A compiler will generate these machine code sequences from a high-level language.
- In high level langauges like C or Java, we don't have to worry about the details of machine code.
- In assembly language, we must specify the machine code instructions directly.
- Learning assembly language is important for understanding how programs execute.
- Sometimes the high level languages we use hide important details that can affect the performance of our programs.
- In this chapter we will learn the details on one particular assembly language, the x86-64.
- Reading assembly requires different skills than writing it.
- We must learn the relationship between source code and the assembly code it generates, and this is a form of *reverse engineering*.
- Learning the details of assembly language is prerequisite to understanding the more general fundamental concepts of computer systems.
## 3.1 A Historical Perspective
- The Intel processor line is often referred to as x86.
    - It started with the 8086 in 1978, a 16-bit processor with 29k transistors.
    - The 8086 was followed by the 80286
    - Then, i386, i486, and Pentium.
- Each processor added new features and instructions, but maintained backward compatibility.
- As a result, the x86-64 architecture has many weird artifacts due to this evolutionary heritage.
- There are several names for Intel's processor line:
    - IA-32 meant Intel Architecture 32-bit.
    - Intel 64 is the name for the 64-bit architecture, the 64-bit extensions to the x86 architecture.
    - Intel 64 is also called x86-64, or just x86.
> 86 refers to the naming scheme of Intel's processors up to the i486.
- The x86 architecture is also used by AMD, and our discussion will apply to their processors as well.
- Much of the complexity of x86 does not concern Linux and GCC.
## 3.2 Program Encodings
- We can use the gcc flag `-Og` to generate assembly code that closely resembles the source code.
- This reduces the optimization level, so the assembly code is easier to match with the source code.
- The `gcc` command invokes a sequence of programs:
    - The C *prepocessor* expands the source code to include any `#include` directives and macro expansions (like `#define`).
    - The *compiler* generates assembly code from the preprocessed source code.
    - The *assembler* generates binary *object code* from the assembly code.
        - Object code is one form of machine code.
        - Object code contains binary representations of the instructions, but global addresses are not yet resolved.
    - The *linker* merges the object code with other object code and libraries to produce an executable.
### 3.2.1 Machine-Level Code
- The format and behavior of a machine-level program is defined by the *instruction set architecture* or **ISA**.
- The ISA defines the processor state, the instruction format, and the effect of each instruction on the state.
- Most ISAs describe the behavior of a program as a sequence of instructions, with one instruction completing before the next begins.
- The hardware is far more elaborate and executes many instructions simultaneously, but it is designed to behave as if it were executing one instruction at a time in a way that matches the ISA.
- The memory addresses used by a machine-level program are *virtual addresses*.
    - This appears to be a very large byte array.
    - The implementation of virtual memory comes from multiple hardware memories and the operating system.
- Assembly has some things that are normally hidden in high level languages:
    - The *program counter* (colloquially called the PC, called `%rip` in x86-64) is the memory address of the next instruction to execute.
    - The integer *register file* has 16 named locations each storing a 64-bit value.
        - These registers can hold addresses (corresponding to C pointers) or integer data.
        - Some registers might hold critical values, while some might be used for temporary storage.
    - The *condition code* registers hold status information about the most recent arithmetic or logical operation.
        - These are used to implement conditional branches and other control flow.
        - For example, `if` and `while` statements in C.
    - A set of vector registers can each hold one or more integer or floating-point values.
- In C we have many data types that we can freely declare, allocate, and use.
- Machine code views the memory as simply a large byte-addressable array.
- Aggregate data types in C (like arrays and structs) are stored in memory as contiguous sequences of bytes.
- Even for scalar types, assembly makes no distinction between signed or unsigned integers, different types of pointers, or even between pointers and integers.
- The program memory contains:
    - Executable machine code
    - Some information required by the operating system
    - A run-time stack for procedure calls and returns
    - Blocks of memory allocated by the user
- At any given time, only limited subranges of virtual addresses are valid.
    - For example, x86 virtual addresses are 64 bits, but current implementations only use 48 bits.
    - This means that the valid addresses are in the range `0x000000000000` to `0x00007FFFFFFFFFFF`.
    - Most typical programs will only be allowed a few megabytes or gigabytes of memory.
- The OS manages the virtual address space, and translates virtual addresses to physical addresses.
- Single machine instructions perform very elementary operations.
    - For example, adding two numbers
    - Transfer data between memory and registers
    - Branching to a different part of the program (instruction address)
### 3.2.2 Code Examples
- Say we have the C code `mstore.c`:
```c
long mult2(long, long);

void multstore(long x, long y, long *dest) {
    long t = mult2(x, y);
    *dest = t;
}
```
- Running `gcc -Og -S mstore.c` will generate the assembly code `mstore.s`:
```asm
multstore:
    pushq   %rbx
    movq    %rdx, %rbx
    call    mult2
    movq    %rax, (%rbx)
    popq    %rbx
    ret
```
- Each indented line is a single instruction.
- For example, `pushq %rbx` pushes the value of `%rbx` onto the program stack.
- All information about local variable names or types is lost in the assembly code.
- Using the `-c` flag with `gcc` will generate an object file `mstore.o`.
- The object file contains the binary representation of the assembly code:
```
53 48 89 d3 e8 00 00 00 00 48 89 03 5b c3
```
- The upshot is that the end result of the compilation process is a sequence of bytes that can be executed by the processor.
- We can inspect machine code with *disassemblers*.
- Disassemblers convert machine code back into assembly code.
- In linux we can use `objdump -d mstore.o` to disassemble the object file.
- The output will look like this:
```asm
0000000000000000 <multstore>:
   0:   53                      push   %rbx
   1:   48 89 d3                mov    %rdx,%rbx
   4:   e8 00 00 00 00          callq  9 <multstore+0x9>
   9:   48 89 03                mov    %rax,(%rbx)
   c:   5b                      pop    %rbx
   d:   c3                      retq
```
- On the left we have the hexadecimal address of the instruction.
- The hex values are in groups of 1-5 bytes, each group corresponding to a single instruction.
- Several features of machine code and its disassembled form are worth noting:
    - x86-64 instructions can be 1-15 bytes long. Commonly used instructions and those with fewer operands require fewer bytes.
    - The instruction format is designed such that there is a unique decoding of the bytes to machine instructions given the starting address.
    - The disassembler determines the assembly code purely from the byte sequence.
    - The disassembler uses a slightly different naming convention from GCC.
        - For example, the 'q' in `pushq` and `movq` are lost in the disassembly.
        - These suffixes are size designators, and `q` means quadword, or 8 bytes.
        - Funnily, the disassembler adds 'q' to `call` and `ret` instructions.
- We can disassembly a fully linked executable, and the output will be slightly different.
- The disassembly of the executable will look something like this:
```asm
0000000000400540 <multstore>:
  400540:       53                      push   %rbx
  400541:       48 89 d3                mov    %rdx,%rbx
  400544:       e8 42 00 00 00          callq  40058b <mult2>
  400549:       48 89 03                mov    %rax,(%rbx)
  40054c:       5b                      pop    %rbx
  40054d:       c3                      retq
  40054e:       90                      nop
  40054f:       90                      nop
```
- This is almost identical to the disassembly of the object file.
- One important difference is that the addresses are different.
- The linker has shifted the addresses of the instructions to a different range.
- The linker also matches function calls to the correct addresses.
- The last two lines of the disassembly are `nop` instructions.
    - These are no-operation instructions, and are used to pad the code to a multiple of 16 bytes.
    - This is so that the code is aligned to a 16-byte boundary.
    - Bettery memory alignment can improve performance.
### 3.2.3 Notes on Formatting
- When we give the command `linux> gcc -Og -S mstore.c`, we get the following assembly code:
```asm
    .file   "010-mstore.c"
    .text
    .globl  multstore
    .type   multstore, @function
multstore:
    pushq   %rbx
    movq    %rdx, %rbx
    call    mult2
    movq    %rax, (%rbx)
    popq    %rbx
    ret
    .size   multstore, .-multstore
    .ident  "GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
    .section    .note.GNU-stack,"",@progbits
```
- All the lines that start with a period are directives to guide the assembler and linker.
- The directives can generally be ignored.
#### Aside - ATT vs Intel Syntax
- The assembly code generated by `gcc` and `objdump` uses the *AT&T* syntax.
- AT&T operated Bell Labs, and the syntax was developed for the Unix operating system.
- Other programming tools, like some from Microsoft and the Intel docunentation, use the *Intel* syntax.
- The two syntaxes are similar, but have some differences.
- For example, running `linux> gcc -Og -S -masm=intel mstore.c` will generate the assembly code in Intel syntax:
```asm
multstore:
    push    rbx
    mov     rbx, rdx
    call    mult2
    mov     QWORD PTR [rbx], rax
    pop     rbx
    ret
```
- We can see the following differences:
    - The Intel code omits the size designators like `q` and `l`.
    - There are no `%` symbols indicating registers.
    - Locations in memory are denoted differently, like `QWORD PTR [rbx]` instead of `(%rbx)`.
    - The order of operands is reversed.
## 3.3 Data Formats
- Intel uses the term **word** to refer to a 16-bit quantity.
- This is due to the original 8086 processor being a 16-bit processor.
- Therefore, 32-bit quantities are called **double words**, and 64-bit quantities are called **quad words**.
- Standard C types:
    - `int` values are stored as double words (32 bits or 4 bytes).
    - Pointers like `char*` are 8-byte quad words.
    - `long` uses 64 bits.
- Here are some common C data types, their Intel data type, asm suffix, and size:

| C Declaration | Intel Data Type  | ASM Suffix | Size (bytes) |
| ------------- | ---------------- | ---------- | ------------ |
| char          | Byte             | b          | 1            |
| short         | Word             | w          | 2            |
| int           | Double Word      | l          | 4            |
| long          | Quad Word        | q          | 8            |
| char*         | Quad Word        | q          | 8            |
| float         | Single Precision | s          | 4            |
| double        | Double Precision | l          | 8            |
- Floating points come in two principle formats: single precision and double precision.
    - Single precision uses 4 bytes, and corresponds to the `float` type in C.
    - Double precision uses 8 bytes, and corresponds to the `double` type in C.
- Microprocessors in the x86 family historically implemented floating point operations with a special 80-bit format.
    - This can be specified in C with the `long double` type.
    - This is not standard, and is not portable.
    - Usually not used in practice.
## 3.4 Accessing Information
- The x86-64 architecture has a set of 16 general-purpose registers.
- These can store integer data or addresses.
- The names of the registers all start with `%r`, but have different naming conventions.
- This is due to the historical evolution of the x86 architecture.
- The registers are: `%rax`, `%rbx`, `%rcx`, `%rdx`, `%rsi`, `%rdi`, `%rbp`, `%rsp`, `%r8`, `%r9`, `%r10`, `%r11`, `%r12`, `%r13`, `%r14`, `%r15`.
- Instructiosn can operate on data of different sizes stored in lower-order portions of a register.
    - For example, `%rax` can be used to store a 64-bit value, `%eax` can store a 32-bit value, `%ax` can store a 16-bit value, and `%al` can store an 8-bit value.
    - Byte level operations can operate the least significant byte of a register.
    - 16-bit operations can operate on the least significant 16 bits or 2 bytes.
    - 32-bit operations can operate on the least significant 32 bits or 4 bytes.
    - 64-bit operations can operate on the entire register.
- We have some conventions for instructions less than 64 bits or 8 bytes:
    - Instructions that generate 1 or 2 byte quantities leave the upper bytes of the destination register unchanged.
    - Instructions that generate 4 byte quantities set the upper 4 bytes of the destination register to all 0s.
- Different registers serve different roles in typical programs.
    - The most unique is `%rsp`, the stack pointer, indicating the top of the run-time stack.
        - Some instructions specifically read and write to `%rsp`.
    - The other 15 registers have more flexible roles.
    - Some instructions make specific use of certain registers.
    - A set of standard programming conventions dictate the use of these registers.
### 3.4.1 Operand Specifiers
- Most instructions have one or more *operands* that specify the source values to use and the destination to write to.
    - Source values can be constants or read from registers or memory.
    - Results can be written to registers or memory.
- Thus, operand types can be of three types:
    - **Immediate**
        - A constant value encoded in the instruction.
        - In ATT syntax, immediates are prefixed with `$` followed by an integer in standard C format.
        - For example, `$-577` or `$0x1F`.
        - The assembler will automatically select the most compact representation.
    - **Register**
        - Denotes the value stored in a register.
        - Also specifies which subset of the register to use.
        - We denote an arbitrary register `a` as `r_a` and its value as `R[r_a]`.
    - **Memory**
        - We access some value in memory by specifying an address.
        - The address is often called the *effective address*.
        - We use the notation `M_b[addr]` to denote a reference to the b-byte value stored in memory at address `addr`.
        - There are many different *addressing modes* for different forms of memory references.
            - The most general form has syntax $Imm(r_b, r_i, s)$.
                - This has four components
                - $Imm$ is a constant offset
                - $r_b$ is a base register
                - $r_i$ is an index register
                - $s$ is a scaling factor
                - $s$ must be 1, 2, 4, or 8.
                - The base and index registers must be 64-bit registers.
                - The effective address is $Imm + R[r_b] + R[r_i] \cdot s$.
            - This general form is often used in array access.
            - Other forms are just this with some of the components omitted.
### 3.4.2 Data Movement Instructions
- Instructions that copy data from one place to another are some of the most used.
- Operand notation is general, so it lets us move data between registers, between registers and memory, and between memory locations.
- We can group instructions into *instruction classes*.
    - This means that instructions in a class perform the same operation, but with different operand types.
- The simplest form of data movement is the `mov` instruction class.
    - This copies data from one place to another.
    - This does not transform the data.
    - The class consists of:
        - `movb` - moves a byte
        - `movw` - moves a word
        - `movl` - moves a double word
        - `movq` - moves a quad word
    - All of these instructions do the same thing with different sizes.
    - The general form of the `mov` instruction is `mov S, D`, where `S` is the source and `D` is the destination.
## 3.5 Arithmetic and Logical Operations
## 3.6 Control
## 3.7 Procedures
## 3.8 Array Allocation and Access
## 3.9 Heterogeneous Data Structures
## 3.10 Combining Control and Data in Machine-Level Programs
## 3.11 Floating-Point Code
## 3.12 Summary
