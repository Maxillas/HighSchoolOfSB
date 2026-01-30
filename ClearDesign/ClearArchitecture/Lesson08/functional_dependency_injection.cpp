#include <iostream>
#include <sstream>
#include <list>


struct RobotState {
    int x = 0;
    int y = 0;
    int direction = 0; // 0: вверх, 1: вправо, 2: вниз, 3: влево
    bool is_cleaning = false;
    int cleaner_state = 0;
};

class IRobot {
public:
	virtual void transfer_to_cleaner() = 0;
	virtual ~IRobot();
	virtual RobotState move(const RobotState& state) = 0;
	virtual RobotState turn(const RobotState& state) = 0;
	virtual RobotState set_state(const RobotState& state) = 0;
	virtual RobotState start(const RobotState& state) = 0;
	virtual RobotState stop(const RobotState& state) = 0;
	virtual RobotState make(int transfer, std::string command, const RobotState& state) = 0;
};

// Функциональная реализация чистильщика, ими	тируе	м
class PureRobot : public IRobot{
public:
	PureRobot() : IRobot() {}
	void transfer_to_cleaner() override;
	RobotState move(const RobotState& state) override;
	RobotState turn(const RobotState& state) override;
	RobotState set_state(const RobotState& state) override;
	RobotState start(const RobotState& state) override;
	RobotState stop(const RobotState& state) override;
	RobotState make(int transfer, std::string command, const RobotState& state) override;
};

// Вместо передачи функции, я сделал передачу указателя на реализацию роботоа
// Таким образом, мы можем передавать в апи нужную нам реализацию(по сути функцию) и
// тем самым осуществлять инъекцию зависимости
// Нам в любом случае нужен объект, т.к. функции внутри класса
// Если сделать функции вне класса, то можно передать указатель на них, как того требует задание
class Api {
public:
	Api() {}
	~Api() {}
	void start(IRobot* fooRobot) {
		state = fooRobot->start(state);
	}

	void stop(IRobot* fooRobot) {
		state = fooRobot->stop(state);
	}

	void move(IRobot* fooRobot) {
		state = fooRobot->move(state);
	}

	void turn (IRobot* fooRobot) {
		state = fooRobot->turn(state);
	}

	void makeCommand(std::string command, int transfer, IRobot* fooRobot) {
		state = fooRobot->make(transfer, command, state);
	}

private:
	RobotState state;
};
