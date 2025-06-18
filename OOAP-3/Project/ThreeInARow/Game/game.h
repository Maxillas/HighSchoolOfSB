#ifndef GAME_H
#define GAME_H

#include "../Field/gamefield.h"
#include "../Game/combination.h"
#include "../Game/gamelogic.h"
#include "../Statistics/statistic.h"
#include "../UserInterface/userinterface.h"
#include "../UserInterface/user.h"
#include <memory>


class Game
{
public:	
	Game(std::unique_ptr<GameField> field,
		 std::unique_ptr<GameLogic> logic,
		 std::unique_ptr<Combination> combo,
		 std::unique_ptr<IUserInterface> ui,
		 std::shared_ptr<User> user)
		: m_field(std::move(field)),
		  m_logic(std::move(logic)),
		  m_combinations(std::move(combo)),
		  m_ui(std::move(ui)),
		  m_user(std::move(user)) {}

	void play();

private:
	std::unique_ptr<GameField> m_field;
	std::unique_ptr<GameLogic> m_logic;
	std::unique_ptr<Combination> m_combinations;
	std::unique_ptr<IUserInterface> m_ui;
	std::shared_ptr<User> m_user;
};

#endif // GAME_H
