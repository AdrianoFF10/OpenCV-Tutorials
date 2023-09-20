
import cv2 as cv
import sys

image = cv.imread("/home/adrianoff10/Desktop/Ronaldo.jpg")

if image is None:
    sys.exit("Could not read this image!")

cv.imshow("Melhor do Mundo", image)

k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("Ronny.png",image)
