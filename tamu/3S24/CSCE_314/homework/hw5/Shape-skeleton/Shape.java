
/* Skeleton provided by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 2
 
   Student Name:
   UIN:
   Acknowledgements:
*/

abstract class Shape implements Comparable<Shape> {
  public Point position;
  public double area;
    
  // constructor that sets position as the Point passed as an argument
  // signature: Shape (Point)
  // implement the constructor

  // implement equals()
  @Override
  public boolean equals(Object o)
  {  // implement this method and explain your implementation
  }

  // area() should be abstract
  public abstract double area();
 
  // implement compareTo()
		@Override
  public int compareTo(Shape s)
  {  // implement this method and explain your implementation
  }
} // end of class Shape




