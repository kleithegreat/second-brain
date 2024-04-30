#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <algorithm>
#include <vector>
#include <fstream>
#define TEST
#include "sort.cpp"

using namespace std;

enum SORT_TYPE {
    BUBBLE_SORT,
    HEAP_SORT,
    MERGE_SORT,
    QUICK_SORT
};

double testSort(SORT_TYPE sort_type, int n) {
    int *arr = new int[n];
    vector<int> arrCopy;

    for(int j=0; j<n; j++){
        arr[j] = rand() % 1000000 + 1;
        arrCopy.push_back(arr[j]);
    }

    sort(arrCopy.begin(), arrCopy.end());

    auto start = std::chrono::high_resolution_clock::now();
    if (sort_type == SORT_TYPE::BUBBLE_SORT) {
       bubbleSort(arr, n);
    } else if (sort_type == SORT_TYPE::HEAP_SORT) {
       heapSort(arr, n);
    } else if (sort_type == SORT_TYPE::MERGE_SORT) {
        mergeSort(arr, 0, n - 1);
    } else if (sort_type == SORT_TYPE::QUICK_SORT) {
        quickSort(arr, 0, n - 1);
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    delete[] arr;
    return elapsed.count();
}

int main(){
    srand(time(NULL));

    ofstream outputFile("sort_data.csv");
    outputFile << "n,time (bubble),time (heap),time (merge),time (quick)" << endl;

    vector<int> sizes = {10, 100, 1000, 10000, 100000, 1000000};

    for (int size : sizes) {
        cout << "Testing size " << size << endl;
        double bubbleTime = (size <= 100000) ? testSort(SORT_TYPE::BUBBLE_SORT, size) : 0;
        double heapTime = testSort(SORT_TYPE::HEAP_SORT, size);
        double mergeTime = testSort(SORT_TYPE::MERGE_SORT, size);
        double quickTime = testSort(SORT_TYPE::QUICK_SORT, size);
        outputFile << size << "," << bubbleTime << "," << heapTime << "," << mergeTime << "," << quickTime << endl;
    }

    outputFile.close();
    return 0;
}