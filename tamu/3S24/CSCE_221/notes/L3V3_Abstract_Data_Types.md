# Abstract Data Types

- Not the same as data structures technically

## Abstraction
- "The essence of abstraction is preserving information that is relevant in a given context, and forgetting information that is irrelevant in that context." - John V. Guttag (MIT)
- Example: Cars
	- Steering, accelerating, braking are abstracted by the steering wheel, gas and brake pedals. 
	- Underlying mechanisms for accomplishing these tasks can vary but are irrelevant to the driver

## Data Types
- A **type** is a collection of values
	- Example: booleans can be true or false
- Integer is **simple type**, since it contains no subparts
- A bank record is an **aggregate** or **composite type** - this contains multiple parts
- A **data type** is a collection of values as well as the operations associated with it
	- Example: Addition is an operation on the integer data type
## Abstract Data Type
- An **abstract data type** (or ADT) is just the specification of a data type in some language, *independent* of its implementation
- This means ADTs are defined in terms of a type and its operations, but not how it works
- Example: Lists
	- These are a collection of elements where each element has a specific index
	- Common operations are inserting, deleting, and accessing elements
	- However, the implementation does not matter to the end user most of the time
		- List ADTs can be **array based** or **linked list based** most commonly

## Data Structure
- This is just an implementation for an ADT
- ADT + Implementation = Class in OOP
- Operations are implemented with methods

> ADTs are concerned with the "what", while data structures also address the "how"