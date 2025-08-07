#include <iostream>

using namespace std;


class BankAccount {

public:
	BankAccount(double balance) {
		m_balance = balance;
	};
	void deposit(double newMoney) {
		m_balance += newMoney;
	}
	void withdraw(double withdraw) {
		m_balance -= withdraw;
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
	cout << "Hello World!" << endl;
	return 0;
}
