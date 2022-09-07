# Chapter 4

import cv2
import numpy as np

img = np.zeros((512, 512, 3),
               np.uint8)  # creates a matrix filled with zeros, pass in a tuple, and has a 3 for rgb values for color
img[::] = 0, 0, 0  # In BGR, 3d array, the first rangeloops through all the length, second the width
print(img)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 5)  # (img, startCoordinate, endCoordinate (remember in shape array, it goes width,height, but in method it goes height width), BGR, thickness)
cv2.rectangle(img, (10,10), (200,300), (0,255,0), cv2.FILLED) # If you put a number in thickness, it'll be thikness. if you use cv2.FILLED, it will make a full rectangle
cv2.circle(img, (400,50), 20, (255,255,255), cv2.FILLED) # (img, centerCoordinates, radius, BGR, thickness
cv2.putText(img, "Hey", (200,400), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 3) # (img, text, topleftcornerCoordinates, Font, scale, BGR, thickness
cv2.imshow("Image", img)


cv2.waitKey()
