cmake_minimum_required(VERSION 3.5)

project(HW3 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(HW3 main.cpp
    taskmanager.h taskmanager.cpp
    taskmanager_tests.h)

include(GNUInstallDirs)
install(TARGETS HW3
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
