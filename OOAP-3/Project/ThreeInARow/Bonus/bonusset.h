#ifndef BONUSSET_H
#define BONUSSET_H

#include "bonus.h"

class BonusSet {
public:
    void add(const std::shared_ptr<IBonus>& bonus);

    void use(const std::string& name);

    const std::list<std::shared_ptr<IBonus>>& all() const;

private:
    std::list<std::shared_ptr<IBonus>> m_bonuses;
};

#endif // BONUSSET_H
