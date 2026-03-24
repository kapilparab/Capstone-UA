#!/bin/bash
#SBATCH --job-name=qwen_test
#SBATCH --account=nlp
#SBATCH --partition=gpu_standard
#SBATCH --nodes=1
#SBATCH --gres=gpu:volta:2
#SBATCH --mem=80gb
#SBATCH --time=02:00:00

module load python/3.11
module load cuda

source test_env/bin/activate

python3 qwen_test.py \
  --image /groups/bethard/geoparsing/image_dataset/polygon_224/test/reference/GL001_242.png \
  --output_dir outputs
