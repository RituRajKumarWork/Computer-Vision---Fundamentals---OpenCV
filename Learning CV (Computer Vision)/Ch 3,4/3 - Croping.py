import cv2
# Read the image
img = cv2.imread('../download (1).jpg')

# Print the original image shape
print("Original image shape:", img.shape)

# Crop the image
cropped_img = img[220:740, 320:940]
#Defining Size

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
