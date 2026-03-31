import numpy as np
import netCDF4 as nc
import fast_nc
import time

def create_dummy_data(filename):
    print(f"Creating dummy NetCDF file: {filename}...")
    # Create a 5,000 x 5,000 grid (25 million points)
    shape = (5000, 5000)
    
    with nc.Dataset(filename, 'w', format='NETCDF4') as ds:
        ds.createDimension('x', shape[0])
        ds.createDimension('y', shape[1])
        
        # Create a double-precision (f8) variable
        temp_var = ds.createVariable('temperature', 'f8', ('x', 'y'))
        
        # Fill it with random data
        temp_var[:] = np.random.rand(*shape)
    print("File created successfully.\n")

def test_custom_reader(filename):
    print("Reading data using custom C++ engine...")
    
    start = time.time()
    # Call our pybind11 wrapper!
    data = fast_nc.read_2d(filename, "temperature")
    end = time.time()
    
    print("-" * 35)
    print(f"Array Shape: {data.shape}")
    print(f"Data Type:   {data.dtype}")
    print(f"Mean Value:  {np.mean(data):.6f}")
    print(f"Read Time:   {end - start:.4f} seconds")
    print("-" * 35)

if __name__ == "__main__":
    test_file = "test_climate_data.nc"
    create_dummy_data(test_file)
    test_custom_reader(test_file)
