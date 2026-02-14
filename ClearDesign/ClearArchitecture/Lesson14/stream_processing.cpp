#include <stack>
#include "../pure_robot.cpp"
#include <map>
#include <vector>
#include <memory>
#include <functional>

// есть события-запросы (MoveRequested) и события-результаты (RobotMoved)
// CommandHandler только генерирует события-запросы, не содержит логики
// EventStore с подписками уведомляет процессоры о новых событиях
// из событий-результатов можно восстановить текущее состояние робота


struct Event {
	virtual ~Event() = default;
	virtual std::string getType() const = 0;
	virtual std::string getRobotId() const = 0;
};

struct MoveRequested : public Event {
	std::string robotId;
	double distance;

	MoveRequested(const std::string& id, double d) : robotId(id), distance(d) {}
	std::string getType() const override { return "MOVE"; }
	std::string getRobotId() const override { return robotId; }
};

struct TurnRequested : public Event {
	std::string robotId;
	double angle;

	TurnRequested(const std::string& id, double a) : robotId(id), angle(a) {}
	std::string getType() const override { return "TURN"; }
	std::string getRobotId() const override { return robotId; }
};

struct SetCleanerRequested : public Event {
	std::string robotId;
	std::string cleaner;

	SetCleanerRequested(const std::string& id, const std::string& c) : robotId(id), cleaner(c) {}
	std::string getType() const override { return "SET_CLEANER"; }
	std::string getRobotId() const override { return robotId; }
};

struct RobotMoved : public Event {
	std::string robotId;
	double distance;
	double newX;
	double newY;

	RobotMoved(const std::string& id, double d, double x, double y)
		: robotId(id), distance(d), newX(x), newY(y) {}
	std::string getType() const override { return "MOVED"; }
	std::string getRobotId() const override { return robotId; }
};

struct RobotTurned : public Event {
	std::string robotId;
	double angle;
	double newAngle;

	RobotTurned(const std::string& id, double a, double newA)
		: robotId(id), angle(a), newAngle(newA) {}
	std::string getType() const override { return "TURNED"; }
	std::string getRobotId() const override { return robotId; }
};

struct CleanerSet : public Event {
	std::string robotId;
	std::string cleaner;

	CleanerSet(const std::string& id, const std::string& c) : robotId(id), cleaner(c) {}
	std::string getType() const override { return "CLEANER_SET"; }
	std::string getRobotId() const override { return robotId; }
};

struct CleaningStarted : public Event {
	std::string robotId;

	CleaningStarted(const std::string& id) : robotId(id) {}
	std::string getType() const override { return "STARTED"; }
	std::string getRobotId() const override { return robotId; }
};

struct CleaningStopped : public Event {
	std::string robotId;

	CleaningStopped(const std::string& id) : robotId(id) {}
	std::string getType() const override { return "STOPPED"; }
	std::string getRobotId() const override { return robotId; }
};

using EventSubscriber = std::function<void(std::unique_ptr<Event>)>;

class EventStore {
public:
	void append(std::unique_ptr<Event> event) {
		std::string robotId = event->getRobotId();
		std::string eventType = event->getType();
		events[robotId].push_back(std::move(event));
		auto& lastEvent = events[robotId].back();
		notifySubscribers(robotId, lastEvent->getType(), std::move(cloneEvent(lastEvent.get())));
	}

	void subscribe(const std::string& robotId, const std::string& eventType, EventSubscriber subscriber) {
		subscribers[robotId][eventType].push_back(subscriber);
	}

	std::vector<Event*> getEvents(const std::string& robotId) {
		std::vector<Event*> result;
		if (events.find(robotId) != events.end()) {
			for (auto& event : events[robotId]) {
				result.push_back(event.get());
			}
		}
		return result;
	}

private:
	void notifySubscribers(const std::string& robotId, const std::string& eventType, std::unique_ptr<Event> event) {
		auto robotIt = subscribers.find(robotId);
		if (robotIt != subscribers.end()) {
			auto typeIt = robotIt->second.find(eventType);
			if (typeIt != robotIt->second.end()) {
				for (auto& subscriber : typeIt->second) {
					subscriber(cloneEvent(event.get()));
				}
			}
		}
	}

	std::unique_ptr<Event> cloneEvent(Event* event) {
		return std::unique_ptr<Event>(event);
	}

	std::map<std::string, std::vector<std::unique_ptr<Event>>> events;
	std::map<std::string, std::map<std::string, std::vector<EventSubscriber>>> subscribers;
};

class EventProcessor {
public:
	virtual ~EventProcessor() = default;
	virtual void process(std::unique_ptr<Event> event) = 0;
};

class MoveProcessor : public EventProcessor {
private:
	EventStore& eventStore;
	std::unique_ptr<IRobot> robot;

public:
	MoveProcessor(EventStore& store) : eventStore(store), robot(std::make_unique<PureRobot>()) {}

	void process(std::unique_ptr<Event> event) override {
		if (event->getType() == "MOVE") {
			auto* moveRequest = dynamic_cast<MoveRequested*>(event.get());
			if (moveRequest) {
				RobotState state = rebuildState(moveRequest->robotId);
				RobotState newState = robot->move(state, moveRequest->distance);

				eventStore.append(std::make_unique<RobotMoved>(
					moveRequest->robotId,
					moveRequest->distance,
					newState.x,
					newState.y
				));
			}
		}
	}

private:
	RobotState rebuildState(const std::string& robotId) {
		RobotState state;
		auto events = eventStore.getEvents(robotId);

		for (auto event : events) {
			if (event->getType() == "MOVED") {
				auto* moved = dynamic_cast<RobotMoved*>(event);
				if (moved) {
					state.x = moved->newX;
					state.y = moved->newY;
				}
			} else if (event->getType() == "TURNED") {
				auto* turned = dynamic_cast<Turned*>(event);
				if (turned) {
					state.angle = turned->newAngle;
				}
			} else if (event->getType() == "CLEANER_SET") {
				auto* cleaner = dynamic_cast<CleanerSet*>(event);
				if (cleaner) {
					// Обновляем состояние cleaner
				}
			}
		}
		return state;
	}
};

class TurnProcessor : public EventProcessor {
private:
	EventStore& eventStore;
	std::unique_ptr<IRobot> robot;

public:
	TurnProcessor(EventStore& store) : eventStore(store), robot(std::make_unique<PureRobot>()) {}

	void process(std::unique_ptr<Event> event) override {
		if (event->getType() == "TURN") {
			auto* turnRequest = dynamic_cast<TurnRequested*>(event.get());
			if (turnRequest) {
				RobotState state = rebuildState(turnRequest->robotId);
				RobotState newState = robot->turn(state, turnRequest->angle);

				eventStore.append(std::make_unique<RobotTurned>(
					turnRequest->robotId,
					turnRequest->angle,
					newState.angle
				));
			}
		}
	}

private:
	RobotState rebuildState(const std::string& robotId) {
		RobotState state;
		auto events = eventStore.getEvents(robotId);

		for (auto event : events) {
			if (event->getType() == "MOVED") {
				auto* moved = dynamic_cast<RobotMoved*>(event);
				if (moved) {
					state.x = moved->newX;
					state.y = moved->newY;
				}
			} else if (event->getType() == "TURNED") {
				auto* turned = dynamic_cast<RobotTurned*>(event);
				if (turned) {
					state.angle = turned->newAngle;
				}
			}
		}
		return state;
	}
};

class CommandHandler {

public:
	CommandHandler(EventStore& store) : eventStore(store) {}

	void handleMove(const std::string& robotId, double distance) {
		eventStore.append(std::make_unique<MoveRequested>(robotId, distance));
	}

	void handleTurn(const std::string& robotId, double angle) {
		eventStore.append(std::make_unique<TurnRequested>(robotId, angle));
	}

	void handleSetCleaner(const std::string& robotId, const std::string& cleaner) {
		eventStore.append(std::make_unique<SetCleanerRequested>(robotId, cleaner));
	}
private:
	EventStore& eventStore;
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
