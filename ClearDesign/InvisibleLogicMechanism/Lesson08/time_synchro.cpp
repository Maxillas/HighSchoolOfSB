#include "thread"
#include "iostream"

// Исправленный вариант с использованием атомарной переменной

class ThreadExample {
private:
	static std::atomic<int> counter;

public:
	static void main() {
		auto task = []() {
			for (int i = 0; i < 1000; i++) {
				counter++;
			}
		};

		std::thread thread1(task);
		std::thread thread2(task);

		thread1.join();
		thread2.join();

		std::cout << "Counter: " << counter << std::endl;
	}
};

std::atomic<int> ThreadExample::counter = 0;

int main() {
	ThreadExample::main();
	return 0;
}
