#include <iostream>

using namespace std;


class BankAccount {

public:
	BankAccount(double balance) {
		m_balance = balance;
	};
	void deposit(double amount) {
		if (amount < 0) {
			throw std::invalid_argument("Deposit amount cannot be negative");
		}
		m_balance += amount;
	}

	void withdraw(double amount) {
		if (amount < 0) {
			throw std::invalid_argument("Withdrawal amount cannot be negative");
		}
		if (amount > m_balance) {
			throw std::runtime_error("Insufficient funds");
		}
		m_balance -= amount;
	}
	double getBalance() {
		return m_balance;
	}

private:
	double m_balance = 0;

};


class TestBankAccount {

public:
	TestBankAccount(const BankAccount &bankAcc) {};
	~TestBankAccount() {
		if(m_bankAcc) delete m_bankAcc;
	}


	bool testDeposit() {
		resetAccount(0);
		m_bankAcc->deposit(100);
		return assertEqual(100, m_bankAcc->getBalance(), "testDeposit");
	}

	bool testWithdraw() {
		resetAccount(200);
		m_bankAcc->withdraw(50);
		return assertEqual(150, m_bankAcc->getBalance(), "testWithdraw");
	}

	bool testInitialBalance() {
		resetAccount(500);
		return assertEqual(500, m_bankAcc->getBalance(), "testInitialBalance");
	}
	bool testNegativeDeposit() {
		resetAccount(100);
		try {
			m_bankAcc->deposit(-50);
			return false; // Should not reach here
		} catch (const std::invalid_argument&) {
			return assertEqual(100, m_bankAcc->getBalance(), "testNegativeDeposit");
		}
	}
	bool testOverdraft() {
		resetAccount(100);
		try {
			m_bankAcc->withdraw(150);
			return false; // Should not reach here
		} catch (const std::runtime_error&) {
			return assertEqual(100, m_bankAcc->getBalance(), "testOverdraft");
		}
	}
	void runAllTests() {
		std::cout << "Running tests...\n";
		bool allPassed = true;

		allPassed &= testDeposit();
		allPassed &= testWithdraw();
		allPassed &= testNegativeDeposit();
		allPassed &= testOverdraft();
		allPassed &= testInitialBalance();

		std::cout << (allPassed ? "ALL TESTS PASSED" : "SOME TESTS FAILED") << "\n";
	}

private:
	BankAccount* m_bankAcc = nullptr;

	void resetAccount(double balance) {
		delete m_bankAcc;
		m_bankAcc = new BankAccount(balance);
	}

	bool assertEqual(double expected, double actual, const std::string& testName) {
		if (std::abs(expected - actual) < 0.001) {
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
	BankAccount account(0);
	TestBankAccount tester(account);
	tester.runAllTests();
	return 0;
}

