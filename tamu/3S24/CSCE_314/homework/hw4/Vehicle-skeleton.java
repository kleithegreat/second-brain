
/* CSCE 314 [Sections 595, 596, 597] Programming Languages, Spring 2024
   Homework Assignment 4 
   Skeleton for Problems 4-9
   Written by Hyunyoung Lee for CSCE 314 Students

   Student Name:
   Student UIN:
   Acknowledgements:
*/

import java.util.*; // for Collections.sort() and ArrayList

class Vehicle {
				// private fields
				// public fields
				// constructors
				// public methods
				// private methods if you need
}

class VehicleTest {
				public static void main(String[] args) {
								// create Vehicle instances
								// test the functionalities you implemented
				}
}


// Hints on the PassengerVehicle class for Problem 9 of Homework 4
class PassengerVehicle extends Vehicle 
                       implements Comparable<PassengerVehicle> 
{
  // private fields specific to PassengerVehicle such as 
  // total # of seats and occupied seats (both can be of type int, 
  // and properly initialized)


  /* constructors: Give three constructors, 
     1. one no-arg constructor,
     2. a constructor with one argument: only owner name as an argument,
     3. a constructor with two arguments: owner name and total # of seats

     Probably you already have the first two constructors in the Vehicle
     class, then, invoke the Vehicle class constructor by using `super`
  */

  /* get methods for the private fields */

  /* set methods for the private fields */

  // override the toString method (inherited from the Object class) 
  // signature: toString() 
  // @Override
  // ...

  // implement compareTo method (to `implements` Comparable)
  // signature: compareTo(PassengerVehicle)
  
  // main method
  public static void main(String[] args) {
    // You can use either the basic Java array [] (and use Arrays.sort)
    // or ArrayList 
    // (or any Collections, whichever you feel the easiest)
    // Using ArrayList, you would do something like,
    ArrayList<PassengerVehicle> pVs = new ArrayList<PassengerVehicle>(); 
    // where pVs is object reference for ArrayList of PassengerVehicles

    // Now, you can add PassengerVehicle objects (at least 5) to pVs
    // e.g., pVs.add( new PassengerVehicle("H Lee", 7) ); 
    // which addes a PassengerVehicle object with 
    // owner name "H Lee" and total 7 seats
    
    Collections.sort(pVs); // Sort the PassengerVehicles 
                           // in an ascending order according to
                           // the compareTo method implementation 

    // Find a way to output the ascending sorted result in descending
    // order. Use a for loop to print out the sorted result 
    // in a descending order

  } // end of main

} // end of class PassengerVehicle

