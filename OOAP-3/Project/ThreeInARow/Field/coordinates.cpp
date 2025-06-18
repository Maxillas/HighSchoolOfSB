#include "coordinates.h"

Coordinates::Coordinates(int x, int y) :
	m_x(x), m_y(y)
{}

void Coordinates::setCoordinates(int x, int y)
{
	m_x = x;
	m_y = y;
}

int Coordinates::x()
{
	return m_x;
}

int Coordinates::y()
{
	return m_y;
}
