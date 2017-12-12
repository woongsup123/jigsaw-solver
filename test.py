import numpy as np
from PIL import Image

img = Image.open("pictures/10.jpg")

new_img = img.rotate(270, expand=True)
new_img.save("pictures/11.jpg")