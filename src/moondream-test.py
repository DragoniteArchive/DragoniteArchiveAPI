import moondream as md
from PIL import Image

model = md.vl(model='./models/moondream-2b-int8.mf.gz')  # Initialize model
image = Image.open("./img/001.pdf.png")  # Load image
encoded_image = model.encode_image(image)  # Encode image (recommended for multiple operations)

# 1. Caption any image (length options: "short" or "normal" (default))
caption = model.caption(encoded_image)["caption"]
print("Caption:", caption)

print("Streaming caption:", end=" ", flush=True)
for chunk in model.caption(encoded_image, stream=True)["caption"]:
    print(chunk, end="", flush=True)