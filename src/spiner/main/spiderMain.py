# coding=UTF-8
from spiner.main import url_manager, ur_downloaderl, html_parser, html_outputer
class SpiderMain1(object):
    
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=ur_downloaderl.downloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def craw(self, root_url1):
        count=1
        new_url=self.urls.add_url("http://baike.baidu.com/view/21087.htm")
        while self.urls.has_new_url():
         try:
            new_url=self.urls.get_new_url()

            print count
            html_content=self.downloader.download(new_url)

            new_urls,new_data=self.parser.parse(new_url,html_content)
            

            self.urls.add_new_urls(new_urls)
            self.outputer.collection(new_data)
            if(count==500):
                break
            
         except:             
                print "failed"
         count=count+1
        self.outputer.output_html()    



if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain1()
    obj_spider.craw(root_url)
    



   
     


