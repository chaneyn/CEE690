# distributed_dask.py
from dask_mpi import initialize
from dask.distributed import Client
import dask.array as da
import sys
import logging
logging.getLogger("distributed.batched").setLevel(logging.ERROR)
logging.getLogger("distributed.worker").setLevel(logging.ERROR)
logging.getLogger("distributed.scheduler").setLevel(logging.ERROR)
logging.getLogger("distributed.core").setLevel(logging.ERROR)

# 1. Initialize the MPI Network
# This acts as the "traffic cop". 
# Rank 0 becomes the Scheduler, Rank 1 becomes the Worker (or Dashboard).
# Only the "Client" rank continues past this line.
initialize()

if __name__ == "__main__":
    try:
        # Connect the Client rank to the Scheduler (Rank 0)
        with Client() as client:
            print(f"Dashboard available at: {client.dashboard_link}")
            
            # 2. The Science Logic (Exactly the same!)
            print("Building the task graph...")
            data = da.random.random((500, 2000, 2000), chunks=(100, 1000, 1000))
            
            # 3. Execution (Exactly the same!)
            # But now, this math is distributed across the entire MPI allocation
            print("Computing the mean...")
            result = data.mean().compute()
            
            print(f"The mean is: {result}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
