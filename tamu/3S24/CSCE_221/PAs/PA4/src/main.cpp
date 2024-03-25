#include "AbstractHashTable.h"
#include "ChainingHashTable.h"
#include "ProbingHashTable.h"
#include "DoubleHashTable.h"
#include <chrono>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>

using namespace std;
using namespace std::chrono;

void testHashTableInsert(AbstractHashTable* aht, vector<string>& words, int size, ofstream& outputFile) {
    cout << "Testing " << aht->getName() << " with input size " << size << endl;
    auto start = high_resolution_clock::now();
    for (int i = 0; i < size; i++) {
        if (!aht->contains(words[i])) {
            aht->insert(words[i], 1);
        } else {
            int curVal = aht->get(words[i]);
            aht->insert(words[i], curVal + 1);
        }
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    outputFile << duration.count() << ",";
}

int main() {
    string filename = "dictionary.txt";
    ifstream file(filename);
    ofstream outputFile("insert_times.csv");
    outputFile << "Input Size,Chaining,Probing,Double Hashing" << endl;

    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        return 0;
    }

    vector<string> words;
    string word;
    while (file >> word) {
        words.push_back(word);
    }

    vector<int> inputSizes = {10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000};
    int numTrials = 30;

    for (int size : inputSizes) {
        if (size > words.size()) {
            break;
        }

        for (int trial = 0; trial < numTrials; trial++) {
            vector<string> subWords(words.begin(), words.begin() + size);

            outputFile << size << ",";

            AbstractHashTable* cht = new ChainingHashTable();
            testHashTableInsert(cht, subWords, size, outputFile);
            delete cht;

            AbstractHashTable* pht = new ProbingHashTable();
            testHashTableInsert(pht, subWords, size, outputFile);
            delete pht;

            AbstractHashTable* dht = new DoubleHashTable();
            testHashTableInsert(dht, subWords, size, outputFile);
            delete dht;

            outputFile << endl;
        }
    }

    outputFile.close();

    return 0;
}