#include <stack>
#include "../pure_robot.cpp"


class Capabilities {
public:
	virtual bool isActive() = 0;
	RobotState state;
};

class MoveCapabilities : public Capabilities {
	virtual bool isActive() { return true; };
};

class TurnCapabilities : public Capabilities {
	virtual bool isActive() { return true; };
};

class StateCapabilities : public Capabilities {
	virtual bool isActive() { return true; };
};

class StartCapabilities : public Capabilities {
	virtual bool isActive() { return true; };
};

class StopCapabilities : public Capabilities {
	virtual bool isActive() { return true; };
};

using Result = Capabilities;

class StateMonad {
public:

	explicit StateMonad() {
		m_robot = new PureRobot();
	}
	Capabilities* move(int dist) {
		Capabilities* result = new MoveCapabilities();
		result->state = m_robot->move(result->state);
		return result;
	};
	Capabilities* turn(int angle) {
		Capabilities* result = new TurnCapabilities();
		result->state = m_robot->move(result->state);
		return result;
	};
	Capabilities* set_state(int state) {
		Capabilities* result = new StateCapabilities();
		result->state = m_robot->move(result->state);
		return result;
	};
	Capabilities* start() {
		Capabilities* result = new StartCapabilities();
		result->state = m_robot->move(result->state);
		return result;
	};
	Capabilities* stop() {
		Capabilities* result = new StopCapabilities();
		result->state = m_robot->move(result->state);
		return result;
	};

private:
	IRobot *m_robot;
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
	std::list<Capabilities*> m_history;
};
