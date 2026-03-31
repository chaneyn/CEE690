# --- SETTINGS ---
CXX      = g++
# Optimized for speed (-O3) and required for shared libs (-fPIC)
CXXFLAGS = -O3 -Wall -shared -std=c++17 -fPIC

# --- PYTHON CONFIG ---
# This command automatically finds the correct include paths for pybind11
PY_INCLUDES = $(shell python3 -m pybind11 --includes)
# This handles the suffix (e.g., .cpython-310-x86_64-linux-gnu.so)
PY_SUFFIX   = $(shell python3-config --extension-suffix)

# --- TARGETS ---
TARGET   = spatial_math$(PY_SUFFIX)
SRC      = spatial_mean.cpp

# --- RULES ---
all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(PY_INCLUDES) $(SRC) -o $(TARGET)

clean:
	rm -f *$(PY_SUFFIX)



