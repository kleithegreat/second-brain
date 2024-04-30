# Linked List and Queue
- Linked list closer to a data structure
- Queue is an abstract data type
## Singly-linked list
- Each node has two attributes
    - Element to be stored
    - Pointer to the next node
- Allows for non-contiguous memory allocation
- Operations:
    - `size()`: returns the number of elements in the list
    - `empty()`: returns `true` if the list is empty, `false` otherwise
    - `front()`: returns the first element (head->element)
    - `insertFront(e)`: inserts a new element `e` at the front of the list
    - `removeFront()`: removes the first element
- `head` and `tail` pointers point to the first and last elements respectively
### Insert at the front
- Create a new node
- Set the new node's next pointer to the current head
- Set the head to the new node
- Cost is O(1)
### Erase the front
- Set the head to the next node
- Delete the node
- Cost is O(1)
### Stack with singly linked list
- This is implementing an ADT with a data structure
- All operations are O(1)
- Space complexity is O(n)
## Queue
- Definition: A line of people or things waiting for something
- First in, first out (FIFO)
    - All insertions are at the back and all removals are at the front
- Operations:
    - `size()`: returns the number of elements in the queue
    - `empty()`: returns `true` if the queue is empty, `false` otherwise
    - `enqueue(e)`: inserts a new element `e` at the back of the queue
    - `dequeue()`: removes the element at the front of the queue
    - `front()`: returns but NOT removes a reference to the front element
- Applications:
    - Waiting lines
    - Access to shared resources (e.g. printer, process scheduling)
    - Auxiliary data structure for algorithms
    - Component of other data structures
### Array based queue
- Create a large array of size N to store queue elements
- Three elements are needed to implement a queue
    - `f` (front): index of the first element
    - `r` (rear): index of the last element
    - `N` (capacity): maximum number of elements
- Location `r` is kept empty
- Performance:
    - Space complexity is O(n)
    - Time complexity is O(1) for all operations
- Size is defined a priori
### Growable array based queue
- Similar to the growable array based stack
- Replace the array with a larger one when the current one is full
    - Incremental or double
- Enqueue now has amortized running time
    - $O(1)$ for doubling
    - $O(n)$ for incremental
### Singly linked list based queue
- Head is the front and tail is the rear
- Enqueue is O(1)
- Dequeue is O(1)
- Space complexity is O(n)
- No need to define a priori size
- Can grow and shrink as needed