#include "statistic.h"

void Statistic::addStep(const Step &step)
{
	m_steps.push_back(step);
}

void Statistic::addScore(int score)
{
	m_totalScore += score;
}

int Statistic::totalScore() const
{
	return m_totalScore;
}
