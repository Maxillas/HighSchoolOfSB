#include <iostream>

// 1. Метод публичен в родительском классе А и публичен в его потомке B;
class General1 {
public:
	void print();
};

class Any1 : public General1 {
};

void foo1() {
	General1 general;
	general.print();
	Any1 any;
	any.print();
}


/*__________________________________*/


// 2. Метод публичен в родительском классе А и скрыт в его потомке B;
class General2 {
public:
	void print();
};

//приватное наследование позволяет сделать публичные методы приватными
class Any2 : private General2 {
};

void foo2() {
	General2 general;
	general.print();
	Any2 any;
	//any.print(); - ошибка
}

/*__________________________________*/

// 3. Метод скрыт в родительском классе А и публичен в его потомке B;
// Такое в с++ недоступно

/*__________________________________*/

// 4. Метод скрыт в родительском классе А и скрыт в его потомке B.
class General4 {
protected:
	void print();
};

// Благодаря protected наследованию и члену класса мы скрыли реализацию от внешнего мира
// и позволили вызывать внутри класса
class Any4 : protected General4 {
	void foo() {
		print();
	}
};

void foo4() {
	General4 general;
	//general.print(); - ошибка
	Any4 any;
	//any.print(); - ошибка
}
