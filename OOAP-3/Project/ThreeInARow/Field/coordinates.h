#ifndef COORDINATES_H
#define COORDINATES_H


class Coordinates
{
public:
	Coordinates() = default;
	Coordinates(int x, int y);
	void setCoordinates(int x, int y);
	int x();
	int y();

	bool operator==(const Coordinates& other) const {
		return (m_x == other.m_x) && (m_y == other.m_y);
	}

private:
	int m_x = 0;
	int m_y = 0;
};

#endif // COORDINATES_H
