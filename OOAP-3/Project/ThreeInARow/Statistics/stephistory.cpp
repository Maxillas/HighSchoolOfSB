#include "stephistory.h"

void StepHistory::add(const Step &step)
{
	m_history.push_back(step);
}
