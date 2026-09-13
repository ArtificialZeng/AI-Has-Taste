CXX ?= c++
CXXFLAGS ?= -std=c++20 -O3 -Wall -Wextra -Wpedantic

.PHONY: all test clean

all: discovery coordinate_discovery

discovery: discovery.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

coordinate_discovery: coordinate_discovery.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

test: discovery coordinate_discovery
	./discovery --self-test
	python3 -m unittest discover -s tests -v

clean:
	rm -f discovery coordinate_discovery
