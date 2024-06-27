import cv2
import numpy as np
imgo = cv2.imread("../Image.png")
img = cv2.imread("../Image.png",cv2.IMREAD_GRAYSCALE)    #storing image in valiable


# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(img, (3, 3), 1.4)

# Apply Canny edge detector
edges = cv2.Canny(blurred_image, 100, 200)
image_del = cv2.dilate(edges,np.ones((3, 3), dtype=np.int8)) #Dilate
img_edge_e = cv2.erode(image_del, np.ones((3, 3), dtype=np.int8))

cv2.imshow("blurred_image",blurred_image)
cv2.imshow("edges",edges)
cv2.imshow("image_dilate",image_del)
cv2.imshow("image_Ori_coloured",imgo)
cv2.imshow("erode",img_edge_e)
cv2.imshow("org img",img)     #displaying that variable
cv2.waitKey(0)      #wait untill exit key pressed