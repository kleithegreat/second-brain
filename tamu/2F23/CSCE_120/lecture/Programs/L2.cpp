#include <iostream>

using std::cout, std::cin, std::endl;

int main() {
    double sum = 0;
    double numCnt = 0;
    double num = 0;

    do {
        cin >> num;
        if (num >= 0) {
            sum += num;
            numCnt++;
        }
    } while(num != -1);

    cout << "Average: ";
    if (numCnt == 0) {
        cout << "Empty list";
    } else {
        cout << sum / numCnt << endl;
    }

    // main does not have to explicitly reuturn 0
}
