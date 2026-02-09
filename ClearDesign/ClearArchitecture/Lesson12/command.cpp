#include <stack>
#include "../pure_robot.cpp"

class Command {
	public:
	Command(std::string commandText) {
		m_name = commandText;
	}
	std::string getName() {return m_name;};
	private:
	std::string m_name;
};

class Api {
public:
	Api() {}
	~Api() {}

	void run(std::list<Command> commandList) {
		while(!commandList.empty()) {
			std::string command = commandList.front().getName();
			commandList.pop_front();
			m_stack.push(command);
		}
	}

private:
	void makeCommand() {
		while(!m_stack.empty()) {
			std::string currentCommand = m_stack.top();
			m_stack.pop();

			std::istringstream iss(currentCommand);
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
			if(currentCommand == "move") {
				m_currentState = m_robot->move(m_currentState);
			} else if(currentCommand == "turn") {
				m_currentState = m_robot->turn(m_currentState);
			} else if(currentCommand == "set") {
				int typeCleaner;
				if(param == "soap") {
					typeCleaner = 0;
				} else if(param == "water") {
					typeCleaner = 1;
				} else if(param == "brush") {
					typeCleaner = 2;
				}
				m_currentState = m_robot->set_state(m_currentState);
			} else if(currentCommand == "start") {
				m_currentState = m_robot->start(m_currentState);
			} else if(currentCommand == "stop") {
				m_currentState = m_robot->stop(m_currentState);
			}
		}
	}
	std::stack<std::string> m_stack;
	IRobot* m_robot = new PureRobot();
	RobotState m_currentState;
};
