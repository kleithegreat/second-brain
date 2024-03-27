
/* Skeleton provided by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 2

   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas notes, course textbook
*/

import java.lang.Math;

class Circle extends Shape {
  private double radius;

  // constructor that accepts a Point (for position) and a double
  // (for the radius).
  public Circle(Point p0, double r) {  // implement the constructor
    super(p0);
    radius = r;
  }

  // implement equals(), hashCode(), area(), and toString()
  @Override
  public boolean equals(Object o) {  // implement this method and explain your implementation
    if (this == o) return true;
    if (!(o instanceof Circle)) return false;
    try {
      Circle c = (Circle) o;
      return position.equals(c.position) && radius == c.radius;
    } catch (ClassCastException e) {
      return false;
    }
  }

  @Override
  public int hashCode() {  // implement this method and explain your implementation
    return 31 * (31 + position.hashCode()) + Double.hashCode(radius);
  }

  @Override
  public double area() {  // implement this method 
    return Math.PI * Math.pow(radius, 2);
  }

  @Override
  public String toString() {  // implement this method and explain your implementation
    return "Circle with radius " + radius + " and center at " + position.toString();
  }
} // end of class Circle

