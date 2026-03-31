from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# This example requires exactly 2 processes to demonstrate clearly
if size < 2:
    if rank == 0:
        print("Please run with at least 2 processes (mpirun -n 2 ...)")
    exit()

def demonstrate_deadlock():
    data_to_send = np.array([rank], dtype=float)
    data_to_receive = np.empty(1, dtype=float)

    if rank == 0:
        print("Rank 0: Attempting to receive from Rank 1...")
        # DEADLOCK TRIGGER: Rank 0 waits here for Rank 1
        comm.Recv(data_to_receive, source=1, tag=100)
        
        print("Rank 0: Received data! Now sending to Rank 1...")
        comm.Send(data_to_send, dest=1, tag=101)

    elif rank == 1:
        print("Rank 1: Attempting to receive from Rank 0...")
        # DEADLOCK TRIGGER: Rank 1 waits here for Rank 0
        comm.Recv(data_to_receive, source=0, tag=101)
        
        print("Rank 1: Received data! Now sending to Rank 0...")
        comm.Send(data_to_send, dest=0, tag=100)

if __name__ == "__main__":
    demonstrate_deadlock()
    # You will never see this print statement if it deadlocks
    print(f"Rank {rank} finished successfully.")



