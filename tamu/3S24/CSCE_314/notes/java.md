# 1: A Quick Tour
## 1.1 Getting Started
- Java builds programs from *classes*
- You can create any number of *objects* from a class definition, which are called *instances*
- A class contains *members*
    - *Fields* are variables that store data, and can belong to the class itself or to objects of the class
    - *Methods* are collections of statements that operate on the fields to manipulate state
- The `main` method is a special method
    - It is the entry point for a Java application
    - It is declared `public` so anyone can invoke it (the JVM)
    - It is declared `static`, which means the method belongs to the class itself, not to some instance of the class
    - It is declared `void` because there is no return value
    - Takes an array of `String` objects as an argument
        - This is the command line arguments passed to the program
        - Equivalent to `int argc, char *argv[]` in C
## 1.2 Variables
- Java has the following primitive types:
    - `boolean`
    - `char`
    - `byte`
    - `short`
    - `int`
    - `long`
    - `float`
    - `double`
- All the primitive types also have a corresponding object type called a **wrapper** class
    - e.g. the `Integer` class wraps the `int` primitive type
    - In most cases, the compiler will automatically convert between the primitive type and the wrapper class
## 1.3 Comments
- Java has three types of comments:
    - `//` for single line comments
    - `/* */` for multi-line comments
    - `/** */` for documentation comments
        - These comments describe declarations that follow them
## 1.4 Named Constants
- Constant values are declared `final`
- Making them `static` means they belong to the class, not to any instance of the class
- We can access them using the class name, e.g. `ClassName.CONSTANT_NAME` when we make them `static`
- Groups of named constants can be made into an **enumeration type** or **enum**
    - e.g. `enum Suit { CLUBS, DIAMONDS, HEARTS, SPADES }`
## 1.5 Unicode Characters
- Java uses Unicode for characters
```java
class Circle {
    static final double π = 3.14159;
}
```
💀💀💀
## 1.6 Flow of Control
- Java has control statements like `if`, `while`, `for`, `switch`, etc.
- `++` and `--` exist
- `+=`, `-=`, `*=`, `/=` exist
- The `+` opertaor becomes string concatenation if at least one of the operands is a string, and it will convert the other operand to a string
## 1.7 Classes and Objects
- Objects are created with the `new` keyword
## 1.8 Methods and Parameters
- The `this` keyword refers to the current object
## 1.9 Arrays
- Arrays are initialized with `Type[] arrayName = new Type[size]`
- Throws `ArrayIndexOutOfBoundsException` if you try to access an index that is out of bounds
## 1.10 String Objects
- Strings are objects in Java
- `length()` returns the number of characters in the string
- `charAt(int index)` returns the character at the specified index
- The `+` operator concatenates strings
## 1.11 Extending a Class
- OOP inheritance 😹😹😹😹😹😹😹😹😹😹😹😹
- Original class = superclass
- New class = subclass
- Subclasses inherit all the members of the superclass
- Subclasses can override methods of the superclass
- Subclasses can add new methods and fields
- We can invoke methods of the superclass with the `super.methodName()` syntax
- Classes that dont explicitly extend another class inherit from `Object`
## 1.12 Interfaces
- Interfaces declare methods that subclasses must implement
- As long as the behavior meets the *contract* of the interface, the subclass can implement the method however it wants
- These declaration define a *type*
- Interfaces can extend other interfaces
## 1.13 Generic Types
- A generic class or interface represents a family of related types
- e.g. `List<T>` represents a list of objects of type `T`
- The type `T` is a *type parameter*
- The `?` thing on its own is the *unbounded wildcard*
- The `? extends T` is the *bounded wildcard*
## 1.14 Exceptions
- try catch finally - like C++ but with `finally`
    - `finally` block is always executed
- `throw` keyword
    - `throw new ExceptionType("message")`
- `throws` keyword
    - `void method() throws ExceptionType`
- `Exception` is the superclass of all exceptions
# 2: Classes and Objects
## 2.1 A Simple Class
- A class can have three kinds of memebers:
    - Fields
    - Methods
    - Nested classes
- Class declarations can have *modifiers*:
    - *annotations* ???
    - `public` - anyone can declare references to the class or access its public members
    - `abstract` - cannot be instantiated
    - `final` - cannot be subclassed
    - `strictfp` - floating point calculations are platform independent
- Classes cannot be both `abstract` and `final`
## 2.2 Fields
- Fields can be:
    - *annotations*
    - *access modifiers*
    - `static`
    - `final`
    - `transient`
    - `volatile`
- Fields cannot be both `final` and `volatile`
- Static fields are shared by all instances of the class
- A final variable cannot change its value after it is initialized
## 2.3 Access Control
- Access modifiers:
    - `private` only accessible to the class itself
    - `package` bruh
    - `protected` accessible to the class itself, its subclasses, and classes in the same package
    - `public` accessible to everyone
## 2.4 Creating Objects
just use the new keyword bruh
## 2.5 Construction and Initialization
.
.
.
.
.
.
# 3: Extending Classes
- Fields cannot be overridden, only hidden
- Static members cannot be overridden, only hidden
- The super keyword is available in all non-static methods
## 3.4 Type Compatibility and Conversion
- Java is strongly typed, i.e. type compatibility is checked at compile time
- Type casting is done like `Base sref = (Base) this;`
- Widening conversions are called *upcasts* and are always safe
- Narrowing conversions are called *downcasts* and are not always safe
- The `instanceof` operator checks if an object is an instance of a class
## 3.8 The Object Class
- The `Object` class is the superclass of all classes
- It has the following methods:
    - `public boolean equals(Object obj)`
    - `public int hashCode()`
    - `protected Object clone() throws CloneNotSupportedException`
    - `public final Class<?> getClass()`
    - `protected void finalize() throws Throwable`
    - `public String toString()`
## 3.9 Cloning Objects
- The `Object.clone` method helps you write your own method to clone objects
- The clone method returns a new object whose initial state is a copy of the current object on which the method was invoked
- The empty `Cloneable` interface is a marker interface that indicates that the class can be cloned
> The `Cloneable` interface should be spelled `Clonable` but the misspelling is now part of the Java language and cannot be changed
# 4: Interfaces
- The fundamental unit of programming in OOP is the *type*
- It is very useful to be able to define types without defining a class
- *Interfaces* are a way to do this
- An interface is an expression of pure design, while classes are a mix of design and implementation
- Classes can implement multiple interfaces
> Java allows multiple inheritance of interfaces but not of classes
## 4.1 A Simple Interface Example
- Many simple interfaces define some property that allow the class to do something
- Some of the standard "ability" interfaces are:
    - `Cloneable` - objects can be cloned
    - `Comparable` - similar to the `Eq` typeclass in Haskell
    - `Runnable` - objects can be run in a separate thread
    - `Serializable` - some jvm shit
## 4.2 Interface Declarations
- Interfaces are declared using the `interface` keyword
- An interface can declare three kinds of members:
    - Constants
    - Methods
    - Nested classes and interfaces
## 4.3 Extending Interfaces
- Interfaces can be extended with the `extends` keyword
- Example:
    ```java
    public interface SerializableRunnable extends java.io.Serializable, Runnable {
        //...
    }
    ```
# 5: Nested Classes and Interfaces
yap
# 6: Enumeration Types
more yap
# 7: Tokens, Values, and Variables
- `null`, `false`, and `true` are not keywords, they are literals like the number 12
# 8: Primitives as Types
- The following is a hierarchy for primitive wrappers:
    - Object
        - Boolean
        - Character
        - Number
            - Byte
            - Short
            - Integer
            - Long
            - Float
            - Double
        - Void
- They have constructors like `Character(char)` or `Integer(int)`
- They have a `valueOf(String str)` method that returns an object with the specified type
    - e.g. `Integer.valueOf("42")` returns an `Integer` object with the value 42
- They have constants like `Integer.MAX_VALUE` and `Integer.MIN_VALUE`
- They implement the `Comparable<T>` interface, so they have the `compareTo(T obj)` method
- Void cannot be instantiated
# 9: Operators and Expressions
yap
# 10: Control Flow
yap
# 11: Generic Types
- Generic types are great for collections
- Type parameters are assumed to be objects
- Types can be bounded
    - `T extends Comparable` means `T` must implement the `Comparable` interface
    - They can have multiple bounds too
    - `T extends Comparable & Serializable` means `T` must implement both interfaces
        - If either bound is a class, it must be the first bound
- *extends* can be used for classes and interfaces
- Wildcards are both for convenience and supporting co/contra-variance
- **F-bounded quantification** allows for the type to appear in its own bounds
    - e.g. `E extends Comparable<E>`
- **Variance** refers to how subtyping between complex types relates to subtyping between their components
    - **Covariance** preserves the ordering of types, going from specific to generic
        - Suppose `C1() <: C2()` and `A <: B`, then `C1<A> <: C2<B>`
        - Typically read only data types
    - **Contravariance** reverses the ordering of types, going from generic to specific
        - `C1<B> <: C2<A>`
        - Write only data types can be contravariant
    - **Invariance** if neither of the above apply
        - `C1<A> <: C2<A>` for example
        - Mutable types with both read and write can be invariant
- Wildcards can be bounded
    - `? extends T` is an upper bound
        - This is covariant
    - `? super T` is a lower bound
        - This is contravariant
        - Due to type erasure, the compiler cannot determine the type of the wildcard, so it is treated as `Object`
- Wildcards cannot be used in places other than type parameters
    - e.g. `List<?> aList = new ArrayList<String>(); aList.add("hello");` is not allowed
    - However **wildcard capture** can be used to get around this in some situations
    - **Type erasure** happens when generic types are used during type checking, and erased during compilation according to these rules:
        - A type parameter is replaced by its first bound
        - Parameterized types throw away their type parameters
        - Casts are inserted where necessary
# 14: Threads
# 16: Reflection