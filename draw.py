import cv2 as cv
import numpy as np

# img = cv.imread('images/brokkol.jpg')
blank = np.zeros((500,500,3), dtype='uint8')

# cv.imshow('asdasd', blank)

# blank[:] = 0,0,255
# cv.imshow('Green', blank)

# Прямоугольник
cv.rectangle(blank,(20,20),(250,250),(0,0,255),thickness=3)
cv.imshow('AS', blank)

# Круг
cv.circle(blank, (250,250), 50, (0,255,0),thickness=-1)
cv.imshow('Circle', blank)

# Линия
cv.line(blank,(0,0),(500,500),(255,255,255),thickness=3)
cv.imshow('Line', blank)

# Текст
cv.putText(blank,'Hello',(0,100),cv.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255),thickness=2)
cv.imshow('asd', blank)


# cv.imshow('asd', img)

cv.waitKey(0)