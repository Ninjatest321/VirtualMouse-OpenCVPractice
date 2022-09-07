import cv2
import numpy as np

# Can only do straightforward method with images that are the same

# Straightforward Horizontal
img = cv2.imread("RandomImage1.jpeg")
img2 = cv2.imread("Image2.jpg")
img2 = cv2.resize(img2, [1100, 618])
print(img.shape)
hor = np.hstack([img, img])  # if you want to switch to vertical, change to vstack
# cv2.imshow("Horizontal", hor)
#
# cv2.waitKey()


# Fancier method
horizontal = cv2.hconcat([img2, img])  # must have same height for horizontal, same height for vertical
cv2.imshow("hor", horizontal)
cv2.waitKey()

vertical = cv2.vconcat([img, img2]) # must have same horizontal
cv2.imshow("vert", vertical)
cv2.waitKey()
