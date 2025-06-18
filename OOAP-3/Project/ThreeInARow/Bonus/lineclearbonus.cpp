#include "lineclearbonus.h"


LineClearBonus::LineClearBonus() : m_active(true) {}

std::string LineClearBonus::name() const {
	return "Line Clear";
}

int LineClearBonus::scoreValue() const {
	return 30;
}

void LineClearBonus::apply() {
	// Логика очистки линии
	m_active = false;
}

bool LineClearBonus::isActive() const {
	return m_active;
}
