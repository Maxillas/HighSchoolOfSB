cmake_minimum_required(VERSION 3.5)

project(sorter_test_task LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=fuzzer -fsanitize=address -g")

add_executable(sorter_test_task main.cpp
    sortertests.h sortertests.cpp
    sorter.h sorter.cpp
)

#include(GNUInstallDirs)
# install(TARGETS sorter_test_task
#     LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
#     RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
# )

#target_link_libraries(fuzz_target PRIVATE sorter_test_task)
