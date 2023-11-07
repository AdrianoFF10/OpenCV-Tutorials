

import numpy as np
import cv2 as cv

img = cv.imread('/home/adrianoff10/opencv/samples/data/home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)

# cv.drawKeypoints(gray,kp,img)
# cv.imwrite('sift_keypoints.jpg',img)

cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift_keypoints.jpg',img)

cv.waitKey(0)
