### Scripts for testing GLaMM inference can be found in [forked repository](https://github.com/VeraJSolo/groundingLMM-UA), under "capstone_testing" folder

#### 🔮 To test inference, use script [run_inference.slurm](https://github.com/VeraJSolo/groundingLMM-UA/blob/main/capstone_testing/slurm/run_inference.slurm) 
Inference will produce a .json output.
#### To visualize the inference mask, use script [run_masker.slurm](https://github.com/VeraJSolo/groundingLMM-UA/blob/main/capstone_testing/slurm/run_masker.slurm) on the .json output.
#### To evaluate performance of inference, use script [run_performance.slurm](https://github.com/VeraJSolo/groundingLMM-UA/blob/main/capstone_testing/slurm/run_performance.slurm)
Evaluation relies on the .json output and .png ground truth.
