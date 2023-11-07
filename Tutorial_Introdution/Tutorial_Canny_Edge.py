
'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

edges = cv.Canny(img, 100,200)

plt.subplot(121), plt.imshow(img, cmap = 'gray'), plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap = 'gray'), plt.title('Canny edeges'), plt.xticks([]), plt.yticks([])


plt.show()
'''

#Exercise


import numpy as np
import cv2 as cv

def nothing(x):
    pass

minValue = 100
maxValue = 200

img = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"


edge = cv.Canny(img, minValue, maxValue, L2gradient = True)
cv.namedWindow('Edge image')

cv.createTrackbar('Min', 'Edge image', 100, 255, nothing)
cv.createTrackbar('Max', 'Edge image', 200, 255, nothing)

cv.imshow('Original Image', img)

while (1):

    cv.imshow('Edge image', edge)
    if cv.waitKey(1) & 0xFF == 27:
        break


    minValue = cv.getTrackbarPos('Min', 'Edge image')
    maxValue = cv.getTrackbarPos('Max', 'Edge image')


    edge = cv.Canny(img , minValue, maxValue, L2gradient = True)

cv.imshow("Original Image", img)

cv.destroyAllWindows()








