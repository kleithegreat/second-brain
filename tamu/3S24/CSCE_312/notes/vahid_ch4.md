# 4 - Datapath Components
## 4.1 Introduction
- Controllers are good for systems with *control* inputs
- This chapter focuses on building blocks for sstems with *data* inputs
- The two differ as follows:
    - **Control**: A control input is usually one bit and represents some particular event or command that influences or directs the system's mode of operation
    - **Data**: A data input is usually multiple bits that represent a single piece of information
        - Example: A 32-bit number for a temperature sensor
        - Example: An 8-bit ASCII character
    - Analogy: A TV remote has control inputs, and the video cable is a data input
    - Analogy: A handheld calculator has the numbers as data inputs and the operations as control inputs
- Not all inputs are just control or just data--some have features of both
- Controllers aren't sufficient for working with data inputs
- **Datapath components** are building blocks for systems with data inputs
- A circuit of datapath components is called a **datapath**
- Datapaths can be quite complex, so using components at a high enough level of abstraction is important
    - For example, building a bicycle would require tires and a frame, but not the individual atoms that make up the tires and frame
    - Likewise, logic gates are too low level for datapath components
## 4.2 Registers
- An **N-bit register** is a sequential component that can store N bits.
    - N is called the **register width**
    - Typical register widths are 8, 16, and 32 bits
    - Though register widths can be as small as 1 or arbitrarily large
- Bits in a register commonly represent data
- Storing data in a register is commonly called **loading**
    - *Writing* and *storing* are also used
- **Reading** a registers contents is the process of using the bits in the register
    - This is not a synchronous operation
- Registers come in many styles and they are the most fundamental datapath component
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

## 4.7 Arithmetic-Logic Units--ALUs

## 4.8 Shifters

### Simple Shifters

### Barrel Shifter

## 4.9 Counters and Timers

### Up-Counter

### Up/Down-Counter

### Counter with Load

### Timers

## 4.10 Register Files

## 4.11 Datapath Component Tradeoffs

## 4.12 Datapath Component Description Using Hardware Description Languages