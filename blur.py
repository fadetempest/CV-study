import cv2 as cv
import numpy as np

def Resize(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimension = (width, height)
    
    return cv.resize(frame, dimension,interpolation=cv.INTER_CUBIC)

img = cv.imread('images/rengar.jpeg')

img_res = Resize(img, scale=0.3)

cv.imshow('Rengar', img_res)

blur = cv.blur(img_res, (3,3))
cv.imshow("Blur", blur)

gauss = cv.GaussianBlur(img_res, (3,3), 0)
cv.imshow("Gauss", gauss)

median = cv.medianBlur(img_res, 3)
cv.imshow("Median", median)

bilateral = cv.bilateralFilter(img_res, 10, 40, 30)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)