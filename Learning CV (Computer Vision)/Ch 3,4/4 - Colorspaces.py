import cv2

# Read the image
img = cv2.imread('../download (1).jpg')

# Convert the image to different color spaces
img_grey = cv2.cvtColor(img, cv2.COLOR_SBG)

# Display the original and HSV images
cv2.imshow('Original Image', img)
cv2.imshow('Grey Image', img_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""import cv2

# Read the image
img = cv2.imread('bird.jpg')

# Convert the image to different color spaces
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display the original and HSV images
cv2.imshow('Original Image', img)
cv2.imshow('HSV Image', img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

