import sys
import os
from PIL import Image

jpg = sys.argv[1]
png = sys.argv[2]

if not os.path.exists(png):
    os.makedirs(png)
    

for filename in os.listdir(jpg):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{jpg}/{filename}')
  img.save(f'{png}/{clean_name}.png')
  print('all done!')


