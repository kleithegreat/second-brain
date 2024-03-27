
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
    super(p0);
    this.side = side;
  }

  // implement equals(), hashCode(), area(), and toString()
  @Override
  public boolean equals(Object o) {  // implement this method and explain your implementation
    if (this == o) return true;
    if (!(o instanceof Square)) return false;
    try {
      Square s = (Square) o;
      return position.equals(s.position) && side == s.side;
    } catch (ClassCastException e) {
      return false;
    }
  }

  @Override
  public int hashCode() {  // implement this method and explain your implementation
    return 31 * (31 + position.hashCode()) + Double.hashCode(side);
  }

  @Override
  public double area() {  // implement this method
    return Math.pow(side, 2);
  }

  @Override
  public String toString() {  // implement this method and explain your implementation
    return "Square with side length " + side + " and upper left corner at " + position.toString();
  }
} // end of class Square

