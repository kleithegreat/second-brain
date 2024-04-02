# Tree ADT
- The tree is an abstract data type
- Recall that ADTs are defined by their operations, not by their implementation
- In CS, we need to be able to deal with many different types of data, so ADTs help us to think about the data in a more abstract way
- For example, the stack ADT is defined by its operations (push, pop, top, etc.), not by its implementation (array, linked list, etc.)
- We must be cognizant of what our data is composed of and what operations should be relevant to it
- We should be looking for the natural organization of the data, and then abstracting that organization into an ADT
- For example, when space/memory is a concern, we might want to use a linked list instead of an array
- When time is a concern, we might want to use a hash table instead of a linked list
## Attributes of Trees
- Trees are an abstract model of an **hierarchical structure**
- A tree consists of **nodes** with a **parent-child** relationship
- These can be used for organization charts, file systems, etc.
> Trees are intentionally open ended by definition. Being a tree does not say anything about the number of children a node can have, or the depth of the tree, or the number of nodes in the tree, etc.
- Example: Linux file system
    - / (root)
        - bin
            - chmod
            - ls
            - mkdir
        - etc
        - tmp
            - foo
            -bar
        - users
            - Guest
            - Tyagi
                - Documents
                    - CSCE 221 Materials
                - Downloads
        - var
- Each *node* is a file or directory
- Each *branch* signifies the parent directory
## Trees Amidst Us
- We have many more specific types of trees that we use in CS
- **Binary Trees**
    - Used in almost every high-bandwidth router
    - We restrict the number of children any node can have to 2
    - We are still allowed to have leaves with only one child
- **Binary Search Trees**
    - Used in many search applications with high data flow
    - Nodes are arranged such that going one level down cuts the number of nodes to search in half
- **Binary Space Partition**
    - Used in many 3D video games
- **Heaps**
    - Used in efficient priority queues
    - Used in scheduling processes in an operating system
    - Used in A* search algorithm
    - Also used in heap sort
- Examples of commonly used trees
    - Huffman coding tree--used in data compression
    - GGM Trees--used in cryptographic key generation
    - Syntax trees--used in compilers
    - Treap--used in randomized data structures
## Terminology
- **Root**: Node with no parent
- **Internal Node**: Node with at least one child
- **Leaf (External Node)**: Node with no children
- **Ancestor**: A node on the path from the root to a node (including the root)
- **Depth**: Number of ancestors of a node, not including itself
- **Height (Of the entire tree)**: Maximum depth of any node in the tree
- **Descendant**: All children, grandchildren, etc. of a node
- **Subtree**: A node and all its descendants
- **Size**: Number of nodes in the tree
## A Linked Structure for General Trees
- We can use a linked structure to represent a tree
- A node is represented by an object that has the following:
    - The element/data in the node
    - A reference to the parent node
    - Sequence of children nodes (any iterable container)
## Operations on the Tree ADT
- By no means comprehensive, but here are some common operations
- Generic
    - `size()`: Returns the number of nodes in the tree
    - `isEmpty()`: Returns true if the tree is empty
    - `elements()`: Returns the elements at all positions of the tree
    - `positions()`: Returns the positions of all nodes in the tree
- Accessor
    - `root()`: Returns the root of the tree
    - `parent(p)`: Returns the parent of node `p`
    - `children(p)`: Returns an iterable collection of the children of node `p`
- Query
    - `isInternal(p)`: Returns true if node `p` has children
    - `isLeaf(p)`: Returns true if node `p` has no children
    - `isRoot(p)`: Returns true if node `p` is the root
## Tree Traversal
- A **traversal** is a systematic way of accessing all the nodes in a tree
- These are classified by the order in which the nodes are visited
- There are two major classifications:
    - **Depth-First Traversals**
        - **Preorder**: Visit the root, then recursively visit the left and right subtrees
        - **Postorder**: Recursively visit the left and right subtrees, then visit the root
        - **Inorder**: Recursively visit the left subtree, visit the root, then recursively visit the right subtree
    - **Breadth-First Traversal**
        - **Level Order**: Visit the nodes level by level, from left to right
## Preorder Traversal
- *Node before children*
- Depth-first traversal
- Only expand horizontally when there are no more children in the current subtree
- Application: Print a structured document
Pseudocode:
```
Algorithm preOrder(v)
    visit(v)
    for each child w of v do
        preOrder(w)
```
Example traversal order:
```
       A(1)
     /  |  \
  B(2) C(5) D(7)
  / \     \
E(3) F(4)  G(6)
```
## Postorder Traversal
- *Node after children*
- Depth-first traversal
- Application: compute space used by files in a directory
Pseudocode:
```
Algorithm postOrder(v)
    for each child w of v do
        postOrder(w)
    visit(v)
```
Example traversal order:
```
       A(7)
     /  |  \
  B(3) C(5) D(6)
  / \     \
E(1) F(2)  G(4)
```
## Inorder Traversal
- *Node after left child, before right child*
- Depth-first traversal
Pseudocode:
```
Algorithm inOrder(v)
    if isInternal(v)
        inOrder(leftChild(v))
    visit(v)
    if isInternal(v)
        inOrder(rightChild(v))
```
Example traversal order:
```
       A(4)
     /  |  \
  B(2) C(5) D(7)
  / \     \
E(1) F(3)  G(6)
```
Here's an intuitive way to think about preorder, postorder, and inorder traversals in a binary tree:

1. Preorder Traversal (Node-Left-Right):
Imagine you are a visitor exploring the binary tree. In preorder traversal, you first visit the current node, then explore its left subtree, and finally explore its right subtree. It's like saying, "I'll visit the current node, then go left to explore, and then go right."

Example:
```
    A
   / \
  B   C
 / \
D   E
```
Preorder traversal: A, B, D, E, C

2. Postorder Traversal (Left-Right-Node):
In postorder traversal, you first explore the left subtree, then the right subtree, and finally visit the current node. It's like saying, "I'll explore everything to the left, then everything to the right, and finally visit the current node."

Example:
```
    A
   / \
  B   C
 / \
D   E
```
Postorder traversal: D, E, B, C, A

3. Inorder Traversal (Left-Node-Right):
In inorder traversal, you first explore the left subtree, then visit the current node, and finally explore the right subtree. It's like saying, "I'll explore everything to the left, then visit the current node, and then explore everything to the right."

Example:
```
    A
   / \
  B   C
 / \
D   E
```
Inorder traversal: D, B, E, A, C

Another way to think about inorder traversal is that it visits the nodes in ascending order for a binary search tree (BST). In a BST, all nodes in the left subtree are smaller than the current node, and all nodes in the right subtree are greater than the current node. Inorder traversal of a BST yields the nodes in sorted order.

These traversals differ in the order in which they visit the nodes and their subtrees. The names "preorder," "postorder," and "inorder" refer to when the current node is visited in relation to its subtrees.
## Binary Trees
- A **binary tree** has the following properties:
    - Each node has at most two children
    - Each child node is labeled as being either a left child or a right child
- A binary tree can be defined recursively as either:
    - A tree with a single node (the base case)
    - A root node with a left subtree and a right subtree
- Applications:
    - Arithmetic expressions
    - Decision trees
    - Searching
## Properties of Binary Trees
- A binary tree is **full** or **proper** if each node is either a leaf or has exactly two children
- A **complete** binary tree of height $h$ has all $2^{h-1}$ nodes at height $h-1$ (nodes are filled in from left to right)
- A **perfect** binary tree has all internal nodes with two children and all leaves at the same depth