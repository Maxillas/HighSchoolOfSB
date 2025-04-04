#include <string>
#include <memory>
#include <iostream>


class General {
public:
    // 1. Копирование (DeepCopy)
    virtual void copyFrom(const General& other) = 0;

    // 2. Клонирование (создание нового объекта + DeepCopy)
    virtual std::unique_ptr<General> clone() const = 0;

    // 3. Сравнение (глубокое)
    virtual bool equals(const General& other) const = 0;

    // 4. Сериализация в строку
    virtual std::string serialize() const = 0;

    // 5. Десериализация из строки
    virtual void deserialize(const std::string& data) = 0;

    // 6. Печать (текстовое представление)
    virtual void print() const = 0;

    // 7. Проверка типа
    virtual bool isInstanceOf(const std::type_info& typeName) const = 0;

    // 8. Получение реального типа
    virtual const std::type_info& getType() const = 0;

    // Виртуальный деструктор
    virtual ~General() = default;
};

class Any : public General {
public:
    void copyFrom(const General& other) override {
        if (this != &other) {
            // Копирование внутренних членов
        }
    }
    virtual std::unique_ptr<General> clone() const override {
		auto newObj = std::make_unique<Any>();
		newObj->copyFrom(*this);
		return newObj;
    }
    virtual bool equals(const General& other) const override {
		//или любое другое сравнение по различным признакам
		//выбран этот, т.к. std::string имеет оператор ==
		return other.serialize() == this->serialize();
    }
    virtual std::string serialize() const override {
		return "Any";
    }
    virtual void deserialize(const std::string& data) override {
		//какой-то принцип десериализации из строки
    }
    virtual void print() const override{
		std::cout << this->serialize() << std::endl;
    }
    virtual bool isInstanceOf(const std::type_info& typeName) const override {
		return typeName == typeid(Any) || typeName == typeid(General);
    }
    virtual const std::type_info& getType() const override {
		return typeid(this);
    };
};
