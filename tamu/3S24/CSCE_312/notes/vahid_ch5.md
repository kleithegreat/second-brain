# 5 - Register Transfer Level (RTL) Design
## 5.1 Introduction
- Previously we have talked about capturing behavior and impementing it as a digital circuit
- Chapter 2 introduced combinational logic
- Chapter 3 introduced sequential logic and FSMs
- Chapter 4 introduced the concept of a datapath and a controller
- This chapter will focus on even higher level sequential behavior
    - We will use someting called a high-level state machine or HLSM
    - This means the inputs, outputs, state actions, and transition conditions can use higher level constructs
    - These higher level constructs can be binary numbers or integers rather than just single bit boolean values
- We will introduce a method to convert HLSMs into a circuit consisting of a controller connected to a datapath, which is together known as a **processor**
- We use the term *higher level* to describe abstraction
    - Transistors making logic gates is called **transistor-level** design
    - Creating a circuit using logic gates is called **logic-level** design
    - Designing processors using building blocks like registers and other datapath components is called **register-transfer level** design or **RTL** design
- RTL design begins with capturing desired behavior, which uses a HLSM as a formalism
## 5.2 High-Level State Machines
- Sometimes behavior can be too complex for just an equation, truth table, or FSM
- Consider we want to design a soda machine that only dispenses soda when enough money is inserted
    - We could have a coin detector that increments a counter
    - When the counter reaches a certain value, the machine dispenses a soda
    - A simple FSM could be used to model this behavior, since it cannot represent memory of multiple bits
- A **high-level state machine (HLSM)** extends FSMs with the data features to capture more complex behavior, which includes:
    - Multibit data inputs and ouputs
    - Local storage
    - Arithmetic operations like add and compare
- We also make the following assumptions:
    - Each transition is implicitly ANDed with a rising edge of a clock signal
    - := is used to denote the assignment of a value to a variable
    - == is used to denote the comparison of two values
## 5.3 RTL Design Process
- RTL design follows a two step process simliar to combinational design
    - First we capture the behavior of the system using a HLSM
    - Then we convert the HLSM into a circuit using RTL level components
- Converting an HLSM to a circuit is aided by a standard processor architecture, similar to how combinational logic used a standard architecture of a state register and combinational logic
- The standard architecture for a processor is a **datapath** and a **controller**
    - The datapath will need whatever components are necessary to perform the operations of the HLSM, like adders, comparators, registers, etc.
    - The controller will need to generate the control signals for the datapath
- The steps to RTL design looks something like this:
    - Step 1: Capture the behavior of the system using a HLSM
    - Step 2: Convert the HLSM into a circuit using RTL level components
        - Step 2A: Create a datapath using the necessary components from a library
        - Step 2B: Connect the datapath to a controller
        - Step 2C: Derive the controller's FSM
## 5.4 More RTL Design
### Additional Datapath Components for the Library
- The following are some common datapath components for RTL design:
    - Subtractor for signed and unsigned numbers
    - Multiplier for signed and unsigned numbers
    - Absolute value for signed numbers
    - Up/down counter with synchronous clear and increment/decrement
    - Register file
### RTL Design Involving Register Files or Memories
- Register files are especially useful for storing arrays
- An **array** is an ordered list of data
    - We sometimes refer to this as a local storage for an HLSM
    - We often use the notation `array_name[index]` to refer to the `index`th element of the array `array_name`
- We can map an array to a register file in the RTL design process
### RTL Design Pitfalls Involving Storage Updates
- A common mistake in making HLSMs is assuming that a clocked storage item is updated in the same state when it is written
    - The key to avoiding this mistake is to remember that a states actions **prepare** the values for the next state
    - The values dont actually get loaded into storage until the next state/rising clock edge
### RTL Design Involving a Timer
- skipping lmao
- button debouncing exists
### A Data-Dominated RTL Design Example
- Some systems have a massive datapath and a relatively simple controller
- This kind of system is called a **data-dominated** system
- In contrast, a **control-dominated** system has a complex controller and a relatively simple datapath
- Data dominated systems tend to only have a few states, and sometimes only one state
- In these few states, however, the system performs a lot of operations on the data
## 5.5 Determining Clock Frequency
- RTL design use a clock to synchronize the registers
- The clock frequency impacts how fast the system can operate
- Higher clock frequencies are generally better, but we are limited by the propagation delay of the slowest component in the system
- The longest register-to-register path is called the **critical path**
- We can choose a clock period that is longer than the critical path
- Designers tend to choose a clock period that is sightly longer than the critical path for safety
- If we want the system to be lower power, we can choose a longer clock period/lower frequency
- For large circuits, automated tools called **timing analysis** tools can be used to determine the critical path, and can also make sure setup and hold times are met
## 5.6 Behavioral-Level Design: C to Gates
- skipping lmao
## 5.7 Memory Components

### Random Access Memory (RAM)

### Bit Storange in a RAM

### Using a RAM

### Read-Only Memory (ROM)

### ROM Types

### The Blurring of the Distinction between RAM and ROM

## 5.8 Queues (FIFOs)

## 5.9 Multiple Processors

## 5.10 Hierarchy--A Key Design Concept

### Managing Complexity

### Abstraction

### Composing a Larger Component from Smaller Versions of the Same Component
