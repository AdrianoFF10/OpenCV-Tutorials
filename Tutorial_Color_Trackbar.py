'''

import numpy as np
import cv2 as cv

def nothing(x):
    pass

# creating a black image and naming it

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

# creating trackbar for color change

cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
#creating the switch 

switch = ' 0: OFF \n 1: ONN'
cv.createTrackbar(switch, 'image',0,1,nothing)

# showing the image

while(1):

    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27: 
        break

#get the value of each variable

    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()

'''

#Ex3

import numpy as np
import cv2 as cv


def nothing(x):
    pass

drawing = False

def drawing_circles(event, x, y, flags, param):
    global drawing
    
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        cv.circle(draw, (x,y), radius, (b,g,r), -1 )
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(draw, (x,y), radius, (b,g,r), -1 )
    elif event == cv.EVENT_LBUTTONUP:
        cv.circle(draw, (x,y), radius, (b,g,r), -1 )
        drawing = False
        

img = np.zeros((300,512,3),np.uint8)
cv.namedWindow('image')

switch = ' 0: OFF\n 1: ON'

cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('Radius', 'image', 5, 25, nothing)
cv.createTrackbar(switch, 'image',1, 1, nothing)



draw = np.zeros((512,512,3),np.uint8)
cv.namedWindow('Draw')
cv.setMouseCallback('Draw',drawing_circles)



while True:
    cv.imshow('image', img)
    cv.imshow('Draw',draw)

    k = cv.waitKey(1) & 0xFF
    if k == 27: 
        break
    
    elif k == ord('s'):
        cv.imwrite('Desenho.png', draw)

    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    radius = cv.getTrackbarPos('Radius', 'image')
    s = cv.getTrackbarPos( switch, 'image')
    
    if s == 0:
        img[:]=0
    
    else:
        img[:] = [b, g, r]


cv.destroyAllWindows()






