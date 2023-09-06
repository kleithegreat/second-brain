# **C++ Basics**

## **1. Prerequisites**

### **1.1 Main Function**
- The starting point for C++ programs is the `main` function:
  ```cpp
  int main() {
      // Your code here
  }
  ```

### **1.2 Include Directives**
- The `#include` directive is used to import libraries or header files.
- Standard C++ libraries, like `<iostream>`, use angle brackets:
  ```cpp
  #include <iostream>
  ```
  - Libraries such as `<iostream>` facilitate input/output operations via `cin` and `cout`.
- User-defined or local header files use double quotes:
  ```cpp
  #include "local_header.h"
  ```

### **1.3 Standard Output (stdout)**
- Traditionally, the primary standard output was the terminal. In the past, with mainframes, input came from punch cards, and stdout directed to printers.
  ```cpp
  std::cout << "jij them" << std::endl;
  ```

### **1.4 Namespaces**
- The directive `using namespace std;` is often discouraged.
  - The `std` namespace encompasses the entire standard library, including functions, classes, and objects.
  - It's advised to be specific about what you're importing to avoid potential naming conflicts and ambiguities.
  - For instance, if only `cout` and `cin` are required, you can use:
    ```cpp
    using std::cout;
    using std::cin;
    ```

### **1.5 Strings and Variables**
- To utilize string objects, import them from the `std` namespace as `std::string`.
- Variables in C++ must be declared before they're used and defined before the program is compiled.

## **2. Functions**

### **2.1 Function Declarations and Definitions**
- In C++, defining a function also serves as its declaration.
  ```cpp
  int myFunction() {
      // Function body
  }
  ```
- However, not all declarations are definitions. A declaration merely introduces the function's signature to the compiler, while a definition provides the actual implementation.

---

## **Example: Finding the Largest Number**
Here's a simple C++ program to understand the integration of various concepts discussed above. This program takes in three values as input and returns the largest among them:

```cpp
#include <iostream>

// It's considered a bad practice to use the entire standard namespace. 
// For demonstration purposes, we've used it here.
using namespace std; 

// Function declaration and definition to find the largest number among three.
double largestNum(double val1, double val2, double val3) {
    if (val1 > val2 && val1 > val3) {
        return val1;
    }
    else if (val2 > val3) {
        return val2;
    }
    else {
        return val3;
    }
}

int main() {
    double val1 = 0;
    double val2 = 0;
    double val3 = 0;
    cin >> val1 >> val2 >> val3;  // Taking input for the three values
    cout << "largest: " << largestNum(val1, val2, val3) << endl; // Printing the largest value among the three
}
```
