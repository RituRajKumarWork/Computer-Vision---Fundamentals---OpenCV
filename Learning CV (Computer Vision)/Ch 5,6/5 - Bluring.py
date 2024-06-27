import cv2

# Read the image

img = cv2.imread('../download (1).jpg')

# Define the kernel size
k_size = 7

# Apply different blurring techniques
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_median_blur = cv2.medianBlur(img, k_size)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', img_blur)
cv2.imshow('Gaussian Blurred Image', img_gaussian_blur)
cv2.imshow('Median Blurred Image', img_median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
