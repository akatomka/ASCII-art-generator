from PIL import Image, ImageDraw, ImageFont
import numpy as np

# ASCII symbols
density = " .:-=+*#%@"
# Comment next line if you want inverted
density = density[::-1]

# Load image
img = Image.open(r"C:\Users\tomas\Desktop\projects\asciiart\mountains.jpg")

# Downscale by 8
factor = 8
new_size = (img.width // factor, img.height // factor)
img_resized = img.resize(new_size, Image.BOX)

# Grayscale
img_gray = img_resized.convert("L")

# Quantize into 10 intervals
arr = np.array(img_gray)
intervals = 10
arr_quantized = np.round(arr / 255 * (intervals - 1))
arr_quantized = (arr_quantized / (intervals - 1) * 255).astype(np.uint8) 
img_quantized = Image.fromarray(arr_quantized)

# Map pixels to ASCII characters
ascii_art = []
for row in arr_quantized:
    line = "".join(density[int(np.round(pixel / 255 * (len(density) - 1)))] for pixel in row)
    ascii_art.append(line)

# Choose font
font = ImageFont.truetype("cour.ttf")

# Get character size
bbox = font.getbbox("A")
char_width = bbox[2] - bbox[0]
char_height = bbox[3] - bbox[1]

# Calculate image size
img_width = char_width * arr_quantized.shape[1]
img_height = char_height * arr_quantized.shape[0]

# Create new image with background color
bg_color = (160, 215, 235)  # background color
fg_color = (10, 48, 61)  # ASCII color
ascii_img = Image.new("RGB", (img_width, img_height), color=bg_color)
draw = ImageDraw.Draw(ascii_img)

# Draw ASCII characters onto the image
for y, line in enumerate(ascii_art):
    draw.text((0, y * char_height), line, fill=fg_color, font=font)

# Save the ASCII image
ascii_img.save(r"C:\Users\tomas\Desktop\projects\asciiart\ascii_image2.png")
ascii_img.show()