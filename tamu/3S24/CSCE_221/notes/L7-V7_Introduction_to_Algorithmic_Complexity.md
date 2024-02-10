# Introduction to Algorithmic Complexity
In this introduction want to go over the background and motivation for analyzing algorithms. We will largely be concerned about runtime complexity. Later, we will discuss a theoretical framework for reoporting runtime growth rate and a basis for comparing algorithms.

## What do we want from an algorithm?
- Correctness
    - We always want the algorithm to produce the correct output
- Efficiency
    - It should use computational resources efficiently
    - e.g. runtime, memory, disk operations, network bandwidth etc.

> Performance (**Running Time**) remains the dominant consideration of algorithm "goodness"

- Say we have two algorithms that sort a list of *n* numbers
    - Algorithm A takes 10 ms
    - Algorithm B takes 11 ms
- However, things are different if we know for example algorithm A was run on a desktop computer and algorithm B was run on a smartphone
- Actual runtime of an algorithm depends on many external factors
    - Hardware
    - Programming language
    - Compiler
    - Background processes
    - even more

## Traditional Measures of Running Time
- Profiling and benchmarking
- Analysis
    - Experimental
    - Theoretical
### Profiling
- Process of understanding bottlenecks
- 90-10 rule says 90% of the time is spent in 10% of the code
### Benchmarking
- Small collection of typical inputs that are representative of the problem
- We want algorithms to perform well on all benchmarks
- We want to vary our benchmarks and test edge cases too
### Experimental studies
- Graphs of running time vs input size

**Limitation of the above methods**
- Implementing the algorithm may be difficult
- Results may be hardware dependent
- It is possible for people to forget about certain inputs and not test them

## Theoretical Analysis
- Combination of three ideas
    - Create a high-level description of the algorithm, not an implementation
    - Characterize runtime as a function of input size
    - Use that function to see how fast runtime grows with input size

pick up on 27:38