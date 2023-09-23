

'''
import numpy as np
import cv2 as cv

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x,y))  

print (x+y)         

'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plp

x = cv.imread('/home/adrianoff10/opencv/samples/data/left11.jpg')

y = cv.imread('/home/adrianoff10/opencv/samples/data/left12.jpg')

img=cv.add(x,y)

img1=x+y

plp.subplot(221), plp.imshow(x, 'gray'), plp.title('Image1')
plp.subplot(222), plp.imshow(y, 'gray'), plp.title('Image2')
plp.subplot(223), plp.imshow(img, 'gray'), plp.title('cv.add')
plp.subplot(224), plp.imshow(img1, 'gray'), plp.title('numpy addition')

plp.show()
