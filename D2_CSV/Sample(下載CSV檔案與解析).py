#-*- encoding:utf-8 -*-
###
#了解 csv 檔案格式與內容
#能夠利用套件存取 csv 格式的檔案
###

import urllib.request

#檔案下載但是網址沒了
# res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
# urllib.request.urlretrieve(res,'./data/example.csv')


import os,sys

#打開文件
dirs = os.listdir("./data") #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。

#輸出所有文件和文件夾
for file in dirs:
    print(file)



####################
##File I/O方式開啟##
####################

# fh = open("./data/example.csv",encoding="utf-8")
# print(type(fh))
# f = fh.read()
# fh.close()
# print(f)


#####################
##CSV Reader方式開啟##
#####################

# import csv

# #開啟CSV檔案
# with open('./data/example.csv', newline='',encoding='utf-8') as csvfile:
#     #讀取 CSV檔案內容
#     rows = csv.reader(csvfile)
#     #以迴圈輸出每一列
#     for row in rows:
#         print(row)


