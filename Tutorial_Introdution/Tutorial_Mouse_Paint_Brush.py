'''
# Verificar os eventos que são possíveis obter com o rato

import cv2 as cv

events =[i for i in dir(cv) if 'EVENT' in i]

print(events)

'''

'''

#Codigo para apenas desenhar circulos de 100 de raio onde houver double click

import numpy as np
import cv2 as cv

def draw_circle(event,x,y, flags, param):    #definir uma funcao
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

'''

'''
import numpy as np
import cv2 as cv

drawing = False 
mode = True # True desenha retangulos, false desenha circulos
ix, iy = -1, -1


def draw(event,x,y,flags,param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv.EVENT_LBUTTONUP:
         drawing = False
         if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
         else:
                cv.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('Image')
cv.setMouseCallback('Image',draw)

while (1):
     cv.imshow('Image',img)
     k = cv.waitKey(1) & 0xFF
     if k == ord('m'):
          mode = not mode
     elif k == 27:
          break
     
cv.destroyAllWindows()

'''

#Exercise2

import numpy as np
import cv2 as cv

mode = False    #mode False draws circle
drawing = False

ix, iy = 0, 0 


def draw(event, x, y, flags, param):
    global ix, iy, mode, drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        if mode == False:
            cv.circle(img, (x,y),5, (0,0,255), -1)
        ix, iy = x, y

    #elif event == cv.EVENT_MOUSEMOVE:
     #   if drawing == True:
      #      if mode == False:
       #         cv.rectangle(img, (ix,iy), (x,y), (0, 255,0), 3)
        #    else:
         #       cv.circle(img, (x,y), (0,0,255), -1)

    elif event == cv.EVENT_LBUTTONUP:
        if mode == True:
            cv.rectangle(img,(ix,iy), (x,y), (0,255,0), 3)

        drawing = False


img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw)

while (1):
    cv.imshow('image',img)

    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode= not mode
    elif k == 27:
        break

cv.destroyAllWindows



