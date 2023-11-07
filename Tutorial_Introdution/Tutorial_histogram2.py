
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/home/adrianoff10/Desktop/wiki.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, 'file could not read'

hist, bins = np.histogram(img.flatten(), 256, [0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max() / cdf.max())



cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]

hist, bins = np.histogram(img2.flatten(), 256, [0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max() / cdf.max())


plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(), 256, [0,256], color='r')
plt.xlim=[0,256]
plt.legend(('cdf','histogram'),loc = 'upper left')

plt.show()

cv.imshow('After Histogram Equalization', img2)

cv.imshow('Before Histogram Equalization', img)

cv.waitKey(0)
cv.destroyAllWindows()
'''


'''
import numpy as np
import cv2 as cv

img = cv.imread('/home/adrianoff10/Desktop/wiki.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, 'file could not read'

equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) # concatenate img side by side

cv.imshow('Image', res)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('Equ.png', res)
'''

import numpy as np
import cv2 as cv

img = cv.imread('/home/adrianoff10/opencv/samples/data/basketball2.png', cv.IMREAD_GRAYSCALE)
assert img is not None, 'file could not read'


# create a CLAHE object (Arguments are optional).

clahe = cv.createCLAHE(clipLimit=2, tileGridSize=(8,8))
cl1 = clahe.apply(img)

equ = cv.equalizeHist(img)
res = np.hstack((img,equ,cl1)) # concatenate img side by side

cv.imshow('Image', res)
#cv.imwrite('clahe_2.jpg',res)

cv.waitKey(0)
cv.destroyAllWindows()




