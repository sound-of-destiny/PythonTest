import re
import requests
from lxml import etree
from bs4 import BeautifulSoup   
import csv  
import bs4 
import json

def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法连接服务器')
'''
def get_contents(ulist,rurl):
    soup = BeautifulSoup(rurl,'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)

def save_contents(urlist):  
    with open("D:/QS.csv",'w') as f:  
        writer = csv.writer(f)  
        writer.writerow(['QS'])  
        for i in range(len(urlist)):  
            writer.writerow([urlist[i][0],urlist[i][1],urlist[i][2]])  
  
def main():  
    urli = []  
    url = 'https://www.topuniversities.com/university-rankings/world-university-rankings/2018'
    rs = check_link(url)  
    get_contents(urli,rs)  
    save_contents(urli)  
  
main()  
'''
url = 'https://www.topuniversities.com/sites/default/files/qs-rankings-data/357051.txt?_=1521446318425'
html = check_link(url)
text = json.loads(html)
for i in text["data"]:
    print(i["title"])
       
#text = '<a class="title" href = "www.baidu.com">....'
#urls = re.findall('<title>(.*?)</title>',html.text,re.S)
#print(urls)
#for each in urls:
#    print(each)
#selector = etree.HTML(html.text)
#content = selector.xpath('//a[starts-with(@class,"title")]/text()')
#for each in content:
#    print(each)

