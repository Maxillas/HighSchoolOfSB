#include <string>
#include <memory>
#include <iostream>


class General {
public:
    // final запрещает дальнейшее переобределение данного метода
    virtual void copyFrom(const General& other) final {};
};

class Any : public General {
public:
	// Ошибка, метод final нельзя переопределять
    // void copyFrom(const General& other) override {
    //     if (this != &other) {
    //         // Копирование внутренних членов
    //     }
    // }
};
