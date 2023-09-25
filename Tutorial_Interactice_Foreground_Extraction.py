

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/home/adrianoff10/opencv/samples/data/messi5.jpg')
assert img is not None, 'could not read the file'

mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)

cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')    # condição, valor para falso, 
#valor para mentira!!
img = img*mask2[:,:,np.newaxis]
'''
plt.imshow(img), plt.colorbar()
plt.show()
'''
plt.subplot(121), plt.imshow(img), plt.colorbar()

# newmask is the mask image I manually labelled
newmask = cv.imread('/home/adrianoff10/Desktop/newmask.jpg', cv.IMREAD_GRAYSCALE)
assert newmask is not None, "file could not be read, check with os.path.exists()"

# wherever it is marked white (sure foreground), change mask=1
# wherever it is marked black (sure background), change mask=0

mask[newmask == 0] = 0
mask[newmask == 255] = 1

mask, bgdModel, fgdModel = cv.grabCut(img,mask,None,bgdModel,fgdModel,5,cv.GC_INIT_WITH_MASK)
mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')

img = img*mask[:,:,np.newaxis]

plt.subplot(122), plt.imshow(img), plt.colorbar()

plt.show()







