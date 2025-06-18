#include <iostream>
#include "Game/game.h"
#include "UserInterface/userinterface.h"
#include "UserInterface/user.h"
#include <iostream>
#include <memory>



using namespace std;

int main() {
	try {
		// 1. Инициализация игры
		std::cout << "=== 3 IN A ROW GAME ===\n";

		// 2. Создание пользователя
		 std::string playerName;
		std::cout << "Enter your name: ";
		std::getline(std::cin, playerName);
		auto player = std::make_shared<User>(playerName.empty() ? "Player" : playerName);

		// 3. Инициализация компонентов
		auto gameField = std::make_unique<GameField>();
		auto gameLogic = std::make_unique<GameLogic>();
		auto combinationFinder = std::make_unique<Combination>();
		auto consoleUI = std::make_unique<ConsoleUI>();

		// 4. Создание и запуск игры
		Game game(
			std::move(gameField),
			std::move(gameLogic),
			std::move(combinationFinder),
			std::move(consoleUI),
			player
		);

		std::cout << "\nGame started! Match 3 or more items to score points.\n";
		std::cout << "Controls: enter coordinates as 'fromX fromY toX toY'\n\n";

		game.play();

	} catch (const std::exception& e) {
		std::cerr << "\nFatal error: " << e.what() << std::endl;
		return 1;
	}

	return 0;
}
