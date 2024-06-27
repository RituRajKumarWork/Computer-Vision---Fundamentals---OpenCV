import cv2

# Load the image
img = cv2.imread('../download (1).jpg')

# Print image dimensions
print(img.shape)

# Draw a green line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

# Draw a filled red rectangle
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1)

# Draw a blue circle with a thick border
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)

# Add yellow text
cv2.putText(img, 'Hey you!', (60    , 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)

# Display the image
cv2.imshow('img', img)
cv2.waitKey(0)
