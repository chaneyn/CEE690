import glob
import os
import numpy as np
import rasterio
import time
from mpi4py import MPI

#Define globals
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
netid = 'nc153'

#Initialize variables
count_files = 0
sum_time = 0.0
npixels = 0
zsum = 0.0

#Read list of all files
files = glob.glob(f'/cwork/{netid}/0.333arcsec/USGS_NED_13/*IMG.img')
files = sorted([f for f in files if f.endswith('.img')])
for file in files[rank::size]:
    tic = time.time()
    #Extract cell geographic location
    geoloc = file.split("_")[5]
    #Read in the file
    data = rasterio.open(file).read(1)
    #Compute the mask
    mask = data > -9999.0
    npixels += np.sum(mask)
    zsum += np.sum(data[mask])
    #Print current cell location and time it took
    count_files += 1
    sum_time += time.time()-tic
    average_time = sum_time/count_files
    print(f'{rank},{geoloc},{average_time}',flush=True)

#Gather the data
zsum_final = comm.reduce(zsum, op=MPI.SUM, root=0)
npixels_final = comm.reduce(npixels, op=MPI.SUM, root=0)
if rank == 0:
    elevation = zsum_final/npixels_final
    print(f"Average elevation over CONUS is {elevation} meters")
