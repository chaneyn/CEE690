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

#Initialize a file to write the localized computed means to
wdir = f'/cwork/{netid}/workspace'
os.system(f'mkdir -p {wdir}')
file = f'{wdir}/rank_{rank}'
fp = open(file,'w')

#Initialize time variables
count_files = 0
sum_time = 0.0

#Read list of all files
files = sorted(glob.glob('/cwork/nc153/0.333arcsec/USGS_NED_13/*.img'))
for file in files[rank::size]:
    tic = time.time()
    #Extract cell geographic location
    geoloc = file.split("_")[5]
    #Read in the file
    data = rasterio.open(file).read(1)
    #Compute the mask
    mask = data > -9999.0
    npixels = np.sum(mask)
    zsum = np.sum(data[mask])
    #Write the mean to a file
    fp.write(f'{geoloc},{npixels},{zsum}\n')
    #Print current cell location and time it took
    count_files += 1
    sum_time += time.time()-tic
    average_time = sum_time/count_files
    print(f'{rank},{geoloc},{average_time}',flush=True)
    
#Close the output file
fp.close()
