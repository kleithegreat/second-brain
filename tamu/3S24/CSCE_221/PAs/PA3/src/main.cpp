#include "AbstractPriorityQueue.h"
#include "PriorityQueueHeap.h"
#include "UnsortedPriorityQueue.h"
#include "SortedPriorityQueue.h"
#include <iostream>
#include <fstream>
#include <chrono>
#include <random>

using namespace std;
using namespace std::chrono;

void testEnqueue(AbstractPriorityQueue<int>& pq, int size, ofstream& file) {
    auto start = high_resolution_clock::now();
    for (int i = 0; i < size; i++) {
        pq.pq_insert(rand() % 100000);
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    file << duration.count() << ",";
}

void testHeapSort(AbstractPriorityQueue<int>& pq, int size, ofstream& file) {
    for (int i = 0; i < size; i++) {
        pq.pq_insert(rand() % 100000);
    }
    auto start = high_resolution_clock::now();
    while (pq.pq_size() > 0) {
        pq.pq_delete();
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    file << duration.count() << ",";
}

#ifndef TEST
int main() {
    ofstream enqueueFile("enqueue_results.csv");
    ofstream heapSortFile("heapsort_results.csv");
    enqueueFile << "Size,UnsortedPQ,SortedPQ,HeapPQ" << endl;
    heapSortFile << "Size,UnsortedPQ,SortedPQ,HeapPQ" << endl;

    vector<int> inputSizes = {1000, 5000, 10000, 50000, 100000};

    for (int size : inputSizes) {
        UnsortedPriorityQueue<int> unsortedPQ;
        SortedPriorityQueue<int> sortedPQ;
        PriorityQueueHeap<int> heapPQ;

        enqueueFile << size << ",";
        testEnqueue(unsortedPQ, size, enqueueFile);
        testEnqueue(sortedPQ, size, enqueueFile);
        testEnqueue(heapPQ, size, enqueueFile);
        enqueueFile << endl;

        heapSortFile << size << ",";
        testHeapSort(unsortedPQ, size, heapSortFile);
        testHeapSort(sortedPQ, size, heapSortFile);
        testHeapSort(heapPQ, size, heapSortFile);
        heapSortFile << endl;
    }

    enqueueFile.close();
    heapSortFile.close();

    return 0;
}
#endif