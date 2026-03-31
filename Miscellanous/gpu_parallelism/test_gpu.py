from numba import cuda

if cuda.is_available():
    print("CUDA GPU is available.")
else:
    print("No CUDA GPU found.")
