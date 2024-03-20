#ifndef UNSORTED_PRIORITY_QUEUE_H
#define UNSORTED_PRIORITY_QUEUE_H

#include "AbstractPriorityQueue.h"

template <typename Type>
class UnsortedPriorityQueue : public AbstractPriorityQueue<Type> {
    private:
        Type *arr;
        int capacity;
        int size;

    public:
        UnsortedPriorityQueue();

        ~UnsortedPriorityQueue();

        void pq_insert(Type value);

        Type pq_delete();

        Type pq_get_min();

        int pq_size();
};

template <typename Type>
UnsortedPriorityQueue<Type>::UnsortedPriorityQueue() {
    arr = new Type[10];
    capacity = 10;
    size = 0;
}

template <typename Type>
UnsortedPriorityQueue<Type>::~UnsortedPriorityQueue(){
    delete[] arr;
    arr = nullptr;
}

template <typename Type>
void UnsortedPriorityQueue<Type>::pq_insert(Type value) {
    if(size == capacity){
        Type *temp = new Type[capacity * 2];
        for(int i = 0; i < size; i++){
            temp[i] = arr[i];
        }
        delete[] arr;
        arr = temp;
        capacity *= 2;
    }
    arr[size] = value;
    size++;
}

template <typename Type>
Type UnsortedPriorityQueue<Type>::pq_delete(){
    if (size == 0){
        throw std::out_of_range("Queue is empty");
    }
    
    Type min = arr[0];
    int min_index = 0;
    for(int i = 1; i < size; i++){
        if(arr[i] < min){
            min = arr[i];
            min_index = i;
        }
    }
    for(int i = min_index; i < size - 1; i++){
        arr[i] = arr[i + 1];
    }
    size--;
    return min;
}

template <typename Type>
Type UnsortedPriorityQueue<Type>::pq_get_min(){
    if (size == 0){
        throw std::out_of_range("Queue is empty");
    }

    Type min = arr[0];
    for(int i = 1; i < size; i++){
        if(arr[i] < min){
            min = arr[i];
        }
    }
    return min;
}

template <typename Type>
int UnsortedPriorityQueue<Type>::pq_size(){
    return size;
}

#endif