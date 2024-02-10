# Deque (Double ended queue)

## Main function
- pronounced as *DECK*
- has insertions and deletions at both ends of the queue

## Motivation
- Some applications might need linear data arrangement with both LIFO and FIFO operations
    - Example: browser history management
    - Example: Task management

## Double ended queues
- Stores arbitrary objects
- richer than stack or queue
- **Main operations**:
    - `insertFirst(object o)`: insert an object `o` at the beginning of the deque
    - `insertLast(object o)`: insert an object `o` at the end of the deque
    - `removeFirst()`: remove and return the first object of the deque
    - `removeLast()`: remove and return the last object of the deque
- Auxiliary operations:
    - `first()`: return the first object of the deque
    - `last()`: return the last object of the deque
    - `size()`: return the number of objects in the deque
    - `isEmpty()`: return `true` if the deque is empty, `false` otherwise
- Can throw `EmptyDequeException` if the deque is empty when trying to call some of the methods

## Doubly linked list
- Linked list where nodes point to both the next and the previous node
- Also has head and tail sentinel nodes
- Has the same main operations as the deque
- Private operations:
    - `add(n, e)`: add element `e` after the node `n`
    - `remove(n)`: remove and return the node `n`
### Adding a node
- Allocate a new node
- Set the `next` and `prev` pointers of the new node
- Set the `next` and `prev` pointers of the nodes around the new node
### Removing a node
- Set the previous node's `next` pointer to the next node
- Set the next node's `prev` pointer to the previous node
- Delete the node

## Deque with doubly linked list
- Front element is head
- Rear element is tail

## Performance and limitations
- **Performance**
    - $O(n)$ space complexity
    - $O(1)$ time complexity for all operations
- Deque is never full (for double linked list)