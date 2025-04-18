#include <iostream>
#include <memory>
#include <vector>


class Bicycle {
public:
	virtual void drive() {}

private:
	// вместо поля - наследники
	//TYPE_OF_BIKE m_type;
};

class MountainBicycle : public Bicycle {
public:
	virtual void drive() {
		// mountain bike drive
	}
};

class RoadBicycle : public Bicycle {
public:
	virtual void drive() {
		// road bike drive
	}
};

class HybridBicycle : public Bicycle {
public:
	virtual void drive() {
		// hibrid bike drive
	}
};
