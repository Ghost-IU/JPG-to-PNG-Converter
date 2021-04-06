import os
import sys
from PIL import Image

input_folder = sys.argv[1]                           #Grab the first argument
output_folder = sys.argv[2]                          #Grab the second argument

if not os.path.exists(output_folder):                #Check if the output folder exists 
  os.makedirs(output_folder)

count = 0
for image in os.listdir(input_folder):                #Loop through the input folder
  img = Image.open(f'{input_folder}{image}')
  new_name = os.path.splitext(image)[0]
  img.save(f'{output_folder}{new_name}.png' , 'png')  #Convert them to PNG and save it to new folder
  count = count + 1
  print(f'Converting image {count} .....')            
  
print('Task Complete')
