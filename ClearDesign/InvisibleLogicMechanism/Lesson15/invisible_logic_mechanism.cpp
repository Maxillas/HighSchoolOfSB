#include "iostream"

// class Animal {
// public:
//     void makeSound() {
//         std::cout << ("Some generic animal sound");
//     }
// };
class Animal {
public:
    void makeGenericSound() {
        std::cout << ("Some generic animal sound");
    }
};

class Cat : public Animal {
    // Переопределение метода makeSound
public:
    void makeSound() {
        std::cout << "Meow";
    }
};

class Main {
public:
    void main(std::string args) {
        Animal* myCat = new Cat();
        myCat->makeSound();  // "Meow"
    }
};

// Вопрос 1: такой код не соберется, компиллятор не сможет найти метод makeSound 
// у класса Animal, т.к. он по-другому называется

// Вопрос 2: Поведение будет аналогичным в строке cat.makeSound(3), 
// Компилятор не сможет найти метод с такой сигнатурой и выдаст ошибку

// Вопрос 3: 
// Может возникнуть проблема гонки данных, т.к. два метода (скорее всего асинхронные), 
// работают с одним и тем же ресурсом, не атомарным
