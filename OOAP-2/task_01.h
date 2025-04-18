#include "iostream"

// Базовый класс
class Animal {
public:
    void eat(){
        std::cout << "Animal eat" << std::endl;
    };
};

// Наследование от базового класса
class Dog : public Animal {
public:
    // Переопределение реализации метода класса предка
    void eat(){
        std::cout << "Dog eat" << std::endl;
    };
};

class Farm {
private:
    // Пример композиции
    Dog m_dog = Dog();
    Animal m_dogSimple = Dog();

    // Пример полиморфизма
    void polymorphExample() {
        m_dogSimple.eat();
    }
};
