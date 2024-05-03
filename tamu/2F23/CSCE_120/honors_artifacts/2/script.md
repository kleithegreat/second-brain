## Object oriented programming tutorial:

Programming paradigms are patterns programmers follow to make writing code easier. One of these practices is called Object oriented programming, or OOP, which is one of the most popular paradigms. OOP uses three big programming concepts: encapsulation, inheritance, and polymorphism. 

Encapsulation is the idea that code should be focused more on what it does rather than how it accomplishes it. In practice, this means separating blocks of code and making sure that only certain parts are allowed to interact with each other. 
Inheritance is the idea that certain parts of code can be reused, highlighting certain parts of related code. 
Polymorphism is the idea of using a single interface to represent multiple kinds of data. 

Everything in OOP is based on the concept of an object. An object can represent almost any kind of data with attributes and behavior. This can be as specific as a single person or as general as a shape. A class is the implementation of an object in code. Put simply, a class outlines all the properties and things that an object can do. For example, we can write a class to represent a person.

```c++
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
                cout << "Age cannot be negative" << endl;
                return;
            }
            this->age = age;
        }
    private:
        int age;
        string name;
};
```

Here we have a class called Person. It has two private variables, age and name, and four public functions. The private keyword means that the variables can only be accessed by functions in the class. The public keyword means that the functions can be accessed by anything.
The function called Person() in the public section is called a constructor. A constructor is a special function that is called when an object is created. In this case, it takes in a name and an age and sets the private variables to those values. 
The other functions are called getters and setters. Getters are used to get the value of a private variable, and setters are used to set the value of a private variable. The reason for using getters and setters rather than accessing the variables directly is that it allows us to control how the variables are accessed. For example, we can make sure that the age is never set to a negative number. This is all part of the concept of encapsulation.

You may also notice the use of the keyword this. This is a special keyword that means the variable belongs to the object. For example, the setName() setter function takes in a string called name. However, the object also has a private variable called name. In order to differentiate between the two, we use the keyword this to refer to the private variable that belongs to the object.

Now that we have a class, we can create an object from it. This is called instantiation. We can create an object like this:

```c++
Person person1 = Person("John", 20);
```

This creates a person object called person1 with the name John and the age 20, and we can access the name and age like this:

```c++
cout << person1.getName() << endl;
cout << person1.getAge() << endl;
```

We can also change the name and age like this:

```c++
person1.setName("Bob");
person1.setAge(30);
```

Sometimes when we want to represented related things, we want to use inheritance. Inheritance is the creation of a new class that is based on an existing class. The new class is called a derived class, and the existing class is called a base class. The derived class inherits all the properties and functions of the base class. For example, we can create a class called Student that inherits from Person.

```c++
class Student : public Person {
    public:
        Student(string name, int age, string major) : Person(name, age) {
            this->major = major;
        }
        string getMajor() {
            return major;
        }
        void setMajor(string major) {
            this->major = major;
        }
    private:
        string major;
};
```

Here, we have a class called Student that inherits from Person. The Student constructor takes in a name, age, and major, and calls the Person constructor with the name and age. This is because the Student class inherits the name and age from the Person class. The Student class also has a private variable called major, and a getter and setter for it. We can create a Student object like this:

```c++
Student student1 = Student("John", 20, "Computer Science");
```

Even though you can't see the getters and setters for the name and age, they are still there and work for the Student class. We can access the name and age like we can with the Person class.

Sometimes, we want to give one function multiple implementations. This is called polymorphism. For example we can add a Person constructor that takes in no arguments, takes only a name, or takes only an age. This is called function overloading.

```c++
class Person {
    public:
        Person() {
            name = "";
            age = 0;
        }
        Person(string name) {
            this->name = name;
            age = 0;
        }
        Person(int age) {
            name = "";
            this->age = age;
        }
        Person(string name, int age) {
            this->name = name;
            this->age = age;
        }
```


We can also re-define a function in a derived class. This is called function overriding. For example, we can re-define the getName() function in the Student class to return the name and major like this:

```c++
string getName() {
    return Person::getName() + " " + major;
}
```