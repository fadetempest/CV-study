import cv2 as cv
import numpy as np

def Resize(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimension = (width, height)
    
    return cv.resize(frame, dimension,interpolation=cv.INTER_CUBIC)

img = cv.imread('images/papper_man.jpeg')

img_res = Resize(img)

cv.imshow('Papper man', img_res)

blank = np.zeros(img_res.shape[:2], dtype='uint8')

mask = cv.rectangle(blank,(600,30),(800,800),255,-1)

masked_img = cv.bitwise_and(img_res, img_res, mask=mask)
cv.imshow('Masked Image', masked_img)

cv.waitKey(0)