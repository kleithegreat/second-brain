# key points

## basics

- **PEMDAS**
  - M/D and A/S have equal precedence
    - operations with equal precedence evaluated left to right
    - regular, floor, and modulus division all have same precedence
- division always returns a float
  - floor division can return either int or float depending on inputs
    - modulus returns int
- `int()` function **truncates** any decimal, does NOT round

- ## variable naming

  - must **start** with a **letter or underscore**
    - can only contain alphanumeric characters and underscores

## math module

- `from math import *` imports all methods from math library
- common methods include `sqrt()`, `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`, `log()`, `log10()`, `exp()`
  - `log()` is NATURAL LOG, `exp()` is exponential base **e**

## booleans

- `True` and `False` are 1 and 0 respectively
  - must be capitalized to be a boolean value
- `None`, 0, and empty iterables evaluate to False for `bool()` method

- ## comparisons

  - `is` keyword compares pointers while `==` compares values
  
- ## precedence

  - relational first (`<`, `>`, `==`, `<=`, `<=`, `!=`)
        - sidenote: **=< and => are not valid**
    - not -> and -> or

## lists

- can be concatenated using "+"

- ## methods

  - `listName.append()` function adds to the end of a list
    - `listName.pop()` removes from the end
    - `listName.remove()` removes the element at the given index
    - `listName.insert()` inserts an element at the given index
    - `len(listName)` returns the length
    - check for an elements existence in a list using the `in` keyword
      - `1 in list` would return a boolean depending if `1` is in the list `list`
    - `min(listName)` and `max(listName)` methods return the minimum and maximum values of a list
    - `listName.index(element)` returns the index of a given element
    - `listName.count(element)` returns the number of occurances of a given elemetn for a list

- ## indexing

  - negative indicies start from the end
        - eg. `listName[-1]` returns the last element
    - slice syntax
      - `listName[start:end:step]`
        - assigning another list to `listName[:]` will create a copy instead of a pointer

## strings

- string **literals** can be concatenated with just a space
  - `"Hello " "world!"` evaluates to `"Hello world!"`
- f strings: `f"string contents {variable}"`
  - formatting bracket stuff:

- ## methods

  - `len(stringName)` returns the length of the string just like an array

## misc

- dictionary syntax: `{key0: value0, key1: value1, etc.}`
  - keys MUST be immutable types (ints, floats, strings, tuples)
  - `del` to remove a key
  - dictionaryName.
