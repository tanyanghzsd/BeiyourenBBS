#coding:utf-8
import urllib
import urllib2
import re
import cookielib
import requests
from bs4 import BeautifulSoup

class Tool:
    removeImg=re.compile('<img.*?>| {7}|')
    removeAddr=re.compile('<a.*?>|</a>')
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')
    replaceTD=re.compile('<td>')
    replacePara=re.compile('<p.*?>')
    replaceBR=re.compile('<br><br>|<br>')
    removeExtraTag=re.compile('<.*?>')
    def replace(self,x):
        x=re.sub(self.removeImg,"",x)
        x=re.sub(self.removeAddr,"",x)
        x=re.sub(self.replaceLine,"\n",x)
        x=re.sub(self.replaceTD,"\t",x)
        x=re.sub(self.replacePara,"\n  ",x)
        x=re.sub(self.replaceBR,"\n",x)
        x=re.sub(self.removeExtraTag,"",x)
        return x.strip()
tool=Tool()
url='http://m.byr.cn/#!default'
s=requests.session()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'}
postdata=urllib.urlencode({'id':'yourid',
                           'passwd':'yourpassword'
                           })
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
req=urllib2.Request(url,data=postdata,headers=headers)
page=opener.open(req).read()
#print page


def getJob(pagenum):
    myurl='http://m.byr.cn/board/JobInfo'+'?p='+str(pagenum)
    page=opener.open(myurl)
    soup=BeautifulSoup(page)
#     regex=re.compile(r'<a href="/article/TobInfo/.*?(.*?).*?</a>',re.S)
#     contents=re.findall(regex,page)
    contents=soup.find_all('a')
    urls=[]
    for content in contents:
        if len(content.text)<20:
            pass
        else:
            if (content['href']):
                if (len(content['href'])==23):
                    print tool.replace(content.text)
                    print'---------------------------------'
                    urls.append('http://m.byr.cn'+content['href'])
    return urls

def getInfo(url_1):
    page=urllib2.urlopen(url_1).read().decode('utf-8')
    regex=re.compile(r'<div class="sp">(.*>)</div>',re.S)
    contents=re.findall(regex,page) 
    for content in contents:
        print tool.replace(content)
        print '---------------------' 
        
urls_1=getJob(1)
urls_2=getJob(2)
# urls_3=getJob(3)
# urls_4=getJob(4)
# urls_5=getJob(5)
for url in urls_2:
    urls_1.append(url)
# for url in urls_3:
#     urls_1.append(url)
# for url in urls_4:
#     urls_1.append(url)
# for url in urls_5:
#     urls_1.append(url)

for url in urls_1:
    getInfo(url)
    

        
    
        
        
        
        
        
        
        
