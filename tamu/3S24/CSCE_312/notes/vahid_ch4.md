# 4 - Datapath Components
## 4.1 Introduction
- Controllers are good for systems with *control* inputs
- This chapter focuses on building blocks for systems with *data* inputs
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
- Previously, the most basic type of register used was just a set of flip-flops loaded on every clock cycle
- This was useful as the state register since it was loaded with the next state on every clock cycle
- However, most other uses of registers need some way to control whether the register is loaded or not on a particular clock cycle
- Controlling whether a register is loaded or not can be done by adding a 2x1 multiplexer in from of each flip-flop in a basic register
    - When the `load` control input is 0 and the clock signal rises, the flip-flop just stores its own `Q` output
    - When the `load` control input is 1 and the clock signal rises, the flip-flop stores the value of the given input
- A register with a load line that control whether the register is loaded with external inputs,with those inputs loaded in parallel, is called a **parallel-load register**
    - This means there is one load line for the entire register
- A **block symbol** is just a representation of an abstract component that does not show its implementation, but just its inputs and outputs
> Why the name "register"?
> Historically, a "register" was a sign or chalkboard that people used to temporarily write cash transactions, and the use it later for bookkeeping. Since a register can store data temporarily, the name "register" was used for the digital component that can store data temporarily.
#### Buses
- Data tends to consits of numerous bits
- A group of N wires in a circuits that transports a data item is called a **data bus** or just a **bus**
    - N is the bus width
- Drawing each bus wise can be very cluttered, so a simpler version is just one thich line with a slanted line through it and the bus width written next to it
### Shift Register
- Sometimes people want to shift a registers contents to the left or right
- **Shifting** means moving each stored bit one position to the right or left
    - If a 4-bit register has originally stores `1101`, shifting right would result in `0110`
    - The rightmost bit is lost, and a 0 is shifted in from the left
- To build a register capable of shifting to the right, the Q outputs of the flip-flops are connected to the D inputs of the next flip-flop to the right
- A register capable of shifting its contents is called a **shift register**
    - It has two control inputs: `shr` and `shr_in`
        - `shr = 1` causes a right shift on a rising clock edge
        - `shr = 0` maintains the present state
        - `shr_in` is the input to the leftmost flip-flop
- A **rotate register** is a slight variation of a shift register
    - Instead of losing the rightmost bit, it is shifted to the leftmost position
    - The design is slightly different where the rightmost flip-flop output is connected to the leftmost mux input
### Multifunction Registers
- Some registers perform a variety of *operations*, also called **functions**
    - These are like load, shift right, shift left, rotate right, rotate left, etc.
    - The desired operation is achieved by setting the control inputs to the appropriate values
#### Register with Parallel Load and Shift Right
- This is a popular combination of operators on a register
    - It has three control inputs: `shr_in`, `s1`, and `s0`
    - `shr_in` is the input to the leftmost flip-flop
    - The design uses a 4x1 instead of a 2x1 mux since each flip-flop can receive its next bit from the input, the previous flip-flop, or its current value
- It has the following **operation table**
$$
\begin{array}{c c|c}
\hline
\text{s1} & \text{s0} & \text{Operation} \\
\hline
0 & 0 & \text{Maintain present value} \\
0 & 1 & \text{Parallel load} \\
1 & 0 & \text{Shift right} \\
1 & 1 & \text{(Unused)}
\end{array}
$$
- Quite obviously, `s1` and `s0` are the control inputs for the parallel 4x1 muxes
#### Register with Parallel Load, Shift Left, and Shift Right
- Adding a shift left operation to the above register is straightforward
    - Add a `shl_in` control input to the rightmost flip-flop
    - Connect the Q outputs of the flip-flops to one of the mux inputs for the next flip-flop to the left
- It has the same operation table, except the last row is now used for the shift left operation
#### Load/Shift Register with Separate Control Inputs for Each Operation
- Registers typically dont have control inputs that encode operations in the least number of bits like the above examples
- Instead, each operation has its own control input
- For example, a register with parallel load, shift left, and shift right might have the following operation table:
$$
\begin{array}{c c c|c}
\hline
\text{ls} & \text{shr} & \text{shl} & \text{Operation} \\
\hline
0 & 0 & 0 & \text{Maintain present value} \\
0 & 0 & 1 & \text{Shift left} \\
0 & 1 & 0 & \text{Shift right} \\
0 & 1 & 1 & \text{Shift right - shr has priority over shl} \\
1 & 0 & 0 & \text{Parallel load} \\
1 & 0 & 1 & \text{Parallel load - ld has priority} \\
1 & 1 & 0 & \text{Parallel load - ld has priority} \\
1 & 1 & 1 & \text{Parallel load - ld has priority} \\
\end{array}
$$
- The four possible operations need at least 2 bits, and this table uses 3 bits
- The register designer must decide how the register responds when more than one control input is 1
- We can design combinational logic for the register to respond to the control inputs using the operation table
### Register Design Process
The general process for designing a register is as follows:
1. **Determine max size**: Count the number of operations (dont forget maintain present) and add in front of each flip-flop a mux with at least that many inputs
2. **Create mux operation table**: Create an operation table defining the operation for each combination of control inputs
3. **Connect mux inputs**: Connect the corresponding mux data input to the appropriate external input or flip-flop output to achieve the desired operation
4. **Map control lines**: Create a truth table that maps external control lines to the internal mux select lines, with appropriate priorities, and then implement with combinational logic
## 4.3 Adders
- Adding two binary numbers is perhaps the most common operation performed on data in a digital system
- An **N-bit adder** is a combinational component that adds two N-bit data inputs A and B resulting in an N-bit sum output S and a carry output C
    - For example, `1111 + 0001` would result in a carry of 1 and a sum of `0000`
    - N is the **width** of the adder
- Designing fast and size efficient adders is a major challenge in digital system design
- Implementing adders using only basic gates is not efficient
    - Building an N-bit adder is not practical when N is much larger than 8
    - The rows of a truth table for an N-bit adder are 2^N rows long
    - A 16-bit adder would have over four billion rows
### Adder--Carry-Ripple Style
- This method mimics how people add numbers instead of using standard combinational logic
- In each column three bits are added: A, B, and the carry from the previous column
- The first column is an exception, as there is no carry from the previous column
- We can make a combinational component to perform the addition of a single column and duplicate it for each column
- This style of adder is sufficient for large N, like the 32-bit adder
#### Half Adder
- A **half adder** is a combinational component that adds two 1-bit inputs `a` and `b`, resulting in a 1-bit sum output `s` and a carry output `co`
- Truth table for a half adder:
$$
\begin{array}{c c|c c}
\hline
a & b & co & s \\
\hline
0 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 \\
1 & 1 & 1 & 0 \\
\end{array}
$$
- The equations for the half adder are: 
    - $co = ab$
    - $s = a \oplus b$
#### Full Adder
- A **full adder** is a combinational component that adds three 1-bit inputs `a`, `b`, and `ci`, resulting in a 1-bit sum output `s` and a carry output `co`
- Truth table for a full adder:
$$
\begin{array}{c c c|c c}
\hline
a & b & ci & co & s \\
\hline
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 0 & 1 \\
0 & 1 & 1 & 1 & 0 \\
1 & 0 & 0 & 0 & 1 \\
1 & 0 & 1 & 1 & 0 \\
1 & 1 & 0 & 1 & 0 \\
1 & 1 & 1 & 1 & 1 \\
\end{array}
$$
- The equations for the full adder are:
    - $co = bc + ac + ab$
    - $s = a \oplus b \oplus ci$
#### 4-Bit Carry-Ripple Adder
- Three full adders and one half adder can be used to create a **4-bit carry-ripple adder**
    - The half adder is used to add the least significant bit
    - The full adders are used to add the remaining bit
- If we use four full adders, we can create a 4-bit carry-ripple adder with a carry-in as well
- It is important to note that the carry bits need time to ripple through all the adders.
    - Until it ripples through, the sum is not correct
    - The intermediate values are called **spurious values**
- The **delay** of a component is the time required for the output to be the stable correct value after the input changes
- The delay of a 4 bit carry ripple adder is the sum of the delays of the full adders and the half adder or just the four full adders
- People often confuse N bit adders with full adders
    - Full adders take three 1 bit inputs and produce a 1 bit sum and a carry
    - N bit adders take two N bit inputs and produce an N bit sum and a carry
    - A full adder is only one column of an N bit adder
#### Incrementer
- Sometimes we just want to add 1 to a number
- A **constant** is a number that doesnt change in a circuit
- A common component is an **incrementer** that adds 1 to a number
    - This is just a 4-bit carry-ripple adder with one input being 1
    - The carry-in is 1
    - The other input is the number to be incremented
    - The output is the incremented number
## 4.4 Comparators
- Oftentime we want to compare two binary numbers and see if theyre equal or if one is greater than the other
### Equality (Identity) Comparator
- An **N-bit equality comparator** (sometimes called an *identity comparator*) is a combinational component that compares two N-bit inputs `A` and `B`, and set an output control bit `eq` to 1 if `A` and `B` are equal, and 0 otherwise
- We can just XNOR each pair of bits and then AND all the results
### Magnitude Comparator--Carry-Ripple Style
- An **N-bit magnitude comparator** is a combinational component that compares two N-bit data inputs `A` and `B` representing binary numbers, and sets three output control bits `AgtB`, `AeqB`, and `AltB` to 1 if `A` is greater than, equal to, or less than `B`, respectively
- This is another case where starting with a truth table is far too cumbersome
- Instead we should consider how humans compare numbers
    - We start by looking at the most significant bit
    - If the most significant bit of `A` is 1 and the most significant bit of `B` is 0, then `A` is greater than `B`
    - If the most significant bits are the same, we move to the next most significant bit
    - If all the bits are the same, then the numbers are equal
- A magnitude comparator can be broken into blocks that compare each pair of bits
    - Each block takes inputs `a`, `b`, `in_gt`, `in_eq`, and `in_lt` and produces outputs `out_gt`, `out_eq`, and `out_lt`
    - The `in_gt`, `in_eq`, and `in_lt` inputs are the carry-in from the previous block
        - If the previous block determined that `A` is greater than `B`, then `in_gt` is 1
        - Same for `in_eq` and `in_lt`
- The output equations are as follows:
    - `out_gt = in_gt + (in_eq * a * b')`
    - `out_lt = in_lt + (in_eq * a' * b)`
    - `out_eq = in_eq * (a XNOR b)`
- Since this way has ripples through stages, it is often called a **carry-ripple style** implementation, even though wer arent necessarily "carrying" anything
- We can extend this to an N-bit magnitude comparator by using N of these blocks
## 4.5 Multiplier--Array Style
- An **NxN multiplier** is a combinational component that multiplies two N-bit input binary numbers A and B, resulting in an (N+N)-bit output binary
- Once again, a truth table is impractical, and we should consider how humans multiply numbers
    - Each partial product is obtained by ANDing the present multiplier bit with the ENTIRE multiplicand
    - A is the multiplicand and B is the multiplier
    - Each partial product starts at the same position as the multiplier bit
    - The total product is the sum of all the partial products in their respective positions
## 4.6 Subtractors and Signed Numbers
- An N-bit **subtractor** is a combinational component that subtracts two N-bit data inputs `A` and `B` (binary numbers) and produces an N-bit result `S` equal to `A - B`
### Subtractor for Positive Numbers Only
- For now lets assume only positive inputs
- Results are only positive when the minuend is greater than or equal to the subtrahend
- Using truth tables here is once again retarded
- We can split an N-bit subtractor into N full subtractors
    - Each full subtractor takes three inputs: `a`, `b`, and `wi`
        - `a` is the minuend bit
        - `b` is the subtrahend bit
        - `wi` is the borrow-in by the previous bit
    - The full subtractor produces two outputs: `s` and `wo`
        - `s` is the difference bit
        - `wo` is the borrow-out to the next bit
- The output equations are as follows:
    sike lmao left as exercise for reader
### Representing Negative Numbers: Two's Complement Representation
- It is quite necessary to represent negative numbers in a computer
- The **signed-magnitude representation** is an obvious but not effective method to represent negative numbers
    - The most significant bit is the sign bit, 0 for positive and 1 for negative
    - The remaining bits are the magnitude of the number
    - This is easy for humans to understand, but makes digital design harder than it needs to be
- The most common method of representing negative numbers and perfoming subtraction actually uses a trick that allows us to use an *adder* to perform subtraction
- The key to this is known as what are called **complements**
    - The complement of a number is just the number that when added to the original number results in the next power of the base
    - For example, the complement of 5 in base 10 is 5, as 5 + 5 = 10
- We can use complements to do subtraction by replacing the subtrahend with its complement, and then adding the minuend and the complemented subtrahend, and then throwing away the carry
- For example: 7 - 4 -> 7 + 6 = 13 -> 13 - 10 = 3
- In binary the complement is just inverting all the bits and adding 1
    - This is called the **two's complement**
    - For example, say we want to find the complement of 001
        - We want the number that when added to 001 results in 1000
        - Inverting the bits gives 110
        - Adding 1 gives 111
- Another type of complement is the **one's complement**
    - This is just inverting all the bits
    - This is not used much
- Two's complement leads to a simple method for representing negative numbers
    - Negative numbers are just the twos complement of the positive number
    - Since a - b = a + (-b)
    - Twos complement of 0 is 0
    - For example, 0111 is 7, and 1001 is -7
    - This is slightly asymmetric, as the range of positive numbers is one less than the range of negative numbers
- Note that all the negative numbers have a 1 in the most significant bit
    - The most significant bit is often called the **sign bit**, with 0 for positive and 1 for negative
    - An N-bit binary number only representing positive numbers is called an **unsigned number**
        - Unsigned numbers have a range of 0 to $2^N - 1$
        - For example, an 8-bit unsigned number has a range of 0 to 255
    - Conversely, an N-bit binary number representing both positive and negative numbers is called a **signed number**
        - Signed numbers have a range of $-2^{N-1}$ to $2^{N-1} - 1$
        - For example, an 8-bit signed number has a range of -128 to 127
- You can't tell if a number is unsigned or signed just by looking at it
    - For example, 1001 could be 9 or -7
    - The context of the number is important
- Finding the magnitude of a two's complement negative number is just taking the two's complement again
### Building a Subtractor Using an Adder and Two's Complement
- We can implement a subtractor using the fact that adding a numbers two's complement is the same as subtracting the number
- Adding a NOT gate to the second input of an adder is the same as adding the two's complement
#### Adder/Subtractor
- An adder/subtractor component can be made by multiplexing the second input of the adder
    - When the control input `sub` is 0, the adder adds the two inputs
    - When the control input `sub` is 1, the adder adds the first input and the two's complement of the second input, which is the same as subtracting the second input from the first input
- You can also use two XOR gates instead of a NOT and a mux for the second input
### Detecting Overflow
- Having an arithmetic result wider than the fixed bitwidth is called **overflow**
- For example, adding `1111 + 0001` would result in `10000`, which is 5 bits, 1 more than the 4 bit inputs
- Overflow can be easily detected by looking at the carry-out bit of the adder
- A final carry-out of 1 means overflow
- Detecting overflow for two's complement numbers is more complicated
    - For example, adding `0111 + 0001` would result in `1000`, which is -8, not 8
    - The problem here is adding two negative numbers and getting a 0 sign bit is overflow
- For negative numbers, overflow can be detected if the most significant bit of the result is 0
- Adding a positive and negative number can never result in overflow
- Detecting overflow in twos complement involves looking at the most significant bit of the inputs and the most significant bit of the result
    - If the most significant bits of the inputs are the same, and the most significant bit of the result is different, then overflow has occurred
    - Say the sign bit of one input is `a` and the sign bit of the other input is `b`, and the sign bit of the result is `r`, overflow happens when `abr' +a'b'r = 1`
- This equation is quite simple, but comparing the carry out to the sign bit is more efficient
## 4.7 Arithmetic-Logic Units--ALUs
- An **N-bit arithmetic-logic unit (ALU)** is a combinational component that performs a variety of arithmetic and logic operations on two N-bit data inputs and generally produces an N-bit result
    - Arithmetic operations include addition and subtraction
    - Logic operations include AND, OR, and XOR, etc
- Control inputs to the ALU indicate which operation to perform
> A **bitwise operation** applies an operation to each pair of bits in two numbers
- We want ALUs because implementing all the operations we want with separate components would be inefficient, and we don't necesarily need all operations in parallel
- Let's start with an adder as the base internal ALU component
    - The inputs to the internal adder are `IA` and `IB` for internal A and B to avoid confusion with the external inputs
- Right now the ALU consists of the adder and some logic in front of the adders inputs called an arithmetic/logic extender, or *AL-extender*
    - The AL-extender's purpose is to set the adders inputs based on the ALU control inputs `x`, `y`, and `z`
    - The inputs are set such that the adders output corresponds to the desired operation
    - The AL-extender consists of identical components labeled `abext` for each bit, one for each pair of bits `ai` and `bi` (external A and B)
    - Also has a `cinext` block for the carry-in
- Thus, we need to design the AL-extender, which consists of the `abext` and `cinext` blocks
    - Say we have the following operation assignment for the control inputs:
    - When `xyz = 000`:
        - We want addition, so `S = A + B`
        - Therefore `IA = A`, `IB = B`, and `cin = 0`
    - When `xyz = 001`:
        - We want subtraction, so `S = A - B`
        - Therefore `IA = A`, `IB = B'`, and `cin = 1`
    - When `xyz = 010`:
        - We want to increment `A`, so `S = A + 1`
        - Therefore `IA = A`, `IB = 0`, and `cin = 1`
    - When `xyz = 011`:
        - We want to pass `A` through, so `S = A`
        - Therefore `IA = A`, `IB = 0`, and `cin = 0`
- For logical operations, we can compute the desired logical operation in the `abext` component and pass it through the adder
- completion of abext and cinext left as exercise for reader lmfaooooooooooo
## 4.8 Shifters
- Shifting is useful for multiplying or dividing unsigned binary numbers by a factor of 2
    - This is similar to how in base 10 we can multiply or divide by 10 by adding or removing a 0
    - Likewise in binary, we can multiply or divide by 2 by shifting left or right
    - For example, shift left one bit is the same as multiplying by 2
    - Shifting left twice is the same as multiplying by 4
    - Shifting right one bit is the same as dividing by 2
- Although we have shift registers, sometimes we want to shift a number by a variable amount and in either direction
### Simple Shifters
- An **N-bit shifter** is a combinational component that shifts an N-bit data input by a fixed amount to generate an N-bit result
- The simplest shift one position in one direction
    - This would just connect each input to the next output, and an additional input `sh` for the bit to be shifted in
- A more capable shifter can shift one position left or pass the input through
    - This would require a 2x1 mux for each bit
- A more capable shifter can shift one position left or right
    - Takes inputs `inR`, `inL`, `shL`, and `shR` for left bit input, right bit input, left shift control, and right shift control
> Remember that shifting is same as multiplication/division for ONLY UNSIGNED numbers
#### Strength Reduction
- Implementing a multiplier that multiplies by a number other than two uses more transistors
- Thus we often use a series of shifts and adds that compute the same result, since shifters and adders are quite fast
- Replacing costly operations by a series of less constly operations is called **strength reduction**
    - This is a common optimization technique in digital design and software compilation
    - For example, 5 times a number can be computed by shifting left 2 and adding the original number
#### Choosing Bitwidths
- Operating on N-bit numbers requires some attention paid to the bitwidths of the components
- Determining the minimum width of all internal wires and components for expected inputs is beyond the scope of this course
- A few guidelines:
    - We can determine the maximum data value that would occur during computation and use that to determine the bitwidth of the components
    - Do division as late as possible to avoid rounding errors
### Barrel Shifter
- An **N-bit barrel shifter** is a general purpose N-bit shifter that can shift any number of positions
- For simplicity, consider only left shifts for now
    - An 8-bit barrel shifter can shift left from 0-7 positions
    - Thus we need 3 control inputs to specify the shift amount
- A barrel shifter is useful to replace several shift components
- Building a barrel shifter with one shifter per shift length and direction is retarded
- A more elegant design uses 3 cascaded simple shifters
    - The first simple shifter can shift left 4 or no positions
    - The second simple shifter can shift left 2 or no positions
    - The third simple shifter can shift left 1 or no positions
    - The shift inputs `x`, `y`, and `z` correspond to each of the three simple shifters
        - `x` is shift left 4
        - `y` is shift left 2
        - `z` is shift left 1
    - We can shift arbitrary amounts by adding the shift amounts
- Although this design can only shift left, it can easily be extended to shift either way
    - Replace the shifters with shifters that can shift either way
    - Add a control input to specify the direction
- We can also easily make the barrel shifter support rotates by changing the internal shifters to rotators that can either shift or rotate, as well as a control input to specify the operation
## 4.9 Counters and Timers
- An **N-bit counter** is a *sequential* component that can increment or decrement its own value on each clock cycle when a count enable control input is on
    - **Increment** means to add 1, and **decrement** means to subtract 1
    - A counter than can increment is called an **up-counter**
    - A counter than can decrement is called a **down-counter**
- A counter *wraps around* when it reaches its maximum or minimum value
    - For example, a 4-bit up counter would go from `1111` to `0000` on the next clock cycle
    - A 4-bit down counter would go from `0000` to `1111` on the next clock cycle
    - This is also known as *rolling over*
- A control output on the counter often called the **terminal count** or `tc` turns on when the counter reaches its maximum or minimum value (before it rolls over)
- A typical up-counter has a `clr` control input that resets the counter to 0, a `cnt` input that increments the counter, the `tc` output, and the N-bit count output
### Up-Counter
- An up counter can be implemented using a parallel load register and an incrementor
- We can feed the N-bit output of the register into an N-bit AND gate for the `tc` output
    - If decrementer, we would use NOR instead of AND to detect roll over
    - This is since NOR is true when all inputs are 0
### Up/Down-Counter
- An up/down counter requires an additional control input `dir` to specify the count direction
    - `dir = 0` means count up
    - `dir = 1` means count down
- Here we would have the register output fed to both an adder and subtractor
    - The outputs of these would be fed to a 2x1 mux
    - The control input of the mux would be `dir`
    - The output of the mux would be fed back to the register input
- The `tc` output would be determined by either a NOR gate or an AND gate
    - Likewise, their outputs are fed into a 2x1 mux with `dir` as the control input
### Counter with Load
- Counters often come with the ability to start with some particular value
- This is done by adding a `ld` control input
    - This is fed into both the register load input and the mux select input
    - The mux selectes between the external input and the register output
#### Using a Counter to Measure Time
- We can use an up coutner to measure the time between events
- Initially the counter is cleared to 0
- The `cnt` input is turned on when the event occurs, and set to 0 when the event ends
- The final value of the counter is the number of clock cycles between the events
- We can use the period of the clock to convert the number of clock cycles to time
### Timers
- A **timer** is as sequential component that can be programmed to repeatedly generate a pulse at a specified time interval
- This is sometimes called a *programmable interval timer*
- Timers have a base time unit such as 1 microsecond
- We can load a binary number representing the desired multiplicative factor of the base time unit
- A timers *width* is the bit width of the number that can be loaded to specify the time interval
- A timer can be designed using a parallel-load down counter and a register
    - The down counter uses an oscillator as the clock input
## 4.10 Register Files
