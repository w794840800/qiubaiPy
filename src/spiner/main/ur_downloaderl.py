# coding=UTF-8

import urllib
import urllib2





class downloader(object):

    
    def download(self,url):
        request=urllib2.Request(url,headers={"user-agent":"mozilla/5.0"})
        response=urllib2.urlopen(request)
        #print "response.read()",response.read()
        return response.read()
    
    
    
    

    
    



