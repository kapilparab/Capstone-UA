import torch
import argparse
import numpy as np
from PIL import Image
from transformers import Sam3Processor, Sam3Model
from huggingface_hub import login
import os

def run_inference(image_path, text_prompt, output_path, hf_token):
    # 1. Authentication
    if hf_token:
        login(token=hf_token)
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    # 2. Load Model and Processor
    # SAM 3 is roughly 848M parameters; ensure your GPU has ~8GB+ VRAM
    processor = Sam3Processor.from_pretrained("facebook/sam3")
    model = Sam3Model.from_pretrained("facebook/sam3", torch_dtype=torch.float16).to(device)

    # 3. Prepare Image and Prompt
    raw_image = Image.open(image_path).convert("RGB")
    
    # SAM 3 handles the 224x224 input well by internal upsampling 
    # to its native 1008x1008 resolution.
    inputs = processor(images=raw_image, text=text_prompt, return_tensors="pt").to(device)

    # 4. Inference
    with torch.no_grad():
        outputs = model(**inputs)

    # 5. Post-Processing
    # SAM 3 returns masks, boxes, and confidence scores for every instance found
    results = processor.post_process_instance_segmentation(
        outputs, 
        threshold=0.3, # Confidence to consider it a 'match'
        mask_threshold=0.5, # Threshold for binarizing pixels
        target_sizes=[raw_image.size[::-1]]
    )[0]

    # 6. Save/Visualize Results
    if len(results["masks"]) > 0:
        print(f"Found {len(results['masks'])} target instances.")
        
        # Combine all masks into one visualization or save them individually
        # Here we create a combined binary mask for the 'TARGET'
        final_mask = torch.sum(results["masks"], dim=0).clamp(0, 1).cpu().numpy().astype(np.uint8) * 255
        Image.fromarray(final_mask).save(output_path)
        print(f"Mask saved to {output_path}")
    else:
        print("No target found for the given prompt.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SAM 3 Concept Segmentation")
    parser.add_argument("--image", type=str, required=True, help="Path to map image")
    parser.add_argument("--prompt", type=str, required=True, help="Text description of the target")
    parser.add_argument("--output", type=str, default="output_mask.png", help="Path to save mask")
    parser.add_argument("--token", type=str, help="Hugging Face Token (if not logged in via CLI)")
    
    args = parser.parse_args()
    run_inference(args.image, args.prompt, args.output, args.token)