#ifndef CELL_H
#define CELL_H
#include "coordinates.h"
#include "vector"

class Cell
{
public:
	Cell(int x, int y);
	Coordinates coordinates();

	const std::vector<Cell*>& neighbors() const;
	void addNeighbor(Cell* cell);

	int type() const;
    void setType(int type);


private:
	Coordinates m_coordinates;
	int m_type;
	std::vector<Cell*> m_neighbors;
};

#endif // CELL_H
