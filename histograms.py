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

cv.imshow('Gray', gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Num of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Num of pixels')

colors = ('b','g','r')
for i,col in enumerate(colors):
    color_hist = cv.calcHist([img_res], [i], None, [256], [0,256])
    plt.plot(color_hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)