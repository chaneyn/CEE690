import numpy as np
import ctypes
import numpy.ctypeslib as npct
import time
import os

def run_ctypes_benchmark():
    # 1. Load the shared library
    # We use os.path.abspath to ensure Python finds the .so file in the current directory
    lib_path = os.path.abspath('./libspatial.so')
    spatial_lib = ctypes.CDLL(lib_path)

    # 2. Define the NumPy C-Pointer Type
    # We strictly enforce that the array MUST be double (float64), 
    # MUST be 3D, and MUST be contiguous in memory.
    array_3d_double = npct.ndpointer(dtype=np.float64, ndim=3, flags='CONTIGUOUS')

    # 3. Define the Function Signature (CRITICAL STEP)
    # void compute_mean(double* array, long total_elements)
    spatial_lib.compute_mean.argtypes = [array_3d_double, ctypes.c_long]
    spatial_lib.compute_mean.restype = ctypes.c_double

    # 4. Generate the Climate Grid
    shape = (100, 180, 360)
    print(f"Generating synthetic grid of shape {shape}...")
    data = np.random.rand(*shape).astype(np.float64)

    # 5. Execute the C++ function
    print("Invoking ctypes C++ Engine...")
    start = time.time()
    # Notice we pass data.size to give the C++ code the total element count
    cpp_result = spatial_lib.compute_mean(data, data.size) 
    end = time.time()

    # 6. Verify against NumPy
    np_result = np.mean(data)
    
    print("-" * 35)
    print(f"C++ (ctypes) Result: {cpp_result:.8f}")
    print(f"NumPy Result:        {np_result:.8f}")
    print(f"Execution Time:      {end - start:.4f} seconds")
    print("-" * 35)

if __name__ == "__main__":
    run_ctypes_benchmark()
