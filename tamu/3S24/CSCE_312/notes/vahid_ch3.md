# 3 - Sequential Logic Design: Controllers
## 3.1 Introduction
- Combinational circuits have **no memory**
- This means they cannot store bits and retain them for later use
- A **sequential circuit** is a circuit whose output depends on not only the inputs but also the current **state**
	- State is all the bits currently stored in the circuit
	- State depends on the past *sequence* of the circuits inputs
- One simple example of a sequential system is a lamp that toggles on and off with the press of a button
- Most digital systems involve sequential circuits
	- Calculators store numbers, digital cameras store pictures, etc.
- Sequential circuits use building blocks called flip-flops and registers, both of which can store bits.
## 3.2 Storing One Bit--Flip-Flops
- Storing a bit means retaining a 0 or a 1
- Consider a flight attendant call system with a call and a reset button
	- The call button turns on the light, and the reset turns it off
	- Since we're using buttons, we need memory to store the on signal until turned off
- Some circuits that can store a bit:
	- Basic SR latch
	- Level-sensitive SR latch
	- Level-sensitive D latch
	- Edge-triggered D flip-flop
		- This can be used to create a block capable of storing multiple bits, called a *register*
		- Registers will serve as the main bit storage block for the rest of this book
		- People today rarely use bit storage other than D flip flops
### Feedback--The Basic Storage Method
- The basic method for storage is **feedback**
- You can think of this as a microphone pointed to a speaker that plays what the mic picks up
- Suppose we have an OR gate with the output feeding into one of its inputs
	- When we set one of the inputs to 1, the output will become 1 and then will remain 1
	- Here there is no way to reset the output to 0
- An **event** is any change on a bit signal from 0 to 1 or 1 to 0
### Basic SR Latch
- The **basic SR latch** combines two cross-couples NOR gates
    - One NOR gate has S and Q as inputs and the other has R and the output of the first gate as inputs (this second gate outputs Q)
	- It has an input Set (S) and an input Reset (R) hence SR
    - Setting S to 1 causes the output Q to be 1
    - Setting R to 1 causes the output Q to be 0
    - Setting both S and R to 0 causes the output to remain the same
- The basic SR latch works since NOR requires both inputs to be 0 for the output to be 1
    - S starts as 0 so the output of the first NOR gate is 1
    - This 1 is fed into the second NOR gate, so the output is 0
    - When S is set to 1, the output of the first NOR gate is 0, so the output of the second NOR gate (Q) is 1
- Values are **stable** when they won't change as long as no external inputs change
#### Problem when SR=11 in a Basic SR Latch
- Undefined behavior results when both S and R are 1
- The latch might store 1, or 0, or oscillate between 1 and 0
- In real circuits, delays in the two gates would be slightly different
    - This causes one of the gates to oscillate slightly ahead of the other
    - This delay continues until it gets far enough to enter a stable state
    - Whether the stable state is 1 or 0 is unknown beforehand
- A situation where the final output of a sequential circuit depends on the dlays of gates and wires is a **race condition**
- When using an SR latch, we must ensure that S and R are never 1 at the same time
- There should be an external circuit that ensures this
- However even with an external circuit, delays in the gates can still cause SR=11 to occur
- A temporary unintended signal value caused by circuit delays is called a **glitch**
### Level-Sensitive SR Latch
- A **level-sensitive SR latch** is a basic SR latch with two AND gates added
    - There are three inputs: S, R, and an **enable** input C
    - S and R feed in to two AND gates, and C feeds into both AND gates
    - The outputs of the two AND gates feed into the inputs of the basic SR latch
- The enable input ensures that the latch only stores the value of S when C is 1
- This SR latch with an enable input is called a **level-sensitive SR latch**
    - This is because it is only sensitive to S and R when the enable input is 1
    - This is also called a **transparent latch**, since the SR latch is transparent to the S and R inputs when the enable input is 1
    - This is also sometimes called a **gated SR latch**
- Since the top NOR gate outputs the opposite of Q, we can easily include a Q' output
### Level-Sensitive D Latch--A Basic Bit Store
- One persisting problem of the level-sensitive SR latch is that SR=11 is still undefined when the enable input is 1
- The **level-sensitive D latch** (or transparent D latch or gated D latch) has a single input D and an enable input C
    - The D input is fed into one AND gate in the level-sensitive SR latch
    - The inverse of D is fed into the other AND gate
    - C remains the same
- The not gate on the D input ensures that S and R are never 1 at the same time
> The level-sensitive D latch stores the value of D when C (enable) is 1, and remembers it when C is 0
> It only resets when D is 0 and C is 1
### Edge-Triggered D Flip-Flop--A Robust Bit Store
- The D latch still has a problem with undefined behavior
    - Suppose we have a bunch of D latches chained with the output of one feeding into the input of the next
    - Say these D latches also all share the same enable input
    - The value of the first D latch will be stored in the second D latch, and so on
    - How many D latches will store the value of the first D latch is unknown due to timing
- Consider pulsing enable signals
    - A **pulse** is a change from 0 to 1 back to 0
    - A pulsing enable signal is called a **clock** signal
- A solution would be to store the input at D only when the clock rises from 0 to 1
- This is called an **edge-triggered D flip-flop**
    - The edge is the transition from 0 to 1
    - The edge-triggered D flip-flop stores the value of D only on the rising edge of the clock
#### Edge-Triggered D Flip-Flop Using a Master-Servant Design
- We can use two D flip flops to create an edge-triggered D flip-flop
    - The first D flip-flop is called the **master**
    - This stores the value of D when the clock is 0 due to the not gate on the clock input (the clock is inverted only for the master)
    - The second D flip-flop is called the **servant**
    - The servant store the value of the master only when the clock changes from 0 to 1
- This can be thought of how a gun only fires when the trigger is pulled, but you can load or unload the gun at any time
- The problem of chaining D latches is solved since only one D flip-flop stores the value of D per clock cycle
- There are many other designs that exist for edge-triggered D flip-flops other than master servant
- The implementation usually doesn't matter as long as the edge-triggered D flip-flop works as expected
    - These work on the basis of the **positive** or **rising** edge of the clock
    - There are also **negative** or **falling** edge-triggered D flip-flops
#### Latches vs Flip-Flops:
- This textbook uses the following definition:
    - Latches are level-sensitive
    - Flip-flops are edge-triggered
- Thus saying edge triggered flip-flop is redundant
### Clocks and Synchronous Circuits
- Most sequential circuits involving flip-flops use a clock signal that oscillates at a regular rate
    - The oscillating enable signal is called a **clock signal**
- A circuit whose storage elements can only change when a clock signal is active is known as a **synchronous circuit** (seqwential is implied)
- Likewise a circuit that does not use a clock signal is known as an **asynchronous circuit**
- An **oscillator** is a digital component that generates a clock signal
    - Oscillators have no inputs, and just output a clock signal
    - The clock signals **period** is the time between two consecutive rising edges
    - A **clock cycle** is just one segement of time between when the clock becomes 1 and when it becomes 0 again
        - The clock cycles includes equal time for the clock to be 1 and 0
    - The clock **frequency** is the number of clock cycles per second
### Basic Register--Storing Multiple Bits
- A **register** is a seqeuential component that can store multiple bits
- A basic register can be built with multiple D flip-flops sharing a common clock signal
    - The register stores the info in all the inputs when the clock is 1
    - This type of register is sometimes just called an n-bit D flip-flop
## 3.3 Finite-State Machines
- Registers store bits in digital circuits
- Stored bits means the circuit has **memory** which results in sequential circuits
- A circuits **state** is the value of all the bits stored in the circuit
- State can be used to design circuits that have a specific behavior over time
- We must have a way to *capture* desired time-ordered behavior, and a technique to *convert* this behavior into a circuit
### Mathematical Formalism for Sequential Behavior-FSMs
- Boolean equations are not sufficient for sequential behavior
- Finite-state machines are a mathematical formalism for capturing sequential behavior
- The main part of an FSM is a set of state representing every possible "situation" the system can be in
- The system can only be in one state at a time, which is called the current or present state
- A **state diagram** is a graph where the nodes are the states and the edges are the transitions between states
- FSMs can only change state once per clock cycle
- We can label transitions with boolean equations that describe the conditions for the transition to occur
- FSMs are comprised of the following:
    - A set of states
    - A set of inputs and outputs
    - An **initial state** - the state the FSM starts in
    - A set of transitions
    - A description of the output for each state
        - Assigning an output in an FSM is known as an **action**
- We can "execute" an FSM by following the transitions based on the inputs, similar to mentally evaluating a boolean equation
#### Simplifying FSM Notation: Making the Rising Clock Implicit
- This book only considers the design of synchronous circuits using edge-triggered flip-flops
- A lot of textbooks and designers use the convention where every FSM transition is *implicitly ANDed* with a rising clock edge `(clk^)`
- For example, a transition labeled `a'` actually means `a' * (clk^)`
### How to Capture Desired System Behavior as an FSM
- The following method may help with creating an FSM that captures desired system behavior:
    - List the states
    - Create the transitions
    - Refine the FSM - execute the FSM and make sure it behaves as expected
- Capturing behavior as an FSM may require some creativity and trial and error
## 3.4 Controller Design
### Standard Controller Architecture for Implementing an FSM as a Sequential Circuit
- This is concerned with converting an FSM into a sequential circuit
- A sequential circuit that implements an FSM is called a **controller**
- Doing this is quite straightforward when a standard pattern or *architecture* is used for the controller
- A standard controller architecture for an FSM consists of a register and combinational logic
- The controller's register is called the **state register**
	- Each state is represented with a unique bit encoding
    - For example, a 2-bit state register can represent 4 states
- The combinational logic computes the output values for the present state and the next state based on the current state and input
### Controller (Sequential Logic) Design Process
- As usual, the first step to designing a controller is to *capture* the desired behavior
- The second step is to *convert* the behavior into a circuit
- Since boolean equations aren't sufficient for sequential behavior, we use FSMs to capture the behavior
#### Controller design process step by step:
1. Capture the desired behavior as an FSM
    - Attempt to create an FSM that captures the desired behavior, and iterate as needed
2. Convert the FSM to a circuit
    1. Set up the architecture
        - Use a state register of appropriate width and combinational logic
        - The logic's inputs are the state register bits and the FSM inputs
        - The logic's outputs are the next state bits and FSM outputs
    2. Encode the states
        - Assign a unique bit pattern to each state
    3. Fill in the truth table
        - Translate the logic into a truth table such that it generates the next state and outputs for each state and input
        - Ordering inputs with state bits first makes the correspondence between the truth table and the FSM easier to see
    4. Implement the combinational logic
### Converting a Circuit to an FSM (Reverse Engineering)
- Circuits, truth tables, and equations are all forms of the same function
- Similarly, circuits, state tables, and FSMs are all forms of the same sequential behavior
- Converting a circuit to equation or FSM is known as **reverse engineering** the behavior of the circuit
    - This can help with understanding the behavior of a circuit
    - This can also check the correctness of a circuit
### Common Mistakes when Capturing FSMs
- Most mistakes when capturing FSMs are due to properties regarding the transitions leaving a state
> The upshot: *one and only one* transition condition should ever evaluate to true during any rising clock edge
#### Some common mistakes:
1. **Non-exclusive transitions**
    - For a given state all state transitions should be **exclusive** for every rising clock edge
    - This is another way of saying only one transition should be true at a time
    - Ab FSM that can always uniquely determine the next state is called a **deterministic FSM**
    - The opposite is a **nondeterministic FSM**, which allows more than one condition to be true at a time and chooses randomly
    - We want deterministic FSMs when designing circuits
2. **Incomplete transitions**
    - For a given state, every transition should be **complete** for every rising clock edge
    - This means that at least one of the conditions for state transitions should be true for every rising clock edge
    - This implies that all inputs combinations should be accounted for at every state
### FSM and Controller Conventions
#### Simplifying FSM Notations: Unassigned Outputs
- Every transition is implicitly ANDed with a rising clock edge
- If an FSM has many outputs, listing the assignent of every output in every state can become cumbersome
    - Therefore a common convention is that if an output is not explicitly assigned in a state, it is assumed to be 0
#### Simplifying Circuit Drawings: Implicit Clock Connections
- Most sequential circuits have a single clock signal connected to all sequential components
- Sequential components are denoted by a small triangle on the clock input
- Therefore, the clock signal is often omitted from the circuit drawing, since the triangle is enough to denote the clock signal
#### Mathamtical Formalisms in Combinational and Sequential Circuit Design
- We have boolean functions and FSMs for combinational and sequential circuits, respectively
- These formalisms aren't necessary for designing circuits, but their benefits are very important
    - They provide a structued method of designing circuits
    - They provide a basis for powerful automated tools for circuit design
    - They allows us to more easily check the correctness of a circuit
## 3.5 More on Flip-Flops and Controllers
### Non-Ideal Flip-Flop Behavior
- Metastability is a common problem in real digital circuits
- Metastability comes from failing to meet flip-flop setup and hold times
#### Setup Times and Hold Times
- Real flip-flops impose some restrictions on when the input can change relative to the clock edge, due to propagation delays in the wires and gates
- The two important restrictions are:
    1. **Setup time**
        - The minimum time the input must be stable before the clock edge
        - This is because the input values must have time to propagate through the flip-flops internal logic and wait for the clock edge
    2. **Hold time**
        - The minimum time the input must be stable after the clock edge
        - The clock signal must have time to propagate through the flip-flops internal logic to create a stable feedback situation
- Minimum clock pulse width is another restriction
    - The pulse must be wide enough to allow the flip-flop to capture the input
- Flip-flops typically comes with a **datasheet** that describes setup times, hold times, and minimum clock pulse width
- Datasheets in general tell designers what a component does and how to properly use it
#### Metastability
- Failing to meet setup and hold times can result in a metastable state
- A **metastable state** is a state other than a stable 0 or 1
    - This can be a voltage between 0 and 1
    - This can be oscillating between 0 and 1
- A single flip-flop in a metastable state can mess up the rest of the circuit
- Violating setup and hold times mostly has to do with interfacing with external inputs, since we cannot control when they change
- In other words, metastability is a problem when dealing with **asynchronous inputs**
- To deal with this, people try to synchronize a circuits asynchronous inputs with the clock signal
    - A common way to do this is to feed the asynchronous input into a D flip-flop
    - The output of the D flip-flop is then used as the input to the rest of the circuit
    - This flip flop is called a **synchronizer**
- Synchronizers also experience the setup/hold time problem, however the issue is relegated to the synchronizer and not the rest of the circuit
- We would typically use a flip-flop that has a very small setup and hold time for the synchronizer
- Flip-flops dont stay metastable for long, and will eventually fall into either 0 or 1
    - Thus we can put multiple flip-flops in series for synchronozation
    - The probability of successive flip-flops falling into a metastable state becomes lower and lower
- Metastability becomes a larger issue with faster clock speeds
- Since metastability is always a possibility, real circuits can be rated using a measure called **mean time between failures**, or **MTBF**
    - People usually aim for MTBFs of many years
    - Serious high speed circuits will need to take this more seriously
### Flip-Flop Reset and Set Inputs
- Some D flip flops come with extra inputs that force the output to 0 or 1 independent of the D input
    - These inputs are the **clear** or **reset**, and **set** inputs
    - These are useful for initializing a circuit to a known state when powering on or resetting circuits
    - These should not be confused with the S and R inputs of an SR latch or flip-flop
    - These take precedence over the D input of the flip-flop
- Reset and set inputs can be synchronous or asynchronous
    - A **synchronous reset** or **synchronous set** forces the output to 0 or 1 on the rising edge of the clock
    - An **asynchronous reset** or **asynchronous set** forces the output to 0 or 1 immediately
### Initial State of a Controller
- Earlier when we described FSMs as controllers, the initial state was not mentioned
- The initial state is the state the controller starts in when powered on
- Not knowing the initial state is problematic
- We can add another input called `reset` to the controller
    - Setting reset to 1 loads a known initial state into the state register
    - The reset input should be 1 when the controller is powered on
### Non-Ideal Controller Behavior: Output Glitches
- **Glitching** is the presence of temporary values on a wire typically caused by different delays of paths leading to the wire
- Glitches can occur in state changes due to different path lengths from each register flip flop to the controller outputs
- One simple solution to controller output glitching is to add a flip-flop to the output
    - An output with a flip-flip added is called a **registered output**
    - This makes sure that only the stable value of the output is used
- If the one cycle shift is not acceptable, another solution is to widen the state register so that each output has its own bit
- This will ensure that the output is connected directly to the state register which will have a stable signal, and not through the combinational logic which would be glitchy
- Both approaches have drawbacks:
    - The first one shifts the outputs but one clock cycle and uses extra flip-flops
    - The second one uses more bits in the state register and more combinational logic
    - Registered outputs should be used when glitches are unacceptable