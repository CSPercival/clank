CXX = g++
CXXFLAGS_RELEASE 	= -std=c++23 -Wall -O3 -Wextra -Wshadow -Wconversion -Wfloat-equal
CXXFLAGS_DEBUG 		= -std=c++23 -Wall -O0 -Wextra -Wshadow -Wconversion -Wfloat-equal -g -fsanitize=address,undefined

MODE ?= release
ifeq ($(MODE),release)
	CXXFLAGS = $(CXXFLAGS_RELEASE)
else ifeq ($(MODE),debug)
	CXXFLAGS = $(CXXFLAGS_DEBUG)
else
	$(error Unknown MODE '$(MODE)'; use 'debug' or 'release')
endif

%: %.cpp
	$(CXX) $(CXXFLAGS) $< -o $@