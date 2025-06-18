#ifndef INVALIDMOVEERROR_H
#define INVALIDMOVEERROR_H

#include "error.h"

class InvalidMoveError : public IError {
public:
    InvalidMoveError(const std::string& details, std::chrono::system_clock::time_point when);

    std::string message() const override;

    std::chrono::system_clock::time_point timestamp() const override;

    int code() const override;

private:
    std::string m_details;
    std::chrono::system_clock::time_point m_timestamp;
};

#endif // INVALIDMOVEERROR_H
