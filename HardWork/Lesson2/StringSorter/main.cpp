#include <iostream>

#include "sorter.h"
// #include <iostream>
// #include <fstream>
// #include <string>
// #include "sorter.h"
#include <cstdint>

//#include "sortertests.h"


// Функция фуззинга
extern "C" int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
    try {
        // Преобразуем данные в строку
        std::string input(reinterpret_cast<const char*>(data), size);
        Sorter sorter(SORTING_METHOD::FIRST_NAME, input);  // Передаем данные в проект
        sorter.sorting();

        Sorter sorter_1 (SORTING_METHOD::SECOND_NAME, input);  // Передаем данные в проект
        sorter_1.sorting();

        Sorter sorter_2 (SORTING_METHOD::NUMBER, input);  // Передаем данные в проект
        sorter_2.sorting();

    } catch (...) {
        // Ловим любые исключения для предотвращения крашей тестера
        std::cerr << "Exception caught!" << std::endl;
    }

    return 0;  // Успешное завершение
}

//TODO переделать на файл!!!
// #include <fstream>
// #include <string>
// #include "YourProject.h"

// extern "C" int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
//     try {
//         // Сохраняем входные данные в файл
//         std::ofstream tempFile("fuzz_input.tmp", std::ios::binary);
//         tempFile.write(reinterpret_cast<const char*>(data), size);
//         tempFile.close();

//         // Передаем файл в проект
//         YourProject project;
//         project.runWithFile("fuzz_input.tmp");  // Метод для обработки файла
//     } catch (const std::exception& e) {
//         std::cerr << "Exception: " << e.what() << std::endl;
//     }
//     return 0;
// }



// int main()
// {
//     ushort sortingMethod;
//     std::cout << "Для сортировки по именам введите - 1,\n"
//                  "по фамилиям введите - 2,\n"
//                  "по телефонам введите - 3\n" << std::endl;
//     std::cin >> sortingMethod;

//     Sorter fileSorter(static_cast<SORTING_METHOD>(sortingMethod), "../../tests/test1.txt");

//     std::cout << "Ввод: " << sortingMethod << std::endl;
//     std::cout << "Вывод: " << std::endl;
//     for (const auto& i : fileSorter.sorting()) {
//         if(sortingMethod == static_cast<int>(SORTING_METHOD::FIRST_NAME)) {
//             std::cout << i.firstName + ' '
//                       << i.lastName + ':' + ' '
//                       << i.number << std::endl;
//             continue;
//         }
//         if(sortingMethod == static_cast<int>(SORTING_METHOD::NUMBER)) {
//             std::cout << i.number + ':' + ' '
//                       << i.lastName + ' '
//                       << i.firstName << std::endl;
//             continue;
//         }
//         std::cout << i.lastName + ' '
//                   << i.firstName + ':' + ' '
//                   << i.number << std::endl;
//     }

//     return 0;
// }
