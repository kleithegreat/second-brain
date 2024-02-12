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
## Example of code fragment runtime analysis
```
(1) small = i
(2) for (j = i + 1; j < n; j++)
(3)     if (A[j] < A[small]) then
(4)         small = j
```
- First start with assumptions
    - in the for loop:
        - assign has a cost of 1
        - test has a cost of 1
        - incremente has a cost of 1
    - comparison has a cost of 1
- Runtime:
    - has two parts: one time cost and reptitive cost
    - one time cost: 
        - 1 unit for initial assignment
        - 1 unit for initializing loop
        - 1 unit for first comparison
    - repetitive cost:
        - total cost of body is 4 units
        - loop runs (n - 1) - (i + 2) = n - 1 - i times
        - total repetitive cost is 4(n - 1 - i)
    - Total cost:
        - 3 + 4(n - 1 - i) = 4(n - i) - 1
- We can see that the runtime of the algorithm is a function of the input size
## Runtime Analysis
- We usually want to identify the **critical code** that would define the **growth rate** of the algorithm with respect to the input size
- The focus is on the **worst-case** running time to "bound" the running time
## Another example: Naive sorting
```
Algorithm sortArray(A, n)
    Input: Array A of n elements
    Output: Sorted A

    for i <- to n-2 do
        for j <- i+1 to n-1 do
            if A[i] > A[j] then
                swap A[i] and A[j]
            endif
        endfor
    endfor
```
- First loop goes from 0 to n - 2
- Second loop goes from i + 1 to n - 1
- Basically this algorithm comapres every element with a smaller and smaller subset of the array
> The code we want to focus on is the if statement
- $T(n) = \sum_{i=0}^{n-2} \sum_{i+1}^{n-1} 1$
- $T(n) = \sum_{i=0}^{n-2} (n - i - 1)$
- $T(n) = \sum_{i=0}^{n-2} n - i - \sum_{i=0}^{n-2} i$
- $T(n) = (n - 1)(n - 2 - 0 + 1) - \sum_{i=0}^{n-2} i$
- $T(n) = (n - 1)(n - 1) - \frac{(n - 2)(n - 1)}{2}$
- ...
- $T(n) = \frac{n^2 - n}{2}$
## Best, worst, and average cases
- Algorithms have a probability distribution of running times
- Average case can be found by assuming any input is equally likely
    - We then use this to calculate the chance of pieces of critical code running
    - We then sum the running times of the critical code and weight them by the chance of them running