#include <iostream>
#include <chrono>
#include <fstream>
#include "AbstractStack.h"
#include "StackArrayDouble.h"
#include "StackArrayLinear.h"
#include "StackLinkedList.h"

using namespace std;
using namespace std::chrono;

template<typename T>
double testPushOperation(AbstractStack<T>& stack, long long inputSize) {
    std::cout << "Testing push operation with input size " << inputSize << std::endl;
    auto start = high_resolution_clock::now();

    for (long long i = 0; i < inputSize; ++i) {
        stack.push(i);
    }

    auto end = high_resolution_clock::now();
    duration<double, milli> duration = end - start;
    return duration.count();
}

int main() {
    ofstream outFile("timing_data.csv");
    if (!outFile.is_open()) {
        cerr << "Failed to open the file for writing." << endl;
        return 1;
    }

    outFile << "InputSize,TimeArrayDouble,TimeArrayLinear,TimeLinkedList\n";

    for (long long inputSize = 128; inputSize <= 2000000; inputSize *= 2) {
        StackArrayDouble<int> stackDouble;
        StackArrayLinear<int> stackLinear;
        StackLinkedList<int> stackLinkedList;

        std::cout << "ArrayDouble: " << std::endl;
        double timeDouble = testPushOperation(stackDouble, inputSize);

        std::cout << "ArrayLinear: " << std::endl;
        double timeLinear = testPushOperation(stackLinear, inputSize);

        std::cout << "LinkedList: " << std::endl;
        double timeLinkedList = testPushOperation(stackLinkedList, inputSize);

        outFile << inputSize << "," << timeDouble << "," << timeLinear << "," << timeLinkedList << "\n";
    }

    outFile.close();
    return 0;
}
