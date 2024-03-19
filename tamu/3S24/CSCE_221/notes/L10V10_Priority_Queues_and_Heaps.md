# Priority Queues and Heaps
- In a priority queue, elements not only have a value but also an associated **priority** that determines their placement in the queue
- A heap is one way of implementing a priority queue
## Queue Recap
- Enqueue adds an element to the end of the queue
- Dequeue removes an element from the front of the queue
## Priority Queue
- This is a special queue ADT
    - Elements have a priority
    - Higher priority elements are dequeued before lower priority elements
    - If two elements have the same priority, they are dequeued in the order they were enqueued
## Example: Job Scheduling
- A priority queue can be used to schedule jobs
    - Each job has a priority
    - We want to process the highest priority jobs first
## Keys
- What is a key?
    - An object assigned to an element in a priority queue that determines its priority
    - Keys do not have to be unique
    - Keys can be any type that can be compared, or ordered in the mathematical sense
- Some examples of keys
    - Simple: money, age, time
    - Complex: location, job market acceptance, etc
## Total Order Relation
- A total order relation is a binary relation that is reflexive, antisymmetric, and transitive
    - Reflexive: $x \leq x$
    - Antisymmetric: if $x \leq y$ and $y \leq x$, then $x = y$
    - Transitive: if $x \leq y$ and $y \leq z$, then $x \leq z$
## Heaps
- The issue with using an array to implement a priority queue is that it is inefficient
- The solution is to use a heap
- A heap is a **data structure** (not abstract) that is used to implement a priority queue
- A heap is a binary tree with the following properties
    - It is a complete binary tree (all levels are completely filled except possibly the last level, which is filled from left to right)
    - It satisfies **heap order**: for all nodes $v$ other than the root, the key of $v$ is greater than or equal to the key of its parent
        - This is technically called a **max-heap**
        - There is also a **min-heap** where the key of $v$ is less than or equal to the key of its parent