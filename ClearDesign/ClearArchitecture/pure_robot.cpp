#include <iostream>
#include <sstream>
#include <list>

struct RobotState {
    int x = 0;
    int y = 0;
    int direction = 0; // 0: вверх, 1: вправо, 2: вниз, 3: влево
    bool is_cleaning = false;
    int cleaner_state = 0;
    bool operator==(RobotState other) {
		if(other.x == x) return true;
		return false;
    }
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

// Функциональная реализация чистильщика, имитируем
class PureRobot : public IRobot{
public:
	void transfer_to_cleaner() override;
	RobotState move(const RobotState& state) override;
	RobotState turn(const RobotState& state) override;
	RobotState set_state(const RobotState& state) override;
	RobotState start(const RobotState& state) override;
	RobotState stop(const RobotState& state) override;
	RobotState make(int transfer, std::string command, const RobotState& state) override;
};
