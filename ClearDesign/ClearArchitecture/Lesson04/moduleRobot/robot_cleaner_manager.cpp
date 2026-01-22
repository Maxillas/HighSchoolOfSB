#include "robot.cpp"
#include "list"
#include <sstream>
#include <iostream>


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
