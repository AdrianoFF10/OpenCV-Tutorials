
'''
import cv2 as cv
import numpy as np

img = cv.imread('/home/adrianoff10/Desktop/Lightning.jpg')
assert img is not None, 'file not read'

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)
contour, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contour[0]

hull = cv.convexHull(cnt, returnPoints = False)
defects = cv.convexityDefects(cnt, hull)

print(defects)


for i in range(defects.shape[0]):
    s, e, f, d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv.line(img, start, end, [0,255,0],2)
    cv.circle(img,far , 5, [0,0,255],-1)

#print(cnt[3,0])


#Ex1

for y in range(img.shape[0]):

    for x in range(img.shape[1]):
        
        Color = 255

        distance = cv.pointPolygonTest(cnt, (x,y), False) 
        
        px = img[y,x]

        if distance == 0:
            img[y,x] = [Color,Color,Color]

        if distance > 0:
            img[y,x]=[0,0,Color]
        
        if distance < 0:
            img[y,x] = [Color,0,0]

            


dist = cv.pointPolygonTest(cnt, (50, 50), True)
print(dist)

cv.imshow('Image', img)
cv.waitKey(0)

cv.destroyAllWindows()
'''

import cv2 as cv
import numpy as np

img1 = cv.imread('/home/adrianoff10/Desktop/Lightning.jpg')
img2 = cv.imread('/home/adrianoff10/Desktop/square.png')

im1gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
im2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

ret, thresh1 = cv.threshold(im1gray, 127, 255,0)
ret, thresh2 = cv.threshold(im2gray, 127, 255,0)

contour1, hierarchy = cv.findContours(thresh1, 1, 2)
contour2, hierarchy = cv.findContours(thresh2, 1, 2)

cnt1 = contour1[0]
cnt2 = contour2[0]

ret = cv.matchShapes(cnt1, cnt2, 1,0)
print(ret)












