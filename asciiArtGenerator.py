from PIL import Image
import numpy as np
import os
import pathlib

#config
imageName= "rei.jpg"
outputFile= "ascii_art.txt"
width= 100

#ordered dark to light
chars= ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']

def loadImage(path):
    return Image.open(path)

def resizeImage(img, newWidth):
    originalWidth, originalHeight= img.size
    aspectRatio= originalHeight / originalWidth
    #0.55 compensates for characters being more taller than wide
    newHeight= int(newWidth * aspectRatio * 0.55)
    return img.resize((newWidth, newHeight))

def mapPixelsToChars(pixelArray):
    numChars= len(chars)
    charArray= np.array(chars)
    indices= (pixelArray / 255 * (numChars-1)).astype(int)
    return "\n".join(["".join(charArray[row]) for row in indices])

def getDownloadsPath():
    return pathlib.Path.home() / "Downloads"

def saveToDownloads(asciiStr, filename):
    fullPath= getDownloadsPath() / filename
    with open(fullPath, "w") as f:
        f.write(asciiStr)
    return fullPath

def main():
    scriptDir= os.path.dirname(os.path.abspath(__file__))
    imagePath= os.path.join(scriptDir, imageName)
    if not os.path.exists(imagePath):
        print(f"Error: Could not find '{imageName}' in the same folder as this script.")
        return
    img= loadImage(imagePath)
    img= resizeImage(img, width)
    img= img.convert("L")
    asciiArt= mapPixelsToChars(np.array(img))
    savedPath= saveToDownloads(asciiArt, outputFile)
    print(f"Saved to: {savedPath}")

if __name__ == "__main__":
    main()