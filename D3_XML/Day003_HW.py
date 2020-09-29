# 比較一下範例檔案中的「File I/O」與「xmltodict」讀出來的內容有什麼差異

# 根據範例檔案的結果：

# 1. 請問高雄市有多少地區有溫度資料？

# 2. 請取出每一個地區所記錄的第一個時間點跟溫度

# 3. 請取出第一個地區所記錄的每一個時間點跟溫度




#下載檔案
import urllib.request
import zipfile

res = "http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(res,'./Data/example.zip')
f = zipfile.ZipFile('./Data/example.zip')
f.extractall('./Data')  #將所有成員從存檔提取到當前工作目錄

#File I/O
#讀檔案
fh = open("./Data/64_72hr_CH.xml","r",encoding='utf-8')
xml = fh.read()
fh.close()



import xmltodict

d = dict(xmltodict.parse(xml))
# 取出 datasetDescription
# datasetDescription = d['cwbopendata']['dataset']['datasetInfo']['datasetDescription']
# print(datasetDescription)


#####################################
# 1. 請問高雄市有多少地區有溫度資料？ #
#####################################
datasetDescription = d['cwbopendata']['dataset']['locations']['location']
datetime = datasetDescription[0]['weatherElement'][0]['time'][1]['dataTime']
Temp = datasetDescription[0]['weatherElement'][0]['time'][1]['elementValue']["value"]
list_all = []
list_firstTimeTemp= []
i = 0
while True:
    try:
        i+=1
        list_all.append(datasetDescription[i]['locationName'])
        list_firstTimeTemp.append([datasetDescription[i]['weatherElement'][0]['time'][0]['dataTime'],datasetDescription[i]['weatherElement'][0]['time'][0]['elementValue']["value"]])
    except IndexError:
        print("搜尋完畢")
        i-=1
        break
    
# print(list_all,"共"+str(i)+"區")
print(list_firstTimeTemp)

##############################################
# 2. 請取出每一個地區所記錄的第一個時間點跟溫度 #
##############################################






