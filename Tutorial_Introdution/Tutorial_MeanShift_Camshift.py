# Meanshift - distribuição matemática em que um vetor aponta na direção da maior densidade de pontos

'''
import numpy as np
import cv2 as cv
import argparse
parser = argparse.ArgumentParser(description='This sample demonstrates the meanshift algorithm. \
                                              The example file can be downloaded from: \
                                              https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4')

cap = cv.VideoCapture('/home/adrianoff10/Desktop/slow_traffic_small.mp4')

# take first frame of the video
ret,frame = cap.read()

# Set up the initial location of window that might be followed
x, y, w, h = 300, 200, 100, 50   #valores definidos para "template"
track_window = (x, y, w, h)

# Set up the ROI for tracking 
roi = frame[y : y + h, x : x + w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0, 60, 32)), np.array((180, 255, 255)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)    #normalizar os valores do roi_hist (tornar a distribuição entre 0 e 255)

# Set up the termination criteria, either 10 iterations or move by at least 1 pt

term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)   # modo necessário para a meanShift

while (1):
    ret, frame = cap.read()

    if ret == True:
         hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
         dst = cv.calcBackProject([hsv],[0],roi_hist, [0,180], 1)   # Calcula a projeção de um histograma

         # Apply meanshift to get the new location
         ret, track_window = cv.meanShift(dst, track_window, term_crit)

         # Draw on image
         x,y,w,h = track_window
         cv.rectangle(frame, (x,y), (x+w, y+h), 255, 2)
         cv.imshow('Frame', frame)

         if cv.waitKey(30) & 0xFF ==27:
              break
    else:
         break

'''

#'''
# Camshift - Processo adaptativo de MeanShift (tamanho da janela varia com a proximidade) - isto combate este problema , bem como o da rotação

import numpy as np
import cv2 as cv
import argparse
parser = argparse.ArgumentParser(description='This sample demonstrates the camshift algorithm. \
                                              The example file can be downloaded from: \
                                              https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4')



cap = cv.VideoCapture('/home/adrianoff10/Desktop/slow_traffic_small.mp4')

# take first frame of the video
ret,frame = cap.read()

# Set up initial location of a window
x, y, w, h = 300, 200, 100, 50
track_window = (x, y, w, h)

# Set up the ROI for tracking
roi = frame[y : y + h, x : x + w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0, 60, 32)), np.array((180, 255, 255)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

while (1):
    ret, frame = cap.read()

    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # apply camshift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit)

        # Draw it on image
        pts = cv.boxPoints(ret)
        print(pts)
        pts = np.int0(pts)
        cv.polylines(frame,[pts],True, 255,2)
        cv.imshow('img2', frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break


#'''












