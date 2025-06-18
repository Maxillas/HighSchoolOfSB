#ifndef COMBINATION_H
#define COMBINATION_H

#include "../Field/gamefield.h"

class Combination
{
public:
	Combination();

	int search(GameField* field);

private:
	void findCombination(Cell* cell, int type,
                        std::vector<Cell*>& combination,
                        std::vector<bool>& processed);
	int calculateScore(int count);
	int m_cols;
};

#endif // COMBINATION_H
