#include <stack>
#include "../pure_robot.cpp"


// Стоит добавить многопоточность и таймеры для опроса входящего потока данных
class Api {
public:
	Api(IRobot* robot) {
		m_robot = robot;
	}
	~Api() {}

	void run(std::list<std::string> commandList) {
		while(!commandList.empty()) {
			std::string command = commandList.front();
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
				move(value);
			} else if(currentCommand == "turn") {
				m_robot->turn(value);
			} else if(currentCommand == "set") {
				int typeCleaner;
				if(param == "soap") {
					typeCleaner = 0;
				} else if(param == "water") {
					typeCleaner = 1;
				} else if(param == "brush") {
					typeCleaner = 2;
				}
				m_robot->set_state(typeCleaner);
			} else if(currentCommand == "start") {
				m_robot->start();
			} else if(currentCommand == "stop") {
				m_robot->stop();
			}
		}
	}
	IRobot* m_robot;
	std::stack<std::string> m_stack;
};
