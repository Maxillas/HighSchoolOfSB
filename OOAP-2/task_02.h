#include "iostream"

// Расширение класса-родителя
// Базовый класс
class Animal {
public:
    void eat(){};
    void sleep(){};
};

// Наследование от базового класса
class Dog : public Animal {
public:
    // расширение функционала базового класса
    void bark(){}; //только собака может лаять
};

/*___________________________________________________ */

// Специализация класса-родителя
// Базовый класс
class Professor {
public:
    virtual void teach(){
        std::cout << "Здесь профессор учит общим знаниям" << std::endl;
    };
    void takeExam(){};
};

class IT_Professor: public Professor {
public:
    // специализация путем переопределения метода базового класса
    void teach() override {
        std::cout << "It профессор учит computer science и языкам программирования" << std::endl;
    };
};
