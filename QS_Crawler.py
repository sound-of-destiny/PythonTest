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

conn= pymysql.connect(
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
    countryName = rank["country"].upper()
    print(countryName)
    if countryName == 'HONG KONG':
        countryName = 'HONG KONG, CHINA'
    if countryName == 'TAIWAN':
        countryName = 'TAIWAN, CHINA'
    if countryName == 'MACAO S.A.R., CHINA':
        countryName = 'MACAU'
    if countryName == 'SOUTH KOREA':
        countryName = 'REPUBLIC OF KOREA'
    if countryName == 'CZECH REPUBLIC':
        countryName = 'CZECH'
    if countryName == 'IRAN, ISLAMIC REPUBLIC OF':
        countryName = 'IRAN'
    if countryName == 'PALESTINIAN TERRITORY, OCCUPIED':
        countryName = 'PALESTINE'

    cur.execute("select nationId from gradms.base_nation where nationEnglishName='"+countryName+"'")
    nationId=cur.fetchone()
    if nationId :
        sql="insert into gradms.newabroad_university_info (nationId,universityName,orderNum,year) values (%d,'%s',%d,'%s')" % (nationId[0],rank["title"].replace("'","''").encode("utf-8").decode("latin1"),i,'2018')
        cur.execute(sql)

conn.commit()
conn.close()