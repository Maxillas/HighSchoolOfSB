#include <string>
#include <cmath>


struct Distance {
	double x = 0;
	double y = 0;
};

class RobotCleaner {

public:
	enum class CLEANER {
		WATER,
		SOAP,
		BRUSH
	};

	void move(int dist) {
		m_dist.x = dist * cos(m_angle);
		m_dist.y = dist * sin(m_angle);
	};
	void turn(int angle) {
		m_angle = angle;
	};
	void set(CLEANER type) {
		m_cleaner = type;
	};
	void start() {};
	void stop() {};

	Distance currentDist() {
		return m_dist;
	}

	int currentTurn() {
		return m_angle;
	}

	CLEANER currentCleaner() {
		return m_cleaner;
	}

	std::string currentCleanerStr() {
		std::string resultStr = "";
		if(m_cleaner == RobotCleaner::CLEANER::WATER) {
			resultStr = "water";
		} else if(m_cleaner == RobotCleaner::CLEANER::BRUSH) {
			resultStr = "brush";
		} if(m_cleaner == RobotCleaner::CLEANER::SOAP) {
			resultStr = "soap";
		}
		return resultStr;
	}

private:
	Distance m_dist;
	int m_angle = 0;
	CLEANER m_cleaner;
};
