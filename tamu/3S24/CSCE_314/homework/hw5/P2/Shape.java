
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
    position = p;
  }

  // implement equals()
  @Override
  public boolean equals(Object o) {  // implement this method and explain your implementation
    if (this == o) return true;
    if (!(o instanceof Shape)) return false;
    try {
      Shape s = (Shape) o;
      return position.equals(s.position) && area == s.area;
    } catch (ClassCastException e) {
      return false;
    }
  }

  // area() should be abstract
  public abstract double area();
 
  // implement compareTo()
		@Override
  public int compareTo(Shape s) {  // implement this method and explain your implementation
    return Double.compare(area, s.area);
  }
} // end of class Shape




