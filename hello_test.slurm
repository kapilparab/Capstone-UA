#!/bin/bash
#SBATCH --job-name=virtual_env_test
#SBATCH --account=nlp
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:01:00

module load python/3.11

source test_env/bin/activate

python3 print_hello.py
