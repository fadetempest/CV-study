import cv2 as cv
import numpy as np

def Resize(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimension = (width, height)
    
    return cv.resize(frame, dimension,interpolation=cv.INTER_CUBIC)


capture = cv.VideoCapture('videos/cook.mp4')

while True:
    isTrue, frame = capture.read()
    # cv.imshow('video', frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    haar_cascade = cv.CascadeClassifier('C:/Users/Fade/Desktop/projects/git_repo/pet1/haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=10)
    
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),thickness=2)
    
    cv.imshow("Video Detection", frame)
    
    if cv.waitKey(10) & 0xFF == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()