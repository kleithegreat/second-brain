/* CellTest.java skeleton written by Hyunyoung Lee 
   CSCE 314 [Sections 595, 596, 597] Spring 2024  
   Homework 5 Problem 3 Test class 
   class CellTest

   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas notes, course textbook
*/

public class CellTest {

  // 15 points for the three methods: int_sum, num_sum, print
  // implement int_sum
  static int int_sum(Cell<Integer> list) {
    if (list == null) return 0;  // return 0 if the list is null, otherwise it would cause an error

    Integer sum = 0;  // initialize sum to 0
    for (Integer i : list) {  // iterate through the list
      sum += i;  // add each value to the sum
    }

    return sum;  // return the sum
  }

  // implement num_sum
  static double num_sum(Cell<? extends Number> list) {
    if (list == null) return 0;  // return 0 if the list is null for the same reason as before

    double sum = 0;  // initialize sum to 0
    for (Number n : list) {  // iterate through the list
      sum += n.doubleValue();  // add the double value of each number to the sum, since we need to specifically add doubles
    }

    return sum;  // return the sum
  }

  // implement print
  static <E> void print(Cell<E> list) {
    for (E e : list) {  // iterate through the list
      System.out.print(e + " ");  // print each element with a space
    }
    System.out.println();  // print a newline at the end
  }
	
  // Feel free to "expand" the main method but do not delete whatever provided 
  public static void main (String args[]) {
    Cell<Integer> intlist = 
        new Cell<Integer>(1, 
          new Cell<Integer>(22, 
            new Cell<Integer>(21, 
              new Cell<Integer>(12, 
                new Cell<Integer>(24, 
                  new Cell<Integer>(17, null))))));
        
    Cell<Integer> nullintlist = null;

    System.out.println("===");
    print(intlist);
    System.out.println("sum of intlist is " + int_sum(intlist));
    System.out.println("sum of null list is " + int_sum(nullintlist));
    System.out.println("===");

    Cell<Double> doublelist = 
        new Cell<Double>(1., 
          new Cell<Double>(16., 
            new Cell<Double>(13.72, 
              new Cell<Double>(5., 
                new Cell<Double>(22., 
                  new Cell<Double>(7.1, null))))));

    System.out.println("===");
    print(doublelist);
    System.out.println("sum ints = " + num_sum(intlist));
    System.out.println("sum doubles = " + num_sum(doublelist));
    System.out.println("===");
  }
}