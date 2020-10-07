"""
請利用 API: https://www.dcard.tw/_api/forums/pet/posts?popular=true 回答下列問題：
1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？



2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」
"""


#引入函式庫
import requests
#想要爬資料的目標網址
r = requests.get('https://www.dcard.tw/_api/forums/job/posts?popular=true')
#模擬發送請求的動作
response = r.text
# print(response)

import json
data = json.loads(response) #利用json解析網頁內容

# print(data)
i=0
for d in data:
    i+=1
    # print(d['id'])


# print("有"+str(i)+"筆資料")

#["id"]["title"]["excerpt"]['anonymousSchool'].......


i=0
commentCount_avage = 0
likeCount_avage = 0
for d in data:
    i+=1
    print(d['title'],d['createdAt'],d['commentCount'],d['likeCount'])
    commentCount_avage += d['commentCount']
    likeCount_avage +=d['likeCount']

print("平均回應數"+str(commentCount_avage/i),"平均按讚數",str(likeCount_avage/i))
 