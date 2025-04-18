#include <iostream>
#include <memory>
#include <vector>


class Bicycle {
public:
	virtual void drive() {}
};

class MountainBicycle : public Bicycle {
public:
	virtual void drive() {
		std::cout << "mountain bike drive" << std::endl;
	}
};

class RoadBicycle : public Bicycle {
public:
	virtual void drive() {
		std::cout << "road bike drive" << std::endl;
	}
};

class HybridBicycle : public Bicycle {
public:
	virtual void drive() {
		std::cout << "hibrid bike drive" << std::endl;
	}

	// Ковариантная типизация
	void fooKov(Bicycle* bike) {
		bike->drive();
	}
};


void fooPoly(Bicycle* bike) {
	//	Полиморфный вызов метода
	bike->drive(); // mountain bike drive
}
