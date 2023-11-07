

'''
import numpy as np
import cv2 as cv

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x,y))  

print (x+y)         

'''


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
'''

'''
import cv2 as cv
import numpy as np


img1 = cv.imread('/home/adrianoff10/opencv/samples/data/pic3.png')
img2 = cv.imread('/home/adrianoff10/opencv/samples/data/pic4.png')

assert img1 is not None, 'file could not be read, check with os.path.exists()'
assert img2 is not None, 'file could not be read, check with os.path.exists()'

dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

cv.imshow('image', dst)
cv.waitKey(0)
cv.destroyAllWindows()
'''




'''
import cv2 as cv
import numpy as np

img1 = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg')
img2 = cv.imread('/home/adrianoff10/opencv/samples/data/opencv-logo-white.png')

assert img1 is not None, 'could not read the file'
assert img2 is not None, 'could not read the file'

# tirar as dimensoes da foto que quero adicionar

rows, columns, channels = img2.shape
roi = img1[0:rows, 0:columns]

# criar a mascara do que quero adicionar e criar a mascara inversa tambem

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mascara = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)  # filtra dos 10 as 255 de gray
mask_inv = cv.bitwise_not(mascara)     

# Retira a zona do logo na ROI

img1_bg= cv.bitwise_and(roi, roi, mask = mask_inv)

# Retirar na imagem do logo a parte que nao pertence ao logo - ficar apenas com o logo

img2_fg = cv.bitwise_and(img2, img2, mask=mascara)

# Adicionar o logo à ROI

dst = cv.add(img1_bg, img2_fg)

img1[0:rows, 0:columns] =dst[:,:]  # colocar a dst na imagem do pessi



cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
'''


# Exercise

import cv2 as cv
import numpy as np

x = cv.imread('/home/adrianoff10/opencv/samples/data/left11.jpg')
y = cv.imread('/home/adrianoff10/opencv/samples/data/left12.jpg')


for i in range(0,11,2):

    img = cv.addWeighted(x, i/10, y,1-i/10,0)
    
    cv.imwrite(str(i) + '_' + 'Image.png', img)







