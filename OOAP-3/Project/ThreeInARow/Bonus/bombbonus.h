#ifndef BOMBBONUS_H
#define BOMBBONUS_H

#include "bonus.h"

class BombBonus : public IBonus {
public:
	BombBonus();

	std::string name() const override;

	int scoreValue() const override;

	void apply() override;

	bool isActive() const override;

private:
	bool m_active;
};

#endif // BOMBBONUS_H
