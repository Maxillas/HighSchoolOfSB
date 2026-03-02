#include <stack>
#include "../pure_robot.cpp"

// Добавил возможные ошибки и реакцию на них

using Result = std::pair<bool, RobotState>;

enum class ErrorCode {
	SUCCESS,
	HIT_BARRIER,
	NO_WATER,
	NO_SOAP,
	NO_BRUSH,
	INVALID_STATE
};

struct Responce {
	bool success;
};

struct MoveResponce : Responce {
	int distance;
};

struct TurnResponce : Responce {
	int turn;
};

struct StateResponce : Responce {
	int state;
};

class Command {
public:
	virtual Responce* next(Command* nextCommand) = 0;
	Responce* commandResponce;
	Command* nextCommand;
};

class MoveCommand : public Command {
public:
	void interpret(int dist) {
		m_distance = dist;
	}
	Responce* next(Command* nextCommand) override {
		nextCommand = nextCommand;
		MoveResponce* moveResponce = new MoveResponce();
		moveResponce->success = true;
		moveResponce->distance = m_distance;
		commandResponce = moveResponce;
		return commandResponce;
	}
private:
	int m_distance;
};

class TurnCommand : public Command {
public:
	void interpret(int angle) {
		m_angle = angle;
	}

	Responce* next(Command* nextCommand) override {
		nextCommand = nextCommand;
		TurnResponce* turnResponce = new TurnResponce();
		turnResponce->success = true;
		turnResponce->turn = m_angle;
		commandResponce = turnResponce;
		return commandResponce;
	}
private:
	int m_angle;
};

class SetStateCommand : public Command {
public:
	void interpret(int state) {
		m_state = state;
	}

	Responce* next(Command* nextCommand) override {
		nextCommand = nextCommand;
		StateResponce* stateResponce = new StateResponce();
		stateResponce->success = true;
		stateResponce->state = m_state;
		commandResponce = stateResponce;
		return commandResponce;
	}
private:
	int m_state;
};

class StopCommand : public Command {
public:
	Responce* next(Command* nextCommand) override {
		return nullptr;
	}

};

class Api {
public:
	Api() {}
	~Api() {}

	void run(std::list<std::string> commandList) {
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

			Command* newCommand;

			if(cmdName == "move") {
				newCommand = new MoveCommand();
			} else if(cmdName == "turn") {
				newCommand = new TurnCommand();
			} else if(cmdName == "set") {
				newCommand = new TurnCommand();
			} else if(cmdName == "stop") {
				newCommand = new StopCommand();
			}
			m_commandList.back()->nextCommand = newCommand;
			m_commandList.push_back(newCommand);
		}
	}

private:
	std::list<Command*> m_commandList;
};
