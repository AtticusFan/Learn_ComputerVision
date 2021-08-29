import cv2 as cv
import numpy as np

img = cv.imread('photos/Female1.jfif')
cv.imshow('Female', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

'''
blur = cv.GaussianBlur(gray, (25,25), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
'''
canny = cv.Canny(img, 75, 115)
cv.imshow('Canny Edges', canny)
'''
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
'''
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)