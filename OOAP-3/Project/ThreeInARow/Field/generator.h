#ifndef GENERATOR_H
#define GENERATOR_H
#include "vector"
#include "cell.h"

class Generator
{
public:
	Generator() = default;
	std::vector<Cell*> generate(int rows, int cols);
};

#endif // GENERATOR_H
