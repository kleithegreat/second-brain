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

}

template <typename T>
StackArrayDouble<T>::~StackArrayDouble(){

}

template <typename T>
StackArrayDouble<T>::StackArrayDouble(const StackArrayDouble& other) {
    
}

template <typename T>
StackArrayDouble<T>& StackArrayDouble<T>::operator=(const StackArrayDouble& other) {
    return *this;
}

template <typename T>
bool StackArrayDouble<T>::isEmpty(){
    return true;
}

template <typename T>
int StackArrayDouble<T>::size(){
    return -1;
}

template <typename T>
T& StackArrayDouble<T>::top(){
    static int temp = -1;
    return temp;
}

template <typename T>
T StackArrayDouble<T>::pop(){
    return -1;
}

template <typename T>
void StackArrayDouble<T>::push(const T& e){

}

#endif