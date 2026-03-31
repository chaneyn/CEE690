import numpy as np
from numba import cuda

# 1. The Kernel (The GPU 'Worker')
@cuda.jit
def hello_cuda_kernel(io_array):
    # Determine the unique thread position in the 1D grid
    rank = cuda.grid(1)
    stride = cuda.gridsize(1) # Total threads in the grid
    
    # Iterate through all the elements
    for i in range(rank,io_array.size,stride):
        io_array[i] *= 2

# 2. Host Setup
data = np.arange(10**5, dtype=np.float64)
print(f"Original array on Host: {data}")

# 3. Step A: Move data to the Device (GPU)
# This is like sending a message in MPI
d_data = cuda.to_device(data)

# 4. Step B: Configure the Grid
# We'll use 5 blocks with 32 threads
threads_per_block = 32
blocks_per_grid = 5

# Launch the kernel
hello_cuda_kernel[blocks_per_grid, threads_per_block](d_data)

# 5. Step C: Move data back to the Host (CPU)
# This is like receiving a message in MPI
result = d_data.copy_to_host()

print(f"Result from Device:     {result}")


