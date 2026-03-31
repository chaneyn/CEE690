import time
import numpy as np
import numba
from numba.openmp import njit, omp_set_num_threads, omp_get_num_threads, openmp_context

@njit
def calculate_mean_pyomp(data):
    """
    Using the Numba-OpenMP extension syntax.
    Note: We do NOT use parallel=True in the decorator because 
    the 'with openmp' block handles the parallelism explicitly.
    """
    val = 0.0
    count = 0
    rows, cols = data.shape

    # 1. Parallel Region (Spawn threads)
    with openmp_context("parallel for private(j) shared(data, val, count) reduction(+:val, count)"):
        for i in range(rows):
            for j in range(cols):
                val += data[i, j]
                count += 1

    return val / count

# 1. Setup Data
niter = 10
np.random.seed(1)
data = np.random.randn(15000, 15000)

# 3. Benchmark Numba-OpenMP
# Warm-up (Compilation happens here)
calculate_mean_pyomp(np.zeros((1, 1)))

for nthreads in [1,2,4,8,16]:
    omp_set_num_threads(nthreads)
    print(f"Running with {nthreads} threads")
    start_p = time.time()
    for i in range(niter):
        res_p = calculate_mean_pyomp(data)
    time_p = (time.time() - start_p)/niter
    print(f"Result:    {res_p} | Time: {time_p:.4f}s")
