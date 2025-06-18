#include "step.h"

Step::Step(Cell *fromCell, Cell *toCell, const std::string &playerName, std::chrono::system_clock::time_point time)
	: from(fromCell),
	to(toCell),
	player(playerName),
	timestamp(time) {}

Cell *Step::getFrom() const { return from; }

Cell *Step::getTo() const { return to; }

std::string Step::getPlayer() const { return player; }
