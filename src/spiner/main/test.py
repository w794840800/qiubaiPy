# coding=UTF-8
import urllib2
from bs4 import BeautifulSoup

request=urllib2.urlopen("http://baike.baidu.com/view/21087.htm").read()
print request
soup=BeautifulSoup(request,"html.parser")
tab=soup.find("h1")
print tab.get_text()



