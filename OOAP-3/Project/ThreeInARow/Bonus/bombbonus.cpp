#include "bombbonus.h"

BombBonus::BombBonus() : m_active(true) {}

std::string BombBonus::name() const {
	return "Bomb";
}

int BombBonus::scoreValue() const {
	return 50;
}

void BombBonus::apply() {
	m_active = false;
}

bool BombBonus::isActive() const {
	return m_active;
}
