### Slurm files for testing GLaMM inference can be found in the [forked repository](https://github.com/VeraJSolo/groundingLMM-UA), under "capstone_testing" folder

#### 🔮 To test inference, use stlurm [run_inference.slurm](https://github.com/VeraJSolo/groundingLMM-UA/blob/main/capstone_testing/slurm/run_inference.slurm) 
Inference will produce a .json output.
#### 🎨 To visualize the inference mask, use slurm [run_masker.slurm](https://github.com/VeraJSolo/groundingLMM-UA/blob/main/capstone_testing/slurm/run_masker.slurm) on the .json output.
#### 📈 To evaluate performance of inference, use slurm [run_performance.slurm](https://github.com/VeraJSolo/groundingLMM-UA/blob/main/capstone_testing/slurm/run_performance.slurm)
Evaluation relies on the .json output and .png ground truth. This script runs evaluation.py, which exists in the forked repository and in this repository, in folder [python_scripts](https://github.com/kapilparab/Capstone-UA/edit/main/python_scripts).
