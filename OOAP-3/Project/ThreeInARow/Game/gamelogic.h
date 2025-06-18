#ifndef GAMELOGIC_H
#define GAMELOGIC_H

#include "../Field/cell.h"

class GameLogic
{
public:
	GameLogic();
	bool isValidMove(Cell* from, Cell* to);
	void swapCells(Cell* a, Cell* b);
};

#endif // GAMELOGIC_H
