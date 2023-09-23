
'''
import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

'''

import cv2 as cv
import numpy as np

cap = cv.VideoCapture('/home/adrianoff10/opencv/samples/data/Megamind.avi')

while (1):

    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # conversao ce bgr para hsv

    #definição dos limites para cada cor

    lowerblue = np.array([110, 50, 50])
    upperblue = np.array([130, 255, 255])

    lowerred = np.array([0, 100, 100])
    upperred = np.array([10, 255, 255])

    lowergreen = np.array([50, 100, 100])
    uppergreen = np.array([70, 255, 255])

    # Definição da mascara 

    mask_blue = cv.inRange(hsv, lowerblue, upperblue)
    mask_red = cv.inRange(hsv, lowerred, upperred)
    mask_green = cv.inRange(hsv, lowergreen, uppergreen)

    mask = mask_blue | mask_green | mask_red

    res = cv.bitwise_and(frame, frame, mask = mask)
    #res_green = cv.bitwise_and(frame, frame, mask = mask_green)
    #res_blue = cv.bitwise_and(frame, frame, mask = mask_blue)
    #res_red = cv.bitwise_and(frame, frame, mask = mask_red)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res',res)
    cv.imshow('azul',mask_blue)
    cv.imshow('verde',mask_green)
    cv.imshow('vermelho',mask_red)


    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()






