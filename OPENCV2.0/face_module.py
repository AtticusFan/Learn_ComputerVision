import sqlite3
import cv2
from datetime import datetime
import time
import requests

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'
key = 'f85d4cd78eda46cab8549149ac0d146a'   
headers_stream = {}   
headers_json = {}    
headers = {}         


def face_init(b, k):
    global base, key, headers_stream, headers_json, headers
    base = b   
    key = k
    headers_stream = {'Ocp-Apim-Subscription-Key': key,  
                      'Content-Type': 'application/octet-stream'}
    headers_json = {'Ocp-Apim-Subscription-Key': key,    
                    'Content-Type': 'application/json'}
    headers = {'Ocp-Apim-Subscription-Key': key}         
gid = 'gp01'    
pid = '893f6049-c9b5-463d-87ab-d14c52bbfe0a' 


def face_use(g, p):
    global gid, pid
    gid = g
    pid = p


def face_add(img):            
    img_encode = cv2.imencode('.jpg', img)[1]
    img_bytes = img_encode.tobytes()
    face_url = f'{base}/persongroups/{gid}/persons/{pid}/persistedFaces'
    response = requests.post(face_url,            
                             headers=headers_stream,
                             data=img_bytes)
    if response.status_code == 200:
        print('新增臉部成功')
    else:
        print('新增臉部失敗:', response.text)


def face_detect(img):
    detect_url = f'{base}/detect?returnFaceId=true' 
    img_encode = cv2.imencode('.jpg', img)[1]
    img_bytes = img_encode.tobytes()                
    response = requests.post(detect_url,
                             headers=headers_stream,
                             data=img_bytes)
    if response.status_code == 200:
        face = response.json()
        if not face:
            print("無偵測到人臉")
        else:
            faceId = face[0]['faceId']             
            return faceId


def face_identify(faceId):
    idy_url = f'{base}/identify'   
    body = str({'personGroupId': gid,
                'faceIds': [faceId]})
    response = requests.post(idy_url, 
                             headers=headers_json,
                             data=body)
    if response.status_code == 200:
        person = response.json()
        if not person[0]['candidates']:
            return None
        else:
            personId = person[0]['candidates'][0]['personId']
            print(personId)
            return personId


def face_who(img):
    faceId = face_detect(img) 
    personId = face_identify(faceId)  
    if personId == None:
        print('查無身分')
    else:
        persons = person_list(gid)    
        for p in persons:      
            if personId == p['personId']:
                print('歡迎:', p['name'])
                db_save('mydatabase.sqlite', p['name'])    
                db_check('mydatabase.sqlite')              


def person_list(gid):
    pson_url = f'{base}/persongroups/{gid}/persons'   
    response = requests.get(pson_url,      
                            headers=headers)
    if response.status_code == 200:
        print('查詢完成')
        return response.json()
    else:
        print("查詢失敗:", response.json) 


def db_save(db, name):
    connect = sqlite3.connect(db)
    sql = 'CREATE TABLE IF NOT EXISTS mytable \
            ("姓名" TEXT, "時間" TEXT)'
    connect.execute(sql)
    save_time = str(datetime.now().strftime('%Y-%m-%d %H.%M.%S'))
    sql = f'insert into mytable values("{name}", "{save_time}")'
    connect.execute(sql)   
    connect.commit()       
    connect.close()      


def db_check(db):
    try:
        connect = sqlite3.connect(db) 
        connect.row_factory = sqlite3.Row 
        sql = 'select * from mytable'   
        cursor = connect.execute(sql)  
        dataset = cursor.fetchall()     
        col1 = dataset[0].keys()[0]     
        col2 = dataset[0].keys()[1]     
        print(f'{col1}\t{col2}')
        print('----\t  ----')
        for data in dataset:
            print(f'{data[0]}\t{data[1]}')
    except:
        print('讀取資料庫錯誤')
    connect.close()


def face_shot(function):
    isCnt = False
    face_detector = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')
    capture = cv2.VideoCapture(0)                  
    while capture.isOpened():                     
        sucess, img = capture.read()      
        if not sucess:
            print('讀取影像失敗')
            continue
        img_copy = img.copy()                      
        faces = face_detector.detectMultiScale(    
            img,
            scaleFactor=1.1,            # 特徵窗口
            minNeighbors=5,             # 誤判率參數
            minSize=(150, 150))         # 特徵窗口尺寸
        if len(faces) == 1:                    
            if isCnt == False:
                t1 = time.time()                
                isCnt = True                   
            cnter = 2 - int(time.time() - t1)   
            for (x, y, w, h) in faces:         
                cv2.rectangle(                 
                    img_copy, (x, y), (x+w, y+h),
                    (0, 255, 0), 2)
                cv2.putText(                    
                    img_copy, str(cnter),
                    (x+int(w/2), y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 2)
            if cnter == 0:                
                isCnt = False           
                filename = datetime.now().strftime(
                    '%Y-%m-%d %H.%M.%S')    
                cv2.imwrite(filename + '.jpg', img) 
                if function == 'add':   
                    face_add(img)
                elif function == 'who': 
                    face_who(img)
        else:                         
            isCnt = False                   

        cv2.imshow('Frame', img_copy)        
        k = cv2.waitKey(1)                  
        if k == ord('q') or k == ord('Q'):  
            print('exit')
            cv2.destroyAllWindows()          
            capture.release()               
            break                             
    else:
        print('開啟攝影機失敗')
