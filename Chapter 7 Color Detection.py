import cv2
import numpy as np

def empty(value):
    pass


# Trackbars
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179,empty)  # Hue goes from 0 to 179 on this, (Title, Window, min, max, function on Change)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)



while True:
    image = cv2.imread("RandomImage1.jpeg")
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars") # gets the value of a certain trackbar (Slider name, window name)
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars") # gets the value of a certain trackbar (Slider name, window name)
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars") # gets the value of a certain trackbar (Slider name, window name)
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars") # gets the value of a certain trackbar (Slider name, window name)
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars") # gets the value of a certain trackbar (Slider name, window name)
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars") # gets the value of a certain trackbar (Slider name, window name)

    lowerlim = np.array([h_min, s_min, v_min])
    upperlim = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lowerlim, upperlim)
    imgResult = cv2.bitwise_and(image, image, mask=mask) # shows where there are pixels on both the original and the masked

    #cv2.imshow("Image", image)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Masked", mask)
    cv2.imshow("CrossReference", imgResult)
    cv2.waitKey(1)
