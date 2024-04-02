
/* Skeleton provided by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 2

   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas notes, course textbook
*/

import java.lang.Math;

class Square extends Shape {
  private double side; // side is the side length

  // constructor that accepts a Point (for position) and a double
  // (for the side length).
  public Square(Point p0, double side) {  // implement the constructor
    super(p0);  // call the constructor of the superclass to initialize the position
    this.side = side;  // set the value of side to the argument side
  }

  // implement equals(), hashCode(), area(), and toString()
  @Override
  public boolean equals(Object o) {  // implement this method and explain your implementation
    if (this == o) return true;  // if the object is the same as the argument, return true
    if (!(o instanceof Square)) return false;  // check if the argument is an instance of Square, if not return false
    try {  // attempt to cast the argument to a Square object
      Square s = (Square) o;  // try to cast the argument to a Square object
      return position.equals(s.position) && side == s.side;  // return true if the position and side values are the same
    } catch (ClassCastException e) {  // catch the exception if the argument cannot be cast to a Square object
      return false;  // return false in this case
    }
  }

  @Override
  public int hashCode() {  // implement this method and explain your implementation
    return 31 * (31 + position.hashCode()) + Double.hashCode(side);  // return the hash code of the position and side values
  }

  @Override
  public double area() {  // implement this method
    return Math.pow(side, 2);  // return the area of the square, which is the side length squared
  }

  @Override
  public String toString() {  // implement this method and explain your implementation
    return "Square with side length " + side + " and upper left corner at " + position.toString();  // return a string that describes the square
  }
} // end of class Square