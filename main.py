import time
from PIL import Image
import os

st = time.time()
#############################################

def main():
    
    path = input("Enter image folder path: ").strip()
    reduce = float(input("Enter percentage you want to reduce: "))
    
    imageURL = get_indi_file(path)
    for img in imageURL:
        convertImg(img, reduce)

def get_indi_file(path):
    allFiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            fullFileName = root+"\\"+file
            allFiles.append(fullFileName)
    return allFiles


def convertImg(imageURL, reduce):
    
    if imageURL.find(".jpeg") >= 0:
        outputPath = imageURL.replace(".jpeg","-converted.jpeg")
    elif imageURL.find(".jpg") >= 0:
        outputPath = imageURL.replace(".jpg","-converted.jpg")
    elif imageURL.find(".png") >= 0:
        outputPath = imageURL.replace(".png","-converted.png")
    else:
        return 0
        
    img = Image.open(imageURL)

    width, height = img.size

    print(width,height, end="----New Size: ")

    per = 100/reduce

    width = int(width/per)
    height = int(height/per)
    
    print(width,height)

    newsize = (width, height)
    img1 = img.resize(newsize)

    img1 = img1.save(outputPath, quality=90, dpi=(300,300))
    
main()


#############################################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')




