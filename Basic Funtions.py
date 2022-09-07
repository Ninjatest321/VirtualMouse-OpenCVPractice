# Chapter 2
import cv2
import numpy as np

img = cv2.imread("RandomImage1.jpeg")
kernel = np.ones((5, 5), np.uint8)  # creates a matrix (5 by 5) filled with ones to start of unsigned integers that use 8 bits (0 to 255)

# GrayScale
imgGrayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
imgBlur = cv2.GaussianBlur(img, (99, 99), 0)

# Edge Detector
#imgCanny = cv2.Canny(img, 100, 100)  # Black screen, white outlines on edge, second input is minValue (all lower are rejected) and third input is Max (all above are edge)

# Image Dilation — make it thicker
#imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)  # Seond value is kernel, need numpy, iterations = 1 is kinda like thickness

# Image Erosion — make it thinner
imgEroded = cv2.erode(img, kernel, iterations=10 )

cv2.imshow("Gray Image", imgEroded)  # First space is title
cv2.waitKey()
