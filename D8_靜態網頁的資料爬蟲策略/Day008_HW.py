# -*- coding: utf-8 -*-
"""
利用 Request + BeatifulSoup 爬取下列兩個網站內容並解析：
1. Dcared 網址： https://www.dcard.tw/f
2. 知乎： https://www.zhihu.com/explore
並且回答下面問題：
1. Request 取回之後該怎麼取出資料，資料型態是什麼？
2. 為什麼要使用 BeatifulSoup 處理？
3. 觀察一下知乎回來的資料好像有點怪怪的，該怎麼解決？
1
"""





# #######################Dcard爬蟲整理#############################
# #引入函式庫
# import requests
# #想要爬資料的目標網址
# r = requests.get('https://www.dcard.tw/f')
# #模擬發送請求的動作
# response = r.text
# # print(response)


# from bs4 import BeautifulSoup

# soup = BeautifulSoup(response, "lxml")

# # print(soup.prettify())    #整理網頁好去爬取
# for span in soup.find_all(attrs={'class':'tgn9uw-3 ebwnQU'}):
#     for span1 in span.find_all(name='span'):
#         print(span1.string)




# #######################知乎爬蟲整理#############################

# #引入函式庫
# import requests

# #定義標頭檔內容
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

# #想要爬資料的目標網址
# r = requests.get('https://www.zhihu.com/explore',headers=headers)
# #模擬發送請求的動作
# response = r.text
# # print(response)



# from bs4 import BeautifulSoup
# soup = BeautifulSoup(response, "lxml")
# # # print(soup.prettify())    #整理網頁好去爬取
# for span in soup.find_all(attrs={'class':'ExploreRoundtableCard-questionTitle'}):
#     print(span.string)