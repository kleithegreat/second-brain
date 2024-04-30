#ifndef SORTED_PRIORITY_QUEUE_H
#define SORTED_PRIORITY_QUEUE_H

template <typename Type>
class SortedPriorityQueue {
    private:
        Type *arr;
        int capacity;
        int startIndex;
        int size;

    public:
        SortedPriorityQueue();

        ~SortedPriorityQueue();

        void pq_insert(Type value);

        Type pq_delete();

        Type pq_get_min();

        int pq_size();
};

template <typename Type>
SortedPriorityQueue<Type>::SortedPriorityQueue() {
    arr = new Type[10];
    capacity = 10;
    startIndex = 0;
    size = 0;
}

template <typename Type>
SortedPriorityQueue<Type>::~SortedPriorityQueue() {
    delete[] arr;
    arr = nullptr;
}

template <typename Type>
void SortedPriorityQueue<Type>::pq_insert(Type value) {
    if (size == capacity) {
        Type *temp = new Type[capacity * 2];
        for (int i = 0; i < size; i++) {
            temp[i] = arr[i];
        }
        delete[] arr;
        arr = temp;
        capacity *= 2;
    }

    int index = 0;
    while (index < size && arr[index] < value) {
        index++;
    }

    for (int i = size; i > index; i--) {
        arr[i] = arr[i - 1];
    }

    arr[index] = value;
    size++;
}

template <typename Type>
Type SortedPriorityQueue<Type>::pq_delete() {
    if (size == 0) {
        throw std::out_of_range("Queue is empty");
    }
    Type min = arr[startIndex];
    startIndex = (startIndex + 1) % capacity;
    size--;
    return min;
}

template <typename Type>
Type SortedPriorityQueue<Type>::pq_get_min() {
    if (size == 0) {
        throw std::out_of_range("Queue is empty");
    }
    return arr[startIndex];
}

template <typename Type>
int SortedPriorityQueue<Type>::pq_size() {
    return size;
}

#endif