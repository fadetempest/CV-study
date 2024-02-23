import cv2 as cv
import numpy as np

img = cv.imread('images/rengar.jpeg')

def resize_img(frame, scale = 0.5):
    
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_CUBIC)

img_res = resize_img(img, scale=0.3)

cv.imshow("rengar", img_res)

#BGR to HSV
hsv = cv.cvtColor(img_res, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB
lab = cv.cvtColor(img_res, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img_res, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

cv.waitKey(0)