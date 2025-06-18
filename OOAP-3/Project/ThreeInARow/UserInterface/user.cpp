#include "user.h"

User::User(const std::string &name) : m_name(name) {}

std::string User::name() const { return m_name; }

const Statistic &User::statistics() const {
	return m_statistics;
}

const ErrorHistory &User::errorsHistory() const {
	return m_errorHistory;
}

void User::setName(const std::string &name) {
	m_name = name;
}

void User::addError(const std::shared_ptr<IError> &error) {
	m_errorHistory.add(error);
}

void User::updateStatistics(const Step &step, int score) {
	m_statistics.addStep(step);
	m_statistics.addScore(score);
}
