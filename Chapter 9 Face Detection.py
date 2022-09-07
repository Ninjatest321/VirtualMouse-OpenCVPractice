import cv2
import numpy as np

# Open CV Cascades

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.imread("Face.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(gray, 1.1, 4) # Returns x,y,width,height
#
# for (x,y,width,height) in faces:
#     cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)
#
# print(faces)
#
# cv2.imshow("Image", img)
# cv2.waitKey()


# Track Face Code

video = cv2.VideoCapture(0)
video.set(3, 640)  # ID number 3 stands for width
video.set(4, 480)  # ID number 4 stands for height
video.set(10, 100) # Id number 10 changes brightness

while True:
    success, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4) # Returns x,y,width,height
    for (x,y,width,height) in faces:
        cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break