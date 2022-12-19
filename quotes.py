import requests
import random
import PIL
from PIL import ImageFilter
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# Download a random quote
response = requests.get("https://api.quotable.io/random")
quote = response.json()['content']

# Download a random image
response = requests.get("https://picsum.photos/300/300/?random")
image = Image.open(BytesIO(response.content))

# Blur the image
image = image.filter(ImageFilter.BLUR)

# Define the font for the quote
font = ImageFont.truetype("arial.ttf", 36)

# Create a new image and draw the quote on it with the blurred image as the background
new_image = Image.new("RGB", (500, 500), (255, 255, 255))
new_image.paste(image, (0, 0))
draw = ImageDraw.Draw(new_image)
draw.text((50, 50), quote, (0, 0, 0), font=font)

# Save the image to a file
new_image.save("quote.jpg")
