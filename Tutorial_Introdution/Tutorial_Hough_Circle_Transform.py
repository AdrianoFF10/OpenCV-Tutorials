

import numpy as np
import cv2 as cv

img = cv.imread('/home/adrianoff10/opencv/samples/data/opencv-logo-white.png', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Could not read'

img = cv.medianBlur(img, 5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, 
                          param1 = 50, param2 = 30, minRadius = 0, maxRadius = 0)
print(circles)

circles = np.uint16(np.around(circles))
print(circles)
print(circles[0,1])

for i in circles[0,:]:
     # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
print(i)

cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()










