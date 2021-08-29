import cv2 as cv
#reading image
"""
img = cv.imread('photos\dog 1.jfif')
cv.imshow('Dog', img)
cv.waitKey(0)
"""
#reading videos
capture = cv.VideoCapture('videos\switch_ad.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()