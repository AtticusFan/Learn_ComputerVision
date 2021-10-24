import requests

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0' 
gId = 'gp01'    # 要訓練的群組
train_url = f'{base}/persongroups/{gId}/training'
key = 'f85d4cd78eda46cab8549149ac0d146a'          # 金鑰
headers = {'Ocp-Apim-Subscription-Key': key}    
response = requests.get(train_url,             
                        headers=headers)
if response.status_code == 200:
    print("訓練結果：", response.json())
else:
    print("查看失敗", response.json())
