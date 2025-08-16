1. Мьютексы

std::mutex mtx;           // Мьютекс для синхронизации
int counter = 0;          // Общая переменная

void increment(int n) {
    for (int i = 0; i < n; ++i) {
        mtx.lock();               // Захватываем мьютекс
        ++counter;                // Критическая секция
        mtx.unlock();             // Освобождаем мьютекс
    }
}
int main() {
    const int num_increments = 100000;

    // Создаём два потока
    std::thread t1(increment, num_increments);
    std::thread t2(increment, num_increments);

    // Ждём завершения потоков
    t1.join();
    t2.join();

    std::cout << "Final counter value: " << counter << std::endl;
    return 0;
}

2. Блокировка (lock_guard)

std::mutex mtx;
int counter = 0;

void increment(int n) {
    for (int i = 0; i < n; ++i) {
        std::lock_guard<std::mutex> lock(mtx);  // Автоматическая блокировка/разблокировка
        ++counter;
    }
}
int main() {
    const int num_increments = 100000;

    std::thread t1(increment, num_increments);
    std::thread t2(increment, num_increments);

    t1.join();
    t2.join();

    std::cout << "Final counter value: " << counter << std::endl;
    return 0;
}

3. Атомарные операции

std::atomic<int> counter{0};  // Атомарная переменная

void increment(int n) {
    for (int i = 0; i < n; ++i) {
        ++counter;  // Атомарная операция — потокобезопасна
    }
}
int main() {
    const int num_increments = 100000;

    // Создаём два потока
    std::thread t1(increment, num_increments);
    std::thread t2(increment, num_increments);

    // Ждём завершения
    t1.join();
    t2.join();

    std::cout << "Final counter value: " << counter << std::endl;
    return 0;
}

4. Семафоры (только С++ 20)

// Пул из 3 "ресурсов"
std::counting_semaphore<3> sem(3);  // счётчик: 3, максимум: 3

void worker(int id) {
    std::cout << "Поток " << id << " ожидает ресурс...\n";

    sem.acquire();  // Захватываем один ресурс (уменьшаем счётчик)
    std::cout << "Поток " << id << " получил ресурс. Работает...\n";

    // Имитация работы
    std::this_thread::sleep_for(std::chrono::seconds(2));

    std::cout << "Поток " << id << " освободил ресурс.\n";
    sem.release();  // Возвращаем ресурс (увеличиваем счётчик)
}
int main() {
    std::vector<std::thread> threads;

    // Запускаем 6 потоков
    for (int i = 1; i <= 6; ++i) {
        threads.emplace_back(worker, i);
    }

    // Ждём завершения
    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Все потоки завершены.\n";
    return 0;
}

5. Фьючерсы

// Функция, которую будем выполнять асинхронно
int calculate_square(int x) {
    std::this_thread::sleep_for(std::chrono::seconds(2));  // Имитация долгой работы
    return x * x;
}

int main() {
    // Запускаем функцию асинхронно — получаем future
    std::future<int> fut = std::async(std::launch::async, calculate_square, 5);

    std::cout << "Ожидаем результат вычисления...\n";

    // Получаем результат (блокируется, пока функция не завершится)
    int result = fut.get();  // После вызова get() future становится пустым

    std::cout << "Результат: " << result << std::endl;

    return 0;
}
