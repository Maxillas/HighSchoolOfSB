#include <iostream>
#include <sstream>
#include <list>
#include <cmath>


// Основная идея в том, чтобы хранить состояние в отдельной СД
// И передавать в методы константную ссылку и возвращать новое состояние
// Таким образом обеспечивается иммутабельность внутренних состояний


struct RobotState {
    int x = 0;
    int y = 0;
    int direction = 0; // 0: вверх, 1: вправо, 2: вниз, 3: влево
    bool is_cleaning = false;
    int cleaner_state = 0;
};

// Функциональная реализация чистильщика, имитируем
class PureRobot {
public:
	void transfer_to_cleaner();
	RobotState move(const RobotState& state);
	RobotState turn(const RobotState& state);
	RobotState set_state(const RobotState& state);
	RobotState start(const RobotState& state);
	RobotState stop(const RobotState& state);
	RobotState make(int transfer, std::string command, const RobotState& state);
};


class Api {
public:
	void start() {
		state = m_robot.start(state);
	}

	void stop() {
		state = m_robot.stop(state);
	}

	void move() {
		state = m_robot.move(state);
	}

	void turn () {
		state = m_robot.turn(state);
	}

	void makeCommand(std::string command, int transfer) {
		state = m_robot.make(transfer, command, state);
	}



private:
	PureRobot m_robot;
	RobotState state;
};
