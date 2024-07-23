from math import floor, ceil
from PIL import Image
import os

image_name = 'l.jpg'

image = Image.open(image_name)
rgb_image = image.convert('RGB')
size = ceil(os.path.getsize(image_name)/1024)

if size > 200:
    percent_from_image = floor(40500/size) #gets what percent of image size is 200 kb

    if percent_from_image == 0:
        percent_from_image = 1
        
    print(percent_from_image)


    rgb_image.save('ii.jpg', optimized=True, quality=percent_from_image)

else:
    print('Too small size to compress')