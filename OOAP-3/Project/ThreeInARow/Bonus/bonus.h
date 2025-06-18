#ifndef BONUS_H
#define BONUS_H

#include <string>
#include <list>
#include <memory>

class IBonus {
public:
	virtual ~IBonus() = default;
	virtual std::string name() const = 0;
	virtual int scoreValue() const = 0;
	virtual void apply() = 0;
	virtual bool isActive() const = 0;
};

#endif // BONUS_H
