


import numpy as np
import cv2 as cv

img = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg')

assert img is not None, "file could not be read, check with os.path.exists()"    # Testar se a imagem foi lida corretamente, como se fosse um if

#px = img[100,100]   #retirar propriedades do pixel da linha 100 e coluna 100

#print(px)

#blue = img[100,100,0]   # tirar apenas quanto azul tem,   caso fosse 1 seria verde e 2 vermelho

#print(blue)

#print(img.item(10,10,2))    #outra maneira de retirar as propriedades dos pixeis

#img.itemset((10,10,2),100)  #alterar as propriedades dos pixeis
#print(img.item(10,10,2))


#print(img.shape)    # devolve o numero de linhas, colunas e canais (cores)

#print(img.size)     #devolve o numoer total de pixeis

#print (img.dtype)  

'''
ball = img[280:340, 330:390]

img[ 273:333, 100:160] = ball

cv.imshow('Image',img)

while True:
    
    k = cv.waitKey(0) & 0xFF

    if k == 27:
        break
'''

#b,g,r = img.split(img)

#b = img[:,:,0]


img[:,:,2] = 0

print(img.item(10,10,2))

#img = cv.merge((b,g,r))

cv.imshow('Image',img)

while True:
    
    k = cv.waitKey(0) & 0xFF

    if k == 27:
        break

'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


BLUE =[255,0,0]

img1 = cv.imread('/home/adrianoff10/opencv/samples/data/opencv-logo.png')

assert img1 is not None, 'file could not be read, check with os.path.exists()'

replicate = cv.copyMakeBorder(img1, 10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1, 10,10,10,10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, 10,10,10,10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, 10,10,10,10, cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1, 10,10,10,10, cv.BORDER_CONSTANT,value=BLUE)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate,'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect,'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101,'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap,'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant,'gray'), plt.title('CONSTANT')

plt.show()

'''









