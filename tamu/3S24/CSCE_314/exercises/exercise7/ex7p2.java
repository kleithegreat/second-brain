//***
// Written by Hyunyoung Lee for CSCE314 students for Exercise 7
// To illustrate dynamic / static binding of Java
// In Java, static binding occurs at compile time and 
//          dynamic binding at run time (when the object is created 
//          by using the "new" keyword).
// Static binding adheres to the "type" of the object reference,
// thus, below, o1 and o2 both have static binding of A, whereas o3 of B.
// Dynamic binding is according to the actual "object" the object reference
// is referring to, thus, below, o1's dynamic binding is to the object of 
// type A whereas o2's and o3's dynamic binding is to the object of type B
// that is, dynamic dispatch of B's methods (unless the method is explicitly 
// defined static, in which case the method associates to the class, not to
// individual object instances).
//
// To compile (at the terminal prompt):
//    javac ex7p2.java
// To run (after compiling):
//    java Main
//***

class A {
  void go() { System.out.println("buy"); } // dynamic binding
  static void to(A x) { System.out.println("kiwi"); } // static binding
  static void to(B x) { System.out.println("fig");  } // static binding
}
class B extends A {
  void go() { System.out.println("eat"); } // dynamic binding
  static void to(A x) { System.out.println("apple"); } // static binding
  static void to(B x) { System.out.println("pear");  } // static binding
}
class Main {
  public static void main(String[] args) {
    A o1 = new A(); // o1's type (static binding) is A and 
                    // o1 refers to an object of type A (dynamic binding)
    A o2 = new B(); // o2's type (static binding) is A but
                    // o2 refers to an object of type B (dynamic binding)
    B o3 = new B(); // o2's type (static binding) is A but
                    // o2 refers to an object of type B (dynamic binding)

    o1.go();   // output1 ______________
    o2.go();   // output2 ______________
    o3.go();   // output3 ______________

    o1.to(o1); // output4 ______________
    o2.to(o2); // output5 ______________
    o3.to(o3); // output6 ______________

    o1.to(o3); // output7 ______________
    o3.to(o1); // output8 ______________
  }
}

