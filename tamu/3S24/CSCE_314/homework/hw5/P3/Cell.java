/* Cell.java skeleton written by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 3 

   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas notes, course textbook, java docs linked in instructions
*/

import java.lang.Iterable;
import java.util.Iterator;
import java.util.NoSuchElementException;

// class Cell: 10 points
// give correct class header - given in the problem statement
public final class Cell<E> implements Iterable<E>{ // modify this header
  // private fields
  private E elem; // stores a value of type E
  private Cell<E> next; // link to the next Cell

  // constructor
  public Cell(E elem, Cell<E> next) {
    // implement this constructor
    this.elem = elem;  // set the value of elem to the argument elem
    this.next = next;  // set the value of next to the argument next
  }

  // iterator() returns a CellIterator object for this object
  @Override
  public CellIterator<E> iterator() {
    // implement this method and explain
    return new CellIterator<E>(this);  // return a new CellIterator object with the current cell object
  }

  // getter and setter methods for the private fields
  public E getVal() {
    // implement this method
    return elem;  // return the value of elem
  }

  public void setVal(E v) {
    // implement this methodn
    this.elem = v;  // set the value of elem to the argument v
  }

  public Cell<E> getNext() {
    // implement this method
    return next;  // return the next cell
  }

  public void setNext(Cell<E> node) {
    // implement this method
    this.next = node;  // set the next cell to the argument node
  }

  // CellIterator: 20 points
  // Having CellIterator as an inner class of Cell makes sense...
  // (2 points) correct class header - given in the problem statement
  class CellIterator<E> implements Iterator<E>{ // modify this header
    private Cell<E> p; // given

    // (3 points) constructor
    public CellIterator(Cell<E> n) {
      // implement this constructor
      this.p = n;  // set the value of p to the argument n
    }

    // (5+10=15 points) two methods to implement the Iterator interface
    // (5 points) hasNext()
    @Override
    public boolean hasNext() {
      // implement this method and explain
      return p != null;  // return true if the current cell is not null, false otherwise
    }

    // (10 points) next()
    @Override
    public E next() {
      // implement this method and explain
      if (!hasNext()) {  // check if there is a next cell
        throw new NoSuchElementException();  // if there is no next cell, throw a NoSuchElementException which is required by the Iterator interface
      }
      E val = p.getVal();  // save the value of the current cell
      p = p.getNext();  // move to the next cell
      return val;  // return the value of the just iterated cell
    }

  } // end of CellIterator
} // end of Cell