# 1. SETTINGS (The "Knobs" of your project)
CXX      = g++
CXXFLAGS = -Wall -O2 -std=c++17
TARGET   = gravity.exe
OBJS     = main.o gravity.o

# 2. THE BUILD RULES
# Build the final executable
$(TARGET): $(OBJS)
	$(CXX) $(OBJS) -o $(TARGET)

# Compile main.o
main.o: main.cpp gravity.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

# Compile gravity.o
gravity.o: gravity.cpp gravity.hpp
	$(CXX) $(CXXFLAGS) -c gravity.cpp

# 3. UTILITIES
clean:
	rm -f $(OBJS) $(TARGET)


