# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.24

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
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Stage_1.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/Stage_1.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Stage_1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Stage_1.dir/flags.make

CMakeFiles/Stage_1.dir/main.cpp.o: CMakeFiles/Stage_1.dir/flags.make
CMakeFiles/Stage_1.dir/main.cpp.o: /Users/taylor/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage\ 1/main.cpp
CMakeFiles/Stage_1.dir/main.cpp.o: CMakeFiles/Stage_1.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Stage_1.dir/main.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Stage_1.dir/main.cpp.o -MF CMakeFiles/Stage_1.dir/main.cpp.o.d -o CMakeFiles/Stage_1.dir/main.cpp.o -c "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/main.cpp"

CMakeFiles/Stage_1.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Stage_1.dir/main.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/main.cpp" > CMakeFiles/Stage_1.dir/main.cpp.i

CMakeFiles/Stage_1.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Stage_1.dir/main.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/main.cpp" -o CMakeFiles/Stage_1.dir/main.cpp.s

# Object files for target Stage_1
Stage_1_OBJECTS = \
"CMakeFiles/Stage_1.dir/main.cpp.o"

# External object files for target Stage_1
Stage_1_EXTERNAL_OBJECTS =

Stage_1: CMakeFiles/Stage_1.dir/main.cpp.o
Stage_1: CMakeFiles/Stage_1.dir/build.make
Stage_1: CMakeFiles/Stage_1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Stage_1"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Stage_1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Stage_1.dir/build: Stage_1
.PHONY : CMakeFiles/Stage_1.dir/build

CMakeFiles/Stage_1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Stage_1.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Stage_1.dir/clean

CMakeFiles/Stage_1.dir/depend:
	cd "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1" "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1" "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/cmake-build-debug" "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/cmake-build-debug" "/Users/taylor/Library/Mobile Documents/com~apple~CloudDocs/Documents/General/Technology/Projects/Blackjack/C++/Alpha/Stage 1/cmake-build-debug/CMakeFiles/Stage_1.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Stage_1.dir/depend
