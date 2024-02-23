import cv2 as cv

img = cv.imread('images/papper_man.jpeg')

def rescaleImage(frame, scale=0.4):
    print(frame.shape)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img_rescale = rescaleImage(img)
cv.imshow('asd', img_rescale)

# # Конвертация в серые оттенки
# gray = cv.cvtColor(img_rescale, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Блюр
# blur = cv.GaussianBlur(img_rescale, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

# # Edges
# canny = cv.Canny(blur,125,175)
# cv.imshow('Canny', canny)

# # Dilating
# dilated = cv.dilate(canny,(5,5),iterations=3)
# cv.imshow('Dilated', dilated)

# # Eroding
# eroded = cv.erode(dilated,(5,5),iterations=3)
# cv.imshow('Eroded', eroded)

# Cropp
cropped = img_rescale[10:50, 50:200]
cv.imshow('Cropp', cropped)

cv.waitKey(0)