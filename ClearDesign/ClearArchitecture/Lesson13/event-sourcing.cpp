#include <stack>
#include "../pure_robot.cpp"
#include <map>
#include <vector>
#include <memory>

struct Event {
	virtual ~Event() = default;
	virtual std::string getType() const = 0;
};

struct RobotMoved : public Event {
	double distance;
	RobotMoved(double d) : distance(d) {}
	std::string getType() const override { return "MOVED"; }
};

struct RobotTurned : public Event {
	double angle;
	RobotTurned(double a) : angle(a) {}
	std::string getType() const override { return "TURNED"; }
};

struct CleanerSet : public Event {
	std::string cleaner;
	CleanerSet(const std::string& c) : cleaner(c) {}
	std::string getType() const override { return "CLEANER_SET"; }
};

struct CleaningStarted : public Event {
	CleaningStarted() {}
	std::string getType() const override { return "STARTED"; }
};

struct CleaningStopped : public Event {
	CleaningStopped() {}
	std::string getType() const override { return "STOPPED"; }
};

class EventStore {
public:
	void append(const std::string& robotId, std::unique_ptr<Event> event) {
		events[robotId].push_back(std::move(event));
	}

	std::vector<Event*> getEvents(const std::string& robotId) {
		std::vector<Event*> result;
		for (auto& event : events[robotId]) {
			result.push_back(event.get());
		}
		return result;
	}
private:
	std::map<std::string, std::vector<std::unique_ptr<Event>>> events;
};

class CommandHandler {
private:
	EventStore& eventStore;
	std::unique_ptr<IRobot> robot;

public:
	CommandHandler(EventStore& store)
		: eventStore(store), robot(std::make_unique<PureRobot>()) {}

	void handleMove(const std::string& robotId, double distance) {
		auto events = eventStore.getEvents(robotId);
		eventStore.append(robotId, std::make_unique<RobotMoved>(distance));
	}

	void handleTurn(const std::string& robotId, double angle) {
		auto events = eventStore.getEvents(robotId);
		eventStore.append(robotId, std::make_unique<RobotTurned>(angle));
	}

	void handleSetCleaner(const std::string& robotId, const std::string& cleaner) {
		auto events = eventStore.getEvents(robotId);
		eventStore.append(robotId, std::make_unique<CleanerSet>(cleaner));
	}

	void undo(const std::string& robotId) {
		auto events = eventStore.getEvents(robotId);
	}
};

class Api {
public:
	Api() {}
	~Api() {}
	void moveRobot(const std::string& robotId, double distance) {
		commandHandler.handleMove(robotId, distance);
	}

	void turnRobot(const std::string& robotId, double angle) {
		commandHandler.handleTurn(robotId, angle);
	}

	void setCleaner(const std::string& robotId, const std::string& cleaner) {
		commandHandler.handleSetCleaner(robotId, cleaner);
	}

	RobotState getCurrentState(const std::string& robotId) {
		auto events = eventStore.getEvents(robotId);
		IRobot* robot = new PureRobot();
		RobotState state;
		return state;
	}

private:
	EventStore eventStore;
	CommandHandler commandHandler{eventStore};
};
