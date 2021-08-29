import cv2 as cv
import numpy as np
img = cv.imread('photos\Scene 2.jfif')
cv.imshow('Scene', img)
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank Image", blank)

mask = cv.circle(blank, (img.shape[1]//2 - 10, img.shape[0]//2 - 25), 50, 255, -1)
cv.imshow("Mask", mask)
'''
#Weird mask
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 50, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (100,100), 255, -1)
weird_shape = cv.bitwise_and(circle, rectangle)
masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weired Masked Image', masked)
'''
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)