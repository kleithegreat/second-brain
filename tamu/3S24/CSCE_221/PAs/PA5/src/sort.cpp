#include <iostream>
#include <queue>
using namespace std;

void bubbleSort(int *arr, int size) {
    return;
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

void mergeSort(int *arr, int start, int end) {

}

void quickSort(int *arr, int start, int end) {

}
