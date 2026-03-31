# xarray_mpi.py
from dask_mpi import initialize
from dask.distributed import Client
import dask.array as da
import xarray as xr
import numpy as np
import sys
import logging

# Suppress the noisy teardown logs for a clean output
logging.getLogger("distributed.batched").setLevel(logging.ERROR)
logging.getLogger("distributed.worker").setLevel(logging.ERROR)
logging.getLogger("distributed.scheduler").setLevel(logging.ERROR)
logging.getLogger("distributed.core").setLevel(logging.ERROR)

# 1. Boot up the MPI network (Blocks Ranks 0 and 1)
initialize()

if __name__ == "__main__":
    try:
        # 2. Connect the Client (Only Rank 2+ runs this)
        with Client() as client:
            print(f"Dashboard available at: {client.scheduler.address.replace('tcp', 'http').split(':')[0]}:8787/status")
            
            # 3. Create the chunked Dask data
            print("\nGenerating distributed data...")
            raw_dask_array = da.random.random((1000, 180, 360), chunks=(100, 45, 90))
            
            # 4. Wrap it in Xarray
            climate_data = xr.DataArray(
                raw_dask_array,
                dims=['time', 'lat', 'lon'],
                coords={
                    'time': np.arange(1000),
                    'lat': np.linspace(-90, 90, 180),
                    'lon': np.linspace(-180, 180, 360)
                },
                name='surface_temperature'
            )
            
            # 5. The Science Logic
            # We want the global average over time
            print("Building the task graph for global time-series...")
            time_series = climate_data.mean(dim=['lat', 'lon'])
            
            # 6. Execution across the MPI Workers
            print("Executing across MPI cluster...")
            final_result = time_series.compute()
            
            print("\n--- First 5 days of Global Mean Temp ---")
            print(final_result[:5].values)
            
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
