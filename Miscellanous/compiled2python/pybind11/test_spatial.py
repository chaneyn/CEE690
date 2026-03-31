import numpy as np
import spatial_math
import time

def run_benchmark():
    # 1. Setup dimensions (e.g., 100 days, 180 latitudes, 360 longitudes)
    # Total points: ~6.4 million
    shape = (100, 180, 360)
    
    # IMPORTANT: Use float64 to match 'double' in C++
    data = np.random.rand(*shape).astype(np.float64)

    # 2. Test the C++ Extension
    print("Invoking C++ Engine...")
    start_cpp = time.time()
    cpp_result = spatial_math.compute_mean(data)
    end_cpp = time.time()
    
    # 3. Test Native NumPy (for verification)
    print("Invoking NumPy (Reference)...")
    start_np = time.time()
    np_result = np.mean(data)
    end_np = time.time()

    # 4. Report Results
    print("-" * 35)
    print(f"C++ Result:   {cpp_result:.8f}")
    print(f"NumPy Result: {np_result:.8f}")
    print(f"Difference:   {abs(cpp_result - np_result):.2e}")
    print("-" * 35)
    print(f"C++ Time:     {end_cpp - start_cpp:.6f} seconds")
    print(f"NumPy Time:   {end_np - start_np:.6f} seconds")
    
    if np.allclose(cpp_result, np_result):
        print("\nSUCCESS: The C++ wrapper is mathematically accurate!")
    else:
        print("\nERROR: Mismatch detected. Check data types or indexing.")

if __name__ == "__main__":
    run_benchmark()



