# --- CONFIGURATION ---
CXX      = g++
# -O3: Maximum speed optimization for the math loops
# -Wall: Show all warnings
# -shared -fPIC: Mandatory flags for building a .so dynamic library
CXXFLAGS = -O3 -Wall -shared -fPIC

# --- FILES ---
TARGET   = libspatial.so
SRC      = spatial_mean_ctypes.cpp

# --- RULES ---

# Default target when the user types 'make'
all: $(TARGET)

# Compile the C++ shared library
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)
	@echo "SUCCESS: Compiled $(TARGET)"

# Clean up the build files
clean:
	rm -f $(TARGET)
	@echo "Cleaned up $(TARGET)"
