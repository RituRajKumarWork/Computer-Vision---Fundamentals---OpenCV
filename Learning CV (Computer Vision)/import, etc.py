"""import os
import cv2

# Correct usage with os.path.join
image_path = os.path.join('.', 'data', 'download (1).jpg')

# Load the image using OpenCV
image = cv2.imread(image_path)

if image is not None:
    print("Image loaded successfully")
else:
    print("Failed to load image")"""


import os

image_path = os.path.join('.', 'data', './/download (1).jpg')
print(image_path)

if not os.path.exists(image_path):
    print("File does not exist")
else:
    print("File exists")
