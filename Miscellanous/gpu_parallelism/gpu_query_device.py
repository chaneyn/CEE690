from numba import cuda

device = cuda.get_current_device()

# Use the .attributes dictionary for hardware-specific constants
# These keys are specifically defined in Numba's CUDA driver
num_sms = device.MULTIPROCESSOR_COUNT
max_threads_per_sm = device.MAX_THREADS_PER_MULTI_PROCESSOR
max_threads_per_block = device.MAX_THREADS_PER_BLOCK

print(f"Device Name: {device.name.decode('utf-8')}")
print(f"Number of SMs (Multiprocessors): {num_sms}")
print(f"Max Threads per SM:             {max_threads_per_sm}")
print(f"Max Threads per Block:          {max_threads_per_block}")



