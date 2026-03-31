import time
import numpy as np
from numba import cuda, float64
import warnings
from numba.core.errors import NumbaPerformanceWarning

# --- 1. THE KERNEL (The "Parallel Region") ---
# This runs on the GPU. Think of this as the body of your 'parallel for'.
@cuda.jit
def mean_kernel_2d(data, global_result):
    rows, cols = data.shape
    
    # IDENTIFY: Who am I? (get 2D coordinates)
    start_x, start_y = cuda.grid(2)
    
    # STRIDE: How big is the army of threads?
    stride_x, stride_y = cuda.gridsize(2)
    
    # PRIVATE VARIABLES: Just like private(j) in OpenMP
    # Each thread keeps its own running total in a register (fastest memory)
    thread_sum = 0.0
    thread_count = 0
    
    # WORK: Grid-Stride Loop
    # Instead of "for i in range(rows)", we jump by the grid size.
    # This ensures every element is covered, no matter the array size.
    for i in range(start_x, rows, stride_x):
        for j in range(start_y, cols, stride_y):
            thread_sum += data[i, j]
            thread_count += 1
            
    # REDUCTION: Combine results
    # We cannot return values. We must use atomic operations to avoid race conditions
    # when adding to the global result in VRAM.
    # index 0 = sum, index 1 = count
    cuda.atomic.add(global_result, 0, thread_sum)
    cuda.atomic.add(global_result, 1, thread_count)

# --- 2. THE HOST FUNCTION (The "Main Controller") ---
def calculate_mean_cuda(data):
    
    # MEMORY TRANSFER: Host (RAM) -> Device (VRAM)
    # This is the "implicit overhead" of GPU computing.
    d_data = cuda.to_device(data)

    # Allocate space on GPU for the result (Sum, Count)
    # We initialize it to 0.0
    d_result = cuda.to_device(np.zeros(2, dtype=np.float64))
    
    # CONFIGURE THE GRID
    # We choose a standard block size (threads per block)
    threads_per_block = (32, 32) 
    
    # Calculate enough blocks to cover the array (standard formula)
    blocks_x = (data.shape[0] + threads_per_block[0] - 1) // threads_per_block[0]
    blocks_y = (data.shape[1] + threads_per_block[1] - 1) // threads_per_block[1]
    blocks_per_grid = (blocks_x, blocks_y)
    
    # LAUNCH KERNEL
    mean_kernel_2d[blocks_per_grid, threads_per_block](d_data, d_result)
    
    # MEMORY TRANSFER: Device (VRAM) -> Host (RAM)
    result = d_result.copy_to_host()
    
    return result[0] / result[1]

# --- 3. SETUP DATA ---
niter = 10
np.random.seed(1)
data = np.random.randn(5000, 5000).astype(np.float64)

# --- 4. BENCHMARK ---
print("Running Numba CUDA Mean Calculation...")

# Warm-up (Compiles the kernel and initializes CUDA context)
# Note: First run always takes longer due to compilation overhead
# Suppress the warning specifically for the warm-up
with warnings.catch_warnings():
    warnings.simplefilter('ignore', category=NumbaPerformanceWarning)
    calculate_mean_cuda(np.zeros((16, 16)))

start_p = time.time()
for i in range(niter):
    res_p = calculate_mean_cuda(data)
    
# Wait for GPU to finish everything before stopping the timer
cuda.synchronize() 
time_p = (time.time() - start_p) / niter

print(f"Result:    {res_p}")
print(f"Time:      {time_p:.4f}s")
