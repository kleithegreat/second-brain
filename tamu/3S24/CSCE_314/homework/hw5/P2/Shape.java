
/* Skeleton provided by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 2
 
   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas notes, course textbook
*/

abstract class Shape implements Comparable<Shape> {
  public Point position;
  public double area;
    
  // constructor that sets position as the Point passed as an argument
  // signature: Shape (Point)
  // implement the constructor
  public Shape(Point p)
  {
    position = p;  // set the value of position to the argument p
  }

  // implement equals()
  @Override
  public boolean equals(Object o) {  // implement this method and explain your implementation
    if (this == o) return true;  // if the object is the same as the argument, return true
    if (!(o instanceof Shape)) return false;  // check if the argument is an instance of Shape, if not return false
    try {  // attempt to cast the argument to a Shape object
      Shape s = (Shape) o;  // try to cast the argument to a Shape object
      return position.equals(s.position) && area == s.area;  // return true if the position and area values are the same
    } catch (ClassCastException e) {  // catch the exception if the argument cannot be cast to a Shape object
      return false;  // return false in this case
    }
  }

  // area() should be abstract
  public abstract double area();
 
  // implement compareTo()
	@Override
  public int compareTo(Shape s) {  // implement this method and explain your implementation
    return Double.compare(area, s.area);  // compare the area values of the two Shape objects using the Double.compare method, which signifies the order of the two objects using a signed integer
  }
} // end of class Shape