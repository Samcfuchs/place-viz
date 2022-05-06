from sklearn.datasets import load_sample_image
import numpy as np
from PIL import Image

t = 2 # Type
c = 0 # Quadrant

png_name = "0-1649111825.png" # Pick a png

# x1 and y1 are top left corner, x2 and y2 are bottom right corner
x1 = 175
y1 = 497
x2 = 244
y2 = 528

output_name = "Canada-100" # Final name

if t==0:
    name1 = "data/img_2022/images_single/"
elif t==1:
    name1 = f"data/img_2022/images_double/{c}/"
elif t==2:
    name1 = f"data/img_2022/images_quadro/{c}/"

name = name1 + png_name

image = Image.open(name)

portion = image.crop((x1, y1, x2, y2))

# use in different section

portion.save('data/sliced/' + output_name + '.png')