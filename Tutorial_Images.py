import cv2 as cv
import sys

img = cv.imread("/home/adrianoff10/opencv/samples/data/messi5.jpg")

if img is None:
    print("Could not read the image!")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("Messi.png",img)

