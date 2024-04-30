#ifndef PRIORITY_QUEUE_H
#define PRIORITY_QUEUE_H

#include <iostream>

using namespace std;

template <typename Type>
class PriorityQueueHeap : public AbstractPriorityQueue<Type> {
private:
    Type *arr;
    int capacity;
    int size;
    
    void minHeapify(int i);
    void bubbleUp(int i);
    int pq_parent(int i);

public:
    PriorityQueueHeap();

    ~PriorityQueueHeap();

    int pq_size();
    
    Type pq_get_min();

    void pq_insert(Type value);

    Type pq_delete();
};

// Your implementation here

template <typename Type>
PriorityQueueHeap<Type>::PriorityQueueHeap(){
    capacity = 10;
    size = 0;
    arr = new Type[capacity];
}

template <typename Type>
PriorityQueueHeap<Type>::~PriorityQueueHeap(){
    delete[] arr;
    arr = nullptr;
}

template <typename Type>
int PriorityQueueHeap<Type>::pq_size() {
    return size;
}

template <typename Type>
int PriorityQueueHeap<Type>::pq_parent(int i){
    return (i - 1) / 2;
}

template <typename Type>
Type PriorityQueueHeap<Type>::pq_get_min(){
    if (size == 0) {
        throw std::out_of_range("The priority queue is empty");
    }

    return arr[0];
}

template <typename Type>
void PriorityQueueHeap<Type>::pq_insert(Type x) {
    if (size == capacity) {
        capacity *= 2;

        Type* newArr = new Type[capacity];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        delete[] arr;
        arr = newArr;
    }

    arr[size] = x;
    bubbleUp(size);
    size++;
}


template <typename Type>
void PriorityQueueHeap<Type>::bubbleUp(int i){
    while (i > 0 && arr[pq_parent(i)] > arr[i]) {
        swap(arr[i], arr[pq_parent(i)]);
        i = pq_parent(i);
    }
}

template <typename Type>
Type PriorityQueueHeap<Type>::pq_delete(){
    if (size == 0) {
        throw std::out_of_range("The priority queue is empty");
    }

    Type min = arr[0];
    arr[0] = arr[size - 1];
    size--;
    minHeapify(0);
    return min;
}

template <typename Type>
void PriorityQueueHeap<Type>::minHeapify(int i){
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    int smallest = i;

    if (left < size && arr[left] < arr[smallest]) {
        smallest = left;
    }

    if (right < size && arr[right] < arr[smallest]) {
        smallest = right;
    }

    if (smallest != i) {
        swap(arr[i], arr[smallest]);
        minHeapify(smallest);
    }
}

#endif