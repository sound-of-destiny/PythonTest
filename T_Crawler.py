import json
import re

import requests

import pymysql


def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法连接服务器')

def levenshtein(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    dif = [([0]*(len1+1))for i in range(len2+1)]
    for a in range(len1+1):
        dif[0][a]=a
    for b in range(len2+1):
        dif[b][0]=b
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if str1[j-1] == str2[i-1]:
                temp = 0
            else:
                temp = 1
            dif[i][j] = min(dif[i-1][j-1]+temp,dif[i-1][j]+1,dif[i][j-1]+1)
    similarity = 1 - dif[len2][len1]/max(len1,len2)
    return similarity

conn = pymysql.connect(
        #host='202.194.15.184',
        #port = 3306,
        #user='gradms',
        #passwd='gradms184.db',
        #db ='gradms',

        host='202.194.14.145',
        port = 3306,
        user='root',
        passwd='qlscadmin',
        db ='gradms',
        charset='UTF8'
    )

cur = conn.cursor() 

url = 'https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2018_limit0_369a9045a203e176392b9fb8f8c1cb2a.json'

html = check_link(url)
text = json.loads(html)
num = 0
cur.execute("select universityName,universityId from gradms.newabroad_university_info")
university = cur.fetchall()
num = 0
univnamelist = []
for rank in text["data"]:
    name = rank["name"].replace("'","''")
    num = num + 1
    univnamelist.append([name,num,0])

for x in university:
    for name in univnamelist:
        if x[0] == name[0]:
            univnamelist.remove(name)

cur.execute("select universityName,universityId from gradms.newabroad_university_info where orderNum1 is null")
universityS = cur.fetchall()
universitylist = list(universityS)

for x in universitylist:

    tempS = []
    for un in univnamelist:
        if un[2] == 1:
            continue
        similarity = levenshtein(un[0],x[0])
        if similarity > 0.4:
            abst = abs(x[1]-un[1])
            tempS.append([similarity,un[1],abst])

    maxabs = 1000
    for s in tempS:
        if s[2] < maxabs:
            maxabs = s[2]
            ordernum = s[1]

    if maxabs < 150:
        Id = str(x[1])
        num1 = str(ordernum)
        i = -1
        for a in univnamelist:
            i = i + 1
            if a[1] == ordernum:
                break
        univnamelist[i][2] = 1
        print(x[0])
        sql="update gradms.newabroad_university_info set orderNum1 = "+num1+" where universityId='"+Id+"'"
        cur.execute(sql)

conn.commit()
conn.close()