'''
# Verificar os eventos que são possíveis obter com o rato

import cv2 as cv

events =[i for i in dir(cv) if 'EVENT' in i]

print(events)

'''

import numpy as np
import cv2 as cv

def draw_circle(event,x,y,flags,param):    #definir uma funcao
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x,y),50, (0,255,0), -1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('Image')
cv.setMouseCallback('Image', draw_circle)

while True:
    cv.imshow('Image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()






