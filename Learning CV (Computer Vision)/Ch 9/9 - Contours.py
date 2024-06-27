import cv2

# Read the image
img = cv2.imread('../birds.jpg')
original_img1 = cv2.imread('../birds.jpg')

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to the grayscale image
_, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles around contours with an area greater than 200
for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the original image with rectangles and the thresholded image
cv2.imshow('Image', img)
cv2.imshow('original_img1', original_img1)
cv2.imshow('Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
