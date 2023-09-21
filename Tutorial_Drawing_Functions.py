'''

import cv2 as cv
import numpy as np
import sys


img = np.zeros((512,512,3),np.uint8)

cv.line(img, (0,0),(511,511),(255,0,0),5)  #Criacao de uma linha no sistema BGR com thickness 5

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv.circle(img, (477,63),63, (0,0,255),-1)  # como a espessura e igual a -1, delimita todo o interior

cv.ellipse(img, (256,256), (100,100),0 ,0,180, 255, -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('image',img)
k = cv.waitKey(0)

if k == ord('q'):
    cv.imwrite('Image.png',img)

'''

# Exercicio 1

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv.ellipse(img, (256,100), (100,100), 0, 120, 420, (0,0,255), -1)

cv.ellipse(img, (256,100), (30,30), 0, 0, 360, (0,0,0), -1)


cv.ellipse(img, (140,300), (100,100), 0, 0, 300, (0,255,0), -1)

cv.ellipse(img, (140,300), (30,30), 0, 0, 360, (0,0,0), -1)


cv.ellipse(img, (365,300), (100,100), 0, -60, 240, (255,0,0), -1)

cv.ellipse(img, (365,300), (30,30), 0, 0, 360, (0,0,0), -1)


font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV', (20,500), font, 4, (255,255,255), 2, cv.LINE_AA)

cv.imshow('OpenCV Logo', img)

if cv.waitKey(0) == ord('s'):
    cv.write('OpenCV_Logo.png',img)









