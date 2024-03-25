
/*   
   CellList.java skeleton written by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 4

   Student Name:
   UIN:
   Acknowledgements:
*/

import java.util.Arrays;
import java.util.Iterator;

// Total 40 points for the CellList class

public class CellList<E> implements Iterable<E>, Cloneable, Comparable<CellList<E>> {   
  private Cell<E> n;
  private int length;

  @Override
  public Iterator<E> iterator() { return n.iterator(); }

  // Task 1: override clone() (5 points)
  @Override
  public CellList<E> clone() {
		// Implement this method and explain
		}

	 @Override
  public int compareTo(CellList<E> list) { 
    if (this.length < list.length) return -1;
    if (this.length == list.length) return 0;
    return 1; 
  }

  // Task 2: override equals() (10 points) 
	 @Override
  public boolean equals(Object o) {
		// Implement this method and explain (read the equality criteria in the
		// problem statement carefully!)
		}

  @Override
  public int hashCode() {
    return length;
  }

  // no-arg constructor - given
  public CellList() { n = null; length = 0; }
    
  // Task 3: one-arg constructor (5 points)
  public CellList(Iterable<E> iterable) {
		// implement this constructor
		}

				
  // Task 4: total 20 points for toString(), push() and pop()
  // 8 points
  public String toString() {
		// implement this method
  }

  // 5 points
  public void push(E item) {
  // implement this method
		}

  // 7 points
  public E pop() {
  // implement this method
		}

  // given 
  public E peek() { return n.getVal(); }

  // given 
  public int getLength() { return length; }
}

