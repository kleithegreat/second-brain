#include <iostream>
#include <queue>
#include <vector>
using namespace std;

void bubbleSort(int *arr, int size) {
    bool swapped;
    do {
        swapped = false;
        for (int i = 0; i < size - 1; i++) {
            if (arr[i] > arr[i+1]) {
                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                swapped = true;
            }
        }
        size--;
    } while (swapped);
}

void heapSort(int *arr, int size) {
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (int i = 0; i < size; i++) {
        pq.push(arr[i]);
    }

    for (int i = 0; i < size; i++) {
        arr[i] = pq.top();
        pq.pop();
    }
}

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

void mergeSort(int* arr, int start, int end) {
    if (start < end) {
        int mid = start + (end - start) / 2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

void quickSort(int* arr, int start, int end) {
    if (start >= end) return;

    int pivot = arr[end];
    int i = start - 1;

    for (int j = start; j < end; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[end]);

    quickSort(arr, start, i);
    quickSort(arr, i + 2, end);
}
