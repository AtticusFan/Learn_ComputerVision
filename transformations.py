import cv2 as cv
import numpy as np
img = cv.imread('photos/kitten_group 1.jfif')
cv.imshow('Kitten', img)

#translations
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
'''-x --> left, -y --> down'''
translated = translate(img, -100, 100)
cv.imshow('Trans', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(img, -75)
cv.imshow('Rotated', rotated)
rotated_rotated = rotate(rotated, 50)
cv.imshow('Rotated rotated', rotated_rotated)

#resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flipping
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

#cropping
cropped = img[20:40, 30:40]
cv.imshow('Cropped', cropped)

cv.waitKey(0)