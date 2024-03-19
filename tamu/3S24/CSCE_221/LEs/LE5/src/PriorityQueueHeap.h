#ifndef PRIORITY_QUEUE_H
#define PRIORITY_QUEUE_H

#include <vector>
#include <iostream>

using namespace std;

template <typename Type, typename Compare = std::greater<Type>>
class PriorityQueueHeap {
private:
    Compare compare;
    Type *arr;
    int capacity;
    int size;

    void heapify(int i);
    void bubbleUp(int i);
    int pq_parent(int i);

public:
    PriorityQueueHeap();

    PriorityQueueHeap(const PriorityQueueHeap& other);

    PriorityQueueHeap(const Compare& comp);

    PriorityQueueHeap& operator=(const PriorityQueueHeap& other);

    ~PriorityQueueHeap();

    int pq_size();

    bool is_pq_empty();
    
    Type pq_top();

    void pq_insert(Type x);

    Type pq_delete();
};

// Your implementation here

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>::PriorityQueueHeap() : compare() {
    capacity = 10;
    size = 0;
    arr = new Type[capacity];
}

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>::~PriorityQueueHeap(){
    delete[] arr;
    arr = nullptr;
}

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>::PriorityQueueHeap(const Compare& _comp) {
    compare = _comp;
    capacity = 10;
    size = 0;
    arr = new Type[capacity];
}

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>::PriorityQueueHeap(const PriorityQueueHeap& other) {
    compare = other.compare;
    capacity = other.capacity;
    size = other.size;

    arr = new Type[capacity];
    for (int i = 0; i < size; i++) {
        arr[i] = other.arr[i];
    }
}

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>& PriorityQueueHeap<Type, Compare>::operator=(const PriorityQueueHeap& other) {
    if (this == &other) {
        return *this;
    }

    capacity = other.capacity;
    size = other.size;
    compare = other.compare;

    delete[] arr;
    arr = new Type[other.capacity];

    for (int i = 0; i < size; i++) {
        arr[i] = other.arr[i];
    }

    return *this;
}

template <typename Type, typename Compare>
int PriorityQueueHeap<Type, Compare>::pq_size() {
    return size;
}

template <typename Type, typename Compare>
bool PriorityQueueHeap<Type, Compare>::is_pq_empty(){
    return size == 0;
}

template <typename Type, typename Compare>
int PriorityQueueHeap<Type, Compare>::pq_parent(int i){
    return (i - 1) / 2;
}

template <typename Type, typename Compare>
Type PriorityQueueHeap<Type, Compare>::pq_top(){
    if (size == 0) {
        throw std::out_of_range("The priority queue is empty");
    }

    return arr[0];
}

template <typename Type, typename Compare>
void PriorityQueueHeap<Type, Compare>::pq_insert(Type x) {
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


template <typename Type, typename Compare>
void PriorityQueueHeap<Type, Compare>::bubbleUp(int i){
    while (i > 0 && compare(arr[pq_parent(i)], arr[i])) {
        Type temp = arr[i];
        arr[i] = arr[pq_parent(i)];
        arr[pq_parent(i)] = temp;
        i = pq_parent(i);
    }
}

template <typename Type, typename Compare>
Type PriorityQueueHeap<Type, Compare>::pq_delete(){
    if (!is_pq_empty()) {
        Type top = arr[0];
        arr[0] = arr[size - 1];
        size--;
        heapify(0);
        return top;
    } else {
        throw std::out_of_range("The priority queue is empty");
    }
}

template <typename Type, typename Compare>
void PriorityQueueHeap<Type, Compare>::heapify(int i){
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    int largest = i;
    if (left < size && compare(arr[largest], arr[left])) {
        largest = left;
    }
    if (right < size && compare(arr[largest], arr[right])) {
        largest = right;
    }
    if (largest != i) {
        Type temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(largest);
    }
}

#endif