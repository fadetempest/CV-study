import cv2 as cv
import numpy as np

def rescaleImage(frame, scale=0.4):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread('images/rengar.jpeg')

img_res = rescaleImage(img, scale=0.3)

cv.imshow('Rengar', img_res)

blank = np.zeros(img_res.shape, dtype='uint8')
cv.imshow('blank',blank)

gray = cv.cvtColor(img_res, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img_res,(5,5),cv.BORDER_WRAP)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

countors, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(countors))

cv.drawContours(blank,countors,-1,(255,255,255),1)
cv.imshow('Draw', blank)

cv.waitKey(0)

