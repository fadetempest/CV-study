import cv2 as cv
import numpy as np

def Resize(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimension = (width, height)
    
    return cv.resize(frame, dimension,interpolation=cv.INTER_CUBIC)

img = cv.imread('images/car 2.jpg')
img_res = Resize(img, scale=0.7)

cv.imshow('Car', img_res)

gray = cv.cvtColor(img_res, cv.COLOR_BGR2GRAY)
cv.imshow('Car Gray', gray)

haar_cascade = cv.CascadeClassifier('C:/Users/Fade/Desktop/projects/git_repo/pet1/haar_plate.xml')
plate_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

for (x,y,w,h) in plate_rect:
    cv.rectangle(img_res, (x,y), (x+w, y+h), (0,255,0),thickness=2)
    
cv.imshow('Detected Plates',img_res)

cv.waitKey(0)