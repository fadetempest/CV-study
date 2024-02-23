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

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> Left  -y --> Up  x--> Right  y--> Down

translated = translate(img_res, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, point=None):
    (height, width) = img.shape[:2]
    
    if point is None:
        point = (width//2,height//2)
        
    rotMat = cv.getRotationMatrix2D(point,angle,1.0)
    dimension = (width,height)
    
    return cv.warpAffine(img,rotMat,dimension)

rotated = rotate(img_res,180)
cv.imshow('Rotated', rotated)

cv.waitKey(0)