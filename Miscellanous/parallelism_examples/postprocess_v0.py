import numpy as np
import glob
netid = 'nc153'
wdir = f'/cwork/{netid}/workspace'
files = glob.glob(f'{wdir}/*')
zsum = 0.0
npixels = 0
for file in files:
    fp = open(file,'r')
    for line in fp:
        npixels += int(line[:-1].split(',')[1])
        zsum += float(line[:-1].split(',')[2])
elevation = zsum/npixels
#Compute elevation mean over Contiguous United States
print(f"Average elevation over CONUS is {elevation} meters")
