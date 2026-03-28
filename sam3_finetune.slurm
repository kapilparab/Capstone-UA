#!/bin/bash
#SBATCH --job-name=sam3_finetune
#SBATCH --account=nlp
#SBATCH --partition=gpu_standard
#SBATCH --nodes=1
#SBATCH --gres=gpu:nvidia_a100_80gb_pcie_3g.40gb
#SBATCH --cpus-per-task=8
#SBATCH --time=01:00:00

module load python/3.11

source sam3_venv/bin/activate

export HF_TOKEN="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"
export CUDA_VISIBLE_DEVICES=0
export HYDRA_FULL_ERROR=0

cd ../sam3-UA/

python sam3/train/train.py -c configs/ua_geo/ua_geo_train.yaml

