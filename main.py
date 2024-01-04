import os
from PIL import Image

inputPath = "photos/"
outputPath = "products/"

resolution = (1170, 1845)

def loadImages(inputPath):
    images = []
    for imgPath in sorted(os.listdir(inputPath)):
        images.append(Image.open(inputPath + imgPath))
        
    return images
        
def cropImages(inputPath, outputPath, width, height):
    imgs = []
    imgs = loadImages(inputPath)
    
    outputs = []
    
    for img in imgs:
        outputs.append(img.crop((0, 681, width, height)))
        
    i = 0 
    for cropped in outputs:
        cropped.save(outputPath + str(i) + ".png")
        i += 1
        
cropImages(inputPath, outputPath, *resolution)
