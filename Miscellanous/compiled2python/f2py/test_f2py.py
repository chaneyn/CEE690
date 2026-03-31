import numpy as np
import spatial_mean_f2py
import time

def run_fortran_benchmark():
    shape = (100, 180, 360)
    print(f"Generating synthetic grid of shape {shape}...")
    
    # HPC PRO-TIP: order='F' ensures the memory is laid out correctly for Fortran.
    # Without this, f2py will secretly copy the entire array!
    data = np.random.rand(*shape).astype(np.float64, order='F')

    print("Invoking Fortran Engine...")
    start = time.time()
    
    # Notice how clean the call is! We don't pass nx, ny, or nz. 
    # The !f2py intent(hide) directives handled it.
    fortran_result = spatial_mean_f2py.compute_mean(data)
    
    end = time.time()

    np_result = np.mean(data)
    
    print("-" * 35)
    print(f"Fortran Result: {fortran_result:.8f}")
    print(f"NumPy Result:   {np_result:.8f}")
    print(f"Execution Time: {end - start:.4f} seconds")
    print("-" * 35)

if __name__ == "__main__":
    run_fortran_benchmark()

