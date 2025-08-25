#include <iostream>
#include <vector>
#include <thread>
#include <random>
#include <atomic>
#include <algorithm>
#include <future>
#include <numeric>

// Оптимизировал путем оптимального распаралеливания через std::async
// Уменьшил количество синхронизационных точке

class ComplexMultiThreadProcessing {
public:
    static void main() {
        constexpr int SIZE = 1000000;
        constexpr int THREADS = 4;

        std::vector<int> data(SIZE);

        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(0, 99);

        // Параллельное заполнение массива
        std::generate(data.begin(), data.end(), [&]() { return dis(gen); });

        std::atomic<int> totalSum = 0;

        const int chunkSize = SIZE / THREADS;
        const int remainder = SIZE % THREADS;

        std::vector<std::future<void>> futures;

        for (int i = 0; i < THREADS; ++i) {
            const int start = i * chunkSize + std::min(i, remainder);
            const int end = start + chunkSize + (i < remainder ? 1 : 0);

            futures.push_back(std::async(std::launch::async, [&data, &totalSum, start, end]() {
                int localSum = 0;
                for (int j = start; j < end; ++j) {
                    localSum += data[j];
                }
                totalSum += localSum;
            }));
        }

        for (auto& future : futures) {
            future.get();
        }

        const int sequentialSum = std::accumulate(data.begin(), data.end(), 0);

        std::cout << "Parallel sum: " << totalSum.load() << std::endl;
        std::cout << "Sequential sum: " << sequentialSum << std::endl;
        std::cout << "Results match: " << (totalSum == sequentialSum) << std::endl;
    }
};

int main() {
    ComplexMultiThreadProcessing::main();
    return 0;
