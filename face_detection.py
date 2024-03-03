import cv2 as cv
import numpy as np

def Resize(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimension = (width, height)
    
    return cv.resize(frame, dimension,interpolation=cv.INTER_CUBIC)

img = cv.imread('images/lady.jpg')
cv.imshow('People', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('C:/Users/Fade/Desktop/projects/git_repo/pet1/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=7)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0),thickness=1)
    
cv.imshow('Detected Faces', img)

cv.waitKey(0)