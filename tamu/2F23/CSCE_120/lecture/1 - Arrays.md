# **Arrays**

## **C-Style Arrays**
- **Memory Allocation**: There are two areas of memory: the stack and the heap. C-style arrays are allocated on the stack.
    - The compiler must know the array size at compile time. This is an issue because the array size is often uncertain at compilation, leading to the practice of using a larger array than needed.
- **Syntax**: 
    - Declaration: `type arrayName[size];`
        - Example: `int myArray[6];`
    - Initialization: 
        - Empty Initialization: `int myArray[6] = {};`
            - This initializes all values to 0.
        - Specific Initialization: `int myArray[6] = {1, 2, 3, 4, 5, 6};`
        - Auto-size Initialization: `int myArray[] = {1, 2, 3, 4, 5, 6};`
            - The size of the array is automatically deduced from the number of elements in the initializer list.

> **Aside**: *Unsigned Variables*: `unsigned` variables (int, short, long) are variables that cannot hold negative values.

> **Another Aside**: *Comparison of Unsigned and Signed Variables*: Comparing unsigned variables to signed variables can cause unexpected results.

- **Array Indexing**: 
    - Indexing outside the bounds of the array results in undefined behavior, commonly resulting in a segmentation fault (segfault).
    - This issue can be more severe when the array is allocated on the heap rather than the stack.
    - The compiler does not check for out-of-bounds indexing, uninitialized variables, uninitialized memory, memory leaks, dangling pointers, memory corruption, memory fragmentation, memory allocation failures, or memory access failures.
        - The compiler will sometimes issue a warning though.