# Standard CPU approach
import numpy as np
x_cpu = np.array([1, 2, 3])
l2_cpu = np.linalg.norm(x_cpu)

# Accelerated GPU approach
import cupy as cp
x_gpu = cp.array([1, 2, 3])
l2_gpu = cp.linalg.norm(x_gpu)



