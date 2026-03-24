#!/bin/bash
#SBATCH --job-name=qwen_test
#SBATCH --account=nlp
#SBATCH --partition=gpu_standard
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --mem=50gb
#SBATCH --time=01:00:00

module load python/3.11

source test_env/bin/activate

python3 qwen_test.py \
  --image images/input.png \
  --output_dir outputs
