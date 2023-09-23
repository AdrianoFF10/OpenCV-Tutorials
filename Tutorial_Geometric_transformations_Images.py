
'''
import cv2 as cv
import numpy as np
'''

'''
#resize

img = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg')

#print(img.shape)

assert img is not None, 'Could not read this file'

res = cv.resize(img, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)

cv.imshow('img',img)
cv.imshow('resize', res)

cv.waitKey(0) 
cv.destroyAllWindows()

'''

'''
#translation

img = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg', cv.IMREAD_GRAYSCALE)

assert img is not None, 'Could not read this file'

rows, columns = img.shape

M = np.float32([[1,0,100], [0,1,50]])       # deslocação de 100 em x e 50 em y

dst = cv.warpAffine(img, M, (columns, rows))  #colunas e linhas estap trocadas!

cv.imshow('img',dst)
cv.imshow('img1',img)
cv.waitKey(0)
cv.destroyAllWindows()
'''

'''
#rotation

img = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg', cv.IMREAD_GRAYSCALE)

assert img is not None, 'Could not read this file'

rows, columns = img.shape

M = cv.getRotationMatrix2D(((columns-1)/2,(rows-1)/2), -90, 1)  # argumentos: centro, rotação escala

dst = cv.warpAffine(img, M, (columns, rows))

cv.imshow('img',dst)
cv.imshow('img1',img)
cv.waitKey(0)
cv.destroyAllWindows()
'''

'''
# Affine transformação

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plp

img = cv.imread('/home/adrianoff10/opencv/samples/data/chessboard.png')

rows,columns,ch = img.shape

point1 = np.float32([[50,50], [200,50], [50,200]])

point2 = np.float32([[10,100],[200,50],[100,250]])

M = cv.getAffineTransform(point1, point2)

dst = cv.warpAffine(img, M, (columns, rows))

cv.circle(img, (50,50), 50, (0,255,0), -1)
cv.circle(img, (200,50), 50, (0,255,0), -1)
cv.circle(img, (50,200), 50, (0,255,0), -1)

cv.circle(dst, (100,100), 50, (0,255,0), -1)
cv.circle(dst, (200,50), 50, (0,255,0), -1)
cv.circle(dst, (100,250), 50, (0,255,0), -1)


plp.subplot(121), plp.imshow(img), plp.title('original')
plp.subplot(122), plp.imshow(dst), plp.title('output')

plp.show()
'''


# Perspective Transformation

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plp

img = cv.imread('/home/adrianoff10/opencv/samples/data/sudoku.png')

assert img is not None, "file could not be read, check with os.path.exists()"

rows,columns,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv.getPerspectiveTransform(pts1, pts2)

dst = cv.warpPerspective( img, M, (300, 300))

plp.subplot(1,2,1), plp.imshow(img), plp.title('Original')

plp.subplot(1,2,2), plp.imshow(dst), plp.title('Output')

plp.show()





