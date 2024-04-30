# Processor Architecture
## 4.3 Sequential Y86-64 Implementations
- First we will describe a processor called **SEQ** (for sequential)
- This means on each clock cycle, SEQ will execute one instruction
- In practice this is very slow, but it is a good starting point for understanding how a processor works
### 4.3.1 Organizing Processing into Stages
- We organize the instructions into a number of operations, or a sequence of stages
- Even though the instructions differ in what they do, they all go through the same stages
- This framework will let us design a processor that makes the best use of the hardware
- The follow are the stages:
    1. *Fetch.* The fetch stage reads the bytes of an instruction that is pointed to by the PC. From there it extracts two 4-bit portions of the byte that specifies which instruction is being executed called `icode` and `ifun`. Depending on the instruction, it also may read a register specifier byte that specifies the registers that are used by the instruction (`rA`, `rB`). It may also fetch an 8-byte constant called `valC` that is used by the instruction. It then calculates `valP`, which is the current PC plus the length of the current instruction.
    2. *Decode.* The decode stage reads the values of the registers `rA` and `rB` from the register file, giving them the values `valA` and `valB`. We may also read from `%rsp` if the instruction uses the stack pointer.
    3. *Execute.* The execute stage performs the arithmetic or logical operation specified by the instruction. It may also calculate the effective address of a memory reference, or adjust the stack pointer. The result of the operation is called `valE`. Here we also set the condition codes.
    4. *Memory.* The memory stage reads or writes memory. If read, the value is called `valM`.
    5. *Write back.* The write back stage writes up to two results to the register file.
    6. *PC update.* The PC update stage updates the PC to the next instruction, which may be `valP` or something else depending on the instruction.
- The processor loops infinitely through these stages until one of the following happens:
    1. The instruction is a halt instruction
    2. There is an invalid instruction
    3. There is an invalid memory address
- More complicated processors will have exception handling modes and execute special code when an exception occurs
- Evidently, there is a lot of work to be done in each stage for just a single instruction (perform the operation itself, compute addresses, update stack pointers, etc.)
- Using a uniform structure is important so we can reuse hardware and simplify the design
### 4.3.3 SEQ Timing
- The SEQ implementation uses combinational logic and memory of two forms: clocked registers and RAM
- We have just four hardware units that need explicit control of their sequencing:
    1. The PC
    2. The register file
    3. The condition codes
    4. The data memory
- The clocking of the registers and memories is all that we need to control the sequencing of the stages
- This is because we have followed the principle of **no reading back**
> **No reading back**: The processor never needs to read back the state updated by an instruction in order to complete the processing of this instruction.
## 4.4 General Principles of Pipelining
- Pipelined systems divide some task into a series of discrete stages
- Each stage is responsible for a different part of the task
    - For example, consider a cafeteria line, a car wash, or an assembly line
    - Rather than have one customer go through the entire process, we have multiple customers at different stages of the process
- The key feature of pipelining is that it increases the *throughput* of the system
- However, it may also increase the *latency* of the system
### 4.4.1 Computational Pipelines
- Suppose we can divide a task into 3 stages: A, B, and C
- We can put *pipeline registers* between each stage so each instruction can be processed in parallel
- This way we increase the throughput at the expense of some added hardware and slightly increased latency (latency due to the added pipeline registers)
### 4.4.2 A Detailed Look at Pipeline Operation
- Signals can propagate at different rates in each stage
- Slowing down the clock signal can help ensure that the signals propagate correctly, and will not change the pipeline behavior
- However, having a clock speed that is too fast (when the values do not have enough time to propagate) can cause the pipeline to fail
- Having clocked registers at the end of each stage can help ensure that the signals propagate correctly
### 4.4.3 Limitations of Pipelining
Unfortunately, there are some factors that can limit the effectiveness of pipelining
#### Nonuniform Partitioning
- The delays of each stage may not be equal
- This means some stages will be idle while others are still working
- Making a pipeline that has equal delays in each stage is a common and difficult design challenge
#### Diminishing Returns of Deep Pipelining
- Doubling the number of stages does not double the throughput
- Modern processors have very deep pipelines (15 or more stages) in an attempt to maximize the clock rate, since each stage can have a shorter delay
### 4.4.4 Pipelining a System with Feedback
- So far we have only considered pipelines where objects passing through don't depend on each other
- However, this is not always the case with Y86 instructions
- Consider the following:
    ```asm
    irmovq $50, %rax
    addq %rax, %rbx
    mrmovq 100(%rbx), %rdx
    ```
- As we can see, the `addq` instruction depends on the `irmovq` instruction, and the `mrmovq` instruction depends on the `addq` instruction
- Another source of sequential dependencies happens due to the instruction control flow
- Consider the following:
    ```asm
    loop:
        subq %rdx, %rbx
        jne targ
        irmovq $10, %rdx
        jmp loop
    targ:
        halt
    ```
- The `jne` instruction depends on the `subq` instruction
- This means we must have a way to handle these dependencies in the pipeline
## 4.5 Pipelined Y86-64 Implementations
- Now we get to the major task of this chapter--designing a pipelined Y86-64 processor
- We start by shifting the PC update stage to the beginning of the pipeline, and adding pipeline registers between each stage
- Our first attempt will not handle dependencies properly, but we can make some modifications to fix this
### 4.5.1 SEQ+: Rearranging the Computation Stages
- First we move the PC update stage to the beginning of the pipeline, so we compute the PC value for the *current* instruction
- We create state registers to hold the signals computed during an instruction
> In SEQ+, there is no PC register. Instead, the PC is dynamically computed based on some state information from the last instruction.
- This is an example of a general transformation called *circuit retiming*
    - This means we change the state representation of a system without changing its behavior
    - Often this is used to balance the delays of the stages in a pipeline
### 4.5.2 Inserting Pipeline Registers
- Call this new design PIPE-, which is the same as SEQ+ but with pipeline registers between each stage
- The - signifies that this processor has less performance than our best design
- PIPE- has the following pipeline registers:
    - **F** holds the *predicted* value of the PC
    - **D** sits between the fetch and decode stages. It holds information about the most recently fetched instruction, and feeds it to the decode stage.
    - **E** sits between the decode and execute stages. It holds information about the most recently decoded instruction, and feeds it to the execute stage.
    - **M** sits between the execute and memory stages. It holds information about the most recently executed instruction, and feeds it to the memory stage. It also holds information about branch conditions and branch targets for conditional jumps.
    - **W** sits between the memory and feedback paths that supply the computed results to the register file for writing and the return address to the PC selection logic for a `ret` instruction.
### 4.5.3 Rearranging and Relabeling Signals
whatever
### 4.5.4 Next PC Prediction
- Our goal in the pipelined design is to *issue* a new instruction on each clock cycle
- This means that every clock cycle we have a new instruction pass into the execute stage
- In other words this means one instruction per cycle
- To do this, we need to determine the location of the next instruction
- Unfortunately, we cannot know the exact location of the next instruction if it is a conditional branch, and the exact PC will only be known several cycles later
- Similarly, if the fetched instruction is `ret`, we cant know the return address until the memory stage
- Aside from these two cases, we can predict the next PC with just the info inthe fetch stage
- For `call` and `jmp`, the next PC is the value of `valC`, since it is guaranteed to be the target of the branch
- Thus we can **predict** the next PC quite reliably, and achieve our goal of one instruction per cycle
- We must also deal with the case where the prediction is wrong (meaning we fetched and partially executed the wrong instructions)
- The technique of predicting the next PC is called *branch prediction*, and is used by basically all modern processors
- We always have the issue of predicting the PC for a `ret` instruction, since there is a nearly unbounded set of possible return addresses
- In our design we will not attempt to predict the return address, and instead we will not process instructions until the `ret` passes through the write back stage
- The PIPE- fetch stage is responsible for predicting the next PC and selecting the actual PC for instruction fetch
### 4.5.5 Pipeline Hazards
- Pipelining can cause issues when there are dependencies between instructions
- These dependencies can be of two forms:
    1. **Data** dependencies: The results computed from one instruction are used by another instruction later in the pipeline
    2. **Control** dependencies: The control flow of the program depends on the result of an instruction (e.g. call and ret instructions)
- The potential issues that can arise from these dependencies are called *hazards*
- Like the dependencides, hazards are respectively called *data* and *control* hazards
#### Avoiding Data Hazards by Stalling
- Stalling is where the process holds back one or more instructions in the pipeline until the hazard is resolved
- Hold back an instruction in the *decode* stage until the instructions generating the source values have passed through the *write back* stage
- Holding back instructions can be done by keeping the PC at a fixed value
- Suppose we have the following code:
    ```asm
    irmovq $50, %rax
    addq %rax, %rbx
    ```
- The `addq` instruction depends on the `irmovq` instruction
- We can hold back the `addq` instruction in the decode stage until the `irmovq` instruction has passed through the write back stage
- While the `addq` instruction is held in the decode stage, we need to insert **bubble** instructions in the execute stage until the `irmovq` instruction has passed through the write back stage
> A bubble instruction is like a dynamically generated `nop` instruction for stalling purposes
#### Avoiding Data Hazards by Forwarding
- Forwarding is where we pass the result of an instruction directly to the stage that needs it
- For example, say we have the following code:
    ```asm
    irmovq $10, %rdx
    irmovq $3, %rax
    addq %rdx, %rax
    ```
- The `addq` instruction depends on the `irmovq` instructions
- The `%rax` register is a source operand for `valB` in the `addq` instruction, and there is also a pending write to `%rax` from the `irmovq` instruction
- We can avoid stalling by forwarding the value of `%rax` to the execute stage
- This requires extra hardware to detect when forwarding is necessary and to actually forward the value
- This also works for pending memory writes
- We can forward to either `valA` or `valB` in the execute stage
- We can forward from the following sources:
    - e_valE (from the execute stage)
    - m_valM (from the memory stage)
    - M_valE (from the memory stage)
    - W_valM (from the write back stage)
    - W_valE (from the write back stage)
#### Load/Use Data Hazards
- A special case of data hazards is the load/use hazard
- This is where a load instruction is followed by an instruction that uses the loaded value
- For example, consider the following code:
    ```asm
    mrmovq 0(%rdx), %rax
    addq %ebx, %eax
    ```
- Since we have no forwarding paths that can help us here, we must stall the `addq` instruction for one cycle
- The use of a stall to handle a load/use hazard is called a *load interlock*
#### Avoiding Control Hazards
- Control hazards happen when the processor cannot reliably determine the next PC based on the current instruction in the fetch stage
- This only happens for `ret` and `jXX` instructions
- We can use the same stalling technique to handle control hazards, and insert bubble instructions until the correct PC is determined
- To handle a mispredicted branch, we can *cancel* the instructions that were fetched after the mispredicted branch by inserting bubble instructions