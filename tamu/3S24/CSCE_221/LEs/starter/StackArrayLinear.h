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
}

template <typename T>
StackArrayLinear<T>::~StackArrayLinear(){
}

template <typename T>
StackArrayLinear<T>::StackArrayLinear(const StackArrayLinear& other) {
}

template <typename T>
StackArrayLinear<T>& StackArrayLinear<T>::operator=(const StackArrayLinear& other) {
    return *this;
}

template <typename T>
bool StackArrayLinear<T>::isEmpty(){
    return true;
}

template <typename T>
int StackArrayLinear<T>::size(){
    return -1;
}

template <typename T>
T& StackArrayLinear<T>::top(){
    static int temp = -1;
    return temp;
}

template <typename T>
T StackArrayLinear<T>::pop(){
    return -1;
}

template <typename T>
void StackArrayLinear<T>::push(const T& e){
}

#endif