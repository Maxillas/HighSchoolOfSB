#ifndef LINECLEARBONUS_H
#define LINECLEARBONUS_H

#include "bonus.h"

class LineClearBonus : public IBonus {
public:
	LineClearBonus();

	std::string name() const override;

	int scoreValue() const override;

	void apply() override;

	bool isActive() const override;

private:
	bool m_active;
};

#endif // LINECLEARBONUS_H
