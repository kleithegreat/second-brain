
/* Skeleton provided by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 2

   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas notes, course textbook
*/

public final class Point {
  public double x;
  public double y;

  // constructor that sets the values of x and y
  public Point(double x, double y) {  // implement the constructor
    this.x = x;  // set the value of x to the parameter x
    this.y = y;  // set the value of y to the parameter y
  }

  // implement equals, hashCode(), toString()
  @Override
  public boolean equals(Object s) { // implement the method and explain your implementation
    if (this == s) return true;  // if the object is the same as the argument, return true
    if (!(s instanceof Point)) return false;  // check if the argument is an instance of Point, if not return false
    try {
      Point p = (Point) s;  // attempt to cast the argument to a Point object
      return x == p.x && y == p.y;  // return true if the x and y values are the same
    } catch (ClassCastException e) {  // catch the exception if the argument cannot be cast to a Point object
      return false;  // return false if the argument cannot be cast to a Point object
    }
  }

  @Override
  public int hashCode() { // implement the method and explain your implementation
    return 31 * (31 + Double.hashCode(x)) + Double.hashCode(y);  // use prime number 31 and the hashCode function of Double to generate a unique hash code
  }

  @Override
  public String toString() { // implement the method and explain your implementation
    return "(" + x + ", " + y + ")";  // return a string representation of the Point object, which is the x and y values in parentheses
  }
} // end of class Point
