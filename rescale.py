import cv2 as cv
img = cv.imread('photos\cat 1.jfif')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.75):
    #for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def changeRes(width, height):
    #only for live videos
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('videos\switch_ad.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.5)
    cv.imshow('Video', frame)
    cv.imshow('Video_Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()