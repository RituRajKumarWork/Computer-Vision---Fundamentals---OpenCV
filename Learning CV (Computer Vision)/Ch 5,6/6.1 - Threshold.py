#Global Threshold
import cv2
# Load image
img = cv2.imread('../download (1).jpg')

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# Apply blurring
thresh = cv2.blur(thresh, (10, 10))

# Apply thresholding again
_, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
