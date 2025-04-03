#include <iostream>

// 1. Ковариантность
// в данном случае метод clone возвращает более конкретный тип после переопределения
class Animal {
public:
    virtual Animal* clone() const {
        std::cout << "Animal::clone()\n";
        return new Animal(*this);
    }
    virtual ~Animal() = default;
};

class Dog : public Animal {
public:
    // Ковариантный возвращаемый тип (Dog* вместо Animal*)
    Dog* clone() const override {
        std::cout << "Dog::clone()\n";
        return new Dog(*this);
    }
};

// 2. Контрвариантность
// Напрямую в с++ не поддерживается, можно имитировать через шаблоны
// например метод может принимать тип Т, который может являться и
// предком и наследником. Но на мой взгляд такой подход очень напоминает
// костыли и совершенно запутывает и усложняет читаемость кода, вместо того,
// чтобы улучшать его.
