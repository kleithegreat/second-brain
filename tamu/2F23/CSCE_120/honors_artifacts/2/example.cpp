// Object oriented programming

#include <iostream>
#include <string>

using namespace std;

class Person {
    public:
        Person(string name, int age) {
            this->name = name;
            this->age = age;
        }
        string getName() {
            return name;
        }
        int getAge() {
            return age;
        }
        void setName(string name) {
            this->name = name;
        }
        void setAge(int age) {
            if (age < 0) {
                throw std::invalid_argument("Age cannot be negative");
            }
            this->age = age;
        }
    private:
        string name;
        int age;
};


int main() {
    Person person1 = Person("John", 20);
    int personAge = person1.getAge();

    std::cout << personAge;

    return 0;
}
