#ifndef STEP_H
#define STEP_H

#include "../Field/cell.h"
#include <memory>
#include <chrono>
#include <string>

class Step
{
public:
    // Основной конструктор
	Step(Cell* fromCell,
		 Cell* toCell,
		 const std::string& playerName,
		 std::chrono::system_clock::time_point time);

    // Геттеры
    Cell* getFrom() const;
    Cell* getTo() const;
    std::string getPlayer() const;
    auto getTime() const { return timestamp; }

private:
    Cell* from;
    Cell* to;
    std::string player;
    std::chrono::system_clock::time_point timestamp;
};

#endif // STEP_H
