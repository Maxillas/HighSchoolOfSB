#include "gamelogic.h"
#include "algorithm"

GameLogic::GameLogic() {}

bool GameLogic::isValidMove(Cell *from, Cell *to)
{
    const auto& neighbors = from->neighbors();
    return std::find(neighbors.begin(), neighbors.end(), to) != neighbors.end();
}

void GameLogic::swapCells(Cell *a, Cell *b)
{
	int temp = a->type();
    a->setType(b->type());
    b->setType(temp);
}
