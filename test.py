import cv2 as cv

# Image reading
img = cv.imread('images/rengar.jpeg')

def rescaleImage(frame, scale=0.4):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img_resize = rescaleImage(img)
cv.imshow('rengar', img_resize)

cv.waitKey(0)

# Video reading

# capture = cv.VideoCapture('videos/cook.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)
    
#     if cv.waitKey(25) & 0xFF == ord('q'):
#         break
    
# capture.release()
# cv.destroyAllWindows()