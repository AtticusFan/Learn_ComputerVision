import cv2
try:
    img = cv2.imread('Photos\car.jpg')
    img_small = cv2.resize(img, (300,100))
    cv2.imshow('Origin', img)
    cv2.imshow('Resize', img_small)
    cv2.waitKey(0)
    cv2.destroyALLWindow()
    try:
        cv2.imwrite('Small.jfif', img_small)
        print('saved')
    except:
        print('Error:write')
except:
    print('Error:read')