
// Written by Hyunyoung Lee for CSCE314 

import static java.lang.System.out;

class A { // by default, extends _______________ [P1.1]
  protected int x = 0xF0; // 0xF0 = _____________ in decimal [P1.2] 
  protected int z;
  public A() {
    z = fun( x );
    out.printf("%x ", z);
  }
  public int fun(int i) { return (i + 1); }
  public static int staticFun(int i) { return (i + 3); }
}

class B extends A {
  protected int y = 0x11;
  public B() {
    z = fun( z );
    out.printf("%x ", z);
  }
  @Override
  public int fun(int i) { return (i + 2); }
  public static int staticFun(int i) { return (i + 4); }

  public static void main(String args[]) {
    int i = 0;
    out.println("[P1.3] Creating B object");
    A a = new B(); // a's type is A but a refers B type object (upcasting)
    out.println(((B)a).y);


    out.println("\n\n[P1.4] a's dynamic/static binding");
    out.print( a.fun( i ) + " ");
    out.println( a.staticFun( i ) );

    out.println("\n[P1.5] Creating another B object");
    B b = new B(); // b's type is B and b refers B type object
    out.println( b.x );

    out.println("\n\n[P1.6] b's dynamic/static binding");
    out.print( b.fun( i ) + " ");
    out.println( b.staticFun( i ) );
  } 
}

