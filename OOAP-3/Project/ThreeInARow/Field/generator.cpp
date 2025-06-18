#include "generator.h"

std::vector<Cell *> Generator::generate(int rows, int cols)
{
	std::vector<Cell*> field;

	for (int r = 0; r < rows; ++r) {
		for (int c = 0; c < cols; ++c) {
			// Создаём новую ячейку и добавляем её в вектор
			field.push_back(new Cell(r, c));
		}
	}

	for (int y = 0; y < rows; ++y) {
		for (int x = 0; x < cols; ++x) {
			Cell* current = field[y * cols + x];

			if (x > 0) current->addNeighbor(field[y * cols + (x - 1)]);
			if (x < cols - 1) current->addNeighbor(field[y * cols + (x + 1)]);
			if (y > 0) current->addNeighbor(field[(y - 1) * cols + x]);
			if (y < rows - 1) current->addNeighbor(field[(y + 1) * cols + x]);
		}
	}

	return field;
}
