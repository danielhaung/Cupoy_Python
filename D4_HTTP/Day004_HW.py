"""
    利用 Python 存取 API
    了解 Server Client 的架構與溝通方法
    知道 HTTP Request & Response 的內容
    什麼是 API？如何用 Python 程式存取 API 資料
"""


#下載檔案
import requests

r = requests.get('https://cat-fact.herokuapp.com/facts')
# print(r.text)

import json 
print(json.loads(r.text))



