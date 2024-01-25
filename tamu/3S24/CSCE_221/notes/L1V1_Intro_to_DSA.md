# Introduction to Data Structures and Algorithms

## Prologue
- How do you figure out how many people make over six figures in a company?
    - Straightforward solution: go through every employee in a table and check their salary
- How many cities with more than 250k people lie within 500 miles of Dallas?
    - Straightforward solution: go through every city in a table and check their population and distance from Dallas
- Can we connect all telephone customers with less than 1000 miles of cable?
    - First blush response: show cable length between all customers and check if you can connect everyone with less than 1000 miles


> DSA is about structuring data to help you store and retrieve it efficiently.

The course will focus on the following:
1. Common data structures and algorithms
2. Tradeoffs between different data structures and algorithms (time vs. space)
3. How to measure the effectiveness of a data structure or algorithm for a given problem

## Data Structures
- *Definition* - A **data structure** is any data representation and its associated operations a way of organizing, storing, and performing operations on data.
    - even an integer or floating point number is a data structure
    - most data structures focus on collections of data
- *Definition* - **Operations** performed on a data structure include **accessing** or **updating** stored data, **searching** for specific data, **inserting** new data, and **removing** stored data.
- Common data structures include array, linked list, binary tree
    - An array is an ordered collection of data items, where each item can be accessed directly by its index
    - A linked list is an ordered collection of data items, where each item is stored in a node that also contains a pointer to the next node in the list
    - A binary tree is an ordered collection of data items, where each item is stored in a node that also contains pointers to at most two child nodes, a left child and a right child

## Algorithms
Computer science is science of systematic problem solving.
An **Algorithm** is a routine of solving a problem through a series of well-defined steps.

Example: A simple algorithm for finding the maximum value in an array of integers is to go through the array and keep track of the largest value seen so far.

### Computational problems and common algorithms
- Shortest total flight distance between two airports?
    - This is the **shortest path problem**. A common algorithm for solving this problem is **Dijkstra's algorithm**.
- Given a list of student records and a students first and last name, what is the student's ID number?
    - One common approach is the **binary search algorithm**.
- Do two student essays share a common phrase consisting of a sequence of more than 100 letters?
    - Longest common substring algorithm

### Algorithmic efficiency
- Algorithmic efficiency is commonly expressed via **asymptotic** analysis of runtime and memory use.
- An efficient algorithm is one whos runtime increase no more than polynomially as the input size increases.

## Relationship between data structures and algorithms
**Algorithms that implement inserting, removing, and searching for data are typically specific to each data structure.**
- For example, appending a linked list is very different from appending an array.