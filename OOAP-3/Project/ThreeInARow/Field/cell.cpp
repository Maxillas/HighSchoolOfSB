#include "cell.h"

Cell::Cell(int x, int y) {
	m_coordinates.setCoordinates(x, y);
}

Coordinates Cell::coordinates()
{
	return m_coordinates;
}

const std::vector<Cell *> &Cell::neighbors() const
{
	return m_neighbors;
}

void Cell::addNeighbor(Cell *cell)
{
	m_neighbors.push_back(cell);
}

int Cell::type() const
{
	return m_type;
}

void Cell::setType(int type)
{
	m_type = type;
}

