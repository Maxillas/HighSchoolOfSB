#ifndef GAMEFIELD_H
#define GAMEFIELD_H

#include "vector"
#include "cell.h"

class GameField
{
public:
	GameField();
	~GameField();
	void init(int rows, int cols);
	Cell* getCell(Coordinates coordinates);
	Cell* getCell(int index);
	size_t size() const;

private:
	std::vector<Cell*> m_field;

};

#endif // GAMEFIELD_H
