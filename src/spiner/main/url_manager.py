# coding=UTF-8
class UrlManager(object):
   
    def  __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    def add_url(self,url):
        if url is None:
            return
       
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
           # print "add_url",url
    
    def has_new_url(self):
        #print "len(self.new_urls)",len(self.new_urls)
        return len(self.new_urls)

    
    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        #print "get_new_url(self):",new_url
        return new_url
    
    def add_new_urls(self,urls):
        for url in urls:
            self.new_urls.add(url)
            
    
    
    
    
    
    
    
    
    
    



