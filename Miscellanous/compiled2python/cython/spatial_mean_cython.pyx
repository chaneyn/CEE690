# cython: boundscheck=False
# cython: wraparound=False

import numpy as np
cimport numpy as cnp

def compute_mean(double[:, :, ::1] grid):
    """Compute the spatial mean of a 3D NumPy array using Cython."""
    
    # 1. Statically type the loop variables
    cdef Py_ssize_t i, j, k
    cdef Py_ssize_t x_max = grid.shape[0]
    cdef Py_ssize_t y_max = grid.shape[1]
    cdef Py_ssize_t z_max = grid.shape[2]
    
    cdef double total_sum = 0.0
    cdef double total_elements = x_max * y_max * z_max

    # 2. The Heavy Lifting
    for i in range(x_max):
        for j in range(y_max):
            for k in range(z_max):
                # 3. Direct memory access
                total_sum += grid[i, j, k]

    return total_sum / total_elements



