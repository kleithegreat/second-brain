1
6 / 6 points
Fill in each of the blanks with a correctly spelled word from the choices (a choice may be used multiple times).

 

Choices:   object,   class,   bytecodes,   bytes,   source,   stack,   heap,   array,   method,   reference,   register

 

1) A Java compiler translates a class definition into a format the JVM understands; the compiled result is stored in a 
Correct answer:
class
 file, (continued in the next question) 

2) which contains the JVM instructions, which are called 
Correct answer:
bytecodes
 .

3) The JVM instruction set is designed around a 
Correct answer:
stack
-based architecture with special object-oriented instructions.

4) Among the runtime data areas of the JVM, the 
Correct answer:
method
 area contains the class information, code and constants.

5) Among the runtime data areas of the JVM, activation records are stored in the 
Correct answer:
stack
 frames.

6) Among the runtime data areas of the JVM, the 
Correct answer:
heap
 is where objects live.

 

Feedback
Based on answering correctly
Super!

General Feedback
Review the terms carefully thinking of the meanings.

Results for question 2.
2
4 / 4 points
Consider the following code snippet:

 

public class BankAccount {

    public BankAccount() { balance = 0; totalAccounts++; }

    public static void main( String[] args ) {
      BankAccount a = new BankAccount();
       . . .
    }

   private double balance;
   private static int totalAccounts = 0;
}

 

Suppose it is compiled and run as 

> java BankAccount

 

Below are some of the steps (at the beginning) taken by the JVM to execute the code. They may not be in a correct order.

 

Put them in the correct order (as the JVM executes).

 

 

Correct Order Answer:
ClassLoader loads BankAccount to the method area.

Correct Order Answer:
A stack frame for main() is pushed onto the Java stack.

Correct Order Answer:
A stack frame for the BankAccount constructor is pushed onto the Java stack.

Correct Order Answer:
A pointer to the BankAccount class data for the object is created in the heap.

Correct Order Answer:
The balance variable of this instance is initialized with a default value.

Correct Order Answer:
totalAccounts is initialized and assigned with 0.

Feedback
Based on answering correctly
Awesome!

General Feedback
Study the JVM steps carefully using the BankAccount code in the JVM.pdf slides (the JVM activation record example) and watching the relevant video -- you may want to take notes while watching the video.  Understanding all these JVM steps will help you understand run-time system and memory handling and many important concepts of Java such as creation and handling of object references and objects, dynamic dispatch, static field, and so on.