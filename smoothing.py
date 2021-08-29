import cv2 as cv
img = cv.imread('photos\Female 2.jfif')
cv.imshow('Female', img)

#Averaging
average = cv.blur(img, (5,5))
cv.imshow('Average Blur', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur
median = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 15, 40, 40)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)