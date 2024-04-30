/* Skeleton provided by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 2
 
   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas notes, course textbook
*/

class TotalAreaCalculator {
  public static double calculate(Shape[] shapes) {
  // for each shape in the shapes array,   
  // invoke the object's area() method,
  // summing up the areas
  // and finally returns the total area
    double totalArea = 0; // starting total area at 0
    for (Shape s : shapes) {  // iterate through the shapes array
      totalArea += s.area();  // add the area of the current shape to the total area
    }
    return totalArea;  // return the total area
  }
}