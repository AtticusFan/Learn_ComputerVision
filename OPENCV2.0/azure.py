import requests
import cv2
import time
import re

base = 'https://japanwest.api.cognitive.microsoft.com/vision/v3.1/read/analyze?%'
recog_url = f'{base}/recognizeText?mode=Printed'
key = '9a16436bb43a434fbdc336f73c7ad55d'
headers = {'Ocp-Apim-Subscription-Key': key}
headers_stream = {'Ocp-Apim-Subscription-Key': key,                
                  'Content-Type': 'application/octet-stream'}

def get_license(img):
    img_encode = cv2.imencode('.jpg', img)[1]
    img_bytes = img_encode.tobytes()                
    r1 = requests.post(recog_url,
                       headers=headers_stream,
                       data=img_bytes)
    if r1.status_code != 202:
        print(r1.json())
        return '請求失敗'
    result_url = r1.headers['Operation-Location']
    r2 = requests.get(result_url, headers=headers)
    while r2.status_code == 200 and r2.json()['status'] != 'succeeded':
        r2 = requests.get(result_url, headers=headers)
        time.sleep(0.5)
        print('status: ', r2.json()['status'])
    carcard = ''
    lines = r2.json()['analyzeResult']['readResults'][0]['lines']
    for i in range(len(lines)):
        text = lines[i]['text']
        m = re.match(r'^[\w]{3,4}[-. ][\w]{3,4}$', text)
        if m != None:
            carcard = m.group()
            return carcard
    if carcard == '':
        return '無此車牌'
"""
try:
    img = cv2.imread('car.jpg')
    print('status:  Start')
    text = get_license(img)
    print('車牌：', text)
    cv2.imshow('Frame', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    print('讀取圖片失敗')
"""