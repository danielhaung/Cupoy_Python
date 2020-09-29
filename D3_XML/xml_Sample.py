"""
Python 下載XML檔案與解析
了解 xml 檔案格式與內容
能夠利用套件存取 xml 格式的檔案
存取 XML 的三種套件
"""

#######################################
# 存取XML的三種套件(一)xml.dom.minidom #
#######################################

# import xml.dom.minidom

# #存取檔案該parse()函數可以使用文件名或打開的文件對象
# doc = xml.dom.minidom.parse('./Data/sample.xml')

# #存取我們的資訊
# print(doc.getElementsByTagName("Title")[0].firstChild.nodeValue)    #搜索具有特定元素類型名稱的所有後代（直系子代，子代子代等）。

# #用迴圈存取我們的資訊
# chapters = doc.getElementsByTagName('Chapter')
# for chapter in chapters:
#     print(chapter.getAttribute('name'), chapter.firstChild.nodeValue)


#############################################
# 存取XML的三種套件(二)xml.etree.ElementTree #
#############################################

# import xml.etree.ElementTree as ET

# #存取檔案
# tree = ET.parse('./Data/sample.xml')
# root = tree.getroot()

# #存取我們的資訊
# print(root[0].text)

# # 用迴圈存取我們的資訊
# chapters = root[2]
# for chapter in chapters:
#     print (chapter.attrib['name'], chapter.text)



#################################
# 存取XML的三種套件(三)xmltodict #
#################################

# import xmltodict

# #存取檔案

# with open('./Data/sample.xml',encoding='utf-8') as fd:
#     doc = dict(xmltodict.parse(fd.read()))


# #存取我們的資訊
# print(doc['CUPOY']["Title"])

# #用迴圈存取我們的資訊
# chapters = doc["CUPOY"]['Chapters']['Chapter']
# for chapter in chapters:
#     print(chapter['@name'], chapter['#text'])




##################################################################
##################################################################

#下載檔案
import urllib.request
import zipfile

res = "http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(res,'./Data/example.zip')
f = zipfile.ZipFile('./Data/example.zip')
f.extractall('./Data')  #將所有成員從存檔提取到當前工作目錄

import os,sys

#打開文件
dirs = os.listdir("./Data")

#輸出所有文件和文件夾
# for file in dirs:
    # print(file)


#File I/O
#讀檔案
fh = open("./Data/64_72hr_CH.xml","r",encoding='utf-8')
xml = fh.read()
fh.close()
# print(xml)



#xmltodict 解析檔案內容

import xmltodict
d = dict(xmltodict.parse(xml))

# 取出 datasetDescription
datasetDescription = d['cwbopendata']['dataset']['datasetInfo']['datasetDescription']
print(datasetDescription)

