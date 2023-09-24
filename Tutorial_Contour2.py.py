
'''
import numpy as np
import cv2 as cv


img = cv.imread('/home/adrianoff10/Desktop/star.png', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Could not read file'

ret, thresh = cv.threshold(img, 127 ,255,0)

contour, hierarchy = cv.findContours(thresh, 1,2)

cnt = contour[0]
M = cv.moments(cnt)

#print(M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print('Centroide: x: {}, y: {}'.format(cx, cy))

area = cv.contourArea(cnt)

print('Area: {}'.format(area))

print('Perimetro: {}'.format(cv.arcLength(cnt, True)))

epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)

cv.drawContours(img, approx, -1, (0,0,255), 3)

hull = cv.convexHull(cnt)
cv.drawContours(img, hull, -1, (0,0,255),3)

cv.imshow('Image', img)

cv.waitKey(0)

cv.destroyAllWindows()

'''

# Bounding 

import cv2 as cv
import numpy as np

img = cv.imread('/home/adrianoff10/Desktop/Lightning.jpg')
assert img is not None, 'file not read'

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)

contour, hierarchy = cv.findContours(thresh, 1,2)

cnt = contour[0]

x,y,w,h = cv.boundingRect(cnt)

cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0,0,255),3)


(x,y), radius =cv.minEnclosingCircle(cnt)

center = ( int(x), int(y))
radius = int(radius)

cv.circle(img,center, radius, (255,0,0),4)

ellipse = cv.fitEllipse(cnt)
cv.ellipse(img, ellipse, (0,0,0), 3)

rows, columns = img.shape[:2]
[vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0,0.01, 0.01)

lefty = int((-x*vy/vx) + y)
righty = int(((columns-x)*vy/vx)+y)

cv.line(img,(columns-1,righty),(0,lefty),(60,255,100),2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
