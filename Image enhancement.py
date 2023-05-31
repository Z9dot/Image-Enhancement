import cv2
import numpy as np

#define the image path
path='image1.jpg'

#Load as grayscale
image=cv2.imread(path,0)

# inverted_thresh=cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,17,2)
thresh = cv2.bitwise_not(cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,17,4))

#performing morphological operations
kernel = np.ones((3,3), np.uint8)

#Performing dilation operation on threshold image
dilated=cv2.dilate(thresh, kernel, iterations=1)

#Performing erosion operation on dilated image
eroded=cv2.erode(dilated, kernel, iterations=1)

#displaying the image
cv2.imshow('Enhanced Numbers', eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()