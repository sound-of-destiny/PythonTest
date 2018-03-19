import re
import requests
import json

def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法连接服务器')

url = 'https://www.topuniversities.com/sites/default/files/qs-rankings-data/357051.txt?_=1521446318425'
html = check_link(url)
text = json.loads(html)
for i in text["data"]:
     print(i["title"])