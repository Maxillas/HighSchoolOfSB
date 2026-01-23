#include <iostream>
#include <sstream>
#include <list>
#include <cmath>


// Функциональная реализация чистильщика, имитируем
class PureRobot {
public:
	void transfer_to_cleaner();
	void move();
	void turn();
	void set_state();
	void start();
	void stop();
	void make(int state, int transfer, std::string command);
};


class Api {
public:
	void start() {
		m_robot.start();
	}

	void stop() {
		m_robot.stop();
	}

	void move() {
		m_robot.move();
	}

	void turn () {
		m_robot.turn();
	}

	void makeCommand(std::string command, int state, int transfer) {
		m_robot.make(state, transfer, command);
	}



private:
	PureRobot m_robot;
};
