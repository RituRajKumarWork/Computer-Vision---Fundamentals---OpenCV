import cv2

# Read image
image_path = '../Image - Input Output/pic.png'
img = cv2.imread(image_path)


# Write image
output_path = './data/output_pic.png'
cv2.imwrite(output_path, img)

# Visualize image
cv2.imshow('window_image_name', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
