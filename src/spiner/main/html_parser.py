# coding=UTF-8
from bs4 import BeautifulSoup
import re
from datetime import date
import urlparse


class HtmlParser(object):

    def parse(self,new_url,html_content):
        urls_set=set()
        data_dict={}
        #self.urlCollection["url"]=new_url
        #print html_content
        soup=BeautifulSoup(html_content,"html.parser")
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        headTag=soup.find("h1")
        #print headTag
        head=headTag.get_text()
       # print head
        #print "head",head
        data_dict["url"]=new_url
        data_dict["title"]=head
        #self.urlCollection["title"]=head
        links=soup.find_all("a", href=re.compile(r"/item/."))
        for url in links:
           
            new_url=urlparse.urljoin("http://baike.baidu.com", url["href"])
            print "new_url",new_url
            urls_set.add(new_url)     
         #<div class="lemma-summary
        content=soup.find("div", class_="lemma-summary")
        data_dict["content"] = content.get_text()     
        return urls_set,data_dict



