import numpy as np
import spatial_mean_cython
import time

# Generate 3D grid
data = np.random.rand(100, 180, 360).astype(np.float64)

start = time.time()
cython_mean = spatial_mean_cython.compute_mean(data)
end = time.time()

print(f"Cython Mean: {cython_mean:.6f}")
print(f"Execution:   {end - start:.4f} seconds")
