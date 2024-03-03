import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def Resize(frame, scale = 0.3):
    width = int(frame.shape[1]*scale)
    heigth = int(frame.shape[0]*scale)
    
    dimension = (width, heigth)
    
    return cv.resize(frame, dimension, interpolation=cv.INTER_CUBIC)

img = cv.imread('images/brokkol.jpg')

img_res = Resize(img, scale=0.3)

cv.imshow('Rengar', img_res)

gray = cv.cvtColor(img_res, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# Simple thresholding

threshold, thresh = cv.threshold(gray, 130, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded image', thresh)

threshold, thresh_inv = cv.threshold(gray, 130, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thresholded image INV', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshold', adaptive_thresh)

adaptive_thresh_gaus = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshold Gaus', adaptive_thresh_gaus)


cv.waitKey(0)