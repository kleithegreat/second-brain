# 1 - Introduction

## 1.1 Digital Systems in the World Around Us
Blah blah blah computers are small and they help us do things.

## 1.2 The World of Digital Systems

### Digital versus Analog
- A **digital** signal is discrete
    - It can only take on a finite number of values
    - Example: number of fingers you can hold up
- An **analog** signal is continuous
    - It can take on any value in a range
    - Example: temperature outside
- Computing systems typically use digital signals that are on or off
    - This is called binary
- A **digital system** is a system that takes digital inputs and makes digital outputs
- A **digital circuit** is a circuit that uses digital components to make a digital system
- A single binary digit is called a **bit**

#### Digital Circuits are the Basis for Computers
- Digital circuits let us build microprocessors
    - Microprocessors serve as the brain for general purpose computers

#### Digital Circuits are the Basis for Much More
- More and more new applications convert analog signals to digital signals
    - This can result in numerous benefits
        - Easier to store and transmit
        - Easier to process
        - Easier to combine with other digital signals
        - Lack of degradation over time
        - Compression
    - Devices such as cell phones, digital cameras, and MP3 players use digital circuits to convert analog signals to digital signals
- Digital circuits found in applications that are not computers are called **embedded systems**
- Analog to digital conversion is called **digitization**
- Digital to analog conversion is called **digital to analog conversion**

### Digital Encodings and Binary Numbers - 0s and 1s

#### Encoding analog phenomena
- A **sensor** measure analog physical phenomena and converts it to an electrical signal
- An **analog to digital converter** converts the electrical signal from sensors to a digital signal
- A **digital to analog converter** converts a digital signal to an electrical signal
- An **actuator** converts an electrical signal to an analog physical phenomena
- Sensors and actuators together are called **transducers**--devices that convert one form of energy to another

#### Encoding Digital Phenomena
- Some phenomena are inherently digital
    - Example: a switch is either on or off
- Digital phenomena can be encoded using binary numbers
    - Example: 0 = off, 1 = on
    - Example: ASCII encoding for characters

#### Encoding Numbers as Binary Numbers
- Binary works where each digit is a power of 2
- The **weight** of a digit is the power of 2 that it represents
- The **least significant bit** is the bit with the smallest weight, or the rightmost bit
- The **most significant bit** is the bit with the largest weight, or the leftmost bit

#### Converting from Binary to Decimal
- Just sum the weights of the bits that have a value of 1
- You can tell if a binary number is odd by looking at the least significant bit

#### Converting from Decimal to Binary Using the Addition Method
- Start with the largest power of 2 that is less than or equal to the number
- Populate the bits from left to right with the largest power of 2 that is less than or equal to the remaining number

#### Hexadecimal and Octal Numbers
- Hexadecimal is base 16
    - Also known as just **hex**
    - The numbers 0-9 are the same as in decimal
    - The numbers 10-15 are represented by the letters A-F
    - Hexadecimal is useful because it is easy to convert to and from binary
    - Each hex digit is 4 bits
- Octal is base 8
    - Octal numbers are also sometimes used as shorthand for binary numbers

#### Automatic Conversion from Decimal to Binary Using the Divide-by-2 Method
- Keep dividing the decimal number by 2 and the remainder at each step is the next bit
    - Example: 12 / 2 = 6 R 0, 6 / 2 = 3 R 0, 3 / 2 = 1 R 1, 1 / 2 = 0 R 1
    - So 12 in binary is 1100
- This method can be generalized to convert from decimal to any base
    - This is called **divide-by-n**, where n is the new base
    - In binary, n = 2

#### Bytes, Kilobytes, Megabytes, and More
- A **byte** is 8 bits
- *kilo* means 10<sup>3</sup>
- *mega* means 10<sup>6</sup>
- *giga* means 10<sup>9</sup>
- *tera* means 10<sup>12</sup>

## 1.3 Implementing Digital Systems: Microprocessors versus Digital Circuits
- A **microprocessor** is a digital circuit that can be programmed to perform a variety of tasks
- A **digital circuit** is a circuit that uses digital components to perform a specific task

### Software on Microprocessors: The Digital Workhorse
- A **microprocessor** is a digital circuit that can be programmed to perform a variety of tasks
- Microprocessors tend to be readily available and inexpensive

### Digital Design--When Microprocessors Aren't Good Enough
- Sometimes microprocessors are too slow
- Custom digital circuits can execute lots of instructions in parallel, where microprocessors can only execute one or a few instructions at a time
- A **circuit** is an interconnection of electric components

# 2 - Combinational Logic Design

## 2.1 Introduction
- A digital circuit whose output depends only on the present state of the inputs is called a **combinational circuit**
- Combinational circuits are a basic class of digital circuits
    - They are sometimes enough to solve a problem
    - Other times they are used as building blocks for more complex circuits

## 2.2 Switches
Electronic switches form the basis of all digital circuits

### Electronics 101
- **Voltage** is the difference in electrical potential between two points
    - Measured in volts
    - Convention says ground is 0V
    - Tells us how "eager" the charged particles are to move
    - Analogous to pressure in a water pipe
- **Current** is the measure of the flow of charged particles
    - Measured in amperes or amps
    - Analogous to the flow of water in a pipe
- **Resistance** is the measure of how much a material resists the flow of charged particles
    - Measured in ohms ($\Omega$)
    - Analogous to the diameter of a pipe
- For example, a 9V battery can power a light since the voltage difference between its terminals is 9V
- Ohms law says that $V = IR$, where $V$ is voltage, $I$ is current, and $R$ is resistance

### The Amazing Shrinking Switch
- Switches are what cause digital circuits to be either on or off

#### Relays
- Electromagnetic relays

#### Vacuum Tubes
- Originally used to amplify weak signals
- Like a light bulb, but with an extra terminal for a control signal
- No moving parts, faster than relays
- Replaced relays, and built the first digital computers

#### Discrete Transistors
- A solid state or discrete transistor is a semiconductor device that can be used to amplify or switch electronic signals
- Smaller, cheaper, faster, and more reliable than vacuum tubes

#### Integrated Circuits
- Integrated circuits revolutionized computing, since they can pack many transistors into a small space

## 2.3 The CMOS Transistor
- The most common type of IC transistor is the CMOS transistor
- The transistor has three terminals
    - The **source** is where current enters the transistor
    - The **drain** is where current leaves the transistor
    - The **gate** is where the control signal is applied

## 2.4 Boolean Logic Gates--Building Blocks for Digital Circuits
Working with just transistors is tedious, so we use logic gates instead

### Boolean Algebra and its Relation to Digital Circuits
- Boolean algebra uses variables that can only be true or false
    - Its operators like AND, OR, and NOT operate on these variables and return true or false
- AND is true if both inputs are true
- OR is true if either input is true
- NOT is true if the input is false, and vice versa

### AND, OR, and NOT Gates

### Building Simple Circuits Using Gates

## 2.5 Boolean Algebra

### Notation and Terminology

### Some Properties of Boolean Algebra

### Completing a Function

## 2.6 Representations of Boolean Functions

### Equations

### Circuits

### Truth Tables

### Converting among Boolean Function Representations

### Standard Representation and Canonical Forms

### Multiple-Output Combinaional Circuits

## 2.7 Combinational Logic Design Process

## 2.8 More Gates

### NAND & NOR

### XOR & XNOR

### Interesting Uses of these Additional Gates

### Completeness of NAND and NOR

### Number of Possible Logic Gates

## 2.9 Decoders and Muxes

### Decoders

### Multiplexers (Muxes)

## 2.10 Additional Considerations

### Nonideal Gate Behavior--Delay

### Active Low Inputs

### Demultiplexers and Encoders

### Schematic Capture and Simulation

## 2.11 Combinational Logic Optimizations and Tradeoffs

## 2.12 Combinaional Logic Description Using Hardware Description Languages

## 2.13 Summary

# 3 - Sequential Logic Design: Controllers

## 3.1 Introduction

## 3.2 Storing One Bit--Flip-Flops

### Feedback--The Basic Storage Method

### Basic SR Latch

### Level-Sensitive D Latch--A Basic Bit Store

### Edge-Triggered D Flip-Flop--A Robust Bit Store

### Clocks and Synchronous Circuits

### Basic Register--Storing Multiple Bits

## 3.3 Finite-State Machines

### Mathematical Formalism for Sequential Behavior-FSMs

### How to Capture Desired System Behavior as an FSM

## 3.4 Controller Design

### Standard Controller Architecture for Implementing an FSM as a Sequential Circuit

### Controller (Sequential Logic) Design Process

### Converting a Circuit to an FSM (Reverse Engineering)

### Common Mistakes when Capturing FSMs

### FSM and Controller Conventions

## 3.5 More on Flip-Flops and Controllers

### Non-Ideal Flip-Flop Behavior

### Flip-Flop Reset and Set Inputs

### Initial State of a Controller

### Non-Ideal Controller Behavior: Output Glitches

## 3.6 Sequential Logic Optimizations and Tradeoffs

## 3.7 Sequential Logic Description Using Hardware Description Languages

## 3.8 Product Profile--Pacemaker

## 3.9 Summary

# 4 - Datapath Components

## 4.1 Introduction

## 4.2 Registers

### Parallel-Load Register

### Shift Register

### Multifunction Registers

### Register Design Process

## 4.3 Adders

### Adder--Carry-Ripple Style

## 4.4 Comparators

### Equality (Identity) Comparator

### Magnitude Comparator--Carry-Ripple Style

## 4.5 Multiplier--Array Style

## 4.6 Subtractors and Signed Numbers

### Subtractor for Positive Numbers Only

### Representing Negative Numbers: Two's Complement Representation

### Building a Subtractor Using an Adder and Two's Complement

### Detecting Overflow

## 4.7 Arithemetic-Logic Units--ALUs

## 4.8 Shifters

### Simple Shifters

### Barrel Shifter

## 4.9 Counters and Timers

### Up-Counter

### Up/Down-Counter

### Counter with Load

### Timers

## 4.10 Register Files

## 4.11 Datapth Component Tradeoffs

## 4.12 Datapath Component Description Using Hardware Description Languages

## 4.13 Product Profile--An Ultrasound Machine

## 4.14 Summary

# 5 - Register Transfer Level (RTL) Design

## 5.1 Introduction

## 5.2 High-Level State Machines

## 5.3 RTL Design Process

### Step 2A--Creating a Datapath using Components from a Library

### Step 2B--Connecting the Datapath to a Controller

### Step 2C--Deriving the Controller's FSM

## 5.4 More RTL Design

### Additional Datapath Components for the Library

### RTL Design Involving Register Files or Memories

### RTL Design Pitfalls Involving Storage Updates

### RTL Design Involving a Timer

### A Data-Dominated RTL Design Example

## 5.5 Determining Clock Frequency

## 5.6 Behavioral-Level Design: C to Gates

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

## 5.11 RTL Design Optimization and Tradeoffs

## 5.12 RTL Design Description Using Hardware Description Languages

## 5.13 Product Profile--Cell Phone

## 5.14 Summary
