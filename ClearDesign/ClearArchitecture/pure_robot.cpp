#include <iostream>
#include <sstream>
#include <list>

// Функциональная реализация чистильщика, имитируем
class IRobot {
public:
	virtual void transfer_to_cleaner() = 0;
	virtual ~IRobot();
	virtual void move(int dist) = 0;
	virtual void turn(int angle) = 0;
	virtual void set_state(int state) = 0;
	virtual void start() = 0;
	virtual void stop() = 0;
	virtual void make(int transfer, std::string command) = 0;
};

// Функциональная реализация чистильщика, имитируем
class PureRobot : IRobot{
public:
	void transfer_to_cleaner() override;
	void move(int dist) override;
	void turn(int angle) override;
	void set_state(int state) override;
	void start() override;
	void stop() override;
	void make(int transfer, std::string command) override;
};
