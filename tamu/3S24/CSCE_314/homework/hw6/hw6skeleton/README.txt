
/* Written by Hyunyoung Lee for CSCE 314 Students Homework 6 Problem 1

   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas slides and videos, course textbook
*/

===================
=====   Part 1   ======
===================

=== Problem 2
To compile and run the code, run the following commands:
```
javac *.java
java Main
```
The following is the expected output:
```
Here's what I bought
Apple 
Gala  
Apple 
Apple 
Gala  
Fruit 
Enjoy!
```

=== Problem 3
To compile and run the code, navigate to the hw6skeleton directory and run the following commands:
```
javac *.java
java SimMain
```
Here are two possible outputs:
```
From Homer to Marge My doctor said don't walk.
From Marge to Homer That was a traffic signal!
From Bart to Homer There?s a 4:30 in the morning now?
From Homer to Bart D'oh!
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
```
```
From Homer to Marge My doctor said don't walk.
From Marge to Homer That was a traffic signal!
From Bart to Homer There?s a 4:30 in the morning now?
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Bart to Homer flooding the message queue...
From Homer to Bart D'oh!
```
The output varies from run to run due to the fact that the threads are running concurrently and the order in which they are executed is not guaranteed.
The JVM is responsible for scheduling the threads and is not controlled by the programmer.



===================
=====   Part 2   ======
===================
We use the wildcard in the sell method to make it more flexible.
As we can see in the main method, we might want to pass different types of objects to the sell method.
To make sure that the sell method works, all we need to do is ensure that it contains at least the amount of information as the type that is parameterizing the stock.
In other words, since we have a stock of fruit objects, we can sell anything as long as the thing we want to sell is a fruit, which can be more specific than just a fruit (like apple or gala).
Additionally, we use the `Collection` interface to achieve the same goal of flexibility.
As long as we have some container that implements the `Collection` interface, we can pass it to the sell method.

If we were to *not* use a wildcard in the sell method, then we would be restricting the method to only accept the type that is parameterizing the stock.
This makes the code more restrictive, less generic, and less reusable.
This way we would have to do a lot more hardcoding and unnecessary overloads to approach the same functionality.



===================
=====   Part 3   ======
===================
We need synchronization in the message queues to ensure thread safety and avoid race conditions. 
Since multiple threads (`sHomer`, `sMarge`, and `sBart`) are sharing the same `messages` queue, without proper synchronization, if multiple threads try to access or modify the `messages` queue simultaneously, it can lead to inconsistent or corrupted data.
Likewise, the `myMessages` queue is shared between the `SimBox` and `SimMain` threads, so synchronization is needed to prevent unexpected behavior.

The implementation in `SimBox` does not create the possibility of deadlock because the synchronization blocks are properly nested, meaning there is no circular wait condition.
The `run()` method first synchronizes on `messages`, and then synchronizes on `myMessages` while still holding the lock on `messages`. 