#include "combination.h"

Combination::Combination() {}

int Combination::search(GameField *field)
{
	int score = 0;
	std::vector<bool> processed(field->size(), false);

	for (size_t i = 0; i < field->size(); ++i) {
		if (!processed[i]) {
			Cell* cell = field->getCell(i);
			std::vector<Cell*> combination;
			findCombination(cell, cell->type(), combination, processed);

			if (combination.size() >= 3) {
				score += calculateScore(combination.size());
				// Удаляем комбинацию
				for (auto c : combination) {
					c->setType(-1); // Помечаем для удаления
				}
			}
		}
	}

	return score;
}

void Combination::findCombination(Cell *cell, int type, std::vector<Cell *> &combination, std::vector<bool> &processed)
{
	if (!cell || processed[cell->coordinates().y() * m_cols + cell->coordinates().x()])
            return;

	if (cell->type() == type) {
		combination.push_back(cell);
		processed[cell->coordinates().y() * m_cols + cell->coordinates().x()] = true;

		for (auto neighbor : cell->neighbors()) {
			findCombination(neighbor, type, combination, processed);
		}
	}
}

int Combination::calculateScore(int count)
{
	if (count == 3) return 10;
	if (count == 4) return 20;
	return 50;
}
