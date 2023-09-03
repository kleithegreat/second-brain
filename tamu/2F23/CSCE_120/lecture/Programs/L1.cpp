#include <iostream>

// It's considered a bad practice to use the entire standard namespace. 
// For demonstration purposes, we've used it here.
using namespace std; 

// Function declaration and definition to find the largest number among three.
double largestNum(double val1, double val2, double val3) {
    if (val1 > val2 && val1 > val3) {
        return val1;
    }
    else if (val2 > val3) {
        return val2;
    }
    else {
        return val3;
    }
}

int main() {
    double val1 = 0;
    double val2 = 0;
    double val3 = 0;
    cin >> val1 >> val2 >> val3;  // Taking input for the three values
    cout << "largest: " << largestNum(val1, val2, val3) << endl; // Printing the largest value among the three
}
