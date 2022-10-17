import time
import pyautogui
from PIL import Image

st = time.time()
#############################################

path = "image.jpeg"
outputPath = "output path"
img = Image.open(path)

width, height = img.size

print(width,height)

reduce = float(input("Enter percentage you want to reduce: "))

per = 100/reduce

width = int(width/per)

height = int(height/per)

newsize = (width, height)
img1 = img.resize(newsize)

img1 = img1.save(outputPath, quality=90, dpi=(300,300))


#############################################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')




