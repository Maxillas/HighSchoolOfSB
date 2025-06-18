#ifndef STEPHISTORY_H
#define STEPHISTORY_H

#include "list"
#include "../Game/step.h"

class StepHistory
{
public:
	void add(const Step& step);
private:
    std::list<Step> m_history;
};

#endif // STEPHISTORY_H
