#!/bin/bash
#SBATCH --job-name=sam3_test
#SBATCH --account=nlp
#SBATCH --partition=gpu_standard
#SBATCH --nodes=1
#SBATCH --gres=gpu:volta:2
#SBATCH --mem=50gb
#SBATCH --time=01:00:00

module load python/3.11

source test_env/bin/activate

python3 sam3_test.py \
  --image "GL011_337.png" \
  --prompt "TARGET is a small stream near RED, GREEN. It has its source near BLUE amidst the forest and flows in northern direction to YELLOW. Above the castle were a swimming pool for the public which was formerly fed by the BLUEerbach. In the big garden of the Castle the brook supplies the MAGENTA with fresh water and then flows further through CYAN and the ORANGE to Ambras, where it merges with the PURPLE and then further into the PINK. The brook has a length of about 7 kilometres." \
  --output "result_mask.png" \
  --token "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"

