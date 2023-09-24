
'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/home/adrianoff10/opencv/samples/data/sudoku.png')
assert img is not None, 'file could not be read, check with os.path.exists()'

laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5) # 1, 0 significa que ha derivaçãom da cor em x e nao ha em y
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5) # 0,1 significa que ha derivaçãom da cor em y e nao ha em x

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')     #cmap isthe color map
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()

'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('/home/adrianoff10/opencv/samples/data/ellipses.jpg')
assert img is not None, 'file could not be read, check with os.path.exists()'

# output dtype = cv.CV_8U
sobelx8u = cv.Sobel(img,cv.CV_8U,1,0,ksize=5)   # perda de informação devido aos valores negativos

# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)   # transformação dos valores em absolutos para contrariar os negativos
sobel_8u = np.uint8(abs_sobel64f)    # transformação dos 64 bits em 8 bits

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()


