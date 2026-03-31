import numpy as np
from numba import cuda

# Create a standard NumPy array (on the Host)
h_data = np.linspace(0, 100, 1000)

# Move it to the GPU
d_data = cuda.to_device(h_data)

print(type(h_data)) # <class 'numpy.ndarray'>
print(type(d_data)) # <class 'numba.cuda.cudadrv.devicearray.DeviceNDArray'>



