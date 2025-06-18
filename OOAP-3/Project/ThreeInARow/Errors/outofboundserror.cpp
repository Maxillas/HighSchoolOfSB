#include "outofboundserror.h"

OutOfBoundsError::OutOfBoundsError(int x, int y, std::chrono::system_clock::time_point when)
	: m_x(x), m_y(y), m_timestamp(when) {}

std::string OutOfBoundsError::message() const {
	return "Coordinates out of bounds: (" + std::to_string(m_x) + ", " + std::to_string(m_y) + ")";
}

std::chrono::system_clock::time_point OutOfBoundsError::timestamp() const {
	return m_timestamp;
}

int OutOfBoundsError::code() const { return 2; }
