#include <iostream>
#include "functions.h"

using std::cout, std::endl;

bool is_valid_range(int a, int b) {
    if (a >= 10 && a <= b && b < 10000) {
        return true;
    }
    return false;
}

char classify_mv_range_type(int number) {
    if (number < 10) {
        return 'N';
    }

    int numDigits = 0;
    int temp = number;
    while (temp > 0) {
        numDigits++;
        temp /= 10;
    }

    int divisor = 1;
    for (int i = 1; i < numDigits; i++) {
        divisor *= 10;
    }

    int lastDigit = number / divisor;
    number %= divisor;
    divisor /= 10;

    int currentDigit;
    char initialPattern = '0';
    char nextPattern;

    while (divisor > 0) {
        currentDigit = number / divisor;
        number %= divisor;
        divisor /= 10;

        if (initialPattern == '0') {
            if (currentDigit > lastDigit) {
                initialPattern = 'U';
                nextPattern = 'D';	 
            } else if (currentDigit < lastDigit) {
                initialPattern = 'D';
                nextPattern = 'U';
            } else {
                return 'N';
            }
        } else {
            if (nextPattern == 'U' && !(currentDigit > lastDigit)) {
                return 'N';  
            } else if (nextPattern == 'D' && !(currentDigit < lastDigit)) {
                return 'N';  
            }
            nextPattern = (nextPattern == 'U') ? 'D' : 'U';
        }
        lastDigit = currentDigit;
    }

    if (initialPattern == 'U') {
        return 'M';
    } else {
        return 'V';
    }
}

void count_valid_mv_numbers(int a, int b) {
    int m = 0;
    int v = 0;
    for (int i = a; i <= b; i++) {
        if (classify_mv_range_type(i) == 'M') {
            m++;
        }
        else if (classify_mv_range_type(i) == 'V') {
            v++;
        }
    }
    cout << "There are " << m << " mountain ranges and " << v << " valley ranges between " << a << " and " << b << "." << endl;
}
