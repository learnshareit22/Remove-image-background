from PIL import Image
from rembg import remove

# Define paths to open and save the image
inputPath = "harris-hawk.jpg"
outputPath = "non-background-hawk.png"

# Read the image
readImage = Image.open(inputPath)

# Remove the background
outImage = remove(readImage)

# Save the image 
outImage.save(outputPath)

# Open the image
with Image.open("non-background-hawk.png") as im:
    im.show()