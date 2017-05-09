# coding=UTF-8


class HtmlOutputer(object):
    def  __init__(self):
        self.datas=[]
    def collection(self,data):
        self.datas.append(data)

    
    def output_html(self):
        out=open("outhtml.html","w")
        out.write("<html>")
        out.write("<body>")
        out.write("<table>")
        for da in self.datas:
            
            out.write("<tr>")
            out.write("<td>%s</td>" % da["url"])
            out.write("<td>%s</td>" % da["title"].encode("utf-8"))
            out.write("<td>%s</td>" % da["content"].encode("utf-8"))

            out.write("</tr>")
        
        out.write("</table>")
        
        
        out.write("</body>")          
        out.write("</html>")
        
        
        
     
    
    
    
    



