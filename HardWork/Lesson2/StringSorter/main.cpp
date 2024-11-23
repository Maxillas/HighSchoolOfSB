#include <iostream>
#include "sorter.h"
#include <cstdint>


// Функция фуззинга
extern "C" int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
    try {
        std::fstream tempFile("../../tests/test1.txt", std::ios::binary);

        tempFile.write(reinterpret_cast<const char*>(data), size);
        tempFile.close();

        Sorter fileSorter(SORTING_METHOD::FIRST_NAME, "../../tests/test1.txt");

        fileSorter.sorting();


    } catch (...) {
        // Ловим любые исключения для предотвращения крашей тестера
        std::cerr << "Exception caught!" << std::endl;
    }

    return 0;  // Успешное завершение
}
