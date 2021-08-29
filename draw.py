import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

'''
#1. Paint colour
blank[200:300, 300:400] = 255, 255, 0
cv.imshow('Green', blank)
'''

#2. Draw rectangle
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (125, 100, 200), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#3. Draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (50, 174, 150), thickness=cv.FILLED)
cv.imshow('Circle', blank)

#4. Draw line
cv.line(blank, (100, 50), (300, 250), (125, 100, 85), thickness=2)
cv.imshow('Line', blank)

#5. Write text
cv.putText(blank, 'Hello', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 255), 2)
cv.imshow('Text', blank)

'''
img = cv.imread('photos\dog 1.jfif')
cv.imshow('Dog', img)
'''

cv.waitKey(0)