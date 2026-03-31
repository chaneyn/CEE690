# --- CONFIGURATION ---
PYTHON = python3
F2PY   = $(PYTHON) -m numpy.f2py

# --- FILES ---
MODULE_NAME = spatial_mean_f2py
SRC         = spatial_mean.f90

# --- RULES ---

# Default target
all: build

# Compile the Fortran code into a Python extension
build: $(SRC)
	@echo "Compiling Fortran to Python using f2py..."
	$(F2PY) -c $(SRC) -m $(MODULE_NAME)
	@echo "SUCCESS: Compiled $(MODULE_NAME) module"

# Clean up the build files and generated folders
clean:
	@echo "Cleaning up generated libraries..."
	rm -f $(MODULE_NAME)*.so
	rm -rf .f2py_f2cmap
	rm -rf __pycache__


