#include <iostream>
#include <sstream>
#include <list>
#include <cmath>


struct Distance {
	double x = 0;
	double y = 0;
};

class RobotCleaner {

public:
	enum class CLEANER {
		WATER,
		SOAP,
		BRUSH
	};

	void move(int dist) {
		m_dist.x = dist * cos(m_angle);
		m_dist.y = dist * sin(m_angle);
	};
	void turn(int angle) {
		m_angle = angle;
	};
	void set(CLEANER type) {
		m_cleaner = type;
	};
	void start() {};
	void stop() {};

	Distance currentDist() {
		return m_dist;
	}

	int currentTurn() {
		return m_angle;
	}

	CLEANER currentCleaner() {
		return m_cleaner;
	}

	std::string currentCleanerStr() {
		std::string resultStr = "";
		if(m_cleaner == RobotCleaner::CLEANER::WATER) {
			resultStr = "water";
		} else if(m_cleaner == RobotCleaner::CLEANER::BRUSH) {
			resultStr = "brush";
		} if(m_cleaner == RobotCleaner::CLEANER::SOAP) {
			resultStr = "soap";
		}
		return resultStr;
	}

private:
	Distance m_dist;
	int m_angle = 0;
	CLEANER m_cleaner;
};


class RobotCleanerManager {


public:
	RobotCleanerManager(RobotCleaner *currentRobot) : m_currentRobot(currentRobot) {}

	void makeCommandList(std::list<std::string> commandList) {

		while(!commandList.empty()) {
			std::string command = commandList.front();
			commandList.pop_front();

			std::istringstream iss(command);
			std::string cmdName;
			int value = 0;
			bool hasValue = false;
			std::string param;

			if (iss >> cmdName) {
				// Пробуем извлечь число
				if (iss >> value) {
					hasValue = true;
				} else {
					// Если не число, может быть строковый параметр
					iss.clear();
					if (iss >> param) {
						// Это строковый параметр
					}
				}
			}

			if(cmdName == "move") {
				makeMove(value);
			} else if(cmdName == "turn") {
				makeTurn(value);
			} else if(cmdName == "set") {
				RobotCleaner::CLEANER typeCleaner;
				if(param == "soap") {
					typeCleaner = RobotCleaner::CLEANER::SOAP;
				} else if(param == "water") {
					typeCleaner = RobotCleaner::CLEANER::WATER;
				} else if(param == "brush") {
					typeCleaner = RobotCleaner::CLEANER::BRUSH;
				}
				setSoap(typeCleaner);
			} else if(cmdName == "start") {
				makeStart();
			} else if(cmdName == "stop") {
				makeStop();
			}
		}
	};

private:
	RobotCleaner* m_currentRobot = nullptr;

	void makeMove(int newPos) {
		if(!m_currentRobot) std::cout << "robot is not set" << std::endl;
		m_currentRobot->move(newPos);
		std::cout << "currentPos is " << m_currentRobot->currentDist().x << m_currentRobot->currentDist().y << std::endl;
	}

	void makeTurn(int newAngle) {
		if(!m_currentRobot) std::cout << "robot is not set" << std::endl;
		m_currentRobot->turn(newAngle);
		std::cout << "currentAngle is " << m_currentRobot->currentTurn() << std::endl;
	}

	void setSoap(RobotCleaner::CLEANER newCleaner) {
		if(!m_currentRobot) std::cout << "robot is not set" << std::endl;
		m_currentRobot->set(newCleaner);
		RobotCleaner::CLEANER currentCleaner = m_currentRobot->currentCleaner();
		std::cout << "currentCleaner is " << m_currentRobot->currentCleanerStr() << std::endl;
	}

	void makeStart() {
		if(!m_currentRobot) std::cout << "robot is not set" << std::endl;
		m_currentRobot->start();
		std::cout << "RobotCleaner is starting clean up with " << m_currentRobot->currentCleanerStr() << std::endl;
	};

	void makeStop() {
		if(!m_currentRobot) std::cout << "robot is not set" << std::endl;
		m_currentRobot->stop();
		std::cout << "RobotCleaner stop working";
	};

};

int main(int argc, char *argv[])
{
	RobotCleaner baseRobot;
	RobotCleanerManager robotManager(&baseRobot);

	std::list<std::string> commandList;

	commandList.push_back("move 100");
	commandList.push_back("turn -90");
	commandList.push_back("set soap");
	commandList.push_back("start");
	commandList.push_back("move 50");
	commandList.push_back("stop");

	robotManager.makeCommandList(commandList);

	return 0;
}
