# include "functions.h"
// add any includes

using std::cout, std::cin, std::endl, std::string;

void deobfuscate() {
    string input;
    string nums;

    cout << "Please enter obfuscated sentence: ";
    getline(cin, input);

    cout << "Please enter deobfuscation details: ";
    getline(cin, nums);

    cout << "Deobfuscated sentence: ";

    unsigned int length = nums.length();
    int tempLength;
    int startIndex = 0;
    for (unsigned int i = 0; i < length; i++) {
        tempLength = nums[i] - '0';
        for (int j = 0; j < tempLength; j++) {
            cout << input[startIndex + j];
        }
        cout << " ";
        startIndex += tempLength;
    }

    cout << endl;
}

void wordFilter() {
    string sentence;
    string filter;

    cout << "Please enter the sentence: ";
    getline(cin, sentence);

    cout << "Please enter the filter word: ";
    getline(cin, filter);

    string replacement;
    for (unsigned int i = 0; i < filter.length(); i++) {
        replacement += "#";
    }

    while (sentence.find(filter) != string::npos) {
        sentence.replace(sentence.find(filter), filter.length(), replacement);
    }

    cout << "Filtered sentence: " << sentence;
    cout << endl;
}

void passwordConverter() {
    // TODO
}

void wordCalculator() {
    // TODO
}

void palindromeCounter() {
    // TODO
}