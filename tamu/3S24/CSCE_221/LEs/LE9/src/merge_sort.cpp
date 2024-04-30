#include <iostream>
#include <thread>
using namespace std;

void merge(int* arr, int start, int mid, int end) {
    int leftSize = mid - start + 1;
    int rightSize = end - mid;
    
    int* leftArr = new int[leftSize];
    int* rightArr = new int[rightSize];
    
    for (int i = 0; i < leftSize; i++) {
        leftArr[i] = arr[start + i];
    }
    for (int i = 0; i < rightSize; i++) {
        rightArr[i] = arr[mid + 1 + i];
    }
    
    int i = 0;
    int j = 0;
    int k = start;
    while (i < leftSize && j < rightSize) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }
    
    while (i < leftSize) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    
    while (j < rightSize) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
    
    delete[] leftArr;
    delete[] rightArr;
}

void mergeSortHelper(int* arr, int start, int end) {
    if (start < end) {
        int mid = start + (end - start) / 2;
        mergeSortHelper(arr, start, mid);
        mergeSortHelper(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

void mergeSort(int* arr, int start, int end, int level) {
    if (level <= 0 || start >= end) {
        mergeSortHelper(arr, start, end);
    } else {
        int mid = start + (end - start) / 2;
        std::thread leftThread(mergeSort, arr, start, mid, level - 1);
        std::thread rightThread(mergeSort, arr, mid + 1, end, level - 1);
        leftThread.join();
        rightThread.join();
        merge(arr, start, mid, end);
    }
}
