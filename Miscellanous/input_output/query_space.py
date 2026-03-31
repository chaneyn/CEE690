import netCDF4 as nc
import time
file = 'era_space_chunks.nc'
fp = nc.Dataset(file)

#Query time dimension
tic = time.time()
data = fp['t2m'][:,0,0]
print('Time dimension',time.time() - tic)

#Query space dimensions
tic = time.time()
data = fp['t2m'][0,:,:]
print('Space dimensions',time.time() - tic)
