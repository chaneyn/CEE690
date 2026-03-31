# ==========================================
# CEE 690: NetCDF + pybind11 Makefile
# ==========================================

CXX      = g++
CXXFLAGS = -O3 -Wall -shared -std=c++17 -fPIC

# Python & pybind11 dynamic paths
PY_INCLUDES = $(shell python3 -m pybind11 --includes)
PY_SUFFIX   = $(shell python3-config --extension-suffix)

# Our custom HPC User-Space paths
MY_PREFIX   = /hpc/home/nc153/miniconda3/envs/cee690
NC_INCLUDES = -I$(MY_PREFIX)/include
NC_LDFLAGS  = -L$(MY_PREFIX)/lib -L$(MY_PREFIX)/lib64
NC_LIBS     = -lnetcdf-cxx4 -lnetcdf

# The RPATH burns the library location into the .so file 
# so Python can find libnetcdf.so at runtime without LD_LIBRARY_PATH!
RPATH       = -Wl,-rpath,$(MY_PREFIX)/lib:$(MY_PREFIX)/lib64

# Targets
TARGET      = fast_nc$(PY_SUFFIX)
SRC         = nc_reader.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(PY_INCLUDES) $(NC_INCLUDES) \
	$(SRC) -o $(TARGET) \
	$(NC_LDFLAGS) $(NC_LIBS) $(RPATH)
	@echo "SUCCESS: Built $(TARGET)"

clean:
	rm -f *$(PY_SUFFIX)
	@echo "Cleaned directory."
