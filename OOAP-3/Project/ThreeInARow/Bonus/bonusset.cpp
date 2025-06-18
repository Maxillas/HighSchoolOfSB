#include "bonusset.h"


void BonusSet::add(const std::shared_ptr<IBonus> &bonus) {
	m_bonuses.push_back(bonus);
}

void BonusSet::use(const std::string &name) {
	for (auto& bonus : m_bonuses) {
		if (bonus->name() == name && bonus->isActive()) {
			bonus->apply();
			return;
		}
	}
}

const std::list<std::shared_ptr<IBonus> > &BonusSet::all() const {
	return m_bonuses;
}
