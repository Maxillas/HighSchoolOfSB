#include "userinterface.h"

void ConsoleUI::displayField(GameField *field) {
	int cols = 8;

	for (size_t i = 0; i < field->size(); ++i) {
		Cell* cell = field->getCell(i);
		std::cout << cell->type() << " ";
		if ((i + 1) % cols == 0) std::cout << "\n";
	}
}

std::pair<Cell *, Cell *> ConsoleUI::getMoveInput(GameField *field) {
	if (!field || field->size() == 0) {
		throw std::runtime_error("Game field is not initialized");
	}

	int x1, y1, x2, y2;
	std::cout << "Enter move (fromX fromY toX toY): ";
	std::cin >> x1 >> y1 >> x2 >> y2;

	int cols = 8;
	int rows = field->size() / cols;

	if (x1 < 0 || x1 >= cols || y1 < 0 || y1 >= rows ||
		x2 < 0 || x2 >= cols || y2 < 0 || y2 >= rows) {
		throw std::out_of_range("Invalid coordinates");
	}

	return {
		field->getCell(y1 * cols + x1),
		field->getCell(y2 * cols + x2)
	};
}

void ConsoleUI::displayMessage(const std::string &msg) {
	std::cout << msg << "\n";
}
