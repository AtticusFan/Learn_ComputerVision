import cv2 as cv
img = cv.imread('photos/Male.jfif')
cv.imshow('Male', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edge', canny)

#Dilating the image
dilated = cv.dilate(canny, (10, 10), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Cropping
cropped = img[5:20, 20:40]
cv.imshow('Cropped', cropped)

cv.waitKey(0)