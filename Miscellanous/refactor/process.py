import xarray as xr

# 1. Load the dataset
ds = xr.open_dataset('era_interim_monthly_197901_201512_upscaled_annual.nc')

# 2. Select the variables you want to KEEP
# (This creates a new dataset with only those variables)
subset = ds[['t2m', 'wspd10']]

# 3. Save to a new file
subset.to_netcdf('era_interim_annual_197901_201512_upscaled_subset.nc')
