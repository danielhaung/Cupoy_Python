###參考資料https://realpython.com/python-csv/
import csv 

"""
import os
path1=os.path.abspath(‘.‘) #表示當前所處的文件夾的絕對路徑
path2=os.path.abspath(‘..‘) #表示當前所處的文件夾上一級文件夾的絕對路徑
"""

##############################
# Reading CSV Files With csv #
##############################

with open('./Data/employee_birthday.txt') as csv_file:      #不寫mode預設為 r讀
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')  #加f：字符串内支持大括号内的表达式 cvs轉字串需使用join做編排  str(row)沒有加join會變成['name', 'department', 'birthday month']
            line_count+=1
        else:
            print(f"\t{row[0]} work in the{row[1]} department, and was born in {row[2]}. ")
            line_count +=1

            # #<<<<<or都可以>>>>> 上面的好處是不用再加+
            # print("\t "+row[0]+'work in the'+ row[1] +'department, and was born in '+ row[2] )
            # line_count +=1


    print(f'Processed {line_count} lines.')



################################################
# Reading CSV Files Into a Dictionary With csv #
################################################
print("####################################################")
with open("./Data/employee_birthday.txt", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0 
    for row in csv_reader:
        # print(row)
        if line_count == 0:
            print(f"Column names are {','.join(row)}")
            line_count+=1
        print(f"\t{row['name']} works in the {row['department']} department , and was born in {row['birthday month']}." )
        line_count += 1
    print(f'Processed {line_count} lines.')


