
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
    this.x = x;
    this.y = y;
  }

  // implement equals, hashCode(), toString()
  @Override
  public boolean equals(Object s) { // implement the method and explain your implementation
    if (this == s) return true;
    if (!(s instanceof Point)) return false;
    try {
      Point p = (Point) s;
      return x == p.x && y == p.y;
    } catch (ClassCastException e) {
      return false;
    }
  }

  @Override
  public int hashCode() { // implement the method and explain your implementation
    return 31 * (31 + Double.hashCode(x)) + Double.hashCode(y);
  }

  @Override
  public String toString() { // implement the method and explain your implementation
    return "(" + x + ", " + y + ")";
  }
} // end of class Point
