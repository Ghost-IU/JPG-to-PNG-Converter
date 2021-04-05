import os
import sys
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

count = 0
for image in os.listdir(input_folder):
  img = Image.open(f'{input_folder}{image}')
  new_name = os.path.splitext(image)[0]
  img.save(f'{output_folder}{new_name}.png' , 'png')
  count = count + 1
  print(f'Converting image {count} .....')
  
print('Task Compplete')
