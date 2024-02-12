#include "Deque.h"
#include <iostream>
#include <string>

void displayTestResult(const std::string& testName, bool result) {
    std::cout << testName << ": " << (result ? "PASS" : "FAIL") << std::endl;
}

void testEmptyAndSize() {
    Deque<int> d;
    bool result = d.isEmpty() && d.size() == 0;
    displayTestResult("testEmptyAndSize", result);
}

void testInsertFirstAndFirst() {
    Deque<int> d;
    d.insertFirst(10);
    bool result = !d.isEmpty() && d.first() == 10 && d.size() == 1;
    displayTestResult("testInsertFirstAndFirst", result);
}

void testInsertLastAndLast() {
    Deque<int> d;
    d.insertLast(20);
    bool result = !d.isEmpty() && d.last() == 20 && d.size() == 1;
    displayTestResult("testInsertLastAndLast", result);
}

void testRemoveFirst() {
    Deque<int> d;
    d.insertFirst(10);
    d.insertFirst(20);
    int removed = d.removeFirst();
    bool result = removed == 20 && d.size() == 1 && d.first() == 10;
    displayTestResult("testRemoveFirst", result);
}

void testRemoveLast() {
    Deque<int> d;
    d.insertLast(30);
    d.insertLast(40);
    int removed = d.removeLast();
    bool result = removed == 40 && d.size() == 1 && d.last() == 30;
    displayTestResult("testRemoveLast", result);
}

void testRemoveFromEmpty() {
    Deque<int> d;
    bool passed = false;
    try {
        d.removeFirst();
    } catch (std::out_of_range& e) {
        passed = true; // Expected to catch an exception
    }
    displayTestResult("testRemoveFromEmpty (removeFirst)", passed);

    passed = false;
    try {
        d.removeLast();
    } catch (std::out_of_range& e) {
        passed = true; // Expected to catch an exception
    }
    displayTestResult("testRemoveFromEmpty (removeLast)", passed);
}

void testInsertAfterRemove() {
    Deque<int> d;
    d.insertFirst(1);
    d.removeFirst();
    d.insertLast(2);
    bool result = d.size() == 1 && d.first() == 2 && d.last() == 2;
    displayTestResult("testInsertAfterRemove", result);
}

void testCopyConstructor() {
    Deque<int> d;
    d.insertLast(1);
    d.insertLast(2);
    Deque<int> dCopy(d);
    bool result = dCopy.size() == 2 && dCopy.first() == 1 && dCopy.last() == 2;
    // Modify original to ensure deep copy
    d.removeFirst();
    result &= (d.size() == 1) && (dCopy.size() == 2);
    displayTestResult("testCopyConstructor", result);
}

void testAssignmentOperator() {
    Deque<int> d;
    d.insertLast(1);
    d.insertLast(2);
    Deque<int> dAssigned;
    dAssigned = d;
    bool result = dAssigned.size() == 2 && dAssigned.first() == 1 && dAssigned.last() == 2;
    // Modify original to ensure deep copy
    d.removeFirst();
    result &= (d.size() == 1) && (dAssigned.size() == 2);
    displayTestResult("testAssignmentOperator", result);
}

int main() {
    testEmptyAndSize();
    testInsertFirstAndFirst();
    testInsertLastAndLast();
    testRemoveFirst();
    testRemoveLast();
    testRemoveFromEmpty();
    testInsertAfterRemove();
    testCopyConstructor();
    testAssignmentOperator();

    return 0;
}