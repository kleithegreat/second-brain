#ifndef STACK_LINEAR_ARRAY_H
#define STACK_LINEAR_ARRAY_H
#include "AbstractStack.h"

template <typename T>
class StackArrayLinear : public AbstractStack<T> {
private:
    T* data;
    int length;
    int topIndex;

public:
    StackArrayLinear();

    ~StackArrayLinear();

    StackArrayLinear(const StackArrayLinear& other);

    StackArrayLinear& operator=(const StackArrayLinear& other);

    bool isEmpty();

    int size();

    T& top();

    T pop();

    void push(const T& e);

};

// Your implementation here
template <typename T>
StackArrayLinear<T>::StackArrayLinear(){
    data = new T[1];
    length = 1;
    topIndex = -1;
}

template <typename T>
StackArrayLinear<T>::~StackArrayLinear(){
    delete[] data;
    data = nullptr;
}

template <typename T>
StackArrayLinear<T>::StackArrayLinear(const StackArrayLinear& other) {
    length = other.length;
    topIndex = other.topIndex;

    data = new T[length];

    for (int i = 0; i <= topIndex; i++){
        data[i] = other.data[i];
    }
}

template <typename T>
StackArrayLinear<T>& StackArrayLinear<T>::operator=(const StackArrayLinear& other) {
    if (this != &other){
        delete[] data;
        length = other.length;
        topIndex = other.topIndex;

        data = new T[length];

        for (int i = 0; i <= topIndex; i++){
            data[i] = other.data[i];
        }
    }

    return *this;
}

template <typename T>
bool StackArrayLinear<T>::isEmpty(){
    return topIndex == -1;
}

template <typename T>
int StackArrayLinear<T>::size(){
    return topIndex + 1;
}

template <typename T>
T& StackArrayLinear<T>::top(){
    if (isEmpty()){
        throw std::out_of_range("Stack is empty");
    }

    return data[topIndex];
}

template <typename T>
T StackArrayLinear<T>::pop(){
    if (isEmpty()){
        throw std::out_of_range("Stack is empty");
    }

    topIndex--;
    return data[topIndex + 1];
}

template <typename T>
void StackArrayLinear<T>::push(const T& e){
    if (this->size() == length){
        T* temp = new T[length + 10];
        for (int i = 0; i < length; i++){
            temp[i] = data[i];
        }
        delete[] data;
        data = temp;
        length += 10;
    }

    topIndex++;
    data[topIndex] = e;
}

#endif