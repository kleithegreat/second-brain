/*
    CSCE 314 Homework 4
    
    Student Name: Kevin Lei
    Student UIN: 432009232
    Acknowledgements: course textbook
*/

import java.util.Scanner;

class SubsetOutputFib {
    static final int MAX_INDEX = 9;

    public static void main(String[] args) {
        int be;  // declare integer variable to store the beginning index
        int en;  // declare integer variable to store the ending index

        Scanner scan = new Scanner(System.in); // create a Scanner object to read user input from the console
        System.out.print("Enter the beginning index: ");  // prompt the user to enter the beginning index
        be = scan.nextInt();  // read the integer input from the user and store it in the beginning index variable
        System.out.print("Enter the ending index: ");  // prompt the user to enter the ending index
        en = scan.nextInt();  // read the integer input from the user and store it in the ending index variable
        scan.close();  // close the Scanner object

        // check if the beginning index is negative
        // if so, convert it to its absolute value and inform the user
        if (be < 0) {  // check if the beginning index is less than 0
            be = -1 * be;  // convert the beginning index to its absolute value if it is negative
            System.out.println("The beginning index cannot be negative. The absolute value is used instead.");  // inform the user about the change
        }

        // check if the ending index is negative
        // if so, convert it to its absolute value and inform the user
        if (en < 0) {  // check if the ending index is less than 0
            en = -1 * en;  // convert the ending index to its absolute value if it is negative
            System.out.println("The ending index cannot be negative. The absolute value is used instead.");  // inform the user about the change
        }

        // check if the beginning index is greater than the ending index
        // if so, swap their values and inform the user
        if (be > en) {  // check if the beginning index is greater than the ending index
            int temp = be;  // create a temporary variable to store the value of the beginning index
            be = en;  // assign the value of the ending index to the beginning index
            en = temp;  // assign the value of the temporary variable to the ending index
            System.out.println("The beginning index is greater than the ending index. The values are swapped.");  // inform the user about the change
        }

        int lo = 1;
        int hi = 1;
        String mark;

        // check if the beginning index is 1
        // if so, print the first fibonacci number
        if (be == 1) 
            System.out.println("1: " + lo);

        // generate and print the fibonacci numbers within the specified range
        for (int i = 2; i <= MAX_INDEX; i++) {
            if (hi % 2 == 0)  // check if the current fibonacci number is even
                mark = " *"; // if so, mark it with an asterisk
            else
                mark = "";  // otherwise, do not mark it
            
            if (i >= be && i <= en)  // check if the current index is within the specified range
                System.out.println(i + ": " + hi + mark);  // if so, print the fibonacci number along with its index and mark (if applicable)

            hi = lo + hi;  // update the fibonacci number
            lo = hi - lo;
        }
    }
}

class ImprovedFibonacci {
    static final int MAX_INDEX = 9;

    // inner class to represent a fibonacci number and its evenness
    public static class Number {
        public int value;  // declare integer variable to store the fibonacci number
        public boolean isEven;  // declare boolean variable to store the evenness of the fibonacci number

        public Number(int value, boolean isEven) {
            this.value = value;  // assign the fibonacci number argument  to the value variable
            this.isEven = isEven;  // assign the evenness argument of the fibonacci number to the isEven variable
        }
    }

    public static void main(String[] args) {
        int lo = 1;
        int hi = 1;

        // create an array to store the fibonacci numbers and their evenness
        Number[] numbers = new Number[MAX_INDEX];
        numbers[0] = new Number(1, false);

        // generate and store the fibonacci numbers and their evenness in the array
        for (int i = 2; i <= MAX_INDEX; i++) {
            numbers[i-1] = new Number(hi, hi % 2 == 0);  // starting with iterator i = 2, index the array with i-1 to store the fibonacci number and its evenness

            hi = lo + hi;  // update the fibonacci number
            lo = hi - lo;
        }

        // print the fibonacci numbers along with their index and mark (if even)
        for (int i = 0; i < MAX_INDEX; i++) {
            String mark = numbers[i].isEven ? " *" : "";  // check if the fibonacci number is even and assign the mark accordingly using a ternary operator
            System.out.println((i + 1) + ": " + numbers[i].value + mark);  // print the fibonacci number along with its index and mark (if applicable)
        }
    }
}