#ifndef OUTOFBOUNDSERROR_H
#define OUTOFBOUNDSERROR_H

#include "error.h"

class OutOfBoundsError : public IError {
public:
	OutOfBoundsError(int x, int y, std::chrono::system_clock::time_point when);

	std::string message() const override;

	std::chrono::system_clock::time_point timestamp() const override;

	int code() const override;

private:
	int m_x, m_y;
	std::chrono::system_clock::time_point m_timestamp;
};

#endif // OUTOFBOUNDSERROR_H
