import json
import re

import requests

import MySQLdb


def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法连接服务器')

conn= MySQLdb.connect(
        host='202.194.15.184',
        port = 3306,
        user='gradms',
        passwd='gradms184.db',
        db ='gradms'
    )

cur = conn.cursor() 

i=0
url = 'https://www.topuniversities.com/sites/default/files/qs-rankings-data/357051.txt?_=1521446318425'
html = check_link(url)
text = json.loads(html)
for rank in text["data"]:
    i=i+1
    print(rank["title"])
    sql1="select nationId from gradms.base_nation where nationEnglishName='"+rank["country"].upper()+"'"
    nationId=cur.execute(sql1)
    sql2="insert into gradms.newabroad_university_info (nationId,universityName,orderNum,year) values (%d,%s,%d,%s)"
    cur.execute(sql2,(nationId,rank["title"],i,'2018'))


cur.close()
conn.commit()
conn.close()