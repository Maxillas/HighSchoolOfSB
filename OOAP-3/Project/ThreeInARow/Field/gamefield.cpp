#include "gamefield.h"
#include "generator.h"
#include "iostream"

GameField::GameField() {}

GameField::~GameField()
{
	for (auto cell : m_field) {
		delete cell;
	}
}

void GameField::init(int rows, int cols)
{
	Generator generator;
	m_field = generator.generate(rows, cols);
}

Cell *GameField::getCell(Coordinates coordinates)
{
	for(const auto& cell : m_field) {
		if(cell->coordinates() == coordinates) {
			return cell;
		}
	}
	return nullptr;
}

Cell *GameField::getCell(int index)
{
	if (index < 0 || index >= static_cast<int>(m_field.size())) {
        std::cout << "Invalid cell index" << std::endl;
        return nullptr;
    }
    return m_field[index];
}

size_t GameField::size() const
{
	return m_field.size();
}
