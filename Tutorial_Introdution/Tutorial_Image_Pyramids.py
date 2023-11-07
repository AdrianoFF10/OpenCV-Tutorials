

'''
# 2 types of pyramids, gaussian and laplacian

import cv2 as cv
import numpy as np

image = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg')
assert image is not None, 'file could not be read, check with os.path.exists()'

lower_res = cv.pyrDown(image)
higher_res = cv.pyrUp(image)

cv.imshow('default', image)
cv.imshow('lower res', lower_res)
cv.imshow('higher res', higher_res)

cv.waitKey(0)
cv.destroyAllWindows()
'''

#Image Blending

import cv2 as cv
import numpy as np,sys

A = cv.imread('/home/adrianoff10/opencv/samples/data/apple.jpg')
B = cv.imread('/home/adrianoff10/opencv/samples/data/orange.jpg')

assert A is not None, "file could not be read, check with os.path.exists()"
assert B is not None, "file could not be read, check with os.path.exists()"

# generate Gaussian pyramid for A

G = A.copy()
gpA = [G]

for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B

G = B.copy()
gpB = [B]

for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A

lpA = [gpA[5]]

for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)


# generate Laplacian Pyramid for B

lpB = [gpB[5]]

for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)


# Now add left and right halves of image in each level

LS= []

for la, lb in zip(lpA, lpB):

    rows, columns, dpt, = la.shape
    ls= np.hstack((la[:,0:columns//2], lb[:, columns//2:]))
    LS.append(ls)
    
# Now reconstruct

ls_ = LS[0]

for i in range(6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.pyrDown(ls_, LS[i])


# image with direct connecting each half

real = np.hstack((A[:,:columns//2],B[:,columns//2:]))


cv.imwrite('Pyramid_blending2.jpg',ls_)
cv.imwrite('Direct_blending.jpg',real)




