"""Quick test to verify Gemini image editing works."""

import io
import os

import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Download a test image (the group builder frame from manifest)
FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
FILE_KEY = "76SQoGqjxrmRLvtWT30ny3"
NODE_ID = "14324-170878"  # Group Builder

r = requests.get(
    f"https://api.figma.com/v1/images/{FILE_KEY}",
    headers={"X-Figma-Token": FIGMA_TOKEN},
    params={"ids": NODE_ID, "format": "png", "scale": 1},
)
url = r.json()["images"][NODE_ID.replace("-", ":")]
img_bytes = requests.get(url).content

# Compress
img = Image.open(io.BytesIO(img_bytes))
img = img.resize((img.width // 2, img.height // 2))
buf = io.BytesIO()
img.save(buf, format="PNG")
buf.seek(0)

print(f"Image size: {img.size}")

# Try Gemini image editing
response = client.models.generate_content(
    model="nano-banana-pro-preview",
    contents=[
        types.Part.from_bytes(data=buf.getvalue(), mime_type="image/png"),
        """This is a screenshot of an interactive Grade 3 math toy called the Group Builder.
It shows bags of oranges that students use to learn multiplication and equal groups.

Your task: edit this image so it shows exactly 3 bags, each containing 4 oranges.

Rules:
- Keep the exact same UI layout, background, guide character, buttons, and visual style
- Only change the number of bags and oranges shown in the interactive area
- The bags should look identical to the ones already in the image
- The oranges inside each bag should match the existing orange style
- Do not add any text, labels, or annotations
- The result should look like a natural screenshot of the same toy in a different state""",
    ],
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
    ),
)

for part in response.candidates[0].content.parts:
    if part.inline_data:
        out_path = "figma_experiment/gemini_test_output.png"
        with open(out_path, "wb") as f:
            f.write(part.inline_data.data)
        print(f"Image saved to {out_path}")
    elif part.text:
        print(f"Text: {part.text}")
