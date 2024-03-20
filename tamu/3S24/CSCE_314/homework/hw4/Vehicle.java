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
        private int currentSpeed;
        private int currentDirection;
        private String ownerName;
        private int vehicleID;

				// public fields
        public static int nextVehicleID = 1;
        public enum Direction {LEFT, RIGHT};

				// constructors
        public Vehicle() {
            currentSpeed = 0;
            currentDirection = 0;
            ownerName = "unknown";
            vehicleID = nextVehicleID;
            nextVehicleID++;
        }

        public Vehicle(String name) {
            currentSpeed = 0;
            currentDirection = 0;
            ownerName = name;
            vehicleID = nextVehicleID;
            nextVehicleID++;
        }

				// public methods
        public void changeSpeed(int speed) {
            currentSpeed = speed;
        }

        public void stop() {
            currentSpeed = 0;
        }

        public void turn(int degrees) {
            currentDirection += degrees;
        }

        public void turn(Direction direction) {
            if (direction == Direction.LEFT) {
                currentDirection -= 90;
            } else {
                currentDirection += 90;
            }
        }

        public void setOwnerName(String name) {
            ownerName = name;
        }

        public int getCurrentSpeed() {
            return currentSpeed;
        }

        public int getCurrentDirection() {
            return currentDirection;
        }

        public String getOwnerName() {
            return ownerName;
        }

        public int getVehicleID() {
            return vehicleID;
        }

        public static int maxID() {
            return nextVehicleID - 1;
        }

        public String toString() {
            return "Owner: " + ownerName + ", Speed: " + currentSpeed + ", Direction: " + currentDirection;
        }

				// private methods if you need
}

class VehicleTest {
				public static void main(String[] args) {
								// create Vehicle instances
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
                Vehicle v6 = new Vehicle("lmao");
                Vehicle v7 = new Vehicle("bruh");
                Vehicle v8 = new Vehicle("poggers");
                Vehicle v9 = new Vehicle("Hyunyoung Lee");
                Vehicle v10 = new Vehicle("Joe Biden");

                Vehicle[] vehicles = {v1, v2, v3, v4, v5, v6, v7, v8, v9, v10};

								// test the functionalities you implemented
                System.out.println("Owner Names: ");
                for (Vehicle v : vehicles) {
                    System.out.println(v.getOwnerName());
                }

                System.out.println("Changing owner name of Vehicle 1: ");
                System.out.println("Vehicle 1 initial owner: " + v1.getOwnerName());
                v1.setOwnerName("bruh lmao");
                System.out.println("Vehicle 1 new owner: " + v1.getOwnerName());

                System.out.println("Vehicle IDs: ");
                for (Vehicle v : vehicles) {
                    System.out.println(v.getVehicleID());
                }

                System.out.println("Max Vehicle ID: " + Vehicle.maxID());

                System.out.println("Testing speed methods: ");
                System.out.println("Vehicle 1 initial speed: " + v1.getCurrentSpeed());
                System.out.println("Changing speed of Vehicle 1 to 50: ");
                v1.changeSpeed(50);
                System.out.println("Vehicle 1 new speed: " + v1.getCurrentSpeed());
                System.out.println("Stopping Vehicle 1: ");
                v1.stop();
                System.out.println("Vehicle 1 new speed: " + v1.getCurrentSpeed());

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
  public PassengerVehicle() {
    super();
    totalSeats = 0;
    occupiedSeats = 0;
  }

  public PassengerVehicle(String name) {
    super(name);
    totalSeats = 0;
    occupiedSeats = 0;
  }

  public PassengerVehicle(String name, int seats) {
    super(name);
    totalSeats = seats;
    occupiedSeats = 0;
  }

  /* get methods for the private fields */
  public int getTotalSeats() {
    return totalSeats;
  }

  public int getOccupiedSeats() {
    return occupiedSeats;
  }

  /* set methods for the private fields */
  public void setTotalSeats(int seats) {
    totalSeats = seats;
  }

  public void setOccupiedSeats(int seats) {
    occupiedSeats = seats;
  }

  // override the toString method (inherited from the Object class) 
  // signature: toString() 
  // @Override
  // ...
  @Override
  public String toString() {
    return super.toString() + ", Total Seats: " + totalSeats + ", Occupied Seats: " + occupiedSeats;
  }

  // implement compareTo method (to `implements` Comparable)
  // signature: compareTo(PassengerVehicle)
  @Override
  public int compareTo(PassengerVehicle pv) {
    return this.totalSeats - pv.totalSeats;
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
    
    Collections.sort(pVs); // Sort the PassengerVehicles 
                           // in an ascending order according to
                           // the compareTo method implementation 

    // Find a way to output the ascending sorted result in descending
    // order. Use a for loop to print out the sorted result 
    // in a descending order

  } // end of main

} // end of class PassengerVehicle