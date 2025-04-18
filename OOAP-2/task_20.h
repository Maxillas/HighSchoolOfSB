#include <iostream>
#include <memory>
#include <vector>

// Наследование вариаций (переопределение родительского метода)
class Bicycle {
public:
	virtual void drive() {
		std::cout << "bike drive" << std::endl;
	}
};

class MountainBicycle : public Bicycle {
public:
	void drive() override {
		std::cout << "mountain bike drive" << std::endl;
	}
};

class RoadBicycle : public Bicycle {
public:
	// в этом случае базовый метод drive() остается и доступен для вызова
	void drive(int road) {
		std::cout << "road bike drive in " << road << std::endl;
	}
};
/*________________________*/

// Наследование с конкретизацией (базовый класс абстрактный)

class Car {
public:
	virtual void drive() = 0;
};

class Lada: public Car {
public:
	void drive() override {
		std::cout << "lada drive" << std::endl;
	}
};

class Bmw: public Car {
public:
	void drive() override {
		std::cout << "Bmw drive" << std::endl;
	}
};

/*________________________*/

// Структурное наследование (Добавление новому типу некоторого нового свойства (от класса Wolf например)
class Wolf {
public:
	virtual void bark(){};
};

class Human {
public:
	virtual void think(){};
};

class Werewolf: public Human, public Wolf {
public:

};

/*________________________*/
