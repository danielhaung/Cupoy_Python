###參考資料https://realpython.com/python-csv/
import csv 




############################## 
# Writing CSV Files With csv #
############################## 


# with open("./Data/employee_birthday1.txt",mode='w',newline='') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])




###############################################  
# Writing CSV File From a Dictionary With csv #
###############################################  

# with open('./Data/employee_file2.csv', mode='w',newline='') as csv_file:
#     fieldnames = ['emp_name', 'dept', 'birth_month']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#     writer.writeheader()    ## 寫入第一列的欄位名稱
#     writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
#     writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})



#################################  
# Reading CSV Files With pandas #
#################################   

import pandas

# df = pandas.read_csv('./Data/hrdata.csv')
# print(df)


##or##
df = pandas.read_csv('./Data/hrdata.csv', 
            index_col='Employee',   #決定index欄位為Employee
            parse_dates=['Hired'],  #日期格式變化
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days']) #顯示欄位
print(df)

df.to_csv('./Data/hrdata_modified.csv')