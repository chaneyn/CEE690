import xarray as xr 

# Open with the original chunks
ds = xr.open_dataset("era_unchunked.nc")

# Aim for that ~100MB per chunk sweet spot we discussed
new_chunks = {"time": 200, "lat": 200, "lon": 200}

# Write the new structure to Zarr
ds.to_zarr("era_interim.zarr", zarr_format=2, consolidated=False)
