cmake_minimum_required(VERSION 3.16)

project(ThreeInARow LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(ThreeInARow main.cpp
	Field/cell.h Field/cell.cpp
	Field/gamefield.h Field/gamefield.cpp
	Field/coordinates.h Field/coordinates.cpp
	Field/generator.h Field/generator.cpp
	Game/game.h Game/game.cpp
	Game/gamelogic.h Game/gamelogic.cpp
	Game/combination.h Game/combination.cpp
	Game/step.h Game/step.cpp
	Bonus/bonus.h Bonus/bonus.cpp
	Bonus/bonusset.h Bonus/bonusset.cpp
	Errors/error.h Errors/error.cpp
	Errors/errorshistory.h Errors/errorshistory.cpp
	Statistics/stephistory.h Statistics/stephistory.cpp
	Statistics/statistic.h Statistics/statistic.cpp
	UserInterface/user.h UserInterface/user.cpp
	UserInterface/userinterface.h UserInterface/userinterface.cpp
	Errors/invalidmoveerror.h Errors/invalidmoveerror.cpp
	Errors/outofboundserror.h Errors/outofboundserror.cpp
	Bonus/bombbonus.h Bonus/bombbonus.cpp
	Bonus/lineclearbonus.h Bonus/lineclearbonus.cpp)

include(GNUInstallDirs)
install(TARGETS ThreeInARow
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
