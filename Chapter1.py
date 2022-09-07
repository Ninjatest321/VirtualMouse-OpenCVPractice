import cv2

# Read Images

# img = cv2.imread("RandomImage1.jpeg")
#
# cv2.imshow("Output", img)
# cv2.waitKey()

# Read videos

# video = cv2.VideoCapture("Video1.mp4")
#
# while True:
#     success, img = video.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# Read Webcam

video = cv2.VideoCapture(0)
video.set(3, 640)  # ID number 3 stands for width
video.set(4, 480)  # ID number 4 stands for height
video.set(10, 100) # Id number 10 changes brightness

while True:
    success, img = video.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
