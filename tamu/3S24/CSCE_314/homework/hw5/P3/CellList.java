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
    if (n == null) return null;  // return null if the list is empty
    return n.iterator();  // call the iterator() method of the head cell and return it
  }

  // Task 1: override clone() (5 points)
  @Override
  public CellList<E> clone() {
    // Implement this method and explain
    if (length == 0) return new CellList<E>();  // return an empty list if the original list is empty
    return new CellList<E>(this);  // use the one-arg constructor to create a new list with the same elements
  }

  @Override
  public int compareTo(CellList<E> list) {
    if (this.length < list.length) return -1;  // return -1 if this list is shorter
    if (this.length == list.length) return 0; // return 0 if the lists are the same length
    return 1; // return 1 if this list is longer
  }

  // Task 2: override equals() (10 points)
  @Override
  public boolean equals(Object o) {
    // Implement this method and explain (read the equality criteria in the
    // problem statement carefully!)
    if (o == this) return true;  // return true if the objects are the same

    if (!(o instanceof CellList)) return false;  // return false if the argument object isnt a CellList
    if (this.length != ((CellList) o).hashCode()) return false;  // return false if the lengths are different
    if (this.length == 0) return true;  // return true if both lists are empty, give the conditions above

    Object[] thisArray = new Object[this.length];  // create arrays to store the elements of the lists so we can sort them and compare later
    Object[] oArray = new Object[this.length];  // do the same for the argument list

    int i = 0;  // initialize the index variable
    for (E item : this) {  // use a for each loop to iterate through the elements of the list in this object
      thisArray[i] = item;  // add the element to the array
      i++;  // increment the index
    }

    i = 0;  // reset the index
    for (Object item : (CellList) o) {  // use a for each loop again for the argument list
      oArray[i] = item;  // add the element to the array for the argument list
      i++;  // increment the index
    }

    Arrays.sort(thisArray);  // sort the arrays
    Arrays.sort(oArray);  // do the same for the argument array

    for (int j = 0; j < this.length; j++) {  // iterate through the arrays
      if (!thisArray[j].equals(oArray[j])) return false;  // return false if the elements arent equal
    }

    return true;  // return true if all the elements are equal and the lists are the same length
  }

  @Override
  public int hashCode() {
    return length;  // return the length of the list as the hash code
  }

  // no-arg constructor - given
  public CellList() {
    n = null;
    length = 0;
  }

  // Task 3: one-arg constructor (5 points)
  public CellList(Iterable<E> iterable) {
    // implement this constructor
    this.n = null;  // initialize the head of the list to null
    this.length = 0;  // initialize the length of the list to 0

    if (iterable != null) {  // we will need to change the head and length if the iterable is not null
      for (E item : iterable) {  // use a for each loop to iterate through the elements of the iterable argument
        Cell<E> newNode = new Cell<E>(item, null);  // create a new cell with the element and a null next pointer
        if (this.n == null) {  // if the head of the list is null, set the head to the new node and increment the length
          this.n = newNode;  // set the head to the new node
          length++;  // increment the length
        } else {  // if the head is not null, we need to find the last node and set its next pointer to the new node
          Cell<E> current = this.n;  // create a pointer to the head of the list
          while (current.getNext() != null) {  // iterate through the list until we reach the last node
            current = current.getNext();  // move the pointer to the next node
          }
          current.setNext(newNode);  // set the next pointer of the last node to the new node
          length++;  // increment the length
        }
      }
    }
  }

  // Task 4: total 20 points for toString(), push() and pop()
  // 8 points
  public String toString() {
    // implement this method
    if (length == 0) return "[(head: )]";  // return an empty list if the list is empty
    String result = "[(head: ";  // initialize the result string
    for (E item : this) {  // use a for each loop to iterate through the elements of the list
      result += item + ") -> (";  // add the element to the result string with some formatting
    }
    result = result.substring(0, result.length() - 5);  // remove the last arrow from the string
    result += "]";  // add the closing bracket
    return result;  // return the resulting string representation of the list
  }

  // 5 points
  public void push(E item) {
    // implement this method
    Cell<E> newNode = new Cell<E>(item, n);  // create a new cell with the element and the current head of the list as the next pointer, since this is supposed to function like the haskell cons operator
    n = newNode;  // set the head of the list to the new node
    length++;  // increment the length
  }

  // 7 points
  public E pop() {
    // implement this method
    if (length == 0) return null;  // return null if the list is empty
    E result = n.getVal();  // store the value of the head of the list
    n = n.getNext();  // set the head of the list to the next node
    length--;  // decrement the length
    return result;  // return the value of the former head of the list
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
