#include <iostream>
using namespace std;
#include "AbstractStack.h"
#include "StackArrayDouble.h"
#include "StackArrayLinear.h"

int main() {
    // Write your own tests here

    StackArrayDouble<int> stackdouble = StackArrayDouble<int>();
    StackArrayLinear<int> stacklinear = StackArrayLinear<int>();

    for (int i = 1; i <= 8; i++){
        stackdouble.push(i);
        cout << stackdouble.size() << endl;

        stacklinear.push(i);
        cout << stacklinear.size() << endl;
    }

    for (int i = 1; i <= 8; i++){
        cout << stackdouble.pop() << endl;
        cout << stackdouble.size() << endl;

        cout << stacklinear.pop() << endl;
        cout << stacklinear.size() << endl;
    }

    return 0;
}