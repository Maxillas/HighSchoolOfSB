#include <iostream>
#include "list"

using namespace std;


class GradeCalculator {

public:
	GradeCalculator() {};

	double calculateAverage(const std::list<double>& grades) {
		double gradeSum = 0;
		if(grades.empty()) return gradeSum;
		for(const auto& grade : grades) {
			if(grade < 0) {
				std::cout << "Ошибка во входных данных";
				continue;
			}
			gradeSum += grade;
		}
		return gradeSum / grades.size();
	}

};


class TestGradeCalculator {
public:
    TestGradeCalculator() {}
    ~TestGradeCalculator() {
        if (m_calculator) delete m_calculator;
    }

    bool testBasicAverage() {
        resetCalculator();
        std::list<double> numbers = {1.1, 2.3, 3.4, 4.6, 5.8};
        return assertEqual(3.44, m_calculator->calculateAverage(numbers), "testBasicAverage");
    }

    bool testSingleElement() {
        resetCalculator();
        std::list<double> numbers = {1.1};
        return assertEqual(1.1, m_calculator->calculateAverage(numbers), "testBasicAverage");
    }

    bool testNegativeNumbers() {
        resetCalculator();
        std::list<double> numbers = {-1, -2, -3, -4, -5};
        return assertEqual(0.0, m_calculator->calculateAverage(numbers), "testNegativeNumbers");
    }

    bool testMixedNumbers() {
        resetCalculator();
        std::list<double> numbers = {-2, 0, 2};
        return assertEqual(0.0, m_calculator->calculateAverage(numbers), "testMixedNumbers");
    }

    bool testEmptyList() {
        resetCalculator();
        std::list<double> numbers = {};
        return assertEqual(0.0, m_calculator->calculateAverage(numbers), "testMixedNumbers");
    }

    void runAllTests() {
        std::cout << "Running AverageCalculator tests...\n";
        bool allPassed = true;

        allPassed &= testBasicAverage();
        allPassed &= testSingleElement();
        allPassed &= testNegativeNumbers();
        allPassed &= testMixedNumbers();
        allPassed &= testEmptyList();


        std::cout << (allPassed ? "ALL TESTS PASSED" : "SOME TESTS FAILED") << "\n";
    }

private:
    GradeCalculator* m_calculator = nullptr;

    void resetCalculator() {
        delete m_calculator;
        m_calculator = new GradeCalculator();
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
	TestGradeCalculator tester;
	tester.runAllTests();
	return 0;
}
