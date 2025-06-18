#ifndef STATISTIC_H
#define STATISTIC_H

#include "list"
#include "../Game/step.h"

class Statistic
{
public:
	void addStep(const Step& step);

	void addScore(int score);

	int totalScore() const;

private:
	std::list<Step> m_steps;
	int m_totalScore = 0;
};

#endif // STATISTIC_H
