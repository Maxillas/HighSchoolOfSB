#include <stack>
#include "../pure_robot.cpp"

using Result = std::pair<bool, RobotState>;

class StateMonad {
public:

	explicit StateMonad() {
		m_robot = new PureRobot();
	}
	Result move(int dist) {
		Result result;
		m_state = m_robot->move(m_state);
		result.second = m_state;
		result.first = (m_state == result.second);
		return result;
	};
	Result turn(int angle) {
		Result result;
		m_state = m_robot->turn(m_state);
		result.second = m_state;
		result.first = (m_state == result.second);
		return result;
	};
	Result set_state(int state) {
		Result result;
		m_state = m_robot->set_state(m_state);
		result.second = m_state;
		result.first = (m_state == result.second);
		return result;
	};
	Result start() {
		Result result;
		m_state = m_robot->start(m_state);
		result.second = m_state;
		result.first = (m_state == result.second);
		return result;
	};
	Result stop() {
		Result result;
		m_state = m_robot->stop(m_state);
		result.second = m_state;
		result.first = (m_state == result.second);
		return result;
	};

private:
	IRobot *m_robot;
	RobotState m_state;
};

class Api {
public:
	Api() {}
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
				m_history.push_back(m_monad.move(value));
			} else if(currentCommand == "turn") {
				m_history.push_back(m_monad.turn(value));
			} else if(currentCommand == "set") {
				int typeCleaner;
				if(param == "soap") {
					typeCleaner = 0;
				} else if(param == "water") {
					typeCleaner = 1;
				} else if(param == "brush") {
					typeCleaner = 2;
				}
				m_history.push_back(m_monad.set_state(typeCleaner));
			} else if(currentCommand == "start") {
				m_history.push_back(m_monad.start());
			} else if(currentCommand == "stop") {
				m_history.push_back(m_monad.stop());
			}
		}
	}
	StateMonad m_monad;
	std::stack<std::string> m_stack;
	std::list<Result> m_history;
};
