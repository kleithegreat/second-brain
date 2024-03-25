
/* 
   CellListTest.java skeleton written by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 4
   Feel free to "expand" the main, but do not remove the original contents

   Student Name:
   UIN:
   Acknowledgements:
*/

import java.util.Iterator;
import java.util.Arrays;
import static java.lang.System.out; 

public class CellListTest {
  public static void main (String args[]) {
    CellList<Integer> empty_list = new CellList<Integer>();
    CellList<Integer> list = new CellList<Integer>(Arrays.asList(1,2,3,4));
    CellList<Integer> list1 = new CellList<Integer>(Arrays.asList(2,4,3,1));
    CellList<Integer> list2 = new CellList<Integer>(list.clone()); 

    CellList<Integer> list3 = new CellList<Integer>(Arrays.asList(1,2,3,1));
    CellList<Integer> list4 = new CellList<Integer>(Arrays.asList(1,2,3,1,4));

    CellList<String> stringlist = 
        new CellList<String>(Arrays.asList("A", "the", "the", "dove"));
    CellList<String> stringlist2 = 
        new CellList<String>(Arrays.asList("A", "dove", "the", "the"));
    CellList<String> stringlist3 = 
        new CellList<String>(Arrays.asList("A", "dove", "dove", "the"));


    out.println("stringlist = " + stringlist);
    out.println("stringlist2 = " + stringlist2);
    out.println("stringlist3 = " + stringlist3);
    out.println("stringlist equals to stringlist2 ? " + 
                 stringlist.equals(stringlist2));
 
    out.println("stringlist equals to stringlist3 ? " + 
                 stringlist.equals(stringlist3));

    out.println("CellList<Integer> equals to CellList<String> ? " + 
                 list.equals(stringlist));
 
    out.println("list  = " + list);
    out.println("list1 = " + list1);

    if (list == list1) out.println("list == list1 is true");
    else out.println("list == list1 is false");

    out.println("list.equals(list1) = " + list.equals(list1));
    out.println("list3 = " + list3);
    out.println("list4 = " + list4);
    out.println("list1.equals(list3) = " + list1.equals(list3));
    out.println("list1.equals(list4) = " + list1.equals(list4));
    out.println("list.compareTo(list1) = " + list.compareTo(list1));
    out.println("list.compareTo(list4) = " + list.compareTo(list4));
    out.println(empty_list);
    out.println(list);
    out.println(list.pop());
    list.push(21);
    list.push(22);
    out.println(list);
    out.println(list.peek());
    out.println(list);
    for (int i : list) {
      list2.push(i); 
      out.println(i + " " + list.pop());
    }
    out.println(list);
    out.println("list1 = " + list1);
    out.println("list2 = " + list2);
    out.println("list2.compareTo(list1) = " + list2.compareTo(list1));
    out.println("=== end of test");
  } // end of main()
}

