#-*- coding:utf8 -*-
import PIL
from PIL import Image
from PIL import ImageDraw

# get the image
file = "head.jpg"
img = Image.open(file)
width, height = img.size[0], img.size[1]
print width, height
# Draw the image
draw = ImageDraw.Draw(img)
draw.text((width - 20, height - 20), "4", (255, 0, 0))
del draw

# save the image 
img.save("target.jpg")