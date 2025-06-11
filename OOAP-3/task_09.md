# Игра три в ряд
## Формирование архитектуры:
1. Field: 
class ICell {
    ICell (Coordinates coordinates);
    
    Coordinates m_coordinates;
}

class IGameField {

    void init(int row, int col); // создается поле и заполняется ячейками
    std::vector<Cell*> m_field;
    Generator m_generator; 
}

2. Game:

class Game {
    
    UserInterface m_userInterface;
    Statistic m_statistic;
    Errors m_errors;
    GameLogic m_logic;
    GameField m_field;
}

class GameLogic {
    Combination m_combination;
}

3. Statistics:

class StepHistory {
    std::list<Step> m_stepHistory;
}

class Statistic {
    StepHistory m_statistic;
}

4. UserInterface:
class UserInterface {
    User m_user;
}

5. Tests:

class Tests {
    void test1();
    void test2();
    
    Game m_game;
}
