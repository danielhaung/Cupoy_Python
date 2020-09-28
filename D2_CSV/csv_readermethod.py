import csv
number_one =[]
number_all =[]

#開啟CSV檔案
with open('./data/example.csv', newline='',encoding='utf-8') as csvfile:
    #讀取 CSV檔案內容
    rows = csv.reader(csvfile)
    #以迴圈輸出每一列
    for row in rows:
        #取出班次一的每一個時間，印出來就好
        # print(row[5])
        number_one.append(row[5])
        for i in range(5,16):
            number_all.append(row[i])
        print(number_all)
#將班次一的每一個時間用一個變數保存