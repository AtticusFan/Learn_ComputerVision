"""
#建立群組
import requests
base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'    
gp_url = base + '/persongroups/gp01'                                   
key = 'f85d4cd78eda46cab8549149ac0d146a'  
headers_json = {'Ocp-Apim-Subscription-Key': key,      
                'Content-Type': 'application/json'}
body = {'name': '范家豪',    
        'userData': '位於家裡'}
body = str(body).encode('utf-8')

response = requests.put(gp_url,
                        headers=headers_json,
                        data=body)
if response.status_code == 200:
    print("創建群組成功")
else:
    print("創建失敗:", response.json()) 
"""


#查詢群組
import requests

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'    # api
gp_url = base + '/persongroups/gp01'                                    # 創建群組的請求路徑
key = 'f85d4cd78eda46cab8549149ac0d146a'                                # 你的 key
headers = {'Ocp-Apim-Subscription-Key': key}   # 請求標頭
response = requests.get(gp_url,
                        headers=headers)       # HTTP GET
if response.status_code == 200:
    print(response.json())
else:
    print("查詢失敗", response.json())