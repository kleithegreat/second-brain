
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
    super(p0);  // call the constructor of the superclass to initialize the position
    radius = r;  // set the value of radius to the argument r
  }

  // implement equals(), hashCode(), area(), and toString()
  @Override
  public boolean equals(Object o) {  // implement this method and explain your implementation
    if (this == o) return true;  // if the object is the same as the argument, return true
    if (!(o instanceof Circle)) return false;  // check if the argument is an instance of Circle, if not return false
    try {  // attempt to cast the argument to a Circle object
      Circle c = (Circle) o;  // try to cast the argument to a Circle object
      return position.equals(c.position) && radius == c.radius;  // return true if the position and radius values are the same
    } catch (ClassCastException e) {  // catch the exception if the argument cannot be cast to a Circle object
      return false;  // return false in this case
    }
  }

  @Override
  public int hashCode() {  // implement this method and explain your implementation
    return 31 * (31 + position.hashCode()) + Double.hashCode(radius);  // return the hash code of the position and radius values
  }

  @Override
  public double area() {  // implement this method 
    return Math.PI * Math.pow(radius, 2);  // return the area of the circle, which is pi times the radius squared
  }

  @Override
  public String toString() {  // implement this method and explain your implementation
    return "Circle with radius " + radius + " and center at " + position.toString();  // return a string that describes the circle
  }
} // end of class Circle