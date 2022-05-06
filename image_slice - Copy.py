from sklearn.datasets import load_sample_image
import numpy as np
from PIL import Image

t = 2 # Type
c = 2 # Quadrant

png_name = "2-1649065581.png" # Pick a png

# x1 and y1 are top left corner, x2 and y2 are bottom right corner
x1 = 950
y1 = 300
x2 = 1000
y2 = 700

output_name = "Void-Test" # Final name

if t==0:
    name1 = "data/img_2022/images_single/"
elif t==1:
    name1 = f"data/img_2022/images_double/{c}/"
elif t==2:
    name1 = f"data/img_2022/images_quadro/{c}/"

name = name1 + png_name

image = Image.open(name)

portion1 = image.crop((x1, y1, x2, y2))

# ------------------------------------------------------------------ Image 2

t = 2 # Type
c = 3 # Quadrant

png_name = "3-1649065581.png" # Pick a png

# x1 and y1 are top left corner, x2 and y2 are bottom right corner
x1 = 0
x2 = 100

output_name = "Minecraft-66" # Final name

if t==0:
    name1 = "data/img_2022/images_single/"
elif t==1:
    name1 = f"data/img_2022/images_double/{c}/"
elif t==2:
    name1 = f"data/img_2022/images_quadro/{c}/"

name = name1 + png_name

image = Image.open(name)

portion2 = image.crop((x1, y1, x2, y2))

# use in different section

concated_image = Image.new('RGB', (portion1.width + portion2.width, portion1.height))
concated_image.paste(portion1, (0, 0))
concated_image.paste(portion2, (portion1.width, 0))

concated_image.save('data/sliced/' + output_name + '.png')