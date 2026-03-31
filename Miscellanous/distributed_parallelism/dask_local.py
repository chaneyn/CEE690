# local_dask.py
from dask.distributed import Client
import dask.array as da

if __name__ == "__main__":
    # 1. Start the Local Cluster
    # This automatically uses all available cores on this specific machine
    client = Client()
    print(f"Dashboard available at: {client.dashboard_link}")

    # 2. The Science Logic
    print("Building the task graph...")
    # Simulating a 120GB 3D grid, chunked into manageable blocks
    data = da.random.random((500, 2000, 2000), chunks=(100, 1000, 1000))
    
    # 3. Execution
    print("Computing the mean...")
    result = data.mean().compute()
    
    print(f"The mean is: {result}")
    
    # Clean up
    client.close()
