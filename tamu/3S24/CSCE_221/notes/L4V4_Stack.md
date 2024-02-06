# Stack
## Basics and operations
- The **stack** is an abstract data type
    - "We are least bothered by how it is implemented"
    - Its just a pile of elements
    - We can query the `size`
    - We can also query if it is empty
- We can `push` elements to the top
- The `top` operation returns the top element
    - This does not remove the top element
- The `pop` operation removes the top element
> Accessing the top of the stack is easy, but accessing the bottom is hard
## Applications of stacks
- Page history in a browser
- Undo/Redo in a text editor
- Function calls in a program
## C++ Run-time stack
- The C++ run-time system keeps track of the chain of active function calls with a stack
- The program counter keeps track of the statement being executed
- When a function returns, it is popped off the stack
## Recursive algorithms
Naïve factorial algorithm:
```
n! = n * (n-1)!
1! = 1
0! = 1
```
- This implementation is memory expensive since every function call is stored in the stack
    - Memory and runtime are both $O(n)$
- We can use a loop to implement the factorial algorithm
```cpp
long int factorial(long int n) {
    long int i, f;

    f = n;
    for (i = n-1; i > 0; i--) {
        f *= i;
    }
    return f;
}
```
- Now memory usage is $O(1)$ and runtime is $O(n)$
    - This is since we are modifying the same variable `f` in place
    - Runtime is $O(n)$ since we are iterating through the loop $n$ times
## Stack implementation
### Array-based implementation
1. Create a large array to store the elements
2. Add elements left to right
3. We have a variable to keep track of the top
#### Performance
- Space is $O(n)$
- Time complexity is $O(1)$ for all operations
    - This is since we are just modifying the top variable
    - We are not iterating through the array
#### Limitations
- Size is determined a priori (cannot be changed)
- Pushing into a full stack causes an overflow
### Growable array-based implementation
- Replace the array with a larger one when the stack is full
    - Incremental: increase the size by a constant
    - Doubling: double the size of the array
#### Performance analysis
- $T(n)$ is the time to perform a series of $n$ push operations
- **Amortized time** is the average time per operation
    - This is since push might take $O(n)$ time in the worst case or $O(1)$ time in the best case
    - This amortized time is like an average
- Incremental strategy:
    - The array is replaced $k = \frac{n}{c}$ times
$$\begin{align*} 
    T(n) &= n + c + 2c + \ldots + kc \\
    &= n + c(1 + 2 + \ldots + k) \\
    &= n + ck \frac{k(k+1)}{2} \\
    &= O(n^2)
\end{align*}$$
- - The amortized time is $\frac{O(n^2)}{n} = O(n)$
- Doubling strategy:
$$\begin{align*}
    T(n) &= n + (1 + 2 + 2^2 + 2^3 + \ldots + 2^k) \\
    &= n + 2^{k+1} - 1 \\
    &= 3n - 1 \\
    &= O(n)
\end{align*}$$
- - The amortized time is $\frac{O(n)}{n} = O(1)$
## Summary
- Stack operates in last in, first out (LIFO) order
- Has many real-world applications
- Common operations are `push()`, `pop()`, `top()`, `empty()`, and `size()`
- We can implement a stack using an array
    - Predetermined ungrwoable stack: $O(1)$ time complexity
    - Growable stack: Doubling strategy has $O(1)$ amortized time complexity (better than incremental strategy)
- Is an ADT since it has multiple implementations