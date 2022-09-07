import  cv2
import numpy as np

#War Perspective — ngl kinda confusing
img = cv2.imread("RandomImage1.jpeg")
print(img.shape)
width, height = 300, 600
points1 = np.float32(([121,121], [700,100], [128, 499], [701, 512]))
points2 = np.float32(([0,0], [width, 0], [0, height], [width,height]))
matrix = cv2.getPerspectiveTransform(points1, points2)
imgFinal = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("image", img)
cv2.imshow("image2", imgFinal)


cv2.waitKey()