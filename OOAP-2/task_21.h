#include <iostream>
#include <memory>
#include <vector>

// Наследование реализации
class Bicycle {
public:
	virtual void drive() = 0;
};

class MountainBicycle : public Bicycle {
public:
	virtual void driveOnMountain() = 0;
};

/*________________________*/

// Наследование с конкретизацией (базовый класс абстрактный)

class Car {
public:
	enum class EngineError {
		LOW_FUEL,
		BAD_LAMBDA,
		HIGHT_TEMP,
		NONE
	};

	virtual void drive() = 0;

	EngineError m_engineError = EngineError::NONE;
};

class Lada: public Car {
public:
	Lada() {
		m_fuel = 100;
		m_lambda = 100;
		m_temp = 90;
	}
	void drive() override {
		while(m_fuel > 100) {
			std::cout << "lada drive" << std::endl;
			m_fuel--;
			if(m_fuel == 0) {
				m_engineError = EngineError::LOW_FUEL;
			}
			m_temp++;
			if(m_temp > 120) {
				m_engineError = EngineError::HIGHT_TEMP;
			}
		}
	}

	EngineError getEngineError() {
		return m_engineError;
	}

private:
	int m_fuel = 0;
	int m_lambda = 0;
	int m_temp = 0;
};

