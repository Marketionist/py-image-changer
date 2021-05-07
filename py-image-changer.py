#!/usr/bin/python

# python py-image-changer.py

# python -m venv py-image-changer
# source py-image-changer/bin/activate

# pip install -r requirements.txt
# OR
# pip install Pillow && pip freeze > requirements.txt

import os
from PIL import Image, ImageFilter

img = Image.open(os.path.join(
    'media', 'images', 'a-test-img.png'
))

print(img.format)
print(img.size)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('smooth.png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('sharpen.png')

filtered_img = img.convert('L')
filtered_img.save('grey.png')

rotated_img = img.rotate(30)
rotated_img.save('rotated-30.png')

cropped_img = img.crop((100, 100, 400, 400))
cropped_img.save('cropped.png')

resized_img = img.resize((300, 300))
resized_img.save('resized-300.png')

img.thumbnail((300, 300))
img.save('resized-with-keeping-aspect-ratio.png')

print(f'New properly resized image size: {img.size}')
resized_img.show()
