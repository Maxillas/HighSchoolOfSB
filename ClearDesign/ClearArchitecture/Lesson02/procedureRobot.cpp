#include <iostream>
#include <sstream>
#include <list>
#include <cmath>


enum class CLEANER {
	WATER,
	SOAP,
	BRUSH
};

std::string soapDefinition(CLEANER state) {
	std::string resultStr = "";
	if(state == CLEANER::WATER) {
		resultStr = "water";
	} else if(state == CLEANER::BRUSH) {
		resultStr = "brush";
	} if(state == CLEANER::SOAP) {
		resultStr = "soap";
	}
	return resultStr;
}

void makeMove(int newPos, const double& angle, double& oldX, double& oldY) {
	oldX += newPos * cos(angle);
	oldY += newPos * sin(angle);
	std::cout << "currentPos is " << oldX << oldY << std::endl;
}

void makeTurn(double newAngle, double& oldAngle) {
	oldAngle += newAngle;
	std::cout << "currentAngle is " << oldAngle << std::endl;
}

void setSoap(CLEANER newCleaner, CLEANER& oldCleaner) {
	oldCleaner = newCleaner;
	std::cout << "currentCleaner is " << soapDefinition(oldCleaner) << std::endl;
}

void makeStart(CLEANER& state) {
	std::cout << "RobotCleaner is starting clean up with " << soapDefinition(state) << std::endl;
};

void makeStop() {
	std::cout << "RobotCleaner stop working";
};


void makeCommandList(std::list<std::string> commandList) {
	double x = 0;
	double y = 0;
	double angle = 0;
	CLEANER typeCleaner = CLEANER::BRUSH;

	while(!commandList.empty()) {
		std::string command = commandList.front();
		commandList.pop_front();

		std::istringstream iss(command);
		std::string cmdName;
		int value = 0;
		bool hasValue = false;
		std::string param;

		if (iss >> cmdName) {
			if (iss >> value) {
				hasValue = true;
			} else {
				iss.clear();
				iss >> param;
			}
		}

		if(cmdName == "move") {
			makeMove(value, angle, x, y);
		} else if(cmdName == "turn") {
			makeTurn(value, angle);
		} else if(cmdName == "set") {
			CLEANER newYypeCleaner;
			if(param == "soap") {
				newYypeCleaner = CLEANER::SOAP;
			} else if(param == "water") {
				newYypeCleaner = CLEANER::WATER;
			} else if(param == "brush") {
				newYypeCleaner = CLEANER::BRUSH;
			}
			setSoap(newYypeCleaner, typeCleaner);
		} else if(cmdName == "start") {
			makeStart(typeCleaner);
		} else if(cmdName == "stop") {
			makeStop();
		}
	}
}

int main(int argc, char *argv[])
{
	std::list<std::string> commandList;

	commandList.push_back("move 100");
	commandList.push_back("turn -90");
	commandList.push_back("set soap");
	commandList.push_back("start");
	commandList.push_back("move 50");
	commandList.push_back("stop");

	makeCommandList(commandList);

	return 0;
}
