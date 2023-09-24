
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/home/adrianoff10/opencv/samples/data/LinuxLogo.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

kernel = np.ones((5,5), np.uint8)

erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)


images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]
titles = ['Default', 'Erosion', 'dilation', 'opening', 'closing', 'gradient', 'tophat', 'blackhat', 'none']

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i]), plt.title(titles[i])

plt.show()

'''

#Scucturing elements . cv.getStructuringElement()
import cv2 as cv
import numpy as np


print(cv.getStructuringElement(cv.MORPH_RECT,(5,5)))

print(cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)))

print(cv.getStructuringElement(cv.MORPH_CROSS,(5,5)))

