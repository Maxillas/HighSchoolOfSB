#pragma once
#include <string>
#include <list>
#include <chrono>
#include <memory>

class IError {
public:
	virtual ~IError() = default;
	virtual std::string message() const = 0;
	virtual std::chrono::system_clock::time_point timestamp() const = 0;
	virtual int code() const = 0;
};


