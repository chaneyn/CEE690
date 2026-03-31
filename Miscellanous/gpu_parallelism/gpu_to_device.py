import numpy as np
from numba import cuda

# Create a standard NumPy array (on the Host)
h_data = np.linspace(0, 100, 1000)

# Move it to the GPU
d_data = cuda.to_device(h_data)

# Don't waste time copying zeros from CPU to GPU
d_result = cuda.device_array((1,), dtype=np.float64)

print(type(h_data)) # <class 'numpy.ndarray'>
print(type(d_data)) # <class 'numba.cuda.cudadrv.devicearray.DeviceNDArray'>
print(type(d_result)) # <class 'numba.cuda.cudadrv.devicearray.DeviceNDArray'>

