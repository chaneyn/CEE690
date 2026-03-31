#!/bin/bash

# 1. Identity
#SBATCH --job-name=spatialstats_test     # The name that appears in 'squeue'
#SBATCH --output=/hpc/home/nc153/CEE690/Miscellanous/slurm/%x_%j.out     # Save normal output
#SBATCH --error=/hpc/home/nc153/CEE690/Miscellanous/slurm/%x_%j.err      # Save error messages

# 2. Partition (The Queue)
#SBATCH --partition=common         # Which line to stand in (ask your admin for names)

# 3. Resources (The Hardware)
#SBATCH --nodes=1                   # Request 1 physical compute node
#SBATCH --ntasks-per-node=4         # Request 4 CPU cores on that node
#SBATCH --mem=16G                   # Request 16GB of RAM total
#SBATCH --time=01:00:00             # Hard time limit: 1 Hour (HH:MM:SS)

# 4. Notifications (Optional but recommended)
#SBATCH --mail-type=END,FAIL        # Email me when it finishes or crashes
#SBATCH --mail-user=nc153@duke.edu # Where to send the email

# --- PART 2: THE EXECUTION (The Body) ---
# This part runs exactly like a normal shell script, but it runs ON the compute node.

echo "Job started on $(hostname) at $(date)"
# 1. Change directory
cd /hpc/home/nc153/CEE690/Miscellanous/slurm

# 2. Activate Virtual Environment (if using one)
source $HOME/.bashrc
conda activate cee690

# 3. Run the Python Code
echo "Starting program..."
spatialstats --JSON_FILE example.json

echo "Job finished at $(date)"






