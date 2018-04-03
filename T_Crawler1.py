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

conn = pymysql.connect(
        host='202.194.15.184',
        port = 3306,
        user='gradms',
        passwd='gradms184.db',
        db ='gradms',

        #host='202.194.14.145',
        #port = 3306,
        #user='root',
        #passwd='qlscadmin',
        #db ='gradms',
        charset='UTF8'
    )

cur = conn.cursor() 

url = 'https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2018_limit0_369a9045a203e176392b9fb8f8c1cb2a.json'
#url = 'https://www.topuniversities.com/sites/default/files/qs-rankings-data/357051.txt?_=1521446318425'
html = check_link(url)
text = json.loads(html)
num = 0

for rank in text["data"]:
    num = num + 1
    numstr = str(num)
    name = rank["name"].replace("'","''")
    sql="update gradms.newabroad_university_info set orderNum1 = "+numstr+" where universityName='"+name+"'"
    cur.execute(sql)

   
conn.commit()
conn.close()