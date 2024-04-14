
/* Written by Hyunyoung Lee for CSCE 314 Students Homework 6 Problem 2 

   Student Name: Kevin Lei
   UIN: 432009232
   Acknowledgements: canvas slides/videos, course textbook
*/

import java.util.*;

public class Market<T> {
  List<T> stock; // stock of the market

  public Market() { stock = new java.util.LinkedList<T>(); }

  void sell(T item) {
    // implement this method
    stock.add(item);  // add the sold item to the end of the stock list
  }
  public T buy() {
    // implement this method
    return stock.remove(0);  // remove the first item from the stock list and return it
  }
  void sell(Collection<? extends T> items) { // modify the parameter type
    // implement this method
    stock.addAll(items);  // add all the items in the collection to the end of the stock list, using the addAll method
  }
  void buy(int n, Collection<T> items) {
    int availableItems = Math.min(n, stock.size()); // determine the number of items that can be bought
    if (n > stock.size()) {  // chekc if the number of items requested is greater than the number of items in stock
        System.out.println("Only bought " + availableItems + " items, the market is now out of stock.");  // print out a message indicating that the market is out of stock and the user only bought the available items
    }

    for (int i = 0; i < availableItems; i++) {  // loop through the number of items that are requested to be bought
        items.add(stock.remove(0));  // add the first item in the stock to the customers basket and remove it from the stock list
    }
  }

} // end of class Market


// Study class Main. You don't need to modify class Main
class Main {
  // three static nested classes expressing example subclass hierarchy
  // Gala <: Apple <: Fruit
  static class Fruit { public String toString () { return "Fruit"; } }
  static class Apple extends Fruit {
                       public String toString () { return "Apple"; }
  }
  static class Gala extends Apple {
                       public String toString () { return "Gala"; }
  }

  public static void main(String args[]) {
    Market<Fruit> farmersmarket = new Market<Fruit> ();

    Deque<Fruit> fruits = new ArrayDeque<Fruit>();
    fruits.addFirst(new Gala());
    fruits.addFirst(new Apple());
    //Fruit a = fruits.remove();
    //if (a instanceof Apple) System.out.println("a is Apple");

    Vector<Apple> apples = new Vector<Apple>();
    apples.addElement(new Apple());
    apples.addElement(new Apple());
    apples.addElement(new Gala());

    farmersmarket.sell(fruits);
    farmersmarket.sell(apples);
    farmersmarket.sell(new Fruit());
    farmersmarket.sell(new Gala());

    ArrayList<Fruit> mybasket = new ArrayList<Fruit>();

    farmersmarket.buy(6, mybasket);

    // print out what you bought
    System.out.println("Here's what I bought");
    for (Fruit e : mybasket) System.out.println(e);
    System.out.println("Enjoy!");
  } // end of main
} // end of class Main

