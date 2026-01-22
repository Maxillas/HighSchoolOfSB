#include "robot.cpp"
#include "robot_cleaner_manager.cpp"
#include <list>


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
