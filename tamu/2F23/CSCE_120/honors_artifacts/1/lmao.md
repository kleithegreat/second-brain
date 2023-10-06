Alright! Here's the prompt for the OOP lab activity based on the outline:

---

### OOP - Designing a Basic Library Management System

#### Objectives:
- Familiarize yourself with the principles of Object-Oriented Programming.
- Develop classes and objects to model real-world entities.
- Incorporate methods to handle primary operations like adding, borrowing, and returning books.

#### Completion Criteria:
- Attend the lab session or have an approved absence.
- Successfully implement and test all the methods in the given classes.
- Ensure your code compiles without any errors or warnings.

#### Submission Requirements:
Please submit the following files:
- `main.cpp`
- `library.cpp`
- `library.h`
- `book.cpp`
- `book.h`

#### Instructions:

1. **Retrieve the Starter Code**:
   - Download the starter code which provides the basic structure of the classes you'll be working on.

2. **Design and Implement the Classes**:

   a. **Book Class**:
      - Attributes: `title`, `author`, `ISBN`, `isBorrowed`.
      - Methods:
        - `borrowBook()`: Change the status of a book to borrowed.
        - `returnBook()`: Change the status of a book to available.
        - Necessary getters and setters.

   b. **Library Class**:
      - Attributes: `books` (a collection of `Book` objects).
      - Methods:
        - `addBook(Book book)`: Integrate a book into the library's collection.
        - `borrowBook(string ISBN)`: Facilitates the borrowing of a book using its ISBN.
        - `returnBook(string ISBN)`: Manage the return of a book using its ISBN.
        - `searchBook(string title)`: Locate a book by its title within the library.

3. **Construct the Main Program**:
   - Establish a user-friendly interface to interact with the library system.
   - Provide options for users to add, borrow, return, and search for books.

4. **Bonus Tasks (If Time Allows)**:
   - Design a `User` class to monitor borrowed books for each user.
   - Enhance the search function to include filters like author, publication year, etc.
   - Incorporate error management for scenarios such as attempting to borrow a book that's already out.

5. **Compilation and Constraints**:
   - Make sure your code compiles without generating errors.
   - Refrain from using non-standard libraries or headers.

6. **Discussion and Analysis**:
   - Engage in discussions about the significance of encapsulation, inheritance, and polymorphism in OOP.
   - Evaluate the efficiency of your search mechanism and suggest possible enhancements.

---

**Note**: This prompt serves as a guide for the lab activity. Depending on the class's pace and understanding, instructors might need to adjust the difficulty or offer more guidance.

Would you like to proceed with drafting the starter code next?


Alright! Here are some additional guidelines, hints, and common pitfalls for students to consider during the lab:

### Additional Guidelines for the OOP Lab:

1. **Understand the Problem**:
   - Before diving into the code, make sure you understand the requirements and the roles of the `Book` and `Library` classes. Draw a diagram or outline the relationships between classes if necessary.

2. **Start Simple**:
   - Begin by implementing the basic methods of the `Book` class, as it is the foundational unit. Test each method after implementation to ensure correctness.

3. **Use the Provided Test Cases**:
   - Regularly run the provided test cases to validate your implementation. This helps in catching errors early and ensures you're on the right track.

4. **Avoid Hardcoding**:
   - Ensure that methods are flexible and not hardcoded for specific test cases. Your methods should work for various inputs, not just the ones provided in the test cases.

5. **Consistent Error Handling**:
   - When implementing methods like `borrowBook` or `returnBook`, decide on a consistent way to handle errors (e.g., when trying to borrow a book that's already borrowed). Whether you choose to return a specific value, print an error message, or handle it some other way, be consistent throughout your code.

6. **Code Comments and Documentation**:
   - Ensure that your code is well-commented. This not only helps graders understand your logic but also assists you when debugging or revisiting your code later.

7. **Optimize Last**:
   - Start with a clear and correct implementation. Once everything is working, then consider optimizations. Often, clarity is more important than slight optimizations.

### Common Pitfalls:

1. **Ignoring Return Types**:
   - Ensure that your methods return the correct type. For instance, if a method is supposed to return a pointer, ensure you're not inadvertently returning a reference or object.

2. **Not Handling All Cases**:
   - Ensure that your methods can handle all edge cases. For instance, consider what should happen if someone tries to borrow a book that doesn't exist in the library or is already borrowed.

3. **Memory Management**:
   - While dynamic memory allocation (using `new` and `delete`) is not a primary focus of this lab, be cautious if you decide to use it. Ensure that memory is managed correctly to avoid leaks.

4. **Overcomplicating Solutions**:
   - Often, the simplest solution is the best. Don't overthink or overengineer your implementations.

5. **Not Testing Incrementally**:
   - Test your code frequently. Don't write the entire program and then test it all at once. This can make debugging challenging as multiple issues may arise simultaneously.

### Bonus Tips:

1. **Engage in Discussions**: Discuss the importance of encapsulation, inheritance, and polymorphism in OOP with your peers. This not only deepens your understanding but also helps solidify these concepts.
2. **Seek Feedback**: If you're unsure about a particular implementation or need clarification, don't hesitate to ask!

---

With these guidelines in place, students should have a clearer roadmap for the lab and be better equipped to avoid common mistakes. The next step would be to **Set Up Compilation & Forbidden Includes Tests**. Would you like to proceed with this step or move to another one?


