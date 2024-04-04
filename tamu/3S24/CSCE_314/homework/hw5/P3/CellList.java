/*   
   CellList.java skeleton written by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 4

   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas notes, course textbook
*/

import java.util.Arrays;
import java.util.Iterator;

// Total 40 points for the CellList class

public class CellList<E> implements Iterable<E>, Cloneable, Comparable<CellList<E>> {
  private Cell<E> n;
  private int length;

  @Override
  public Iterator<E> iterator() {
    return n.iterator();
  }

  // Task 1: override clone() (5 points)
  @Override
  public CellList<E> clone() {
    // Implement this method and explain
    CellList<E> clone = new CellList<E>();
    Cell<E> current = n;
    for (E item : this) {
      clone.push(item);
    }
    return clone;
  }

  @Override
  public int compareTo(CellList<E> list) {
    if (this.length < list.length)
      return -1;
    if (this.length == list.length)
      return 0;
    return 1;
  }

  // Task 2: override equals() (10 points)
  @Override
  public boolean equals(Object o) {
    // Implement this method and explain (read the equality criteria in the
    // problem statement carefully!)
    if (o == this) return true;
    if (o == null || this.getClass() != o.getClass()) return false;

    CellList<E> otherList = (CellList<E>) o;
    if (otherList.hashCode() != this.hashCode()) return false;

    Object[] thisArray = new Object[this.length];
    Object[] otherArray = new Object[otherList.hashCode()];

    int i = 0;
    for (E item : this) {
      thisArray[i] = item;
      i++;
    }

    i = 0;
    for (E item : otherList) {
      otherArray[i] = item;
      i++;
    }

    Arrays.sort(thisArray);
    Arrays.sort(otherArray);
    
    return Arrays.equals(thisArray, otherArray);
  }

  @Override
  public int hashCode() {
    return length;
  }

  // no-arg constructor - given
  public CellList() {
    n = null;
    length = 0;
  }

  // Task 3: one-arg constructor (5 points)
  public CellList(Iterable<E> iterable) {
    // implement this constructor
    for (E item : iterable) {
      this.push(item);
    }
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
  public E peek() {
    return n.getVal();
  }

  // given
  public int getLength() {
    return length;
  }
}
