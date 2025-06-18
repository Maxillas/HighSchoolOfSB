#include "invalidmoveerror.h"

InvalidMoveError::InvalidMoveError(const std::string &details, std::chrono::system_clock::time_point when)
	: m_details(details), m_timestamp(when) {}

std::string InvalidMoveError::message() const {
	return "Invalid move: " + m_details;
}

std::chrono::system_clock::time_point InvalidMoveError::timestamp() const {
	return m_timestamp;
}

int InvalidMoveError::code() const { return 1; }
