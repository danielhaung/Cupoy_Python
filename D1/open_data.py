"""
「下載指定檔案到 Data 資料夾，存成檔名 Homework.txt」的檔案網址：https://www.w3.org/TR/PNG/iso_8859-1.txt 或任一個 .txt 的檔案網址

檢查 Data 資料夾是否有 Homework.txt 檔名之檔案

將「Hello World」字串覆寫到 Homework.txt 檔案

檢查 Homework.txt 檔案字數是否符合 Hello World 字數

"""

# 根據需求引入正確的 Library
from urllib.request import urlretrieve
import os,sys

## 下載檔案到 Data 資料夾，存成檔名 Homework.txt
#urlretrieve(url, filename=None, reporthook=None, data=None)
#os.makedirs() v.s. os.mkdir() https://blog.csdn.net/ljl6158999/article/details/70807738

os.makedirs('./Data', exist_ok=True)    #exist_ok:避免在目录已经存在的情况下引发异常
path = "./Data/Homework.txt"
urlretrieve("https://www.w3.org/TR/PNG/iso_8859-1.txt",filename=path)


## 將「Hello World」字串覆寫到 Homework.txt 檔案
try:
    with open(path,'w') as fh :
        # print(fh.read())  
        fh.write("Hello World")
        # print(len("Hello World")) #11
        #print(l)
except EnvironmentError as e:
    print(e)    #[Errno 2] No such file or directory: './Data1/Homework1.txt'
    



# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數
#EnvironmentError是来自Python(操作系统，文件系统等)外部的错误的基类。如[Errno 2] No such file or directory: 'JohnDoe.txt'

with open(path,'r') as fh :
    if len("Hello World") == len(fh.read()) :
        print("[O] 檢查Homework.txt 檔案字數是否符合 Hello World 字數")
    else :
        print("[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數")