/* CSCE 314 [Sections 595, 596, 597] Programming Languages, Spring 2024
   Homework Assignment 4 
   Skeleton for Problems 4-9
   Written by Hyunyoung Lee for CSCE 314 Students

   Student Name: Kevin Lei
   Student UIN: 432009232
   Acknowledgements: course textbook
*/

import java.util.*; // for Collections.sort() and ArrayList

class Vehicle {
				// private fields
        private int currentSpeed;  // integer to store the current speed of the vehicle
        private int currentDirection;  // integer to store the current direction of the vehicle, where 0 is north, 90 is east, 180 is south, and 270 is west (in degrees)
        private String ownerName;  // string to store the name of the owner of the vehicle
        private int vehicleID;  // integer to store the unique ID of the vehicle

				// public fields
        public static int nextVehicleID = 1;  // integer to store the ID of the next vehicle to be created, static because it is shared among all instances of the class
        public enum Direction {LEFT, RIGHT};  // enum to represent the direction of a turn, either left or right, which will be used in the turn method

				// constructors
        public Vehicle() {  // no-arg constructor
            currentSpeed = 0;  // initialize the current speed to 0
            currentDirection = 0;  // initialize the current direction to 0
            ownerName = "unknown";  // initialize the owner name to "unknown"
            vehicleID = nextVehicleID;  // assign the next vehicle ID to the vehicle
            nextVehicleID++;  // increment the next vehicle ID for the next vehicle
        }

        public Vehicle(String name) {  // constructor with one argument: owner name
            currentSpeed = 0;  // initialize the current speed to 0
            currentDirection = 0;  // initialize the current direction to 0
            ownerName = name;  // assign the owner name argument to the owner name
            vehicleID = nextVehicleID;  // assign the next vehicle ID to the vehicle
            nextVehicleID++;  // increment the next vehicle ID for the next vehicle
        }

				// public methods
        public void changeSpeed(int speed) {  // method to change the speed of the vehicle, takes an integer argument for the new speed
            currentSpeed = speed;  // assign the argument to the current speed
        }

        public void stop() {  // method to stop the vehicle
            currentSpeed = 0;  // set the current speed to 0
        }

        public void turn(int degrees) {  // method to turn the vehicle, takes an integer argument for the number of degrees to turn
            currentDirection += degrees;  // add the argument to the current direction
        }

        public void turn(Direction direction) {  // method to turn the vehicle, takes an enum argument for the direction to turn
            if (direction == Direction.LEFT) {  // check if the direction is left
                currentDirection -= 90;  // subtract 90 degrees from the current direction, which is equivalent to turning left
            } else {  // if the direction is not left (right)
                currentDirection += 90;  // add 90 degrees to the current direction, which is equivalent to turning right
            }
        }

        public void setOwnerName(String name) {  // method to set the owner name of the vehicle, takes a string argument for the new owner name
            ownerName = name;  // assign the argument to the owner name
        }

        public int getCurrentSpeed() {  // method to get the current speed of the vehicle
            return currentSpeed;  // return the current speed
        }

        public int getCurrentDirection() {  // method to get the current direction of the vehicle
            return currentDirection;  // return the current direction
        }

        public String getOwnerName() {  // method to get the owner name of the vehicle
            return ownerName;  // return the owner name
        }

        public int getVehicleID() {  // method to get the ID of the vehicle
            return vehicleID;  // return the vehicle ID
        }

        public static int maxID() {  // method to get the maximum vehicle ID
            return nextVehicleID - 1;  // return the next vehicle ID minus 1, since the next vehicle ID is always one greater than the maximum vehicle ID in existence
        }

        public String toString() {  // method to return a string representation of the vehicle
            return "Owner: " + ownerName + ", Speed: " + currentSpeed + ", Direction: " + currentDirection;  // return a string with all of the fields of the vehicle, labeled too
        }

				// private methods if you need
}

class VehicleTest {
				public static void main(String[] args) {
								// create Vehicle instances
                // first 5 vehicles are created using no-arg constructor, and their names are set using setOwnerName method
                Vehicle v1 = new Vehicle();
                v1.setOwnerName("bruh1");
                Vehicle v2 = new Vehicle();
                v2.setOwnerName("bruh2");
                Vehicle v3 = new Vehicle();
                v3.setOwnerName("bruh3");
                Vehicle v4 = new Vehicle();
                v4.setOwnerName("bruh4");
                Vehicle v5 = new Vehicle();
                v5.setOwnerName("bruh5");
                // last 5 vehicles are created using constructor with one argument, and their names are set in the constructor
                Vehicle v6 = new Vehicle("lmao");
                Vehicle v7 = new Vehicle("bruh");
                Vehicle v8 = new Vehicle("poggers");
                Vehicle v9 = new Vehicle("Hyunyoung Lee");
                Vehicle v10 = new Vehicle("Joe Biden");

                // create an array of vehicles for easy access
                Vehicle[] vehicles = {v1, v2, v3, v4, v5, v6, v7, v8, v9, v10};

								// test the functionalities you implemented
                // print out the owner names of all vehicles
                System.out.println("Owner Names: ");
                for (Vehicle v : vehicles) {
                    System.out.println(v.getOwnerName());
                }
                
                // change the owner name of the first vehicle and print out the new owner name
                System.out.println("Changing owner name of Vehicle 1: ");
                System.out.println("Vehicle 1 initial owner: " + v1.getOwnerName());
                v1.setOwnerName("bruh lmao");
                System.out.println("Vehicle 1 new owner: " + v1.getOwnerName());

                // print out the vehicle IDs of all vehicles and the maximum vehicle ID
                System.out.println("Vehicle IDs: ");
                for (Vehicle v : vehicles) {
                    System.out.println(v.getVehicleID());
                }

                // print out the maximum vehicle ID
                System.out.println("Max Vehicle ID: " + Vehicle.maxID());

                // test the speed and direction methods
                // print out the initial speed of the first vehicle, change the speed, print the new speed, stop the vehicle, and print the new speed
                System.out.println("Testing speed methods: ");
                System.out.println("Vehicle 1 initial speed: " + v1.getCurrentSpeed());
                System.out.println("Changing speed of Vehicle 1 to 50: ");
                v1.changeSpeed(50);
                System.out.println("Vehicle 1 new speed: " + v1.getCurrentSpeed());
                System.out.println("Stopping Vehicle 1: ");
                v1.stop();
                System.out.println("Vehicle 1 new speed: " + v1.getCurrentSpeed());

                // test the direction methods
                // print out the initial direction of the first vehicle, turn the vehicle 22 degrees, print the new direction, turn the vehicle left, print the new direction, turn the vehicle right, and print the new direction
                System.out.println("Testing direction methods: ");
                System.out.println("Vehicle 1 initial direction: " + v1.getCurrentDirection());
                System.out.println("Turning Vehicle 1 22 degrees: ");
                v1.turn(22);
                System.out.println("Vehicle 1 new direction: " + v1.getCurrentDirection());
                System.out.println("Turning Vehicle 1 left: ");
                v1.turn(Vehicle.Direction.LEFT);
                System.out.println("Vehicle 1 new direction: " + v1.getCurrentDirection());
                System.out.println("Turning Vehicle 1 right: ");
                v1.turn(Vehicle.Direction.RIGHT);
                System.out.println("Vehicle 1 new direction: " + v1.getCurrentDirection());

                // test the toString method by just printing out the first vehicle
                System.out.println("Testing toString on v1: ");
                System.out.println(v1.toString());
				}
}


// Hints on the PassengerVehicle class for Problem 9 of Homework 4
class PassengerVehicle extends Vehicle 
                       implements Comparable<PassengerVehicle> 
{
  // private fields specific to PassengerVehicle such as 
  // total # of seats and occupied seats (both can be of type int, 
  // and properly initialized)
  private int totalSeats;
  private int occupiedSeats;


  /* constructors: Give three constructors, 
     1. one no-arg constructor,
     2. a constructor with one argument: only owner name as an argument,
     3. a constructor with two arguments: owner name and total # of seats

     Probably you already have the first two constructors in the Vehicle
     class, then, invoke the Vehicle class constructor by using `super`
  */
  public PassengerVehicle() {  // no-arg constructor
    super();  // call the no-arg constructor of the superclass to first initialize the fields of the superclass
    totalSeats = 0;  // initialize the total seats to 0
    occupiedSeats = 0;  // initialize the occupied seats to 0
  }

  public PassengerVehicle(String name) {  // constructor with one argument: owner name
    super(name);   // call the constructor of the superclass with one argument to set the owner name
    totalSeats = 0;  // initialize the total seats to 0
    occupiedSeats = 0;  // initialize the occupied seats to 0
  }

  public PassengerVehicle(String name, int seats) {  // constructor with two arguments: owner name and total seats
    super(name);  // call the constructor of the superclass with one argument to set the owner name
    totalSeats = seats;  // assign the total seats argument to the total seats
    occupiedSeats = 0;  // initialize the occupied seats to 0
  }

  /* get methods for the private fields */
  public int getTotalSeats() {  // method to get the total seats of the vehicle
    return totalSeats;  // return the total seats
  }

  public int getOccupiedSeats() {  // method to get the occupied seats of the vehicle
    return occupiedSeats;  // return the occupied seats
  }

  /* set methods for the private fields */
  public void setTotalSeats(int seats) {  // method to set the total seats of the vehicle, takes an integer argument for the new total seats
    totalSeats = seats;  // assign the argument to the total seats
  }

  public void setOccupiedSeats(int seats) {  // method to set the occupied seats of the vehicle, takes an integer argument for the new occupied seats
    occupiedSeats = seats;  // assign the argument to the occupied seats
  }

  // override the toString method (inherited from the Object class) 
  // signature: toString() 
  // @Override
  // ...
  @Override  // override the toString method of the superclass to include the total seats and occupied seats
  public String toString() {
    return super.toString() + ", Total Seats: " + totalSeats + ", Occupied Seats: " + occupiedSeats;  // we can call the toString method of the superclass to get the owner name, speed, and direction, and then add the total seats and occupied seats
  }

  // implement compareTo method (to `implements` Comparable)
  // signature: compareTo(PassengerVehicle)
  @Override  // override the compareTo method of the Comparable interface to compare PassengerVehicle objects based on the total seats
  public int compareTo(PassengerVehicle pv) {
    return this.totalSeats - pv.totalSeats;  // return the difference between the total seats of this PassengerVehicle and the total seats of the other PassengerVehicle, totally ordering the PassengerVehicles by total seats
  }

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
    pVs.add(new PassengerVehicle("Hyunyoung Lee", 1));
    pVs.add(new PassengerVehicle("Joe Biden", 2));
    pVs.add(new PassengerVehicle("Donald Trump", 3));
    pVs.add(new PassengerVehicle("Barack Obama", 4));
    pVs.add(new PassengerVehicle("George W. Bush", 5));

    pVs.get(0).setOccupiedSeats(1);
    pVs.get(1).setOccupiedSeats(2);
    
    Collections.sort(pVs); // Sort the PassengerVehicles 
                           // in an ascending order according to
                           // the compareTo method implementation 

    // Find a way to output the ascending sorted result in descending
    // order. Use a for loop to print out the sorted result 
    // in a descending order
    for (int i = pVs.size() - 1; i >= 0; i--) {  // iterate through the PassengerVehicles in reverse order, since they are sorted in ascending order and we want to print them in descending order
      System.out.println(pVs.get(i));  // print the PassengerVehicle at the current index
    }

  } // end of main

} // end of class PassengerVehicle