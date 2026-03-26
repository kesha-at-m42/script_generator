import base64
import io
import os

import anthropic
import requests
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

if not FIGMA_TOKEN:
    raise EnvironmentError("FIGMA_TOKEN environment variable is not set.")

FILE_KEY = "76SQoGqjxrmRLvtWT30ny3"
NODE_ID = "11246-36751"

# Step 1: Get image URL from Figma
figma_response = requests.get(
    f"https://api.figma.com/v1/images/{FILE_KEY}",
    headers={"X-Figma-Token": FIGMA_TOKEN},
    params={"ids": NODE_ID, "format": "png", "scale": 1},
)
image_url = figma_response.json()["images"]["11246:36751"]

# Step 2: Download, compress, and encode image
img = Image.open(io.BytesIO(requests.get(image_url).content))
img = img.resize((img.width // 2, img.height // 2))
buffer = io.BytesIO()
img.save(buffer, format="PNG", optimize=True)
image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

# Step 3: Pass to Claude
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe this toy's visual state. What mode is it in, what data is visible, and what interactions are available to the student?",
                },
            ],
        }
    ],
)

print(response.content[0].text)
