from math import floor, ceil
from PIL import Image
import os
from django.conf import settings

def compress(image_name):

    image = Image.open(image_name)
    rgb_image = image.convert('RGB')
    size = ceil(os.path.getsize(image_name)/1024)
    
    if size > 200:
        percent_from_image = floor(40500/size) #gets what percent of image size is 200 kb
        print(image_name)
        if percent_from_image == 0:
            percent_from_image = 1
            
    rgb_image.save(image_name, format='jpg',optimized=True, quality=percent_from_image)
