

from __future__ import print_function
import cv2 as cv
import argparse


parser = argparse.ArgumentParser(description = 'This program shows how to use background subtraction methods provided by \
                                                OpenCV. You can process both videos and images.')

parser.add_argument('--input', type = str, help = 'Path to a video or sequence of image', default = '/home/adrianoff10/opencv/samples/data/vtest.avi')
parser.add_argument('--algo', type = str, help = 'Background subtracyion method (KNN, MOG2).', default = 'MOG2')
args = parser.parse_args()

print(args.algo, args.input)

#create Background Subtractor objects
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()   # pode ter variáveis no interior

else:
    backSub = cv.createBackgroundSubtractorKNN()

backsub2 = cv.createBackgroundSubtractorKNN()

capture = cv.VideoCapture(args.input)

if not capture.isOpened():
    
    print('Unable too open {}.'.format(args.input))
    exit(0)

## [capture]
while True:

    ret, frame = capture.read()
    if frame is None:
        break

    #update the background model
    fgMask= backSub.apply(frame)
    fgMask2 = backsub2.apply(frame
                             )
    #get the frame number and write it on the current frame int top left
    cv.rectangle(frame, (10,2), (100,20), (255, 255, 255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15,15), cv.FONT_HERSHEY_SIMPLEX, 0.5, 0)   # diz o frame em que se vai

    #show the current frame and the fg masks
    cv.imshow('Frame', frame)
    cv.imshow('FG MASK', fgMask)
    cv.imshow('FG Mask2', fgMask2)

    keyboard = cv.waitKey(30)
    if keyboard == ord('q') | keyboard & 0xFF == 27:
        break






