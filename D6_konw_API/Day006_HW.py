"""
作業目標
根據範例提供的 API ，完成以下問題：

1.取出知乎問題發問時間
2.取出第一筆與最後一筆回答的時間
"""

#載入函式庫
import requests

#定義標頭檔
headers = {'user-agent':'my_app/0.0.1'}


#發送請求
r = requests.get("https://www.zhihu.com/api/v4/questions/55493026/answers",headers=headers)
# print(r.text)

import json
data = json.loads(r.text) #利用json解析網頁內容

#取出知乎問題發問時間
for d in data['data']:
    print(d['question']['created'])



#取出第一筆與最後一筆回答的時間
for d in data['data']:
    print(d['question']["updated_time"])









