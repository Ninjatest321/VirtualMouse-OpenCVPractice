# Chapter  3

import cv2
import numpy as np

img = cv2.imread("RandomImage1.jpeg")
print(img.shape)  # (height, width, bgr channel

# Resize
imgResize = cv2.resize(img, (500, 200)) # width, height

# Cropping
imgCropped = img[0:500, 200:500]

cv2.imshow("Image1", img)
cv2.imshow("Image", imgCropped)
cv2.waitKey(0)
