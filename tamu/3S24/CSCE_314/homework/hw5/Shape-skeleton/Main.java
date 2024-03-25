
/* Main (file input function) provided by Hyunyoung Lee
   For CSCE 314 [Sections 595, 596, 597] Spring 2024, Assignment 5 Problem 2
   The student is supposed to add the part that outputs the sorted shapes 
   (see below).

   Student Name:
   UIN:
   Acknowledgements:
*/

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.Scanner;
import static java.lang.System.*;

public class Main {
  public static Shape[] shapes; // using an array is a requirement

  public static Point readPoint(Scanner scan)
  { String point = scan.next();
    //out.println(point);
    Scanner aPoint = new Scanner(point).useDelimiter("\\s*,\\s*");
    double x = aPoint.nextDouble();
    double y = aPoint.nextDouble();
    //  out.println("double " + x);
    //  out.println("double " + y);
    return new Point(x, y);
  }
 
  public static Square readSquare(Scanner scan)
  {
    Point p1 = readPoint(scan);
    String dbls = scan.next();
    Scanner dblScan = new Scanner(dbls);
    Double len = dblScan.nextDouble();
    return new Square(p1, len);
  }

  public static Circle readCircle(Scanner scan)
  {
    Point p1 = readPoint(scan);
    String dbls = scan.next();
    Scanner dblScan = new Scanner(dbls);  

    Double r = dblScan.nextDouble();
    //out.println("double " + r);
    return new Circle(p1, r);
  }

  public static Shape[] fileInputShapes(String inFileName) 
    throws IOException {
  // read in the shape specifications from infile,
  // construct the shapes and store them in a Shape array
  // This method is essentially "parsing" the input shapes,
  // and involves quite some thought.
    out.println(inFileName);
    File infile = new File(inFileName);
    String delim = "\\s*;[\\s*\\n]*";
    //FileInputStream fi = null;
    int arrSize = 0;
    Scanner fs = new Scanner(infile).useDelimiter(delim);
 
    String s = null;
    while (fs.hasNext()) {
      ++arrSize;
      s = fs.next();
      out.println(s); 
    }
    out.println("The input file contains " + arrSize + " shapes.");  
    shapes = new Shape[arrSize]; // we now know how many shapes are in input

    fs = new Scanner(infile).useDelimiter(delim);
    int i = 0;
    String aShape = null;
    while (fs.hasNext()) {
      aShape = fs.next();
      aShape.trim();
      //out.println("aShape = "+aShape);
      Scanner inAShape = new Scanner(aShape).useDelimiter("\\s*[()]\\s*");
      String kind = inAShape.next();
      //out.println( kind );
      switch( kind )
      {
						  case "s": shapes[i] = readSquare(inAShape);
                  //out.println(shapes[i]);
                  break;
        case "c": shapes[i] = readCircle(inAShape);
                  //out.println(shapes[i]);
                  break;
      }
      shapes[i].area = shapes[i].area();
      ++i;
    }
    out.println(shapes.length +" shapes have been created");
    
    //for (Shape e : shapes) out.println(e);

    fs.close(); // important to close the handle 
    return shapes;
  }

  public static void main (String args[]) {
				try {
				if (args.length == 2 && args[0].equals("S")) {
      //out.println(args[1]);
      shapes = fileInputShapes( args[1] );
						for (Shape e : shapes) { out.println(e); }
				}
				else System.err.println("Usage: "+
																												"java Main S input_file_name\n");
    }
    catch (IOException e) {}

				
  // Task 10.
		// Sort the shapes according to their area and output them nicely in 
  // an ascending order of area 

  // output the total area of all the shapes

  } // end of main()
} // end of class Main

