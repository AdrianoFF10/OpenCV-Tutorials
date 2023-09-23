

import cv2 as cv
import numpy as np


'''
e1 = cv.getTickCount()

x=2
y=3

print (x+y)

e2 = cv.getTickCount()

time = (e2-e1)/cv.getTickFrequency()
print (time)

'''


'''
img1 = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg')

assert img1 is not None, 'Could not read the file!'

e1 = cv.getTickCount()

for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
    cv.imshow('aaa',img1)

    if cv.waitKey(200) & 0xFF ==27:
        break

e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
'''

#print(cv.useOptimized())
#cv.setUseOptimized(False)
#cv.setUseOptimized(True)








