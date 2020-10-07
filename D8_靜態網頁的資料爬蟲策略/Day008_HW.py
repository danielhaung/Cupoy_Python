#Dcard爬蟲整理
#引入函式庫
import requests
#想要爬資料的目標網址
r = requests.get('https://www.dcard.tw/f')
#模擬發送請求的動作
response = r.text
# print(response)


from bs4 import BeautifulSoup

soup = BeautifulSoup(response, "html5lib")
print(soup.title)