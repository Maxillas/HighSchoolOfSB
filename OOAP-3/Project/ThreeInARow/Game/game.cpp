#include "game.h"
#include "string"
#include "../Errors/invalidmoveerror.h"

void Game::play()
{
	m_field->init(8, 8);

	while (true) {
		// Отображение поля и статистики
		m_ui->displayField(m_field.get());
		std::cout << "Player: " << m_user->name()
				  << " | Score: " << m_user->statistics().totalScore() << "\n";

		try {
			// Получение хода от игрока
			auto [from, to] = m_ui->getMoveInput(m_field.get());

			// Проверка и выполнение хода
			if (m_logic->isValidMove(from, to)) {
				m_logic->swapCells(from, to);

				// Проверка комбинаций
				int score = m_combinations->search(m_field.get());

				if (score > 0) {
					Step currentStep(
						from,    // ICell* - исходная ячейка
						to,      // ICell* - целевая ячейка
						m_user->name(), // имя игрока
						std::chrono::system_clock::now() // текущее время
					);
					m_user->updateStatistics(currentStep, score);
					m_ui->displayMessage("Combo! +" + std::to_string(score) + " points");
				} else {
					m_logic->swapCells(from, to); // Отмена хода
					m_ui->displayMessage("No combinations found");
				}
			}
		}
		catch (const std::exception& e) {
			// Запись ошибки и продолжение игры
			m_user->addError(std::make_shared<InvalidMoveError>(
				e.what(),
				std::chrono::system_clock::now()
			));
			m_ui->displayMessage("Error: " + std::string(e.what()));
		}

		// Условие завершения игры можно добавить по желанию
	}

}
