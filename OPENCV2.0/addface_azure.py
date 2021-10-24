#新增成員資料
import requests
base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'
pson_url = f'{base}/persongroups/gp01/persons'
key = 'f85d4cd78eda46cab8549149ac0d146a'
headers_json = {'Ocp-Apim-Subscription-Key': key,  
                'Content-Type': 'application/json'}
body = {'name': '曹家憲',  
        'userData': '位於家裡'}
body = str(body).encode('utf-8')  
response = requests.post(pson_url, 
                         headers=headers_json,
                         data=body)
if response.status_code == 200:
    print('新增完成: ', response.json())
else:
    print("新增失敗:", response.json())


