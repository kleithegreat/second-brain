import java.util.Scanner;
// import static java.lang.System.out;

class SubsetOutputFib {
    static final int MAX_INDEX = 9;

    /** * Print out the first few Fibonacci numbers, * marking evens with a '*' */
    public static void main(String[] args) {
        int be;
        int en;

        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the beginning index: ");
        be = scan.nextInt();
        System.out.print("Enter the ending index: ");
        en = scan.nextInt();
        scan.close();

        if (be < 0) {
            be = -1 * be;
            System.out.println("The beginning index cannot be negative. The absolute value is used instead.");
        }

        if (en < 0) {
            en = -1 * en;
            System.out.println("The ending index cannot be negative. The absolute value is used instead.");
        }

        if (be > en) {
            int temp = be;
            be = en;
            en = temp;
            System.out.println("The beginning index is greater than the ending index. The values are swapped.");
        }

        int lo = 1;
        int hi = 1;
        String mark;
        if (be == 1) 
            System.out.println("1: " + lo);
        for (int i = 2; i <= MAX_INDEX; i++) {
            if (hi % 2 == 0)
                mark = " *";
            else
                mark = "";
            
            if (i >= be && i <= en)
                System.out.println(i + ": " + hi + mark);

            hi = lo + hi;
            lo = hi - lo;
        }
    }
}

class ImprovedFibonacci {
    static final int MAX_INDEX = 9;

    public static class Number {
        public int value;
        public boolean isEven;

        public Number(int value, boolean isEven) {
            this.value = value;
            this.isEven = isEven;
        }
    }

    /** * Print out the first few Fibonacci numbers, * marking evens with a '*' */
    public static void main(String[] args) {
        int lo = 1;
        int hi = 1;

        Number[] numbers = new Number[MAX_INDEX];
        numbers[0] = new Number(1, false);

        for (int i = 2; i <= MAX_INDEX; i++) {
            numbers[i-1] = new Number(hi, hi % 2 == 0);

            hi = lo + hi;
            lo = hi - lo;
        }

        for (int i = 0; i < MAX_INDEX; i++) {
            String mark = numbers[i].isEven ? " *" : "";
            System.out.println((i + 1) + ": " + numbers[i].value + mark);
        }
    }
}