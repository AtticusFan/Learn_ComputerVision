import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('harr_face.xml')
people = ['Female 1', 'Female 2', 'Ishihara Satomi', 'Male 1', 'Male 2', 'Male 3']


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img = cv.imread(r'C:\workspace\OPENCV\Faces\Val\image.jfif')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#detect the face
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=4)
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    labels, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[labels]} with a confidence of {confidence}')
    cv.putText(img, str(people[labels]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 1)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow('Detected Face', img)
cv.waitKey(0)

