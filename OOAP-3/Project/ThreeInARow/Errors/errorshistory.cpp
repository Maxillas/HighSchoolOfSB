#include "errorshistory.h"

void ErrorHistory::add(const std::shared_ptr<IError> &error) {
	m_errors.push_back(error);
	if (m_errors.size() > MAX_HISTORY_SIZE) {
		m_errors.pop_front();
	}
}

const std::list<std::shared_ptr<IError> > &ErrorHistory::all() const {
	return m_errors;
}

void ErrorHistory::clear() {
	m_errors.clear();
}
