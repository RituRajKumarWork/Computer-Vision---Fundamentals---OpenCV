import cv2
# Read the image
img = cv2.imread('../download (1).jpg')

# Resize the image to 640x640
resized_img = cv2.resize(img, (640, 640))
# Resize Keyword is main in this


# Print original and resized image shapes
print("Original image shape:", img.shape)
print("Resized image shape:", resized_img.shape)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()