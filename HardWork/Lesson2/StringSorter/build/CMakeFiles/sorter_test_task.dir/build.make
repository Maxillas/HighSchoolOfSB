# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build

# Include any dependencies generated for this target.
include CMakeFiles/sorter_test_task.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/sorter_test_task.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/sorter_test_task.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/sorter_test_task.dir/flags.make

CMakeFiles/sorter_test_task.dir/main.cpp.o: CMakeFiles/sorter_test_task.dir/flags.make
CMakeFiles/sorter_test_task.dir/main.cpp.o: /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/main.cpp
CMakeFiles/sorter_test_task.dir/main.cpp.o: CMakeFiles/sorter_test_task.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/sorter_test_task.dir/main.cpp.o"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/sorter_test_task.dir/main.cpp.o -MF CMakeFiles/sorter_test_task.dir/main.cpp.o.d -o CMakeFiles/sorter_test_task.dir/main.cpp.o -c /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/main.cpp

CMakeFiles/sorter_test_task.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/sorter_test_task.dir/main.cpp.i"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/main.cpp > CMakeFiles/sorter_test_task.dir/main.cpp.i

CMakeFiles/sorter_test_task.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/sorter_test_task.dir/main.cpp.s"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/main.cpp -o CMakeFiles/sorter_test_task.dir/main.cpp.s

CMakeFiles/sorter_test_task.dir/sortertests.cpp.o: CMakeFiles/sorter_test_task.dir/flags.make
CMakeFiles/sorter_test_task.dir/sortertests.cpp.o: /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/sortertests.cpp
CMakeFiles/sorter_test_task.dir/sortertests.cpp.o: CMakeFiles/sorter_test_task.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/sorter_test_task.dir/sortertests.cpp.o"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/sorter_test_task.dir/sortertests.cpp.o -MF CMakeFiles/sorter_test_task.dir/sortertests.cpp.o.d -o CMakeFiles/sorter_test_task.dir/sortertests.cpp.o -c /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/sortertests.cpp

CMakeFiles/sorter_test_task.dir/sortertests.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/sorter_test_task.dir/sortertests.cpp.i"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/sortertests.cpp > CMakeFiles/sorter_test_task.dir/sortertests.cpp.i

CMakeFiles/sorter_test_task.dir/sortertests.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/sorter_test_task.dir/sortertests.cpp.s"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/sortertests.cpp -o CMakeFiles/sorter_test_task.dir/sortertests.cpp.s

CMakeFiles/sorter_test_task.dir/sorter.cpp.o: CMakeFiles/sorter_test_task.dir/flags.make
CMakeFiles/sorter_test_task.dir/sorter.cpp.o: /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/sorter.cpp
CMakeFiles/sorter_test_task.dir/sorter.cpp.o: CMakeFiles/sorter_test_task.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/sorter_test_task.dir/sorter.cpp.o"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/sorter_test_task.dir/sorter.cpp.o -MF CMakeFiles/sorter_test_task.dir/sorter.cpp.o.d -o CMakeFiles/sorter_test_task.dir/sorter.cpp.o -c /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/sorter.cpp

CMakeFiles/sorter_test_task.dir/sorter.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/sorter_test_task.dir/sorter.cpp.i"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/sorter.cpp > CMakeFiles/sorter_test_task.dir/sorter.cpp.i

CMakeFiles/sorter_test_task.dir/sorter.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/sorter_test_task.dir/sorter.cpp.s"
	clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/sorter.cpp -o CMakeFiles/sorter_test_task.dir/sorter.cpp.s

# Object files for target sorter_test_task
sorter_test_task_OBJECTS = \
"CMakeFiles/sorter_test_task.dir/main.cpp.o" \
"CMakeFiles/sorter_test_task.dir/sortertests.cpp.o" \
"CMakeFiles/sorter_test_task.dir/sorter.cpp.o"

# External object files for target sorter_test_task
sorter_test_task_EXTERNAL_OBJECTS =

sorter_test_task: CMakeFiles/sorter_test_task.dir/main.cpp.o
sorter_test_task: CMakeFiles/sorter_test_task.dir/sortertests.cpp.o
sorter_test_task: CMakeFiles/sorter_test_task.dir/sorter.cpp.o
sorter_test_task: CMakeFiles/sorter_test_task.dir/build.make
sorter_test_task: CMakeFiles/sorter_test_task.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable sorter_test_task"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sorter_test_task.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/sorter_test_task.dir/build: sorter_test_task
.PHONY : CMakeFiles/sorter_test_task.dir/build

CMakeFiles/sorter_test_task.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/sorter_test_task.dir/cmake_clean.cmake
.PHONY : CMakeFiles/sorter_test_task.dir/clean

CMakeFiles/sorter_test_task.dir/depend:
	cd /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build /home/maxillas/Lessons/HighSchoolOfSB/HardWork/Lesson2/StringSorter/build/CMakeFiles/sorter_test_task.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/sorter_test_task.dir/depend

