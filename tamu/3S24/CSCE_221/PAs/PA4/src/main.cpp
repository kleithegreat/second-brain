#include <iostream>
#include <fstream>
#include <chrono>
#include <random>
#include <vector>
#include "AbstractHashTable.h"
#include "ChainingHashTable.h"
#include "ProbingHashTable.h"
#include "DoubleHashTable.h"

using namespace std;
using namespace std::chrono;

const int NUM_TRIALS = 30;

void saveResults(const string& filename, const vector<int>& inputSizes,
                 const vector<vector<double>>& trialTimes) {
    ofstream outputFile(filename);
    outputFile << "Input Size,Trial,Chaining,Probing,Double Hashing\n";
    for (int i = 0; i < inputSizes.size(); i++) {
        for (int j = 0; j < NUM_TRIALS; j++) {
            outputFile << inputSizes[i] << "," << j + 1 << ","
                       << trialTimes[i][j * 3] << ","
                       << trialTimes[i][j * 3 + 1] << ","
                       << trialTimes[i][j * 3 + 2] << "\n";
        }
    }
    outputFile.close();
}

void runTrials(AbstractHashTable* hashTable, int size, double& elapsedTime) {
    random_device rd;
    mt19937 rng(rd());
    uniform_int_distribution<int> dist(0, 1000000);

    auto start = high_resolution_clock::now();
    for (int i = 0; i < size; i++) {
        int key = dist(rng);
        hashTable->insert(to_string(key), key);
    }
    auto end = high_resolution_clock::now();
    elapsedTime = duration_cast<milliseconds>(end - start).count();
}

int main() {
    vector<int> inputSizes = {10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000};
    vector<vector<double>> trialTimes(inputSizes.size(), vector<double>(NUM_TRIALS * 3));

    for (int i = 0; i < inputSizes.size(); i++) {
        int size = inputSizes[i];
        cout << "Running trials for input size " << size << "..." << endl;

        for (int trial = 0; trial < NUM_TRIALS; trial++) {
            cout << "Trial " << trial + 1 << "..." << endl;
            ChainingHashTable chainingTable;
            ProbingHashTable probingTable;
            DoubleHashTable doubleHashTable;

            runTrials(&chainingTable, size, trialTimes[i][trial * 3]);
            runTrials(&probingTable, size, trialTimes[i][trial * 3 + 1]);
            runTrials(&doubleHashTable, size, trialTimes[i][trial * 3 + 2]);
        }
    }

    saveResults("insert_trials.csv", inputSizes, trialTimes);

    return 0;
}