from diffusers import QwenImageLayeredPipeline
import torch
from PIL import Image
import argparse

# Arguments
parser = argparse.ArgumentParser(description="QWEN Segmentation")
parser.add_argument("--image", type=str, required=True, help="Path to map image")
parser.add_argument("--output_dir", type=str, default="output_mask.png", help="Path to save mask")
args = parser.parse_args()

# Pipeline
pipeline = QwenImageLayeredPipeline.from_pretrained("Qwen/Qwen-Image-Layered", torch_dtype=torch.bfloat16)
pipeline = pipeline.to("cuda")
pipeline.set_progress_bar_config(disable=None)

# Load image
image = Image.open(args.image).convert("RGBA")

# Inputs
inputs = {
    "image": image,
    "generator": torch.Generator(device='cuda').manual_seed(777),
    "true_cfg_scale": 4.0,
    "negative_prompt": " ",
    "num_inference_steps": 30,
    "num_images_per_prompt": 1,
    "layers": 2,
    "resolution": 224,      # Using different bucket (640, 1024) to determine the resolution. For this version, 640 is recommended
    "cfg_normalize": True,  # Whether enable cfg normalization.
    "use_en_prompt": True,  # Automatic caption language if user does not provide caption
}

# Run model
with torch.inference_mode():
    output = pipeline(**inputs)
    output_image = output.images

# Save outputs
import os
os.makedirs(args.output_dir, exist_ok=True)

for i, img in enumerate(output_image):
    img.save(f"{args.output_dir}/{i}.png")
