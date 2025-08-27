#include <iostream>
#include <cmath>
#include <functional>
#include <variant>
#include <vector>
#include <algorithm>

class Circle {
private:
	const double radius;

public:
	static Circle create(double r) {
		if (r <= 0) {
			throw std::invalid_argument("Радиус должен быть положительным");
		}
		return Circle(r);
	}

	double get_radius() const { return radius; }
	double area() const { return M_PI * radius * radius; }
	double perimeter() const { return 2 * M_PI * radius; }

private:
	Circle(double r) : radius(r) {}
};

class Rectangle {
private:
	const double width;
	const double height;

public:
	static Rectangle create(double w, double h) {
		if (w <= 0 || h <= 0) {
			throw std::invalid_argument("Стороны должны быть положительными");
		}
		return Rectangle(w, h);
	}

	double get_width() const { return width; }
	double get_height() const { return height; }
	double area() const { return width * height; }
	double perimeter() const { return 2 * (width + height); }

private:
	Rectangle(double w, double h) : width(w), height(h) {}
};

using Shape = std::variant<Circle, Rectangle>;

// Функциональные операции над фигурами
namespace ShapeOperations {
	// Чистая функция для вычисления площади
	double calculate_area(const Shape& shape) {
		return std::visit([](const auto& s) { return s.area(); }, shape);
	}

	// Чистая функция для вычисления периметра
	double calculate_perimeter(const Shape& shape) {
		return std::visit([](const auto& s) { return s.perimeter(); }, shape);
	}

	// Функция для масштабирования фигуры, возвращает новый объект
	Shape scale(const Shape& shape, double factor) {
		if (factor <= 0) {
			throw std::invalid_argument("Коэффициент масштабирования должен быть положительным");
		}

		return std::visit([factor](const auto& s) -> Shape {
			using T = std::decay_t<decltype(s)>;

			if constexpr (std::is_same_v<T, Circle>) {
				return Circle::create(s.get_radius() * factor);
			} else if constexpr (std::is_same_v<T, Rectangle>) {
				return Rectangle::create(s.get_width() * factor, s.get_height() * factor);
			}
		}, shape);
	}
}



int main() {
	auto circle = Circle::create(5.0);
	auto rectangle = Rectangle::create(4.0, 6.0);
	std::vector<Shape> shapes = { circle, rectangle };

	// Масштабирование фигур (чистая функция возвращает новые объекты)
	std::cout << "\nПосле масштабирования в 2 раза:" << std::endl;
	for (const auto& shape : shapes) {
		auto scaled = ShapeOperations::scale(shape, 2.0);
	}

	return 0;
}
