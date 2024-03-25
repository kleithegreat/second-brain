#ifndef DOUBLEHASHING_H
#define DOUBLEHASHING_H

#include "AbstractHashTable.h"
#include <vector>

// Double hashing hash table class
class DoubleHashTable : public AbstractHashTable {
    private:
    // helper functions
    int secondHash(std::string s) const;
    int DoubleHash(std::string s) const;
    std::vector<HashEntry> table;
    int prevPrime;
    void resizeAndRehash();

    public: 
    DoubleHashTable();
    ~DoubleHashTable(); 
    void insert(std::string key, int val); 
    int remove(std::string key); 
    int get(std::string key) const; 
    bool contains(std::string key) const;
    std::string getName() const { return "Double Hashing"; };
};


///////////////////// TODO: FILL OUT THE FUNCTIONS /////////////////////

// constructor 
DoubleHashTable::DoubleHashTable(): AbstractHashTable() {
    maxLoadFactor = 0.5;
    table = std::vector<HashEntry>(capacity);
    prevPrime = 11;
}

// destructor
DoubleHashTable::~DoubleHashTable() {
	
}

// inserts the given string key
void DoubleHashTable::insert(std::string key, int val) {
	if (contains(key)) {
        table[DoubleHash(key)].val = val;
    } else {
        int index = DoubleHash(key);
        table[index] = HashEntry(key, val);
        num_elements++;
    }

    if (load_factor() > maxLoadFactor) {
        resizeAndRehash();
    }
}

// removes the given key from the hash table - if the key is not in the list, throw an error
int DoubleHashTable::remove(std::string key) {
    if (!contains(key)) {
        throw std::out_of_range("Key not found");
    }

    int index = DoubleHash(key);
    table[index].DELETED = true;
    table[index].key = "";
    num_elements--;

    return table[index].val;
}

// getter to obtain the value associated with the given key
int DoubleHashTable::get(std::string key) const {
    if (contains(key)) {
        return table[DoubleHash(key)].val;
    } else {
        throw std::out_of_range("Key not found");
    }
}

bool DoubleHashTable::contains(std::string key) const {
    if (table[DoubleHash(key)].key == key && !table[DoubleHash(key)].DELETED) {
        return true;
    }

    return false;
}

void DoubleHashTable::resizeAndRehash() {
    int oldCapacity = capacity;
    std::vector<HashEntry> oldTable = table;

    capacity = findNextPrime(capacity * 2);
    table = std::vector<HashEntry>(capacity);

    for (int i = 0; i < oldCapacity; i++) {
        if (oldTable[i].isFilled && !oldTable[i].DELETED && oldTable[i].key != "") {
            int index = DoubleHash(oldTable[i].key);
            table[index] = oldTable[i];
        }
    }
}

// helper functions 
int DoubleHashTable::secondHash(std::string s) const {
    int c = 31;
    unsigned long hash = 0;
    int n = s.length();

    for (int i = 0; i < n; i++) {
        hash = c * hash + static_cast<int>(s[i]);
    }

    return prevPrime - (hash % prevPrime);
}

int DoubleHashTable::DoubleHash(std::string s) const {
    int index = hash(s);
    int offset = secondHash(s);

    while (table[index].isFilled && table[index].key != s) {
        index = (index + offset) % capacity;
    }

    return index;
}


#endif