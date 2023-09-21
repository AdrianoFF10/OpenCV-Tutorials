
# Video from camera

"""
import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0) #the argument is the index of camera

if not cap.isOpened():
    sys.exit("Cannot open the camera!")    #same as print("...")
    exit()

while True:
    ret, frame = cap.read()   # capture frame by frame

    if not ret:  
        print("Can't receive the frame.")  #In frames are correctly saved, ret is true
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # sistema de cores para gray

    cv.imshow('frame', gray)

    k = cv.waitKey(0)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

"""

#----------------------------------------------------------------------------------------

# Playing Video from file

'''

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('/home/adrianoff10/opencv/samples/data/Megamind.avi')

while cap.isOpened():
 ret, frame = cap.read()

 # if frame is read correctly ret is True

 if not ret:
    print("Can't receive frame. Stream ending. Exiting ...")
    break
 
 
 gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 cv.imshow('frame', gray)

 if cv.waitKey(25) == ord('q'):
    break
 
cap.release()
cv.destroyAllWindows()

'''

#----------------------------------------------------------------------------------------

# Saving a video


import cv2 as cv
import numpy as np

cap = cv.VideoCapture('/home/adrianoff10/opencv/samples/data/Megamind.avi')

fourcc = cv.VideoWriter_fourcc(*'XVID') #definir a codificação do video e criar o objeto video writer
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480)) #Definições do que vai ser guardado 
#(video, codificacao, fps, dimensao)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can not receive frame. Stream ending. Exiting...")
        break
    frame = cv.flip(frame,0)  # reescrever os frames na direção vertical

    out.write(frame)   # guardar os frames de novo

    cv.imshow('Video', frame)

    k = cv.waitKey(25)

    if k == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()












