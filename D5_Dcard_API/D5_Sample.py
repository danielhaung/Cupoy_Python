"""
當我們對 API 發送請求：
https://www.dcard.tw/_api/forums/job/posts?popular=true
可以得到的回應是： Job 版且熱門的所有文章
"""
#引入函式庫
import requests
#想要爬資料的目標網址
r = requests.get('https://www.dcard.tw/_api/forums/job/posts?popular=true')
#模擬發送請求的動作
response = r.text
# print(response)

import json
data = json.loads(response) #利用json解析網頁內容

for d in data:
    print(d['title'])