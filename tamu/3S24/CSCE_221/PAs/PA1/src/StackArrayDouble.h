#ifndef STACK_DOUBLE_ARRAY_H
#define STACK_DOUBLE_ARRAY_H
#include "AbstractStack.h"

template <typename T>
class StackArrayDouble : public AbstractStack<T> {
private:
    T* data;
    int length;
    int topIndex;

public:
    StackArrayDouble();

    ~StackArrayDouble();

    StackArrayDouble(const StackArrayDouble& other);

    StackArrayDouble& operator=(const StackArrayDouble& other);

    bool isEmpty();

    int size();

    T& top();

    T pop();

    void push(const T& e);

};

// Your implementation here

template <typename T>
StackArrayDouble<T>::StackArrayDouble(){
    data = new T[1];
    length = 1;
    topIndex = -1;
}

template <typename T>
StackArrayDouble<T>::~StackArrayDouble(){
    delete[] data;
    data = nullptr;
}

template <typename T>
StackArrayDouble<T>::StackArrayDouble(const StackArrayDouble& other) {
    length = other.length;
    topIndex = other.topIndex;

    data = new T[length];

    for (int i = 0; i <= topIndex; i++){
        data[i] = other.data[i];
    }
}

template <typename T>
StackArrayDouble<T>& StackArrayDouble<T>::operator=(const StackArrayDouble& other) {
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
bool StackArrayDouble<T>::isEmpty(){
    return topIndex == -1;
}

template <typename T>
int StackArrayDouble<T>::size(){
    return topIndex + 1;
}

template <typename T>
T& StackArrayDouble<T>::top(){
    if (topIndex == -1){
        throw std::out_of_range("Stack is empty");
    } else {
        return data[topIndex];
    }
}

template <typename T>
T StackArrayDouble<T>::pop(){
    if (topIndex == -1){
        throw std::out_of_range("Stack is empty");
    }

    topIndex--;
    return data[topIndex + 1];
}

template <typename T>
void StackArrayDouble<T>::push(const T& e){
    if (this->size() == length) {
        T* temp = new T[length * 2];

        for (int i = 0; i < length; i++){
            temp[i] = data[i];
        }

        delete[] data;
        data = temp;
        length *= 2;
    }

    topIndex++;
    data[topIndex] = e;
}

#endif