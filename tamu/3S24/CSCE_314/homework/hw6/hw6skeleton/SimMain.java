 
/* Written by Hyunyoung Lee for CSCE 314 Students Homework 6 Problem 3
   This test code better not be modified.
*/

class SimMain {
  static void pause(long n) {
    try { Thread.sleep(n); } catch (InterruptedException e) {}
  }

  public static void main (String[] args) {
    final String homer = "Homer"; // "My doctor said don't walk."
    final String marge = "Marge"; // "That was a traffic signal!"
    final String bart  = "Bart";  // "There’s a 4:30 in the morning now?"

    final SimBox sHomer = new SimBox(homer);
    final SimBox sMarge = new SimBox(marge, sHomer); // shares sHomer.messages
    final SimBox sBart  = new SimBox(bart, sHomer);  // shares sHomer.messages

    // send out some messages on another thread
    new Thread( new Runnable() {
      public void run() {
        sHomer.send(marge, "My doctor said don't walk."); pause(1000);
        sMarge.send(homer, "That was a traffic signal!"); pause(500);
        String msg = "There’s a 4:30 in the morning now?";
        sBart.send(homer, msg); pause(500);
        sHomer.send(bart, "D'oh!"); pause(500);
        //sBart.send(homer, msg);
        for (int i=0; i<20; ++i) {
            sBart.send(homer, "flooding the message queue...");
        }
      } // end run()
    } ).start();

    SimBox[] simpsons = { sMarge, sHomer, sBart };
    long startTime = System.currentTimeMillis();

    // poll for messages in a tight loop for 5 secs
    while (true) {
      for (SimBox aSimpson : simpsons)
        for (String m : aSimpson.retrieve()) System.out.println(m);              
      if (System.currentTimeMillis() - startTime > 5000) break;
    } // endwhile

    // stop each mailbox
    for (SimBox aSimpson : simpsons) { aSimpson.stop(); }
  } // end main()
} // end class SimMain

