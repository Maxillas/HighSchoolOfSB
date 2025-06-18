#ifndef USERINTERFACE_H
#define USERINTERFACE_H

#include "string"
#include "iostream"
#include "../Field/gamefield.h"

class IUserInterface {
public:
	virtual void displayField(GameField* field) = 0;
	virtual std::pair<Cell*, Cell*> getMoveInput(GameField* field) = 0; // Добавили параметр field
	virtual void displayMessage(const std::string& msg) = 0;
};

class ConsoleUI : public IUserInterface {
public:
	void displayField(GameField* field) override;

	std::pair<Cell*, Cell*> getMoveInput(GameField* field) override;

	void displayMessage(const std::string& msg) override;
};

#endif // USERINTERFACE_H
