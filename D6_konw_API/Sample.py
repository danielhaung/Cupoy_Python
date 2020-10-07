#載入函式庫
import requests

#定義標頭檔
headers = {'user-agent':'my_app/0.0.1'}


#發送請求
r = requests.get("https://www.zhihu.com/api/v4/questions/55493026/answers",headers=headers)
# print(r.text)

import json
data = json.loads(r.text) #利用json解析網頁內容

#取出資料
for d in data['data']:
    print(d)


