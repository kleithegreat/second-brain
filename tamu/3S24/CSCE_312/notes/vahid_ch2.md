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
- Values for variables can only be 0 or 1 for true and false
- The axioms and rules of boolean algebra lay the foundation of digital design
### AND, OR, and NOT Gates
- AND, OR, and NOT gates are called **logic gates**
- These are made of transistors - knowing how they work is not necessary but might be useful
#### NOT Gate
- Returns the inverse of the input
- Oftentimes called an **inverter** for this reason
- Represented by a triangle and a dot in a schematic
or gate and gate ez
### Building Simple Circuits Using Gates
- We can combine logic gates to represent more complex boolean expressions
- We can make AND and OR gates with multiple inputs by combining them
## 2.5 Boolean Algebra
### Notation and Terminology
- Boolean algebra has the following notation:
	- `NOT(a)` is represented by $\overline{a}$ or $a'$
	- `a OR b` is represented by $a + b$
    - `a AND b` is represented by $a * b$, $a \cdot b$, or $ab$ as long as there is no ambiguity
- Boolean algebra has the following order of operations:
    - Parentheses have the highest precedence
    - `NOT` has the next precedence
    - `AND` has the next highest precedence
    - `OR` has the lowest precedence
- Variables are usually a single letter for simplicity
### Some Properties of Boolean Algebra
- Boolean algebra has the following properties:
    - Commutativity
        - $a + b = b + a$
        - $a * b = b * a$
    - Associativity
        - $(a + b) + c = a + (b + c)$
        - $(a * b) * c = a * (b * c)$
    - Distributivity
        - $a * (b + c) = (a * b) + (a * c)$
        - $a + (b * c) = (a + b) * (a + c)$ **THIS ONE IS FUNNY**
	- Identity
        - $a + 0 = a$
        - $a * 1 = a$
    - Complement
        - $a + \overline{a} = 1$
        - $a * \overline{a} = 0$
- Using the rules of boolean algebra, complex functions and deductions from truth tables can be simplified into nicer expressions
- Boolean algebra also has the following theorems:
	- Null elements
        - $a + 0 = a$
        - $a * 1 = a$
    - Idempotence
        - $a + a = a$
        - $a * a = a$
    - Involution
        - $\overline{\overline{a}} = a$
    - De Morgan's Laws
        - $\overline{a + b} = \overline{a} * \overline{b}$
        - $\overline{a * b} = \overline{a} + \overline{b}$
### Complementing a Function
- A **complement** of a function is a function that returns the opposite value of the original function
- Simplifying a functions complement oftentimes uses De Morgan's laws and other boolean algebra rules
## 2.6 Representations of Boolean Functions
- A **boolean function** is a function that takes boolean inputs and returns a boolean output
### Equations
- Boolean functions can be represented by equations
- Example: `F(a, b) = a'b' + a'b`
- The RHS of the above equation is called an **expression**
- One advantage of equations is they can be manipulated using algebraic rules
### Circuits
- A **circuit** is an interconnection of electronic components
- Different circuits can represent the same boolean function
- Advantage of circuits is they can be implemented in hardware
### Truth Tables
- A **truth table** is a table that shows the output of a boolean function for all possible inputs
- Truth tables can also be found in other disciplines
- Boolean functions can only have *one* truth table representation, which is an advantage over equations and circuits
- One drawback is that truth tables can be very large for complex functions
### Converting among Boolean Function Representations
#### Equations to Circuits
- Just use an AND gate for multiplication and an OR gate for addition
- Use a NOT gate for complementing a variable
#### Circuits to Equations
- Start with the circuits inputs and write the output of each gate as an expression of the inputs
- The expression for the last gate in the circuit is the equation for the circuit
#### Equations to Truth Tables
- Just evaluate the equation for all possible inputs
#### Truth Tables to Equations
- Create a product term for each 1 in the output column
- Create a sum (OR) term for each product term
- Then simplify the equation if needed
#### Circuits to Truth Tables
- Convert the circuit to an equation, then convert the equation to a truth table
#### Truth Tables to Circuits
- Convert to an equation, then convert to a circuit
### Standard Representation and Canonical Forms
- A **standard representation** is a representation that is unique for a given function
- Since there can only be one truth table for a function, it is a standard representation
- Standard representations are useful for comparing functions
- A **canonical form** is a standard representation that only describes the function when it is true
- Example: In algebra, the canonical form for $\mathbb{P}_2$ is $ax^2 + bx + c$
- One common canonical form for boolean functions is the **sum-of-minterms** form
    - A **minterm** is a product term that contains all the variables in the function exactly once
    - An equation is in sum of minterms form if it is in sum of products form and each product term is a minterm
    - Example: `F(a, b, c) = a'b'c' + a'b'c + a'bc' + abc`
- Another common canonical form for boolean functions is the **product-of-maxterms** form
    - A **maxterm** is a sum term that contains all the variables in the function exactly once
    - An equation is in product of maxterms form if it is in product of sums form and each sum term is a maxterm
    - Example: `F(a, b, c) = (a + b + c)(a + b + c')(a + b' + c)(a' + b + c)`
#### Compact sum-of-minterms representation
- A more compact sum-of-minterms representation uses listing each minterm as a binary number with the variables in the order they appear in the function
- Example:
    - `a'bcde` corresponds to 01111 which is 15 in decimal
    - `abcde'` corresponds to 11110 which is 30 in decimal
    - `abcde` corresponds to 11111 which is 31 in decimal
    - So `H = a'bcde + abcde' + abcde` can be represented as H = $\sum$ m(15, 30, 31)
### Multiple-Output Combinaional Circuits
- A common approach to designing multiple-output combinational circuits is to treat each output as a separate function
- Circuite do not have to be competely separate for each output
## 2.7 Combinational Logic Design Process
- The first step in describing the desired behavior of logic is called **capturing** the behavior
- The second step is **converting** it into a circuit
- Directly converting a sum of products equation to a circuit results in a column of AND gates feeding into an OR gate
    - There could be some NOT gates in there too
    - This is known as **two-level logic** or a **two-level circuit**
### Simplifying Circuit Notations
- You can list a single input multiple times in different places in a circuit
- This reduces the amount of crossing lines in the circuit
- You can also use an **inversion bubble** to represent a NOT gate
## 2.8 More Gates
- Beyond AND, OR, and NOT gates, there are other gates that are useful
- These gates include NAND, NOR, XOR, and XNOR gates
### NAND & NOR
- A **NAND** gate, short for "not AND", is an AND gate followed by a NOT gate
    - Outputs 0 when all inputs are 1, otherwise outputs 1
- A **NOR** gate, short for "not OR", is an OR gate followed by a NOT gate
    - Outputs 1 when all inputs are 0, otherwise outputs 0
- There are no boolean algebra symbols for NAND and NOR gates, since they can just be written as AND and OR gates with a NOT gate at the end
### XOR & XNOR
- An **XOR** gate, short for "exclusive OR", outputs 1 if and only if exactly one input is 1
    - A two input XOR gate is equivalent to the function $a'b + ab'$
    - Written as $a \oplus b$ in boolean algebra
- An **XNOR** gate, short for "exclusive NOR", is simply the opposite of XOR
    - A two input XNOR gate is equivalent to the function $ab + a'b'$
    - Outputs 1 if and only if both inputs are 0 or both inputs are 1
    - Like a biconditional in logic (but this analog only applies to two input XNOR)
### Interesting Uses of these Additional Gates
#### Detecting Binary 0 Using NOR
- A NOR gate can be used to detect if a binary number is 0 since NOR is 1 when all inputs are 0
#### Detecting Equality Using XNOR
- An XNOR gate can be used to detect if two binary numbers are equal since XNOR is 1 when all inputs are 0 or all inputs are 1
- You can detect equality for multiple inputs by using an XNOR gate for each pair of inputs and then ANDing all the outputs together
#### Generating and Detecting Parity Using XOR
- XOR can generate a parity bit for a binary number
    - Recall that a parity bit wants to maintain either even or odd parity
    - XORing the data bits together will result in a 1 if the number of 1s is odd and a 0 if the number of 1s is even
- XOR can also detect if a binary number has even or odd parity
    - XORing all the bits can detect errors for even parity
    - XNOR can be used to detect errors for odd parity
### Completeness of NAND and NOR
- AND, OR, and NOT can form any boolean function, so they are called **complete**
    - OR can be made putting NOT gates on all the inputs and the output of an AND gate
    - AND can be made by putting NOT gates on all the inputs and the output of an OR gate
- NAND and NOR are also complete
    - We can make any boolean function with just NAND gates
    - Thus, NAND is called a **universal gate**
    - NOR is also a universal gate
### Number of Possible Logic Gates
- A two variable truth table has $2^2 = 4$ rows
- Thus, there are $2^{4} = 16$ possible two input gates, or two input boolean functions
$$\begin{array}{|c c|c c c c c c c c c c c c c c c c c|}
\hline
a & b & f0 & f1 & f2 & f3 & f4 & f5 & f6 & f7 & f8 & f9 & f10 & f11 & f12 & f13 & f14 & f15 \\
\hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 \\
1 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \\
\hline
 & & 0 & ab & & a & & b & a \oplus b & a + b & (a + b)' & (a \oplus b)' & b' & & a' & & (ab)' & 1 \\
\hline
\end{array}$$
- In addition to AND, OR, NAND, NOR, XOR, and XNOR, there are some other slightly commonly used functions
    - 0 just outputs 0 for all inputs
    - a just outputs a for all inputs
    - b just outputs b for all inputs
    - a' just outputs a' for all inputs
    - b' just outputs b' for all inputs
    - 1 just outputs 1 for all inputs
- The rest of the functions are more obscure but can still be useful in some situations
- A more general and common question is how many boolean function exist for a function of $N$ variables
    - This $N$ variable function will have $2^N$ rows in its truth table
    - Since each row has two possible outputs, there are $2^{2^N}$ possible boolean functions for $N$ variables
## 2.9 Decoders and Muxes
- In addition to logic gates, decoders and multiplexers are also very commonly used in digital circuits
- They themselves can be built using logic gates
### Decoders
- A **decoder** decodes an input, an n-bit binary number, by setting one of its $2^n$ outputs to 1
- Example: A two input decoder would have $2^2 = 4$ outputs: d3, d2, d1, d0
    - If the inputs i1 and i0 are 00, then d0 is 1 and the rest are 0
    - If i1 i0 is 01, then d1 is 1 and the rest are 0
    - If i1 i0 is 10, then d2 is 1 and the rest are 0
    - If i1 i0 is 11, then d3 is 1 and the rest are 0
- One and only one output of a decode will ever be 1 at a time, which corresponds to the binary number of the input
- Decoders often come with an extra input called **enable**
- When enable is 1, the decoder works as described above
- When enable is 0, all the outputs are 0 regardless of the input
- Decoders decrease the complexity of combinational logic circuits
- Decoders are useful when exactly one of many possible outputs should be on at a time for the given inputs
### Multiplexers (Muxes)
- Mux is short for multiplexer, and is another high level component
- An Mx1 **multiplexer** has M inputs and 1 output, and allows only one of the inputs to pass through to the output
- A set of additional inputs called select inputs determine which input is passed through
- Multiplexers are sometimes called **selector** because they select one of the inputs to pass through
- A mux can be thought of as a railroad switch with M rails leading into it and one rail leading out of it
- Generally, an Mx1 mux has $\log_2 M$ select inputs
- We often want to multiplex more than one bit at a time, so N-bit-wide Mx1 muxes are common
    - These are basically just N separate Mx1 muxes with the same select inputs
## 2.10 Additional Considerations
### Nonideal Gate Behavior--Delay
- Gates would ideally have instantaneous output changes, but in reality they have a delay
- However real gates have a delay, which is the time it takes for the output to change after the input changes
- The maximum time for a gates output to change is called the **delay** of the gate
- Modern gates have delays of less than 1 nanosecond
- The delay of a circuit's longest path is the maximum delay of any gate in the circuit, and is called **circuit delay**
- The longest path in a circuit is called the **critical path**
### Active Low Inputs
- Component inputs can generally be two types:
    - **Control inputs** are inputs that control the behavior of the component
        - Example: Mux select inputs
        - Example: Decoder enable inputs
    - **Data inputs** are inputs that are used in the logical computation of the component
- Some control inputs involve the notion of being **active**, which means it is carrying out its function
    - Activity can be split into **active high** and **active low**
    - An active high input is active when it is 1
    - An active low input is active when it is 0
- Sometimes input names will be modified to suggest that it is active low
    - Example: $\overline{enable}$ instead of enable
    - Example: select_L instead of select
- People use the term **assert** to mean that a control input has the active value, which helps avoid confusion due to active low inputs
### Demultiplexers and Encoders
- Demultiplexers and encoders are also two high level components
- These are used far less than decoders and muxes
#### Demultiplexer
- A **demultiplexer** is the opposite of a mux
- A 1xM demultiplexer has 1 input and M outputs
- The input is passed through to one of the outputs based on the $log_2 M$ select inputs
- All other outputs are 0
#### Encoder
- An **encoder** is the opposite of a decoder
- An $n \times log_2 n$ encoder has $n$ inputs and $log_2 n$ outputs
- Exactly one of the $n$ inputs is assumed to be 1 at any given time
- The encoder outputs a binary number corresponding to the index of the input that is 1
- A **priority encoder** handles the case where multiple inputs are 1 at the same time
    - The priority encoder outputs the index of the highest priority input that is 1
    - Priority is talking about the index of the input
### Schematic Capture and Simulation
- One method of checking a circuit is to reverse engineer the function from the circuit
    - Start with the circuit, and convert to equations, then to a truth table
    - If the truth table matches the desired truth table, then the circuit is correct
- However, if people start with equations instead of truth tables, it can be hard to check the circuit
> Canonical forms can be massive for large functions since they describe truth tables line by line, so it is not practical to use them to check circuits
- Thus, people often use **simulation** to check circuits, with the help of a computer
- A **schematic capture tool** helps people draw circuits on computers and test them
- Once a circuit is drawn, the schematic capture tool can simulate the circuit
- An inputs **waveform** is a graph of the input over time
- Waveforms can be used to check against test cases
- We can also use checking statements called **assertions** (kind of like the python keyword) to check the circuit
## 2.11 Combinational Logic Optimizations and Tradeoffs
redirects to section 6.2
## 2.12 Combinational Logic Description Using Hardware Description Languages
- Hardware description languages (HDLs) are a textual language to describe digital circuits
redirects to section 9.2