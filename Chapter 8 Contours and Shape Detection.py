import cv2
import numpy as np


def getCountours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)  # image, retrievalmethod External receives outer corners,generally make approximation none
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(str(area))
        if area > 300:  # make sure there is a minimum area so it avoids noise
            cv2.drawContours(imgContour, cnt, -1, (255, 255, 255), 3)  # img you want to show contours on, contour you want to show, -1 stands for all of them, BGR, thikness)
            perimeter = cv2.arcLength(cnt, True)
            print("Perimeter: " + str(perimeter))

            #Estimating corner points

            approximatePoints = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
            print(len(approximatePoints))
            objectCorners = len(approximatePoints)
            x,y,width,height = cv2.boundingRect(approximatePoints) # Makes a rectangle outside from the points, and gives x,y,width,height

            objectType = "Circle"
            if objectCorners == 3:
                objectType = "Triangle"
            elif objectCorners == 4:
                if 0.95 < width/float(height) < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objectCorners == 5:
                objectType = "Pentagon"
            elif objectCorners == 6:
                objectType = "Hexagon"
            else:
                objectType = "Circle"
            cv2.putText(imgContour, objectType, (x+(width//2), y+(height//2)), cv2.FONT_HERSHEY_PLAIN, 0.6, (255,255,255), 1)
            cv2.rectangle(imgContour, (x,y), (x+width, y+height), (0,0,255), 2)


img = cv2.imread("ShapePractice2.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgContour = img.copy()
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getCountours(imgCanny)

imgStack = cv2.hconcat([imgGray, imgBlur, imgCanny])
# cv2.imshow("Blurred", imgBlur)
cv2.imshow("Canny", imgContour)
cv2.imshow("Stack", imgStack)
cv2.waitKey(0)
