#define TEST
#include <iostream>
#include "deque.h"
#include <vector>
#include <string>

using namespace std;

template<typename T>
bool testCopyConstructor(int n) {
    Deque<T> originalDeque;
    for (int i = 0; i < n; i++) {
        T randomNumber = static_cast<T>(rand() % n + 1);
        originalDeque.insertFirst(randomNumber);
    }
    Deque<T> copiedDeque(originalDeque);
    if (copiedDeque.size() != n) {
        return false;
    }
    for (int i = 0; i < n; i++) {
        if (copiedDeque.removeFirst() != originalDeque.removeFirst()) {
            return false;
        }
        if (copiedDeque.size() != n - 1 - i) {
            return false;
        }
    }
    return true;
}

template<typename T>
bool testCopyAssignment(int n) {
    Deque<T> sourceDeque;
    for (int i = 0; i < n; i++) {
        T randomNumber = static_cast<T>(rand() % n + 1);
        sourceDeque.insertFirst(randomNumber);
    }
    Deque<T> targetDeque;
    for (int i = 0; i < rand() % (n * 2) + 1; i++) {
        T randomNumber = static_cast<T>(rand() % (n * 2) + 1);
        targetDeque.insertFirst(randomNumber);
    }
    targetDeque = sourceDeque;
    if (targetDeque.size() != n) {
        return false;
    }
    for (int i = 0; i < n; i++) {
        if (targetDeque.removeFirst() != sourceDeque.removeFirst()) {
            return false;
        }
        if (targetDeque.size() != n - 1 - i) {
            return false;
        }
    }
    return true;
}

template<typename T>
bool testInsertFirstAndRemoveFirst(int n) {
    vector<T> numbers;
    Deque<T> deque;
    for (int i = 0; i < n; i++) {
        T randomNumber = static_cast<T>(rand() % n + 1);
        numbers.push_back(randomNumber);
        deque.insertFirst(randomNumber);
    }
    for (int i = 0; i < n; i++) {
        if (deque.removeFirst() != numbers[n - 1 - i]) {
            return false;
        }
        if (deque.size() != n - 1 - i) {
            return false;
        }
    }
    return true;
}

template<typename T>
bool testInsertLastAndRemoveLast(int n) {
    vector<T> numbers;
    Deque<T> deque;
    for (int i = 0; i < n; i++) {
        T randomNumber = static_cast<T>(rand() % n + 1);
        numbers.push_back(randomNumber);
        deque.insertLast(randomNumber);
    }
    for (int i = 0; i < n; i++) {
        if (deque.removeLast() != numbers[n - 1 - i]) {
            return false;
        }
        if (deque.size() != n - 1 - i) {
            return false;
        }
    }
    return true;
}

template<typename T>
bool testInsertAndRemove(int n) {
    vector<T> expected;
    Deque<T> actual;
    for (int i = 0; i < n; i++) {
        T value = static_cast<T>(rand() % n + 1);
        int operation = rand() % 4;
        switch (operation) {
            case 0:
                expected.insert(expected.begin(), value);
                actual.insertFirst(value);
                break;
            case 1:
                expected.push_back(value);
                actual.insertLast(value);
                break;
            case 2:
                if (!actual.isEmpty()) {
                    if (!expected.empty()) {
                        T expectedValue = expected.front();
                        expected.erase(expected.begin());
                        if (actual.removeFirst() != expectedValue) {
                            return false;
                        }
                    }
                }
                break;
            case 3:
                if (!actual.isEmpty()) {
                    if (!expected.empty()) {
                        T expectedValue = expected.back();
                        expected.pop_back();
                        if (actual.removeLast() != expectedValue) {
                            return false;
                        }
                    }
                }
                break;
        }
        if (actual.size() != expected.size()) {
            return false;
        }
    }
    return true;
}

template<typename T>
bool testRemoveFromEmptyDeque() {
    Deque<T> deque;
    try {
        deque.removeFirst();
        return false;
    } catch (const out_of_range& e) {
        return true;
    }
    try {
        deque.removeLast();
        return false;
    } catch (const out_of_range& e) {
        return true;
    }
}

int main() {
	srand(time(0));
    int finalScore = 0;
	try {
		if (!testCopyConstructor<int>(rand() % 50 + 10))
			cout << "copy constructor test failed" << endl;
		else {
            finalScore += 10;
            cout << "copy constructor test passed" << endl;
        }
			

		if (!testCopyAssignment<short>(rand() % 50 + 10))
			cout << "copy assignment test failed" << endl;
		else {
            finalScore += 10;
            cout << "copy assignment test passed" << endl;
        }
			

		if (!testInsertFirstAndRemoveFirst<double>(rand() % 50 + 10))
			cout << "insertFirst & removeFirst test failed" << endl;
		else {
            finalScore += 15;
            cout << "insertFirst & removeFirst test passed" << endl;
        }
			

		if (!testInsertLastAndRemoveLast<long>(rand() % 50 + 10))
			cout << "insertLast & removeLast test failed" << endl;
		else {
            finalScore += 15;
            cout << "insertLast & removeLast test passed" << endl;
        }
			

		if (!testInsertAndRemove<char32_t>(rand() % 50 + 10))
			cout << "insert & remove test failed" << endl;
		else {
            finalScore += 25;
            cout << "insert & remove test passed" << endl;
        }
			

		if (!testRemoveFromEmptyDeque<int>())
            cout << "remove from empty deque test failed" << endl;
        else {
            finalScore += 5;
            cout << "remove from empty deque test passed" << endl;
        }
            
	} catch (const exception& e) {
		cout << "An exception occurred: " << e.what() << endl;
	}

    cout << "Final score is: " << finalScore << " / 80" << endl;
	return 0;
}
