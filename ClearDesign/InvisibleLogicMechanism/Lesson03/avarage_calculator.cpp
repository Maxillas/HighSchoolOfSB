#include <iostream>
#include "vector"

using namespace std;


class AverageCalculator {

public:
	AverageCalculator() {};
	double calculateAvarage(const std::vector<int>& numbers) {
		double sum = 0;
		for (auto& num : numbers) {
			sum += num;
		}
		return sum / numbers.size();
	};
};

//Отсутствует тест на пустой вектор соответственно будет ошибка деления на 0

class TestAverageCalculator {
public:
    TestAverageCalculator() {}
    ~TestAverageCalculator() {
        if (m_calculator) delete m_calculator;
    }

    bool testBasicAverage() {
        resetCalculator();
        std::vector<int> numbers = {1, 2, 3, 4, 5};
        return assertEqual(3.0, m_calculator->calculateAvarage(numbers), "testBasicAverage");
    }

    bool testSingleElement() {
        resetCalculator();
        std::vector<int> numbers = {42};
        return assertEqual(42.0, m_calculator->calculateAvarage(numbers), "testSingleElement");
    }

    bool testNegativeNumbers() {
        resetCalculator();
        std::vector<int> numbers = {-1, -2, -3, -4, -5};
        return assertEqual(-3.0, m_calculator->calculateAvarage(numbers), "testNegativeNumbers");
    }

    bool testMixedNumbers() {
        resetCalculator();
        std::vector<int> numbers = {-2, 0, 2};
        return assertEqual(0.0, m_calculator->calculateAvarage(numbers), "testMixedNumbers");
    }

    void runAllTests() {
        std::cout << "Running AverageCalculator tests...\n";
        bool allPassed = true;

        allPassed &= testBasicAverage();
        allPassed &= testSingleElement();
        allPassed &= testNegativeNumbers();
        allPassed &= testMixedNumbers();

        std::cout << (allPassed ? "ALL TESTS PASSED" : "SOME TESTS FAILED") << "\n";
    }

private:
    AverageCalculator* m_calculator = nullptr;

    void resetCalculator() {
        delete m_calculator;
        m_calculator = new AverageCalculator();
    }

    template<typename T>
    bool assertEqual(T expected, T actual, const std::string& testName) {
        if (expected == actual) {
            std::cout << "[PASS] " << testName << "\n";
            return true;
        }

        std::cerr << "[FAIL] " << testName
                  << " - Expected: " << expected
                  << ", Actual: " << actual << "\n";
        return false;
    }

    bool assertEqual(double expected, double actual, const std::string& testName) {
        const double epsilon = 0.0001;
        if (std::abs(expected - actual) < epsilon) {
            std::cout << "[PASS] " << testName << "\n";
            return true;
        }

        std::cerr << "[FAIL] " << testName
                  << " - Expected: " << expected
                  << ", Actual: " << actual << "\n";
        return false;
    }
};


int main()
{
	TestAverageCalculator tester;
	tester.runAllTests();
	return 0;
}
