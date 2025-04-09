#include <iostream>

class None; //предварительное объявление, что Any знал про None

class General {
public:
	virtual void print() = 0;
};

class Any : virtual public General {
public:
	void print() override {
		std::cout << "copy from Any" << std::endl;
	}
	void anySpecific() {
		std::cout << "From Any" << std::endl;
	}
};

class Other : virtual public General {
public:
	void print() override {
		std::cout << "copy from Other" << std::endl;
	}
	void otherSpecific() {
		std::cout << "From Other" << std::endl;
	}
};

//Добавили виртуальное наследование, чтобы избежать неоднозначности при вызове метода через указатель на None
class None : public Any,  public Other {
	// пустой внутри
public:
	void print() override {
		Any::print();
	}
};

// Попытка присваивания
// Если типы будут несовместимы вызовется исключение и присвоится объект типа None
// Присвоить внутри класса не удастся, т.к. класс не знает про существование класса None.
// А базовых типов, встроенных в язык нет.
template <typename T, typename S>
void assignment_attempt(T* target, S* source) {
	try {
		target = source;
	} catch (const std::exception& e){
		None* Void = new None() ;
		target = Void;
		std::cout << "Ошибка #" << e.what() << std::endl;
	}
}

int main () {
	Any* true_any = new Any();
	None* none = new None();

	none->anySpecific();// выведет From Any
	none->otherSpecific(); // выведет From Other

	return 0;
}
