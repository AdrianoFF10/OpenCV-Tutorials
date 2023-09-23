

# 2D convolution - Image Filter

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

'''

img = cv.imread('/home/adrianoff10/opencv/samples/data/opencv-logo.png')
assert img is not None, "file could not be read, check with os.path.exists()"

kernel = np.ones((5,5),np.float32)/25

dst = cv.filter2D(img, -1, kernel)    # argumentos: foto, profundidade, kernel

plt.subplot(121),plt.imshow(img),plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging'), plt.xticks([]), plt.yticks([])

plt.show()

'''

# Image bluring

'''
# averaging 

img = cv.imread('/home/adrianoff10/opencv/samples/data/opencv-logo-white.png')
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.blur(img, (5,5))

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img, -1, kernel) 

plt.subplot(131), plt.imshow(img), plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(blur), plt.title('Blurred'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(dst), plt.title('Filter'), plt.xticks([]), plt.yticks([])

plt.show()
'''


'''
# Gaussian Blurring

img = cv.imread('/home/adrianoff10/opencv/samples/data/opencv-logo-white.png')
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.GaussianBlur(img,(5,5),0)

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img, -1, kernel) 

plt.subplot(131), plt.imshow(img), plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(blur), plt.title('Blurred'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(dst), plt.title('Filter'), plt.xticks([]), plt.yticks([])

plt.show()

'''

'''
# Median Blurring

img = cv.imread('/home/adrianoff10/opencv/samples/data/opencv-logo-white.png')
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.medianBlur(img, 5)

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img, -1, kernel) 

plt.subplot(131), plt.imshow(img), plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(blur), plt.title('Blurred'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(dst), plt.title('Filter'), plt.xticks([]), plt.yticks([])

plt.show()
'''

# bilateral filter

img = cv.imread('/home/adrianoff10/opencv/samples/data/aloeL.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.bilateralFilter(img, 9, 75, 75)

kernel = np.ones((5,5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)

plt.subplot(131), plt.imshow(img), plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(blur), plt.title('Blurred'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(dst), plt.title('Filter'), plt.xticks([]), plt.yticks([])

plt.show()




