#include <iostream>
#include <vector>
#include <cmath>
#include "SortedPriorityQueue.h"

using namespace std;

void radixSort(int *arr, int n) {
    int maxVal = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
        }
    }

    int maxDigits = 0;
    while (maxVal > 0) {
        maxVal /= 10;
        maxDigits++;
    }

    for (int i = 1; i <= maxDigits; i++) {
        std::vector<int> buckets [10];

        for (int j = 0; j < n; j++) {
            int digit = (arr[j] / static_cast<int>(pow(10, i - 1))) % 10;
            buckets[digit].push_back(arr[j]);
        }

        int index = 0;
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < buckets[j].size(); k++) {
                arr[index++] = buckets[j][k];
            }
        }
    }
}


void insertionSort(int *arr, int n) {
    SortedPriorityQueue<int> pq;
    for (int i = 0; i < n; i++) {
        pq.pq_insert(arr[i]);
    }

    for (int i = 0; i < n; i++) {
        arr[i] = pq.pq_delete();
    }
}
