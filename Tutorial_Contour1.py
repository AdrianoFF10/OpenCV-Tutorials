
import numpy as np
import cv2 as cv


im = cv.imread('/home/adrianoff10/opencv/samples/data/detect_blob.png')

assert im is not None, ' File not found'

im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(im_gray, 127 ,255,0)

contours, hierarchy = cv.findContours( thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #argumentos . image, mode, metodo

# os contornos estao guardados em contours

cv.drawContours(im, contours, -1, (0,255,255), 3)

#cv.drawContours(im, contours, 1, (0,255,255), 3)

#cnt = contours[1]
#cv.drawContours(im, [cnt], 0, (0,0,255), 3)



cv.imshow('original', im)
cv.waitKey(0)

cv.destroyAllWindows()