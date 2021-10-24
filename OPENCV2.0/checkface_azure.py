#查詢成員
import requests

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'
key = 'f85d4cd78eda46cab8549149ac0d146a' 
headers = {'Ocp-Apim-Subscription-Key': key} 
def person_list(gid):
    pson_url = base + f'/persongroups/{gid}/persons' 
    response = requests.get(pson_url,
                            headers=headers)
    if response.status_code == 200:
        print('查詢人員完成')
        return response.json()
    else:
        print("查詢人員失敗:", response.json())
persons = person_list('gp01')
print(persons)
