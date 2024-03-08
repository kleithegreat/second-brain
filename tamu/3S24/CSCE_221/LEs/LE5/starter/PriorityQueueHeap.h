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
  
}

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>::~PriorityQueueHeap(){
    
}

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>::PriorityQueueHeap(const Compare& _comp) {
   
}

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>::PriorityQueueHeap(const PriorityQueueHeap& other) {
   
}

template <typename Type, typename Compare>
PriorityQueueHeap<Type, Compare>& PriorityQueueHeap<Type, Compare>::operator=(const PriorityQueueHeap& other) {
    return *this;
}

template <typename Type, typename Compare>
int PriorityQueueHeap<Type, Compare>::pq_size() {
    return -1;
}

template <typename Type, typename Compare>
bool PriorityQueueHeap<Type, Compare>::is_pq_empty(){
    return false;
}

template <typename Type, typename Compare>
int PriorityQueueHeap<Type, Compare>::pq_parent(int i){
    return -1;
}

template <typename Type, typename Compare>
Type PriorityQueueHeap<Type, Compare>::pq_top(){
   return Type();
}

template <typename Type, typename Compare>
void PriorityQueueHeap<Type, Compare>::pq_insert(Type x) {
    
}


template <typename Type, typename Compare>
void PriorityQueueHeap<Type, Compare>::bubbleUp(int i){
    
}

template <typename Type, typename Compare>
Type PriorityQueueHeap<Type, Compare>::pq_delete(){
   return Type();
}

template <typename Type, typename Compare>
void PriorityQueueHeap<Type, Compare>::heapify(int i){
   
}

#endif