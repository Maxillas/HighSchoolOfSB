#include <iostream>
#include <memory>
#include <vector>


// 1. Метод публичен в родительском классе А и публичен в его потомке B;
class General {
public:
	virtual void print() {};
};

class Any : public General {
};

template <typename T>
class Vector : public General{
public:
	Vector(T newValue) {
		m_value = newValue;
		m_size = 1;
	}

	int len() {
		return m_size;
	}

	T getT() {
		return m_value;
	}

	Vector<T>* operator+ (const Vector& other) {
		if(len() != other.len()) {
			return nullptr;
		}
		// главное чтобы тип Т поддерживал сложение, или можно применить std::concept для проверки этого
		return new Vector<T>(this->m_value + other.m_value);
	}
private:
	T m_value;
	int m_size;
};


void foo() {
	Vector<int> inner(42);
	Vector<Vector<int>> middle(inner);
	Vector<Vector<Vector<int>>> outer(middle);

	Vector<int> inner2(87);
	Vector<Vector<int>> middle2(inner);
	Vector<Vector<Vector<int>>> outer2(middle);

	// базово так не работает, но есть способ через рекурсивный обход через std::is_class_v<T>
	auto result = outer + outer2;

}
