####################
##File I/O方式開啟##
####################
import time
list_All_ans=[]
number_one = []
number_all = []

fh = open("./data/example.csv",encoding="utf-8")
# print(type(fh))
f = fh.read()
fh.close()
list_All = f.split('\n')



#分類每行的數據成為列表
for list_single in list_All:
    list_All = str(list_single).split(',')
    # print(list_single)
    list_All_ans.append(list_single)
# print(list_All_ans)


import re
regex = r"\d+"
fake ="38,51,香"

  #找出班次1的全部時間  
for item_single in list_All_ans:
    # print(item_single)
    matchObj = re.match(regex, item_single)
    # print(matchObj)
    if matchObj != None:
        number = str(item_single).split(',')
        # print(number[5])
        number_one.append(number[5])
        
        #全部班次
        for i in range(5,16) :
            number_all.append(number[i])
        # print(number_one)
print(number_one)     #<<<所有班次一的時間表
print(number_all)     #<<<所有班次的時間表


 


