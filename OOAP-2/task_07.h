#include "iostream"

// Базовый абстрактный класс
class Animal {
public:
    virtual void eat() = 0;
};

// Наследование от базового класса
class Dog : public Animal {
public:
    // Переопределение реализации метода класса предка
    void eat(){
        std::cout << "Dog eat" << std::endl;
    };
};

// Наследование от базового класса
class Cat : public Animal {
public:
    // Переопределение реализации метода класса предка
    void eat(){
        std::cout << "Cat eat" << std::endl;
    };
};

void foo() {
    Animal* dog = new Dog; //создаем объект класса Dog и присваиваем его указателю на базовый класс
    dog->eat(); // вызовется "Dog eat" - произойдет динамическое связывание
    
    //Аналогично для Cat
    Animal* сat = new Cat; //создаем объект класса Cat и присваиваем его указателю на базовый класс
    сat->eat(); // вызовется "Cat eat" - произойдет динамическое связывание
    
};