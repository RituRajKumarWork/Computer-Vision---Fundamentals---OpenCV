#Adaptive Threshold
import cv2
# Load image
img = cv2.imread('../download (1).jpg')

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

# Apply simple thresholding
_, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Adaptive Threshold', adaptive_thresh)
cv2.imshow('Simple Threshold', simple_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
