import os

import requests
import torch
from diffusers import Flux2KleinPipeline
from diffusers.utils import load_image
from dotenv import load_dotenv

load_dotenv()

# Fetch a Figma frame to use as reference
FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
FILE_KEY = "76SQoGqjxrmRLvtWT30ny3"
NODE_ID = "14324-170878"  # Group Builder

print("Fetching reference image from Figma...")
r = requests.get(
    f"https://api.figma.com/v1/images/{FILE_KEY}",
    headers={"X-Figma-Token": FIGMA_TOKEN},
    params={"ids": NODE_ID, "format": "png", "scale": 1},
)
url = r.json()["images"][NODE_ID.replace("-", ":")]
img_data = requests.get(url).content
with open("figma_experiment/flux_reference.png", "wb") as f:
    f.write(img_data)
print("Reference image saved to scripts/flux_reference.png")

# Load model
dtype = torch.bfloat16
print("Loading FLUX.2-Klein...")
pipe = Flux2KleinPipeline.from_pretrained(
    "black-forest-labs/FLUX.2-klein-4B",
    torch_dtype=dtype,
)
pipe.enable_model_cpu_offload()
print("Model loaded.")

# Run
reference_image = load_image("figma_experiment/flux_reference.png")
prompt = (
    "A math toy showing 3 bags each containing 5 oranges, flat illustration style, teal background"
)

image = pipe(
    image=reference_image,
    prompt=prompt,
    height=1024,
    width=1024,
    guidance_scale=4.0,
    num_inference_steps=4,
    generator=torch.Generator(device="cpu").manual_seed(0),
).images[0]

image.save("figma_experiment/flux_test_output.png")
print("Output saved to scripts/flux_test_output.png")
