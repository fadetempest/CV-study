import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def Resize(frame, scale = 0.3):
    width = int(frame.shape[1]*scale)
    heigth = int(frame.shape[0]*scale)
    
    dimension = (width, heigth)
    
    return cv.resize(frame, dimension, interpolation=cv.INTER_CUBIC)

img = cv.imread('images/rengar.jpeg')

img_res = Resize(img)

cv.imshow('Rengar', img_res)

gray = cv.cvtColor(img_res, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# Laplacing
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow('Sobel X', sobel_x)
cv.imshow('Sobel Y', sobel_y)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 100, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)