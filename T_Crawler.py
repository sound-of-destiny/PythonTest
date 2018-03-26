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
        #host='202.194.15.184',
        #port = 3306,
        #user='gradms',
        #passwd='gradms184.db',
        #db ='gradms'

        host='202.194.14.145',
        port = 3306,
        user='root',
        passwd='qlscadmin',
        db ='gradms'
    )

cur = conn.cursor() 
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')
url = 'https://www.timeshighereducation.com/sites/default/files/the_data_rankings/world_university_rankings_2018_limit0_369a9045a203e176392b9fb8f8c1cb2a.json'
html = check_link(url)
text = json.loads(html)
num = 0
for rank in text["data"]:
    num = num + 1
    numstr = str(num)
    name = rank["name"].replace("'","''").encode("utf-8").decode("latin1")
    sql="update gradms.newabroad_university_info set orderNum1 = "+numstr+" where universityName='"+name+"'"
    cur.execute(sql)

conn.commit()
conn.close()